from django.shortcuts import render

# Create your views here.
def qq(request):
    return render(request, 'qq.html')
