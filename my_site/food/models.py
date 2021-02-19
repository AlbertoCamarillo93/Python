from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#Cada que haya cambios aquí se debe ejecutar en el CMD makemigrations, sqlmigrate y migrate

class Item (models.Model): 

    #Función dentro de la clase Item que devolverá el nombre de la variable item_name cuando se invoque la clase
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default= "https://www.fnasafety.com/wp-content/uploads/2016/04/ComingSoon2-fnasafety.png")

    def get_absolute_url(self):
          return reverse("food:detail", kwargs={"pk": self.pk})  