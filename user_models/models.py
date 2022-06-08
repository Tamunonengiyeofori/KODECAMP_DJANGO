from django.db import models

# Create your models here.
# create model for people
class People(models.Model):
    # define fields for people
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    #return 
    def __str__(self):
        return self.name
    
class Address(models.Model):
    # define fields for address
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    # one to one relationship with people
    resident = models.ForeignKey(People, on_delete=models.CASCADE)
    # return the full address
    def __str__(self):
        return self.street + " " + self.city + " " + self.state + " " + self.country

class Doctor(models.Model):
    #define fields for doctor
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    hospital = models.CharField(max_length=100)
    email = models.EmailField()
    field = models.CharField(max_length=30)
    # phone_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    patients = models.ManyToManyField(People, 
                                      through="DoctorPatients",
                                      through_fields=("doctor", "patient")
                                      )
    def __str__(self):
        return self.name + " " + self.field
  
class DoctorPatients(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    patient = models.ForeignKey(People, on_delete=models.CASCADE)
    
    
class Product(models.Model):
    #define fields for product
    id = models.BigAutoField(primary_key=True)
    product_group = models.CharField(max_length=100, default="")
    product_name = models.CharField(max_length=100)
    products_price = models.FloatField(max_length=20)
    # return the product name
    def __str__(self):
        return self.product_name


class Bio(models.Model):
    #define fields for bio
    id = models.BigAutoField(primary_key=True)
    bio = models.TextField()
    # one to one relationship with people
    author = models.OneToOneField(People, on_delete=models.CASCADE)
    # return the bio
    def __str__(self):
        return self.bio
