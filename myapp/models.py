from django.db import models

class sathick(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    sal=models.IntegerField()
    mobile=models.IntegerField()
    degree=models.CharField(max_length=20,default='')

class Datas(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    Mail=models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" %(self.Name,self.Age,self.Address)

