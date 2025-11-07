from django.db import models

class Incident(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыт'),
        ('in_progress', 'В работе'),
        ('resolved', 'Решён'),
    ]

    SOURCE_CHOICES = [
        ('operator', 'Оператор'),
        ('monitoring', 'Мониторинг'),
        ('partner', 'Партнёр'),
    ]

    description = models.TextField(verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open',
        verbose_name='Статус',
    )
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        verbose_name='Источник',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )

    def __str__(self):
        return f"[{self.get_status_display()}] {self.description[:50]}"

