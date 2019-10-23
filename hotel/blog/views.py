from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    tag= Tag.objects.all()
    articl = Article.objects.all()
    article = Article.objects.all()
    
    
    
    
    paginator = Paginator(article, 2)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    data= {
        'articl': articl,
        'tag': tag,
    
        'article': article,
        'articles': articles,
        
    }
    return render(request, 'pages/blog.html', data, {'articles': articles})



def single(request, pk):
    
    arti = Article.objects.get(pk=pk)
    article = Article.objects.all()
    articl = Article.objects.all()
    tag= Tag.objects.all()
    comment= Commentaire.objects.all()
    
    nom= request.POST.get("nom")
    email= request.POST.get("eamil")
    web= request.POST.get("web")
    message= request.POST.get("message")
    
    
    
    
    data= {
        'arti': arti,
        'articl': articl,
        'tag': tag,
        'article': article,
        'comment': comment,
        'nom': nom,
        'email': email,
        'web': web,
        'message': message,
    }
    #formule = Commenter(nom=nom,eamil=email,web=web,message=message)
    #formule.save()
    
    return render(request, 'pages/single.html', data)


