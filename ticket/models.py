from django.db import models

# Create your models here.


class Ticket(models.Model):
    full_name = models.CharField(max_length=255)
    bussiness = models.CharField(max_length=255) 
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name



# class Resume():
 