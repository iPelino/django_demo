from pyexpat import model
from tabnanny import verbose
from django.db import models

# models.ForeignKey(name of the related model) one to many
# models.OneToOneField()
# models.ManyToManyField()


class Person(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # date_of_birth= models.DateField()
    is_registered = models.BooleanField(default=False)
    email = models.EmailField()
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    # profile_photo = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)