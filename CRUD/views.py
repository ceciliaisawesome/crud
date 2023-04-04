from django import render

def Home(request):
    return render(request, 'index.html')
