from django.db import models
from django.urls import reverse

from .validators import validate_file_extension


class Category(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True,
        help_text="请输入分类",
        verbose_name="名称"
    )
    icon = models.ForeignKey(
        'Icon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="图标"
    )
    weight = models.PositiveIntegerField(
        default=0,
        help_text="请输入正数，最大100",
        verbose_name="权重"
    )
    father = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="请选择父类别，可以为空",
        verbose_name="父类别"
    )
    app = models.ManyToManyField('App')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别"


class Icon(models.Model):
    title = models.CharField(
        max_length=16,
        unique=True,
        help_text="请输入图标标题"
    )
    icon = models.ImageField(
        upload_to="icon/",
        validators=[validate_file_extension],
        null=True,
        blank=True
    )
    path = models.CharField(max_length=100,
                            null=True,
                            unique=True,
                            help_text="请输入图标地址")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "图标"
        verbose_name_plural = "图标"


class App(models.Model):
    name = models.CharField(
        max_length=16,
        unique=True,
        help_text="请输入站点名称"
    )
    site = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=100,
        help_text="简介"
    )
    image = models.ForeignKey(
        'Icon',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('app-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "应用"
        verbose_name_plural = "应用"

