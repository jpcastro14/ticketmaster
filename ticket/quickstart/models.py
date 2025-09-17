from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50, null=False)
    dificulty = models.IntegerField(null=False, default=1)
    isVegan = models.BooleanField(default=False)
    ingredients = models.TextField(null=False)
    servings = models.IntegerField(default=1)
    prepareTime = models.IntegerField(default=1)
    prepareSteps = models.TextField(null=False)

    class Meta: 
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"

    def __str__(self):
        return self.description
