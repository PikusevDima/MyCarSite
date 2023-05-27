from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=31,
                            null=False,
                            unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    carManufacturer = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    cost = models.CharField(max_length=12,
                            null=False)
    speed = models.CharField(max_length=4,
                             null=False)
    brand_id = models.ForeignKey(Brand,
                                 null=True,
                                 on_delete=models.SET_NULL)
    users = models.ManyToManyField(Person, symmetrical=True)
    image = models.CharField(max_length=401,
                             null=False,
                             unique=True)

    def __str__(self):
        return self.name
