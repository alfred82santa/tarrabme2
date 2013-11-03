from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission, GroupManager
from common.models import CommonModel
from orgs.models import Organization
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.forms import Textarea

class Event(CommonModel):
    name = models.CharField(max_length=100, unique=True)
    commercial_name = models.CharField(max_length=150, unique=True)
    prefix = models.CharField(max_length=4, unique=True)
    organizations = models.ManyToManyField(Organization, 
        through='EventMembership', related_name="events")
    start_date = models.DateTimeField(_('Start datetime'), required=True)
    end_date = models.DateTimeField(_('End datetime'))

    description = models.TextField(db_index=True)

    logo = ProcessedImageField(
        upload_to="logos",
        processors=[ResizeToFit(900, 900)],
        )
        
    logo_thumbnail = ImageSpecField(source='logo',
        processors=[ResizeToFill(50, 50)],)
    logo_header = ImageSpecField(source='logo',
        processors=[ResizeToFit(900, 200)],)
    def __unicode__(self):
        return self.name

class EventRole(CommonModel):
    name = models.CharField(max_length=100, validators=[ 
        MinLengthValidator(4), 
        RegexValidator( 
            regex="^[a-z0-9_]+$", 
            message=_("Organization role name must be a string with just letters and number without spaces") 
            ) 
        ])
    permissions = models.ManyToManyField(Permission,
        verbose_name=_('permissions'), blank=True)

    objects = GroupManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
    event = models.ForeignKey(Event, related_name="organizaion_roles")
    caption = models.CharField(max_length=100, validators=[ 
            MinLengthValidator(4) 
        ])
        
    class Meta:
        unique_together = (("name", "event"),("caption", "event"),)
        verbose_name = _('event role')
        verbose_name_plural = _('event roles')
    def __unicode__(self):
        return self.caption

class EventSequence(CommonModel):
    name = models.CharField(max_length=100, unique=True, validators=[ 
        MinLengthValidator(4), 
        RegexValidator( 
            regex="^[a-z0-9_]+$", 
            message=_("Organization role name must be a string with just letters and number without spaces") 
            ) 
        ])
    event = models.ForeignKey(Event, related_name="organizaion_roles")

    objects = EventSequenceManager()

    def __unicode__(self):
        return self.name
        
    class Meta:
        unique_together = (("name", "event"),("caption", "event"),)
        verbose_name = _('event role')
        verbose_name_plural = _('event roles')
    def __unicode__(self):
        return self.caption

class EventMembership(models.Model):
    event = models.ForeignKey(Event)
    organization = models.ForeignKey(Organization, related_name="event_role")
    roles = models.ManyToManyField(EventRole)
    creation_date = models.DateTimeField('creation datetime', auto_now_add=True)
    modified_date = models.DateTimeField('modified datetime', auto_now=True)
    class Meta:
        unique_together = (("event", "organization"),)
    def __unicode__(self):
        return "%s in %s" % (self.organization.name, self.event.name)
        
def create_event(sender, instance, created, **kwargs):
    if created:
        EventRole.objects.create( 
                created_by=instance.created_by, 
                modified_by=instance.modified_by, 
                event=instance,
                name="organizer", 
                caption=_("Organizer"), 
            )
        EventRole.objects.create( 
                created_by=instance.created_by, 
                modified_by=instance.modified_by, 
                event=instance, 
                name="seller", 
                caption=_("Seller"),
            )
        EventRole.objects.create( 
                created_by=instance.created_by, 
                modified_by=instance.modified_by,
                event=instance, 
                name="ticket_checker", 
                caption=_("Ticket checker"), 
            )
           
models.signals.post_save.connect(create_event, sender=Event)

# Create your models here.
