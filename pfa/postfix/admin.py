from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models


admin.site.register(models.Domain)
admin.site.register(models.Mailbox)
admin.site.register(models.Alias)
admin.site.register(models.Vacation)
admin.site.register(models.Log)
