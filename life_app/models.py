from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/imgs')
    
    def __str__(self):
        return f'{self.title}'
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/ServiceImages')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categorias')
    
    def __str__(self):
        return f'{self.title}'