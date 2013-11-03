from django.contrib import admin
from events import models
from common.admin import CommonAdmin
from adminForms import EventAdminForm, EventRoleAdminForm

class EventAdmin(CommonAdmin):
    form = EventAdminForm        
admin.site.register(models.Event, EventAdmin)

class EventRoleAdmin(CommonAdmin):
    form = EventRoleAdminForm
admin.site.register(models.EventRole, EventRoleAdmin)
    
class EventMembershipAdmin(CommonAdmin):
    pass
admin.site.register(models.EventMembership, EventMembershipAdmin)
