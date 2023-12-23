# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

# Create your models here.
class Forlog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    edesc = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    erem = models.BooleanField(default=False, verbose_name='Удалить?')

    class Meta:
        abstract = True

class gurnal(Forlog):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Создатель')
    fiostud = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фио студента')
    facul = models.CharField(max_length=100, blank=True, null=True, verbose_name='Факультет')
    kafedra = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кафедра')
    groupnumber = models.CharField(max_length=100, blank=True, null=True, verbose_name='Учебная группа')
    napravlenie = models.CharField(max_length=100, blank=True, null=True, verbose_name='Направление подготовки (специальность)')
    vidpract = models.CharField(max_length=100, blank=True, null=True, verbose_name='Вид практики')
    rukpractic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Руководитель практики от маи фамилия и инициалы')
    familinic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фамилия с инициалами студента')
    datasdacha = models.DateTimeField(blank=True, null=True, verbose_name='Дата сдачи')
    datanach = models.DateTimeField(blank=True, null=True, verbose_name='Дата начала практики')
    datakonec = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания практики')
    predpriat = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название структурного подразделения (отдел, лаборатория)')
    zadanie = models.CharField(max_length=100, blank=True, null=True, verbose_name='Индивидуальное задание студенту ')
    dataotziv = models.DateTimeField(blank=True, null=True, verbose_name='Дата отзыва')

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in gurnal._meta.fields]

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'
