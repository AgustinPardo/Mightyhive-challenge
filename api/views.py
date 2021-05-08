from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Task
import re

@api_view(['GET'])
def getdata(request):

    task=Task.objects.first()
    data=task.data

    key=request.GET.get('key')

    if not key:
        return HttpResponse(status=400)

    res=None

    if re.search('^\w*\[\d+\]$', key):
        key1=key.split("[")[0]
        index=int(key.split("[")[1].rstrip("]"))
        res=data.get(key1)
        if res and len(res)>index:
            res=data.get(key1)[index]
        else:
            res=None

    if re.search('^\w+\.\w+', key):
        key1=key.split(".")[0]
        key2=key.split(".")[1]
        res=data.get(key1)
        if res and type(res) != list:
            res=res.get(key2)
        else:
            res=None

    if re.search('^\w+$', key):
        res=data.get(key)

    if res:
        return Response(res)
    else:
        return HttpResponse(status=404)


@api_view(['GET'])
def home(request):
    task=Task.objects.first()
    data=task.data
    return Response(data)