from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def contact(request):
    
    nom= request.POST.get("nom")
    email= request.POST.get("eamil")
    web= request.POST.get("web")
    message= request.POST.get("message")
    
    data= {
        'nom': nom,
        'email': email,
        'web': web,
        'message': message,
    }
    
    formule= Contact(nom=nom, eamil=email, web=web, message= message)
    formule.save()
    return render(request, 'pages/contact.html', data)

