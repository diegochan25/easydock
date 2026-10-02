from typing import TYPE_CHECKING, Self
from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

if TYPE_CHECKING:
    from django.db.models.fields.related_descriptors import ManyRelatedManager, RelatedManager

SUPERADMIN_ROLE_NAME = '__superadmin__'

class UserManager(BaseUserManager['User']):
    def _create_user(self, email: str, password: str, admin: bool = False, **extra):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=self.normalize_email(email), **extra)
        user.set_password(password)
        user.save(using=self._db)
        if admin:
            template = Role.superadmin_role()
            role, _ = Role.objects.get_or_create(
                internal=template.internal,
                superadmin=template.superadmin,
                defaults={'name': template.name},
            )
            UserRole.objects.create(user=user, role=role)
        return user

    def create_user(self, email: str, password: str, **extra):
        return self._create_user(email, password, **extra)

    def create_superuser(self, email: str, password: str, **extra):
        return self._create_user(email, password, admin=True, **extra)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid4, primary_key=True)

    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    roles: 'ManyRelatedManager[Role, UserRole]' = models.ManyToManyField('Role', through='UserRole', through_fields=('user', 'role'), related_name='users')

    # Annotations
    role_assignments: 'RelatedManager[UserRole]'

    # BaseUserManager fields
    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = 'users'

    @property
    def is_superuser(self) -> bool:
        return any(r.superadmin for r in self.roles.all())

    @property
    def is_staff(self) -> bool:
        return True # TODO decide real check

    def can(self, permission: str):
        """
        Checks whether any of the user's roles
        includes the specified permission.

        Args
            permission: the permission to check

        Returns
            True if the permission is included in any roles the user has assigned.
        """
        return any(r.includes_permission(permission) for r in self.roles.all())


class UserRole(models.Model):
    pk = models.CompositePrimaryKey('user', 'role')

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    assigned_by = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='role_assignments')

    assigned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_roles'


class Role(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)

    name = models.CharField(max_length=255, unique=True)
    internal = models.BooleanField(default=False)
    superadmin = models.BooleanField(default=False)
    permissions = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Annotations
    users: 'ManyRelatedManager[User, UserRole]'

    class Meta:
        db_table = 'roles'
        constraints = [
            models.UniqueConstraint(
                fields=['internal', 'superadmin'],
                condition=models.Q(internal=True, superadmin=True),
                name='single_internal_superadmin_role',
            ),
        ]

    @classmethod
    def superadmin_role(cls) -> Self:
        return cls(name=SUPERADMIN_ROLE_NAME, internal=True, superadmin=True)

    def includes_permission(self, permission: str) -> bool:
        """
        Checks whether a string `permission` is 
        included in this role.

        Args
            permission: the permission to check

        Returns
            True if the permission is included in the role.
        """
        if self.superadmin:
            return True
        return permission in self.permissions


class Invite(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)

    token = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
