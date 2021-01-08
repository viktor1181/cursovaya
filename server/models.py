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
class EnginesManager(models.Manager):
    def get_by_natural_key(self, nameEngine, weight, price):
        return self.get(nameEngine=nameEngine, weight=weight, price=price)

class Engines(models.Model):
    nameEngine = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    # fuelConsumption = models.PositiveIntegerField(max_length=30)
    objects = EnginesManager()

    class Meta:
        unique_together = [['nameEngine', 'weight', 'price']]

    def natural_key(self):
        return (self.nameEngine, self.weight, self.price)

class TransmissionsManager(models.Manager):
    def get_by_natural_key(self, Transmissions, weight, price):
        return self.get(nameTransmission=nameTransmission, weight=weight, price=price)

class Transmissions(models.Model):
    nameTransmission = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    objects = TransmissionsManager()
    class Meta:
        unique_together = [['nameTransmission', 'weight', 'price']]

    def natural_key(self):
        return (self.nameTransmission, self.weight, self.price)

class DrivesManager(models.Manager):
    def get_by_natural_key(self, nameDrive, weight, price):
        return self.get(nameDrive=nameDrive, weight=weight, price=price)

class Drives(models.Model):
    nameDrive = models.CharField(max_length=200)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    objects = DrivesManager()

    class Meta:
        unique_together = [['nameDrive', 'weight', 'price']]

    def natural_key(self):
        return (self.nameDrive, self.weight, self.price)

class ModelsManager(models.Manager):
    def get_by_natural_key(self, nameModel):
        return self.get(nameModel=nameModel)

class Models(models.Model):
    nameModel = models.CharField(max_length=200)
    objects = ModelsManager()
    class Meta:
        unique_together = [['nameModel']]

    def natural_key(self):
        return self.nameModel

class Configuration(models.Model):  # комплектация
    engine = models.ForeignKey(Engines, related_name='engine', max_length=200, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmissions, max_length=200, on_delete=models.CASCADE)
    drive = models.ForeignKey(Drives, max_length=200, on_delete=models.CASCADE)
    model = models.ForeignKey(Models, max_length=200, on_delete=models.CASCADE)

    @property
    def sum(self):
        return self.engine.price + self.transmission.price + self.drive.price

    @property
    def avg(self):
        return (self.engine.price + self.transmission.price + self.drive.price)/3


