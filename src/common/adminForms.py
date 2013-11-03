from django import forms

class CommonAdminForm(forms.ModelForm):
    class Meta:
        exclude = ('created_by', 'modified_by')
