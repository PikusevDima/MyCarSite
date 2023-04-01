from django.http import HttpResponse



def homePage(request):
    return HttpResponse('<h1>ЧТО-ТО</h1>')

def index(request):
    return render(request, 'index.html')
