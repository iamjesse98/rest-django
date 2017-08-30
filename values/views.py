from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

data = []
# Create your views here.
@csrf_exempt
def values(request):
    if request.method == 'POST':
        data.append(json.loads(json.dumps((request.POST['data']))))
        return JsonResponse(data, safe=False)
    if request.method == 'GET':
        #data = json.loads(json.dumps((request.POST['temperature'])))
        return JsonResponse(data, safe=False)
    return HttpResponse(request,data)