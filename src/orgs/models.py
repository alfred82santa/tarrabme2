from django.db import models
from common.models import CommonModel, AbstractContact, AbstractAddress
from django.contrib.auth.models import Group
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

class Organization(CommonModel):
    name = models.CharField(max_length=100, unique=True)
    commercial_name = models.CharField(max_length=150, unique=True)
    prefix = models.CharField(max_length=6, unique=True)
    active = models.BooleanField('active', default=True)
    logo = ProcessedImageField(
        upload_to="logos",
        processors=[ResizeToFill(400, 400)],
        )
        
    logo_thumbnail = ImageSpecField(source='logo',
        processors=[ResizeToFill(50, 50)],)
        
    def logo_thumbnail_img(self):
        return '<img src="%s"/>' % self.logo_thumbnail.url
    logo_thumbnail_img.allow_tags = True
    logo_thumbnail_img.short_description = ''

    class Meta:
        pass

    def __unicode__(self):
        return self.name

class Contact(AbstractContact):
    organization = models.ForeignKey(Organization, blank=False,
                                     null=False, related_name="contacts_list"
                                     )


class BillingAccount(AbstractAddress):
    fiscal_number = models.CharField(max_length=126, unique=True)

    payment_method = models.CharField(max_length=126, unique=True)
    payment_data = models.CharField(max_length=126, unique=True)

    organization = models.ForeignKey(Organization, blank=False,
                                     null=False, related_name="contacts"
                                     )


class OrganizationRole(Group):
    organization = models.ForeignKey(Organization, blank=False,
                                     null=False, related_name="roles"
                                     )

