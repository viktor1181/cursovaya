from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Car(models.Model):
    vin = models.CharField(verbose_name="Vin", db_index=True, max_length=64)
    color = models.CharField(verbose_name="Color", max_length=64)
    brand = models.CharField(verbose_name="Brand", max_length=64)
    CAR_TYPES = (
        (1, "sedan"),
        (2, "carm"),
        (3, "car3"),
        (4, "car4"),
    )
    car_type = models.IntegerField(verbose_name="Car_Type", choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name="Polzovatel", max_length=64, on_delete=models.CASCADE)


class Engines(models.Model):
    nameEngine = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    # fuelConsumption = models.PositiveIntegerField(max_length=30)

class Transmissions(models.Model):
    nameTransmission = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

class Drives(models.Model):
    nameDrive = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

class Models(models.Model):
    nameModel = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Configuration(models.Model):  # комплектация
    engine = models.ForeignKey(Engines, max_length=200, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmissions, max_length=200, on_delete=models.CASCADE)
    drive = models.ForeignKey(Drives, max_length=200, on_delete=models.CASCADE)
    model = models.ForeignKey(Models, max_length=200, on_delete=models.CASCADE)

