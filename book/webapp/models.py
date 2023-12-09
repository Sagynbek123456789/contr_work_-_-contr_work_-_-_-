from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'В Заблокировано')]


# Create your models here.
class Task(models.Model):
    author = models.CharField(max_length=60, null=False, blank=False, verbose_name='автор')
    mail = models.EmailField(max_length=70, null=False, blank=False, verbose_name='почта')
    description = models.TextField(max_length=50, null=False, blank=False, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_choices, default='active',
                              verbose_name='Статус')

    def __str__(self):
        return f"{self.author} - {self.description[:50]}"


