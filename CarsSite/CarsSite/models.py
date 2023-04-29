from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=31,
                            null=False,
                            unique=True)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)
    CarManufacturer = models.CharField(max_length=31)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField(null=False)
    Cost = models.TextField(null=False)
    Speed = models.TextField(null=False)
    BrandId = models.ForeignKey(Brand,
                                null=True,
                                on_delete=models.SET_NULL)


class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Stars = models.CharField(max_length=3, null=True)
