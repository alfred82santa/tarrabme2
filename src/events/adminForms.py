from models import Event, EventRole
from common.adminForms import CommonAdminForm

class EventAdminForm(CommonAdminForm):
    class Meta(CommonAdminForm.Meta):
        model = Event
        
class EventRoleAdminForm(CommonAdminForm):
    class Meta(CommonAdminForm.Meta):
        model = EventRole
