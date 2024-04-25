from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Index Page
    """
    
    if request.method == "GET":
        return render(request, 'index.html')

def about(request):
    """
    """
    if request.method == "GET":
        return render(request, 'about.html')
    
def service(request):
    """
    
    """
    if request.method == "GET":
        return render(request, 'service.html')
    
def contact(request):
    """
    
    """
    if request.method == "GET":
        return render(request, "contact.html")


def testimonial(request):
    """
    
    """
    if request.method == "GET":
        return render(request, "testimonial.html")