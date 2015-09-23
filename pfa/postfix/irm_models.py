from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Admin(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=5)
    passwordlastchange = models.DateTimeField()
    settings = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'admin'


class Alias(models.Model):
    address = models.CharField(primary_key=True, max_length=255)
    goto = models.TextField()
    name = models.CharField(max_length=255)
    moderators = models.TextField()
    accesspolicy = models.CharField(max_length=30)
    domain = models.CharField(max_length=255)
    islist = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'alias'


class AliasDomain(models.Model):
    alias_domain = models.CharField(primary_key=True, max_length=255)
    target_domain = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'alias_domain'


class AnyoneShares(models.Model):
    from_user = models.CharField(primary_key=True, max_length=255)
    dummy = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'anyone_shares'


class DeletedMailboxes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    timestamp = models.DateTimeField()
    username = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    maildir = models.CharField(max_length=255)
    admin = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'deleted_mailboxes'


class Domain(models.Model):
    domain = models.CharField(primary_key=True, max_length=255)
    description = models.TextField()
    disclaimer = models.TextField()
    aliases = models.BigIntegerField()
    mailboxes = models.BigIntegerField()
    maxquota = models.BigIntegerField()
    quota = models.BigIntegerField()
    transport = models.CharField(max_length=255)
    settings = models.TextField()
    backupmx = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'domain'


class DomainAdmins(models.Model):
    username = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'domain_admins'


class Mailbox(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=5)
    storagebasedirectory = models.CharField(max_length=255)
    storagenode = models.CharField(max_length=255)
    maildir = models.CharField(max_length=255)
    quota = models.BigIntegerField()
    domain = models.CharField(max_length=255)
    transport = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    employeeid = models.CharField(max_length=255, blank=True)
    isadmin = models.SmallIntegerField()
    isglobaladmin = models.SmallIntegerField()
    enablesmtp = models.SmallIntegerField()
    enablesmtpsecured = models.SmallIntegerField()
    enablepop3 = models.SmallIntegerField()
    enablepop3secured = models.SmallIntegerField()
    enableimap = models.SmallIntegerField()
    enableimapsecured = models.SmallIntegerField()
    enabledeliver = models.SmallIntegerField()
    enablelda = models.SmallIntegerField()
    enablemanagesieve = models.SmallIntegerField()
    enablemanagesievesecured = models.SmallIntegerField()
    enablesieve = models.SmallIntegerField()
    enablesievesecured = models.SmallIntegerField()
    enableinternal = models.SmallIntegerField()
    enabledoveadm = models.SmallIntegerField()
    enablelib_storage = models.SmallIntegerField(db_column='enablelib-storage')  # Field renamed to remove unsuitable characters.
    enablelmtp = models.SmallIntegerField()
    lastlogindate = models.DateTimeField()
    lastloginipv4 = models.GenericIPAddressField()
    lastloginprotocol = models.CharField(max_length=255)
    disclaimer = models.TextField()
    allowedsenders = models.TextField()
    rejectedsenders = models.TextField()
    allowedrecipients = models.TextField()
    rejectedrecipients = models.TextField()
    settings = models.TextField()
    passwordlastchange = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()
    local_part = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mailbox'


class RecipientBccDomain(models.Model):
    domain = models.CharField(primary_key=True, max_length=255)
    bcc_address = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'recipient_bcc_domain'


class RecipientBccUser(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    bcc_address = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'recipient_bcc_user'


class SenderBccDomain(models.Model):
    domain = models.CharField(primary_key=True, max_length=255)
    bcc_address = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sender_bcc_domain'


class SenderBccUser(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    bcc_address = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()
    active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sender_bcc_user'


class ShareFolder(models.Model):
    from_user = models.CharField(max_length=255)
    to_user = models.CharField(max_length=255)
    dummy = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'share_folder'


class UsedQuota(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    bytes = models.BigIntegerField()
    messages = models.BigIntegerField()
    domain = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'used_quota'
