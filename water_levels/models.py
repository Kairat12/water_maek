from django.db import models

# Create your models here.
class RPV5(models.Model):
    value = models.FloatField(verbose_name='Значение')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-5'
        verbose_name_plural = 'РПВ-5'

class RPV6(models.Model):
    value = models.FloatField(verbose_name='Значение')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-6'
        verbose_name_plural = 'РПВ-6'

class RPV7(models.Model):
    value = models.FloatField(verbose_name='Значение')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.39)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-7'
        verbose_name_plural = 'РПВ-7'
