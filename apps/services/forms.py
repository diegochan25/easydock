from django import forms

from apps.services.catalog import DATABASES, RUNTIMES


class CreateDatabaseService(forms.Form):
    dbms = forms.ChoiceField(choices=[(d.slug, d.label) for d in DATABASES])


class CreateFunctionService(forms.Form):
    runtime = forms.ChoiceField(choices=[(r.slug, r.label) for r in RUNTIMES])
