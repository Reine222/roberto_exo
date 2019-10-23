# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'date_add', 'date_upd', 'satut')
    list_filter = (
        'date_add',
        'date_upd',
        'satut',
        'id',
        'titre',
        'date_add',
        'date_upd',
        'satut',
    )
    raw_id_fields = ('Tag_id',)


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'date',
        'description_cat',
        'content',
        'date_add',
        'date_upd',
        'Categorie_id',
        'User_id',
        'satut',
    )
    list_filter = (
        'date',
        'date_add',
        'date_upd',
        'Categorie_id',
        'User_id',
        'satut',
        'id',
        'nom',
        'image',
        'date',
        'description_cat',
        'content',
        'date_add',
        'date_upd',
        'Categorie_id',
        'User_id',
        'satut',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image',
        'message',
        'date',
        'User_id',
        'Article_id',
        'date_add',
        'date_upd',
        'satut',
    )
    list_filter = (
        'date',
        'User_id',
        'Article_id',
        'date_add',
        'date_upd',
        'satut',
        'id',
        'image',
        'message',
        'date',
        'User_id',
        'Article_id',
        'date_add',
        'date_upd',
        'satut',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_upd', 'statut')
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'nom',
        'date_add',
        'date_upd',
        'statut',
    )


class CommenterAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'email', 'web', 'message', 'date_add')
    list_filter = (
        'date_add',
        'id',
        'nom',
        'email',
        'web',
        'message',
        'date_add',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Tag, TagAdmin)
_register(models.Commenter, CommenterAdmin)
