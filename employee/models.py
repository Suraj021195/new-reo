from django.db import models

# Create your models 
choice =(('operator', 'operator'), 
          ('manager', 'manager'),
          ('account', 'account'), 
          ('worker', 'worker')
          )

class desingations(models.Model):
    name=models.CharField(max_length=20,choices=choice)
    
    def __str__(self):
        return self.name
    
class employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    designatin= models.ForeignKey(desingations, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.first_name

