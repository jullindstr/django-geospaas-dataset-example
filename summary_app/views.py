# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.views import generic
from django.core.serializers import serialize

from geospaas.catalog.models import Dataset, GeographicLocation


class DatasetView(generic.DetailView):
    
    ''' Display an individual dataset summary '''
    
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
    
    ''' Display a list of available datasets '''
	 
    model = Dataset
    context_object_name = 'datasets'
    template_name = 'summary_app/index.html'
    

def output_json(request, pk):
    
    ''' Display a dataset parameters, including geometry coordinates, in JSON format '''

    ds = Dataset.objects.get(pk=pk)
    ds_json = json.loads(serialize('geojson', [ds]))
    ds_json['features'][0]['geometry'] = json.loads(serialize('geojson', [ds.geographic_location]))['features'][0]['geometry']
    return HttpResponse(json.dumps(ds_json), content_type='json')
