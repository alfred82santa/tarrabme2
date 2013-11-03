from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from orgs.models import Organization

class User(AbstractUser):
    avatar = ProcessedImageField(
        upload_to="avatars",
        processors=[ResizeToFill(200, 200)],
        )
    main_organization = models.ForeignKey(
        Organization,
        related_name="members",
        null=True,
        on_delete=models.SET_NULL
    )
