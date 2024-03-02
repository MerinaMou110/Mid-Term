from django.db import models
from Brand.models import brand
from django.contrib.auth.models import User


class car(models.Model):
    Brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Car/media/uploads/',blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
   
    def __str__(self):
        return self.name
    

    


class Comment(models.Model):
    car = models.ForeignKey(car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"