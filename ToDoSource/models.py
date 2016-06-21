# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BoardTbl(models.Model):
    board_id = models.AutoField(db_column='BOARD_ID', primary_key=True)  # Field name made lowercase.
    board_name = models.CharField(db_column='BOARD_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    group_id = models.IntegerField(db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    memebership_id = models.IntegerField(db_column='MEMEBERSHIP_ID', blank=True, null=True)  # Field name made lowercase.
    created_dttm = models.DateTimeField(db_column='CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOARD_TBL'


class GroupTbl(models.Model):
    group_id = models.AutoField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    group_code = models.CharField(db_column='GROUP_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    created_dttm = models.DateTimeField(db_column='CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUP_TBL'


class MembershipTbl(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    group_id = models.IntegerField(db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEMBERSHIP_TBL'


class PanelTbl(models.Model):
    panel_id = models.AutoField(db_column='PANEL_ID', primary_key=True)  # Field name made lowercase.
    panel_name = models.CharField(db_column='PANEL_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    board_id = models.IntegerField(db_column='BOARD_ID', blank=True, null=True)  # Field name made lowercase.
    create_dttm = models.DateTimeField(db_column='CREATE_DTTM', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PANEL_TBL'


class ReminderTbl(models.Model):
    seq_id = models.AutoField(db_column='SEQ_ID', primary_key=True)  # Field name made lowercase.
    task_id = models.IntegerField(db_column='TASK_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    reminder_type = models.CharField(db_column='REMINDER_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_emailid = models.CharField(db_column='USER_EMAILID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reminder_time = models.DateTimeField(db_column='REMINDER_TIME', blank=True, null=True)  # Field name made lowercase.
    reminder_timezone = models.CharField(db_column='REMINDER_TIMEZONE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REMINDER_TBL'


class TasksTbl(models.Model):
    task_id = models.AutoField(db_column='TASK_ID', primary_key=True)  # Field name made lowercase.
    task_name = models.CharField(db_column='TASK_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    panel_id = models.IntegerField(db_column='PANEL_ID', blank=True, null=True)  # Field name made lowercase.
    board_id = models.IntegerField(db_column='BOARD_ID', blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TASKS_TBL'


class UserProfileTbl(models.Model):
    user_id = models.AutoField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EMAILID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    avatar_url = models.ImageField(upload_to="profile")  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    access_token = models.CharField(db_column='ACCESS_TOKEN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastupd_dttm = models.DateTimeField(db_column='LASTUPD_DTTM', blank=True, null=True)  # Field name made lowercase.
    created_dttm = models.DateTimeField(db_column='CREATED_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_PROFILE_TBL'

