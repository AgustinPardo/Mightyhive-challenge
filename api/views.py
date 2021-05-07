from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Task

@api_view(['GET'])
def getdata(request):

    task=Task.objects.all()[0]
    data=task.data

    key=(request.GET.get('key'))
    res=data.get(key)
    
    try:
        if "[" in key :
                key1=key[:-3]
                index=int(key[-2])
                res=data.get(key1)[index]
    except:
        return HttpResponse(status=404)

    if len(key.split("."))>1:
        key1=key.split(".")[0]
        key2=key.split(".")[1]
        res=data.get(key1).get(key2)
    
    if res:
        return Response(res)
    else:
        return HttpResponse(status=404)