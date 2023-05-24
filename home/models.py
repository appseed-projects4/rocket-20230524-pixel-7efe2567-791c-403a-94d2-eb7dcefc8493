# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Type(models.Model):

    #__Type_FIELDS__
    txn_type = models.CharField(max_length=255, null=True, blank=True)
    txn_desc = models.CharField(max_length=255, null=True, blank=True)

    #__Type_FIELDS__END

    class Meta:
        verbose_name        = _("Type")
        verbose_name_plural = _("Type")


class Category(models.Model):

    #__Category_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    catgry_type = models.CharField(max_length=255, null=True, blank=True)
    catgry_desc = models.CharField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    txn_date = models.CharField(max_length=255, null=True, blank=True)
    txn_id = models.CharField(max_length=255, null=True, blank=True)
    txn_type = models.CharField(max_length=255, null=True, blank=True)
    catgry_type = models.CharField(max_length=255, null=True, blank=True)
    less_vat = models.CharField(max_length=255, null=True, blank=True)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")



#__MODELS__END
