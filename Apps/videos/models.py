from django.db import models

class Videos(models.Model):
	titulo = models.CharField(max_length=100)
	categoria= models.CharField(max_length=100)
	descripcion= models.CharField(max_length=100)
	creacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
        	return f"{self.titulo}"