from .serializers import URlSerializer
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import URl
from django.http import HttpResponse
from rest_framework.response import Response

from . import serializers



# Create your views here.
def create_url(req):
    if req.method == 'POST':
        full_url = req.POST.get('full_url')
        obj = URl.create(full_url)
        return render(req,'my_app/index.html',{
            'full_url' : obj.full_url,
            'short_url' : req.get_host()+'/'+ obj.short_url
        })

    
    return render(req,'my_app/index.html')



def routetoURL(req, key):
    try:
        obj = URl.objects.get(short_url = key)
        return redirect('https://'+obj.full_url)
    except:
        return redirect(create_url)

@api_view(['GET'])
def api(request):
    if request.method == "GET":
    
        all_api = URl.objects.all()
        
        serializer = URlSerializer(all_api,many=True)
        
        return Response(serializer.data)

    