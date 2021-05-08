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

    if re.search('^\w*\[\d+\]\.\w+$', key):
        key1=key.split("[")[0]
        key2=key.split("]")[1].lstrip(".")
        index=int(re.search('(?<=\[)(.*?)(?=\])', key)[0])
        if data.get(key1) and len(data.get(key1))>index :
            if type(data.get(key1)[index]) == dict:
                res=data.get(key1)[index].get(key2)

    if re.search('^\w*\[\d+\]$', key):
        key1=key.split("[")[0]
        index=int(key.split("[")[1].rstrip("]"))
        if data.get(key1) and len(data.get(key1))>index:
            res=data.get(key1)[index]

    if re.search('^\w+\.\w+$', key):
        key1=key.split(".")[0]
        key2=key.split(".")[1]
        if data.get(key1) and type(data.get(key1)) == dict:
            res=data.get(key1).get(key2)

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