from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.views.generic import View
from Items.models import Items

""" def search(request, input):
    if request.method == 'GET':
        searchResults = Items.objects.filter(title__icontains=input)
        if len(searchResults) == 0:
            return JsonResponse({ 'status': 'error', 'message': 'No results found. Please try other keywords' }, safe=False)
        serailizedReuslts = serialize('json', searchResults, fields=('title', 'image', 'price', 'slug', 'date', 'user'))
        return HttpResponse(serailizedReuslts, content_type='application/json') """

class Search(View):
    def get(self, request, *args, **kwargs,):
        input = self.kwargs['input']
        searchQuery = Items.objects.filter(title__icontains=input)
        print(searchQuery)
        return HttpResponse(searchQuery.serialize(), content_type='application/json')