from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # your custom fields here

        groups = models.ManyToManyField(
            Group,
            verbose_name=_('groups'),
            blank=True,
            help_text=_(
                'The groups this user belongs to. A user will get all permissions '
                'granted to each of their groups.'
            ),
            related_name="custom_user_set",
            related_query_name="user",
        )

        user_permissions = models.ManyToManyField(
            Permission,
            verbose_name=_('user permissions'),
            blank=True,
            help_text=_('Specific permissions for this user.'),
            related_name="custom_user_set",
            related_query_name="user",
        )


