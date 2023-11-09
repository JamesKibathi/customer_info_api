from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    county = models.CharField(max_length=255)
    subcounty = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.county}, {self.subcounty}, {self.ward}, Floor: {self.floor}"

class Business(models.Model):
    business_name = models.CharField(max_length=255)
    registration_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @property
    def age_of_business(self):
        from datetime import date
        today = date.today()
        return today.year - self.registration_date.year - ((today.month, today.day) < (self.registration_date.month, self.registration_date.day))

    def __str__(self):
        return f"{self.business_name} ({self.category})"

class Customer(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    nationality = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.business}) - {self.location}"