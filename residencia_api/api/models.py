from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Añadir un related_name único
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Añadir un related_name único
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Room(models.Model):
    number = models.CharField(max_length=5)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.number

class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    room = models.OneToOneField(Room, null=True, blank=True, on_delete=models.SET_NULL)
    medical_info = models.TextField()
    activities = models.ManyToManyField('Activity', related_name='residents', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name

