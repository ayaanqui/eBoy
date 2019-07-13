from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User
from Items.models import Items

def search(request, input):
    if request.method == 'GET':
        searchResult = Items.objects.filter(title__icontains=input)
        return JsonResponse(searchResult, safe=False)