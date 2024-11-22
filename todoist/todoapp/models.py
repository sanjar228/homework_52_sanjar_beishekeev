from django.db import models

status_choices = [('new', 'Новая'),('in_progress','В процессе'), ('done','Сделано')]

class Todo(models.Model):
    desc = models.CharField(max_length=256, verbose_name='Описание')
    status = models.CharField(max_length=64, choices=status_choices, verbose_name='Статус', default='new')
    date = models.DateField(null=True, blank=True)