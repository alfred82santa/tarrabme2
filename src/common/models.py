from django.db import models
from django.conf import settings


class CommonModel(models.Model):
    creation_date = models.DateTimeField(
        'creation datetime',
        auto_now_add=True)
    modified_date = models.DateTimeField('modified datetime', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                   null=True, on_delete=models.SET_NULL,
                                   related_name="created_%(app_label)s_%(class)s",
                                   )
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                    null=True, on_delete=models.SET_NULL,
                                    related_name="modification_%(app_label)s_%(class)s",
                                    )

    class Meta:
        abstract = True
        
class AbstractAddress(CommonModel):
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=126)
    country = models.CharField(max_length=126)
    
    class Meta:
        abstract = True
        
class AbstractContact(AbstractAddress):
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)

    class Meta:
        abstract = True
