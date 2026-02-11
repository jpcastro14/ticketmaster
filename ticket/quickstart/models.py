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
    sector = models.ForeignKey(Sector,null=True, on_delete=models.CASCADE)
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
    
class Sales(models.Model):
    title = models.CharField(max_length=50)
    saleValue = models.BigIntegerField(default=0,null=False,blank=False)
    saleDate = models.DateField(blank=False, null=False, auto_now_add=False)

class Broker(models.Model):
    title = models.CharField(max_length=50)
    team = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    creci = models.CharField(max_length=7)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12)
    sales = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Corretores"

    def __str__(self):
        return self.title

