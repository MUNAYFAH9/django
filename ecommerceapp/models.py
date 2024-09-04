from django.db import models

# Create your models here.
class storetype(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class items(models.Model):
    nameitems=models.CharField(max_length=50)
    description=models.CharField(max_length=200) 
    image=models.ImageField(upload_to='images/',null=True)
    price=models.FloatField()
    availability=models.BooleanField(default=False)
    st=models.ForeignKey(storetype,on_delete=models.CASCADE,null=True)
    def __str__(self):
        template='{0.nameitems} {0.description} {0.image} {0.price} {0.availability}'
        return template.format(self)

class itemsdetails(models.Model):
    color=models.CharField(max_length=50)
    qty=models.FloatField()
    tax=models.FloatField()
    barcoode=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    items=models.ForeignKey(items,on_delete=models.CASCADE,null=True)
    def __str__(self):
        template='{0.color} {0.qty} {0.tax} {0.barcoode} {0.country}'
        return template.format(self)
    

class cart(models.Model):
    itemsid=models.IntegerField()   
