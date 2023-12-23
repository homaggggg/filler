# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True, verbose_name='Примечание')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    telefon = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телефон')
    kabinet = models.CharField(max_length=50, null=True, blank=True, verbose_name='Кабинет')
    dolgnost = models.CharField(max_length=50, null=True, blank=True, verbose_name='Должность')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        ordering = ['user']

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Profile._meta.fields]
