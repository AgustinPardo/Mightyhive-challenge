import json
from api.models import Task

#Task.objects.all().delete()
f = open('api/dataDump/data.json','r')
data = json.load(f)
first=Task(data=data)
first.save()
