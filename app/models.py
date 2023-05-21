from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    limit = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Transaccion(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=75)
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    amount = models.IntegerField()
    date = models.DateField()
    ignore = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description
