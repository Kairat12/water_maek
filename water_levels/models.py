from django.db import models
from django.utils.timezone import now


# Create your models here.
class RPV5(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-5'
        verbose_name_plural = 'РПВ-5'

class RPV6(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-6'
        verbose_name_plural = 'РПВ-6'

class RPV7(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.39)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'РПВ-7'
        verbose_name_plural = 'РПВ-7'

class OtherRPV(models.Model):
    tsuvs2 = models.FloatField(verbose_name='ЦУВС-2 - ЦУВС-3')
    tsuvs3 = models.FloatField(verbose_name='ЦУВС-3 - город', null=True, blank=True)
    tes1 = models.FloatField(verbose_name=' Зад.85- ТЭЦ-1 ', null=True, blank=True)
    prom_zona = models.FloatField(verbose_name='Пром. Зона', null=True, blank=True)
    tsuvs4 = models.FloatField(verbose_name='ЦУВС-2-ЦУВС- 4', null=True, blank=True)
    pri_ozerny = models.FloatField(verbose_name='Приозерный (счетчик)',null=True, blank=True)
    mor_port = models.FloatField(verbose_name=' СЭЗ   морпорт (счетчик)',null=True ,blank=True)
    kaz_gaz_aimak = models.FloatField(verbose_name='КазГазАймак (счетчик)',null=True, blank=True)
    kaspi_ecology = models.FloatField(verbose_name='Каспий Эколоджи (счетчик)',null=True, blank=True)
    sn = models.FloatField(verbose_name='Собственные нужды', null=True, blank=True)

    def __str__(self):
        return f'{self.tsuvs2}'
