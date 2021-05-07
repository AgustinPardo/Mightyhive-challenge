import json
from api.models import Task

Task.objects.all().delete()
f = open('data.json','r')
data = json.load(f)
first=Task(data=data)
first.save()

#python3 manage.py shell < model_dump.py 
