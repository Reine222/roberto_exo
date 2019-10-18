from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):

    titre= models.CharField(max_length=250)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    Tag_id= models.ManyToManyField("Tag")
    satut= models.BooleanField()


    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.titre


class Article(models.Model):

    nom= models.CharField(max_length=250)
    image= models.ImageField(upload_to='categorie')
    date= models.DateField(auto_now=False, auto_now_add=False)
    description= models.TextField()
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    Categorie_id= models.ForeignKey("Categorie", on_delete=models.CASCADE, related_name= "Categorie_Article")
    User_id= models.ForeignKey( User, on_delete=models.CASCADE, related_name= "User_Article")
    satut= models.BooleanField()


    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.nom

    
class Commentaire(models.Model):

    image= models.ImageField(upload_to='categorie')
    message= models.TextField()
    date= models.DateTimeField(auto_now=True, auto_now_add=False)
    User_id= User_id= models.ForeignKey( User, on_delete=models.CASCADE, related_name= "User_Commentaire")
    Article_id= models.ForeignKey("Article", on_delete=models.CASCADE, related_name= "Article_Commentaire")
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    satut= models.BooleanField()

    class Meta:
        verbose_name = ("Commentaire")
        verbose_name_plural = ("Commentaires")

    def __str__(self):
        return self.message

    
    


class Tag(models.Model):

    nom= models.CharField(max_length=250)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.nom


class Commenter(models.Model):

    nom= models.CharField(max_length=250)
    email= models.EmailField(max_length=254)
    web= models.URLField(max_length=200)
    message= models.TextField()
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Commenter")
        verbose_name_plural = ("Commenter")