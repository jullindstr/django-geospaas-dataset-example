# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.serializers import serialize
from geospaas.catalog.models import Dataset


class DatasetView(generic.DetailView):
    model = Dataset
    template_name = 'summary_app/dataset_table.html'

class IndexView(generic.ListView): 	 
    context_object_name = 'datasets'
    template_name = 'summary_app/index.html'
    
    def get_queryset(self):
        return Dataset.objects.all()
	 

def output_json(request,pk):
    data = Dataset.objects.all().filter(pk = pk)
    result = serialize('geojson', data, geometry_field = 'polygon')
    context = {'output':result}
    #return render(request, 'summary_app/dataset_json.html', context, content_type = 'json')
    return HttpResponse(result, content_type = 'json')

	
