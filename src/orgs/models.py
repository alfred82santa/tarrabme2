from django.db import models
from common.models import CommonModel
from django.contrib.auth.models import Group

class Organization(CommonModel):
    name = models.CharField(max_length=100, unique=True)
    commercial_name = models.CharField(max_length=150, unique=True)
    prefix = models.CharField(max_length=6, unique=True)
    active = models.BooleanField('active', default=True)
 #   members = models.ManyToManyField(User, through='Membership', related_name="organizations")
    class Meta:
        pass
    def __unicode__(self):
        return self.name
        
        
class OrganizationContact(CommonModel):
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    
    organization = models.ForeignKey(Organization, blank=False,
                                     null=False, related_name="contacts"
                                     )
    
class BillingAccount(CommonModel):
    fiscal_number = models.CharField(max_length=126, unique=True)
    
    payment_method = models.CharField(max_length=126, unique=True)
    payment_data = models.CharField(max_length=126, unique=True)
        
    address = models.ForeignKey(OrganizationContact, blank=False,
                                null=False, related_name="billing_accounts"
                               )
    organization = models.ForeignKey(Organization, blank=False,
                                 null=False, related_name="contacts"
                                 )
    
class OrganizationRole(Group):
    organization = models.ForeignKey(Organization, blank=False,
                                     null=False, related_name="roles"
                                     )
                                     
class User(BaseUser):
    picture = models.FileField(upload_to="pictures")
    main_organization = models.ForeignKey(
        Organization, 
        related_name="members", 
        null=True,
        on_delete=models.SET_NULL
    )
