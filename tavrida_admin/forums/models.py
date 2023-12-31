import random
import uuid
from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField


def random_code():
    return random.randint(1000, 9999)


class Forum(models.Model):
    id = models.UUIDField(primary_key=True, db_column="Id", default=uuid.uuid4)
    logo_url = models.ImageField(max_length=2048, db_column="LogoUrl", verbose_name="Ссылка на логотип")
    image_urls = ArrayField(
        models.TextField(), null=True, blank=True, db_column="ImageUrls", verbose_name="Изображения"
    )
    title = models.CharField(max_length=256, db_column="Title", verbose_name="Название")
    description = models.CharField(max_length=1024, db_column="Description", verbose_name="Описание")
    started_at = models.DateTimeField(db_column="StartedAt", verbose_name="Время начала")
    ended_at = models.DateTimeField(null=True, blank=True, db_column="EndedAt", verbose_name="Время окончания")
    deleted_at = models.DateTimeField(null=True, blank=True, db_column="DeletedAt", verbose_name="Время удаления")
    map_urls = ArrayField(
        models.TextField(), null=True, blank=True, db_column="MapUrls", verbose_name="Ссылки на карты"
    )
    # user_id = models.ForeignKey()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "Forums"
        verbose_name = "форум"
        verbose_name_plural = "форумы"


class Model(models.Model):
    id = models.UUIDField(primary_key=True, db_column="Id", default=uuid.uuid4)
    logo_url = models.ImageField(max_length=2048, db_column="LogoUrl", verbose_name="Изображение")
    title = models.CharField(max_length=256, db_column="Title", verbose_name="Название")
    description = models.TextField(max_length=512, db_column="Description", verbose_name="Описание")
    value_url = models.FileField(db_column="ValueUrl", verbose_name="Модель")
    updated_at = models.DateTimeField(
        default=datetime.now, blank=True, db_column="UpdatedAt", verbose_name="Время окончания"
    )
    deleted_at = models.DateTimeField(null=True, blank=True, db_column="DeletedAt", verbose_name="Время удаления")
    count_views = models.IntegerField(db_column="CountViews", default=0, verbose_name="Количество просмотров")
    count_likes = models.IntegerField(db_column="CountLikes", default=0, verbose_name="Количество лайков")
    code = models.CharField(
        max_length=4, db_column="Code", verbose_name="Уникальный код", default=random_code, unique=True
    )
    forum = models.ForeignKey("Forum", on_delete=models.CASCADE, db_column="ForumId")
    created_at = models.DateTimeField(
        default=datetime.now, blank=True, db_column="CreatedAt", verbose_name="Время удаления"
    )
    # user_id = models.ForeignKey()

    class Meta:
        db_table = "Models"
        verbose_name = "модель"
        verbose_name_plural = "модели"
