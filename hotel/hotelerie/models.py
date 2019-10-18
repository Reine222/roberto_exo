from django.db import models

# Create your models here.
class Chambre(models.Model):

    image= models.ImageField(upload_to='categorie')
    titre= models.CharField(max_length=250)
    prix= models.CharField(max_length=250)
    capacite= models.CharField(max_length=250)
    lit= models.CharField(max_length=250)
    services= models.CharField(max_length=250)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    satut= models.BooleanField()


class testimony(models.Model):

    image= models.ImageField(upload_to='categorie')
    titre= models.CharField(max_length=250)
    description= models.TextField()
    fonction= models.CharField(max_length=250)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    satut= models.BooleanField()


class Reservation(models.Model):

    date_debut= models.DateTimeField(auto_now=True, auto_now_add=False)
    date_fin= models.DateTimeField(auto_now=True, auto_now_add=False)
    nbr_adult=models.IntegerField()
    nbr_enfant= models.IntegerField()
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    satut= models.BooleanField()