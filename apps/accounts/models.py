from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.plants.models import PlantedTree, Plant
from django.shortcuts import get_object_or_404

class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, \
                digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, unique=True)
    about = models.TextField(max_length=500, blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    UNIQUE_FIELDS = ['email']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email.split('@')[0]
        super(User, self).save(*args, **kwargs)

    def plant_tree(self, tree, location):
        '''
            This method is called when a user plants a tree
            getting a tree id (int) and a location (tuple)
            and create the planted tree object
        '''
        try:
            tree = get_object_or_404(Plant, pk=tree)
            PlantedTree.objects.create(
                user=self,
                tree=tree,
                latitude=location[0],
                longitude=location[1]
            )
        except Exception as e:
            return e

    def plant_trees(self, plants):
        '''
            This method receives one array containing the
            tree ids and tuples of their locations
            and create the planted tree object
        '''
        for index, plant in enumerate(plants, start=0):
            try:
                tree = get_object_or_404(Plant, pk=plant[0])
                PlantedTree.objects.create(
                    user=self,
                    tree=tree,
                    latitude=plant[1][0],
                    longitude=plant[1][1]
                )
                print('Created')
            except Exception as e:
                return e


class Accounts(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name="users", blank=True)

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
