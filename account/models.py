from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Card(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    status_choice = (
        ('N', 'Не выполнено'),
        ('W', 'В работе'),
        ('Y', 'Выполнено'),
    )

    status = models.CharField(
        max_length=1,
        choices=status_choice,
        default='N',
        verbose_name='Статус',
    )

    date_end = models.DateField(
        null=True,
        blank=True,
        default=timezone.now,
        verbose_name='Срок',
    )
    
    ls = models.ForeignKey(
        'List',
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Список',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Карточки'
        verbose_name = 'Карточка'
        ordering = ['-title']


class List(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
    )
    
    board = models.ForeignKey(
        'Board',
        on_delete=models.CASCADE,
        verbose_name='Доска',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Списки'
        verbose_name = 'Список'


class Board(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
    )

    creator = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        verbose_name='Создатель',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Доски'
        verbose_name = 'Доска' 


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True,
    )

    cards = models.ManyToManyField(
        Card,
        verbose_name='Карточки',
    )

    boards = models.ManyToManyField(
        Board,
        verbose_name='Доски',
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'


# Signals:

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()