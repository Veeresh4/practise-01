from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return f"{self.country_name}"  


class Person(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='person', null=True)
    person_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    citizenship = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.person_name}"  


class Vehicle(models.Model): 
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='vehicle', null=True)
    brand = models.CharField(max_length=100, null=True)
    varient = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.brand}"


GENDER = (('male', 'male'), ('female', 'female'))

class Pet(models.Model):
    brand = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='pet', null=True)
    pet_name = models.CharField(max_length=100, null=True)
    breed = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True)

    def __str__(self) -> str:
        return f"{self.pet_name}"
