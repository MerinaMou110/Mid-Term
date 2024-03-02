from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from Car.models import car

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} purchased {self.car.name} on {self.purchase_date}"
