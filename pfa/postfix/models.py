# models.py
from os.path import normpath, join

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
#from django.utils.translation import ugettext as _

import logging
import datetime

from django.utils.encoding import python_2_unicode_compatible

def now_plus(delta_days=3650):
    return datetime.datetime.now() + datetime.timedelta(days=delta_days)

logger = logging.getLogger(__name__)

@python_2_unicode_compatible
class Domain(models.Model):
    TRANSPORT_CHOICES = [(x, x) for x in ('virtual', 'relay', 'smtp')]
    domain = models.CharField(blank=False, max_length=127, unique=True)
    description = models.CharField(max_length=255, default='', blank=True)
    aliases = models.IntegerField(blank=False, default=0)
    mailboxes = models.IntegerField(blank=False, default=0)
    maxquota = models.IntegerField(blank=False, default=0)
    quota = models.IntegerField(blank=False, default=0)
    transport = models.CharField(
        max_length=8, choices=TRANSPORT_CHOICES, default='virtual')
    backupmx = models.BooleanField(blank=False, default=False)
    created = models.DateTimeField(blank=False, auto_now_add=True)
    modified = models.DateTimeField(blank=False, auto_now=True)
    expired = models.DateTimeField(blank=False, default=now_plus())
    active = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return "{0} -> {1}".format(self.domain, self.transport)

    def get_absolute_url(self):
        return reverse('pfa:domain:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'domain'
        verbose_name_plural = "domain"
        verbose_name_plural = "domains"
        ordering = ['domain']

@python_2_unicode_compatible
class Mailbox(models.Model):
    domain = models.ForeignKey(Domain, related_name="maiilbox_domain")
    email = models.EmailField(blank=False, max_length=255)
    password = models.CharField(blank=False, max_length=255)
    maildir = models.CharField(
        blank=False, max_length=255, default='never get here')
    quota = models.IntegerField(blank=False, default=0)
    created = models.DateTimeField(blank=False, auto_now_add=True)
    modified = models.DateTimeField(blank=False, auto_now=True)
    expired = models.DateTimeField(blank=False, default=now_plus())
    active = models.BooleanField(blank=False, default=True)

    def get_absolute_url(self):
        return reverse('mailbox_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.maildir = normpath(
                join(settings.PFA_DEFAULT_MAILDIR, self.email))
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}, {1}".format(self.email, self.active)

    class Meta:
        db_table = 'mailbox'
        verbose_name_plural = "mailbox"
        verbose_name_plural = "mailboxes"
        ordering = ['domain', 'email']


@python_2_unicode_compatible
class Alias(models.Model):
    address = models.CharField(blank=False, max_length=255, unique=True)
    goto = models.CharField(max_length=255)
    domain = models.ForeignKey(
        Domain, blank=False, related_name='alias_domain')
    created = models.DateTimeField(blank=False, auto_now_add=True)
    modified = models.DateTimeField(blank=False, auto_now=True)
    expired = models.DateTimeField(blank=False, default=now_plus())
    active = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return "{0} -> {1}".format(self.address, self.goto)

    class Meta:
        db_table = 'alias'
        verbose_name_plural = "alias"
        verbose_name_plural = "aliases"
        ordering = ['domain', 'address']

@python_2_unicode_compatible
class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    username = models.CharField(max_length=63)
    domain = models.CharField(max_length=63)
    action = models.CharField(max_length=255)
    data = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(self.timestamp, self.username, self.action)

    class Meta:
        db_table = 'log'
        verbose_name_plural = "log"
        verbose_name_plural = "logs"
        ordering = ['timestamp']

@python_2_unicode_compatible
class Vacation(models.Model):
    email = models.ForeignKey(
        Mailbox, blank=False, related_name='vacation_email')
    subject = models.CharField(blank=False, max_length=255)
    body = models.CharField(blank=False, max_length=255)
    cache = models.CharField(max_length=255)
    domain = models.ForeignKey(
        Domain, blank=False,  related_name='vacation_domain')
    created = models.DateTimeField(blank=False, auto_now_add=True)
    modified = models.DateTimeField(blank=False, auto_now=True)
    expired = models.DateTimeField(blank=False, default=now_plus())
    active = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return "{0}, {1}".format(self.email, self.active)

    class Meta:
        db_table = 'vacation'
        verbose_name_plural = "vacation"
        verbose_name_plural = "vacations"
        ordering = ['email']
