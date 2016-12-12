from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
def home(request):
    #variable qui affiche la chaine de caracteres
    test = "fjksjdfhkds kqdsjhksjh lqksjlkdj"
    #tableau
    menu = ['toto', 'tata', 'titi']
    #dictionnaire
    context = {'page':'accueil', 'page2' : test, 'page3' : menu }
    #si je mets le mot test en "test" la page m'affichera le mot test
    return render(request,'home.html', context)
