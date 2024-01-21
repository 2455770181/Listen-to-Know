# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_openid = models.CharField(unique=True, max_length=45, blank=True, null=True, db_comment='微信小程序的登录API返回的用户唯一标识符')
    user_session_key = models.CharField(unique=True, max_length=45, blank=True, null=True, db_comment='微信小程序的登录API返回的本次登录的会话密钥')
    user_token = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_user'
        db_table_comment = '用户基本信息表'
