
from django.conf.urls import url

from . import views



urlpatterns = [
 
    url(r'^$',views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DatasetView.as_view(), name = 'dataset_table'),
    url(r'^(?P<pk>[0-9]+)/json/$',views.output_json, name = 'output_json'),
    
] 
