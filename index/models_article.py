# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TsContentArticle(models.Model):
    _user_model_dict = {}
    article_id = models.PositiveIntegerField(primary_key=True, db_comment='文章ID')
    content = models.TextField(blank=True, null=True)

    @classmethod
    def set_db_table(cls, index):
        table_name = f'ts_content_{index}'
        print(table_name)
        if table_name in cls._user_model_dict:
            return cls._user_model_dict[table_name]

        class Meta:
            db_table = table_name

        attrs = {
            '__module__': cls.__module__,
            'Meta': Meta
        }

        user_db_model = type(str('Ts_content_%d') % index, (cls,), attrs)
        cls._user_model_dict[table_name] = user_db_model
        return user_db_model

    class Meta:
        managed = False
        db_table_comment = '文章内容'
        abstract = True





class TsContentArticleMul(models.Model):
    _user_model_dict = {}
    article_id = models.PositiveIntegerField(primary_key=True, db_comment='文章ID')  # The composite primary key (article_id, page_num) found, that is not supported. The first column is selected.
    page_num = models.PositiveSmallIntegerField(db_comment='页码')
    content = models.TextField(blank=True, null=True)

    @classmethod
    def set_db_table(cls, index):
        table_name = f'ts_content_mul_{index}'
        print(table_name)
        if table_name in cls._user_model_dict:
            return cls._user_model_dict[table_name]

        class Meta:
            db_table = table_name

        attrs = {
            '__module__': cls.__module__,
            'Meta': Meta
        }

        user_db_model = type(str('Ts_content_mul_%d') % index, (cls,), attrs)
        cls._user_model_dict[table_name] = user_db_model
        return user_db_model

    class Meta:
        managed = False
        unique_together = (('article_id', 'page_num'),)
        db_table_comment = '文章内容'
        abstract = True


