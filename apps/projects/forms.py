from django import forms

class CreateProject(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    project_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'flex-1 focus:outline-0'})
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'flex-1 focus:outline-0 resize-y px-2 py-1', 'rows': '4', 'placeholder': 'What this project is for'})
    )