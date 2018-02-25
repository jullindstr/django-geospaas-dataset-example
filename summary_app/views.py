# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views import generic

from django.core.serializers import serialize
from geospaas.catalog.models import Dataset, GeographicLocation
import json

class DatasetView(generic.DetailView):
    model = Dataset
    template_name = 'summary_app/dataset_table.html'
    

    #def get_context_data(self, **kwargs):
       # context = super(DatasetView, self).get_context_data(**kwargs)
        #data = Dataset.objects.all().filter(pk = self.kwargs['pk'])
	#dataset_result = json.loads(serialize('geojson', data, geometry_field = 'geographic_location__geometry'))
        #gl = GeographicLocation.objects.filter(dataset=data)
       # gl_result = json.loads(serialize('geojson', gl, geometry_field='geometry'))
       # geom_dict = gl_result.get('features')[0]
       # dataset_result.update(geom_dict)
       # context['output'] =json.dumps(dataset_result)
	#return context

    

class IndexView(generic.ListView): 	 
    model = Dataset
    context_object_name = 'datasets'
    template_name = 'summary_app/index.html'
    

class JsonView(generic.DetailView):
    template_name = 'summary_app/dataset_json.html'
    model = Dataset

    def get(self, request, pk):
        data = Dataset.objects.all().filter(pk = pk)
        dataset_result = json.loads(serialize('geojson', data, geometry_field = 'geographic_location__geometry'))
        gl = GeographicLocation.objects.filter(dataset=data)
        gl_result = json.loads(serialize('geojson', gl, geometry_field='geometry'))
        geom_dict = gl_result.get('features')[0]
        dataset_result.update(geom_dict)
        #context= {'output':json.dumps(dataset_result, sort_keys = True)}
        return HttpResponse(json.dumps(dataset_result, sort_keys = True, indent = 4), content_type = 'json')
	#return JsonResponse(context)
   
    

    

	
