from django.db import models

# Create your models here.
class Todo(models.Model):
    sl_no=models.IntegerField()
    items_name=models.CharField(max_length=50)
    description=models.CharField(max_length=300)

    def __str__(self) :
        return self.items_name


    

    