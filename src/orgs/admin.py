from django.contrib import admin
from .models import Organization
from .adminForms import OrgAdminForm
from common.admin import CommonAdmin

class OrgAdmin(CommonAdmin):
    form = OrgAdminForm
    
    actions_on_top = True
    actions_on_bottom = False
    
    list_display = ('logo_thumbnail_img', 'name', 'commercial_name', 'prefix', )
    list_filter = ('active',)
        

		
admin.site.register(Organization, OrgAdmin)
