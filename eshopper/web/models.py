from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='client')


    def __str__(self):
        return self.name
    

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='contact'
        verbose_name_plural='contact'

class Carosuel(models.Model):
    image = models.ImageField(upload_to="Carosuel")
    sub_content = models.CharField(max_length =100)
    main_content= models.CharField(max_length =100)

    def __str__(self):
       return self.main_content
    
    class Meta:
        verbose_name='Carosuel'
        verbose_name_plural='Carosuel'
