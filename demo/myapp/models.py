from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title= models.CharField(max_length=200)
    completed= models.BooleanField(default=False)




class Comentario(models.Model):
    correo = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.correo