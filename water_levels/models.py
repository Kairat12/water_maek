from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.timezone import now


class InputOutputWater(models.Model):
    input_water = models.FloatField(verbose_name='Выработка питьевой воды', null=True, blank=True)
    output_water = models.FloatField(verbose_name='Потребление питьевой воды', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создание', default=now, editable=False)
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)


class RPV5(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)
    # time_1 = models.FloatField(verbose_name='t1(1.29)', blank=True, null=True)
    # time_2 = models.FloatField(verbose_name='t1(1.09)', blank=True, null=True)
    input_output_water = models.ForeignKey(InputOutputWater, on_delete=models.CASCADE, verbose_name='Вход/Выход воды', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.value}'

    # def save(self, *args, **kwargs):
    #     try:
    #         output_water = self.input_output_water.output_water
    #         if output_water is not None and output_water != 0:
    #             self.time_1 = ((self.value - 5100) * 3) / output_water if self.value > 5100 else 0
    #             self.time_2 = ((self.value - 4300) * 3) / output_water if self.value > 4300 else 0
    #     except ObjectDoesNotExist:
    #         self.time_1 = 0
    #         self.time_2 = 0
    #
    #     super().save(*args, **kwargs)

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
    # time_1 = models.FloatField(verbose_name='t1(1.29)', blank=True, null=True)
    # time_2 = models.FloatField(verbose_name='t1(1.09)', blank=True, null=True)
    input_output_water = models.ForeignKey(InputOutputWater, on_delete=models.CASCADE, verbose_name='Вход/Выход воды', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.value}'

    # def save(self, *args, **kwargs):
    #     try:
    #         output_water = self.input_output_water.output_water
    #         if output_water is not None and output_water != 0:
    #             self.time_1 = ((self.value - 5100) * 3) / output_water if self.value > 5100 else 0
    #             self.time_2 = ((self.value - 4300) * 3) / output_water if self.value > 4300 else 0
    #     except ObjectDoesNotExist:
    #         self.time_1 = 0
    #         self.time_2 = 0
    #
    #     super().save(*args, **kwargs)

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
    input_output_water = models.ForeignKey(InputOutputWater, on_delete=models.CASCADE, verbose_name='Вход/Выход воды', blank=True, null=True)
    # time_1 = models.FloatField(verbose_name='t1(1.29)', blank=True, null=True)
    # time_2 = models.FloatField(verbose_name='t1(1.09)', blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     try:
    #         output_water = self.input_output_water.output_water
    #         if output_water is not None and output_water != 0:
    #             self.time_1 = ((self.value - 6300) * 3) / output_water if self.value > 6300 else 0
    #             self.time_2 = ((self.value - 5300) * 3) / output_water if self.value > 5300 else 0
    #     except ObjectDoesNotExist:
    #         self.time_1 = 0
    #         self.time_2 = 0

    def __str__(self):
        return f'{self.record_time}-{self.value}'

    class Meta:
        verbose_name = 'РПВ-7'
        verbose_name_plural = 'РПВ-7'


class OtherRPV(models.Model):
    tsuvs2 = models.FloatField(verbose_name='ЦУВС-2 - ЦУВС-3')
    tsuvs3 = models.FloatField(verbose_name='ЦУВС-3 - город', null=True, blank=True)
    tes1 = models.FloatField(verbose_name=' Зад.85- ТЭЦ-1 ', null=True, blank=True)
    prom_zona = models.FloatField(verbose_name='Пром. Зона', null=True, blank=True)
    tsuvs4 = models.FloatField(verbose_name='ЦУВС-2-ЦУВС- 4', null=True, blank=True)
    pri_ozerny = models.FloatField(verbose_name='Приозерный (счетчик)', null=True, blank=True)
    mor_port = models.FloatField(verbose_name=' СЭЗ   морпорт (счетчик)', null=True, blank=True)
    kaz_gaz_aimak = models.FloatField(verbose_name='КазГазАймак (счетчик)', null=True, blank=True)
    kaspi_ecology = models.FloatField(verbose_name='Каспий Эколоджи (счетчик)', null=True, blank=True)
    sn = models.FloatField(verbose_name='Собственные нужды', null=True, blank=True)

    def __str__(self):
        return f'{self.tsuvs2}'


class RPPV1(models.Model):
    level = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=0.5)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.level}'

    class Meta:
        verbose_name = 'РППВ-1'
        verbose_name_plural = 'РППВ-1'


class RPPV2(models.Model):
    level = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=0.5)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.level}'

    class Meta:
        verbose_name = 'РППВ-2'
        verbose_name_plural = 'РППВ-2'


class BRD3(models.Model):
    level = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=0.5)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.level}'

    class Meta:
        verbose_name = 'БРД-3'
        verbose_name_plural = 'БРД-3'


class BRD4(models.Model):
    level = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=0.5)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.level}'

    class Meta:
        verbose_name = 'БРД-4'
        verbose_name_plural = 'БРД-4'


class RPV1(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.value}'

    class Meta:
        verbose_name = 'РПВ-1'
        verbose_name_plural = 'РПВ-1'


class RPV2(models.Model):
    value = models.FloatField(verbose_name='Уровень')
    critical_level = models.FloatField(verbose_name='Критическое значение', default=1.09)
    consumption = models.FloatField(verbose_name='Расход', null=True, blank=True)
    pressure = models.FloatField(verbose_name='Давление', null=True, blank=True)
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)

    def __str__(self):
        return f'{self.record_time}-{self.value}'

    class Meta:
        verbose_name = 'РПВ-2'
        verbose_name_plural = 'РПВ-2'


class DGO(models.Model):
    tec_1 = models.FloatField(verbose_name='ТЭЦ-1', null=True, blank=True)
    tec_2 = models.FloatField(verbose_name='ТЭЦ-2', null=True, blank=True)
    tes = models.FloatField(verbose_name='ТЭС', null=True, blank=True)
    kaz_azot = models.FloatField(verbose_name='КазАзот', null=True, blank=True)
    total = models.FloatField(verbose_name='Итого ДГО:', null=True, blank=True)
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создание', default=now)

    def __str__(self):
        return f'{self.record_time}-{self.tec_1}'

    class Meta:
        verbose_name = 'ДГО'
        verbose_name_plural = 'ДГО'

class DOP(models.Model):
    poliv = models.FloatField(verbose_name='Полив', null=True, blank=True)
    dop_left = models.FloatField(verbose_name='ДОП в цех №2 (левый)', null=True, blank=True)
    dop_right = models.FloatField(verbose_name='ДОП в цех №2 (правый)', null=True, blank=True)
    dop_ceh_2 = models.FloatField(verbose_name='ДОП в цех №2', null=True, blank=True)
    cn = models.FloatField(verbose_name='СН', null=True, blank=True)
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)
    total = models.FloatField(verbose_name='Итого ДОП:', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создание', default=now)

    def __str__(self):
        return f'{self.record_time}-{self.tec_1}'

    class Meta:
        verbose_name = 'ДОП'
        verbose_name_plural = 'ДОП'

class Temperature(models.Model):
    temp = models.FloatField(verbose_name='Температура', null=True, blank=True)
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создание', default=now)

    def __str__(self):
        return f'{self.temp}'
    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температура'

class DOPInput(models.Model):
    dop_left = models.FloatField(verbose_name='Приход ДОП в цех №2  (левый)')
    dop_right = models.FloatField(verbose_name='Приход ДОП в цех №2  (правый)')
    record_time = models.DateTimeField(verbose_name='Время записи', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создание', default=now)

    class Meta:
        verbose_name = 'Приход ДОП в цех №2 '
        verbose_name_plural = 'Приход ДОП в цех №2 '
