# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __unicode__(self):
        return '%d %s %s' % (self.employee_id,self.employee_name,self.email)
