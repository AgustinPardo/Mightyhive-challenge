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

    keys=key.split(".")
    # Save query strings with the correct structure: list[int] or a string of characters, otherwise "None"
    query_strings=[re.search('^\w+$', key) or re.search('^\w+\[\d+\]$', key) for key in keys]

    res=None

    # Check if all the query strings are well formated with the required structure
    if all(query_strings):

        # Format the query string as a list of steps(path) of strings or integers to go through the json file structure
        path=[]
        for step in keys:
            if "[" in step:
                path.append(step.split("[")[0])
                path.append(int(re.search('(?<=\[)(.*?)(?=\])', step)[0]))
            else:
                path.append(step)

        # Use the steps of the path to search in the data structure
        def recuriveSearch(data, path):
            if len(path)>0 and (type(data) == str or type(data) == int or type(data) == type(None)):
                return None
            if len(path)==0:
                return data
            if type(data) == dict:
                data=data.get(path[0])
                return recuriveSearch(data,path[1:])
            if type(data) == list:
                if type(path[0]) == int and len(data)>path[0]:
                    data=data[path[0]]
                else:
                    data=None
                return recuriveSearch(data,path[1:])

        res=recuriveSearch(data, path)

    if res:
        return Response(res)
    else:
        return HttpResponse(status=404)

@api_view(['GET'])
def home(request):
    task=Task.objects.first()
    data=task.data
    return Response(data)