from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('<html><body>Hi Django.</body>', content_type='text/html')
