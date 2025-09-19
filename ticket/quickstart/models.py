from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

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
    
class Sector(models.Model):
    name = models.CharField(max_length=10)
    code = models.IntegerField(null=False)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def __str__(self):
        return self.name

class Ticket(Base):
    title = models.CharField(max_length= 30)
    type = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    area = models.CharField(max_length=30)
    criticality = models.IntegerField()
    criticalityColor = models.CharField(blank=True, max_length=30)
    priority = models.IntegerField()
    description = models.TextField()
    closeDesc = models.TextField(blank=True)
    finalStatus = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

    def __str__(self):
        return self.title
