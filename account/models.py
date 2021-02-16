from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'


class Card(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    ls = models.ForeignKey(
        'List',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Список'
    )

    class Meta:
        verbose_name_plural = 'Карточки'
        verbose_name = 'Карточка'
        ordering = ['-title']


class List(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    
    profile = models.ForeignKey(
        'Profile',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Профиль'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Списки'
        verbose_name = 'Список'


# Signals:

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()