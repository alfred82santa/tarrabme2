from django import forms
from .models import Organization
from common.adminForms import CommonAdminForm

class OrgAdminForm(CommonAdminForm):
    class Meta(CommonAdminForm.Meta):
        model = Organization
