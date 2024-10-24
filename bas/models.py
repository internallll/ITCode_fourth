from django.db import models
from django.utils.module_loading import module_has_submodule


class BusPark(models.Model):
  title = models.CharField(verbose_name='Название', max_length=255)
  address = models.CharField(verbose_name='Адрес', max_length=255)
  description = models.TextField(verbose_name='Описание', blank=True)
  phone_number = models.CharField(verbose_name='Номер телефона', max_length=11, blank=True)
  logo = models.ImageField(upload_to='media', null = True, blank = True)
  year_found = models.IntegerField(verbose_name='Год основания', null=True)

  class Meta:
    verbose_name='Автопарк'
    verbose_name_plural='Автопарки'
    ordering = ['-title']

  def __str__(self):
    return self.title

class Bus(models.Model):
  number = models.CharField(verbose_name='Госномер', max_length=255)
  type_of_bus = models.CharField(verbose_name='Тип автобуса', max_length=255)

  busPark = models.ForeignKey(
     'BusPark',
    verbose_name='Автопарк',
    blank=True,
    null=True,
    related_name='buses',
    on_delete=models.SET_NULL,
  )
  class Meta:
    verbose_name='Автобус'
    verbose_name_plural='Автобусы'
    ordering = ['-number']

  def __str__(self):
    return self.number


class Route(models.Model):
  title = models.CharField(verbose_name='Название маршрута', max_length=255)
  stay_1 = models.CharField(verbose_name='Начальная остановка', max_length=255)
  stay_2 = models.CharField(verbose_name='Конечная остановка', max_length=255)

  busPark = models.ForeignKey(
    'BusPark',
    on_delete=models.CASCADE,
    verbose_name='Автопарк',
    blank=True,
    null=True,
    related_name='routes',

  )
  class Meta:
    verbose_name='Маршрут'
    verbose_name_plural='Маршруты'
    ordering = ['-title']
  def __str__(self):
    return self.title

class Employer(models.Model):
  surname = models.CharField(verbose_name='Фамилия', max_length=255)
  name = models.CharField(verbose_name='Имя', max_length=255)
  patronymic = models.CharField(verbose_name='Отчество', max_length=255)
  job_title = models.CharField(verbose_name='Должность', max_length=255)

  bus_park = models.ForeignKey(
    'BusPark',
    verbose_name='Автопарк',
    blank=True,
    null=True,
    related_name='employers',
    on_delete=models.SET_NULL
  )

  class Meta:
    verbose_name = 'Работник'
    verbose_name_plural = 'Работники'
    ordering = ['-surname']
  def __str__(self):
    return f'{self.surname} {self.name} {self.patronymic}'


class Flight(models.Model):
  date_of_flight = models.DateField(verbose_name='Дата рейса')
  time_of_flight = models.TimeField(verbose_name='Время рейса')
  direction = models.CharField(verbose_name='Направление рейса', max_length=255)

  employer = models.ManyToManyField(
    Employer,
    verbose_name='Рейсы',
    related_name='flights',
    blank=True,
    null =True,
  )

  class Meta:
    verbose_name = 'Рейс'
    verbose_name_plural = 'Рейсы'

  def __str__(self):
    return f'{self.date_of_flight} {self.time_of_flight} {self.direction}'
