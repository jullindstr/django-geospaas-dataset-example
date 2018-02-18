# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json 
from django.test import TestCase

from django.core.urlresolvers import reverse

from geospaas.catalog.models import Dataset, Source, GeographicLocation, Parameter, DatasetParameter, DatasetURI
from django.conf import settings  
from django.test import RequestFactory
from geospaas.vocabularies.models import *


class SummaryAppViewsTestCase(TestCase):
    fixtures = ['summary_app/fixtures/vocabularies.json','summary_app/fixtures/catalog.json']

    def setUp(self):
	self.ds = Dataset.objects.all().get(pk = 1)
    
    def viewtest_dataset_table(self):
	loc = GeographicLocation.objects.all().get(pk = 1)
	uri = DatasetURI.objects.all().get(pk = 1)
	resp = self.client.get('/summary_app/1/')
	self.assertEqual(resp.status_code, 200)
	self.assertEqual(resp.context['datasets'].pk, 1)
	self.assertEquals(resp.context['datasets'].entry_title, 'Test dataset')
	#self.assertTrue(str(ds.source) in resp.content)
	#self.assertTrue(str(ds.ISO_topic_category) in resp.content)
	#self.assertTrue(str(ds.data_center) in resp.content)
	self.assertContains(resp, str(ds.data_center))
	self.assertContains(resp, str(ds.cource))
	self.assertContains(resp, str(ds.ISO_topic_category))
	#self.assertContains(resp, str(ds.source.platform))
	#self.assertTrue(str(ds.source.platform) in resp.content)
	#self.assertTrue(str(ds.source.instrument) in resp.content)
	self.assertEqual(str(ds.gcmd_location.category), Location.objects.all().get(pk = 1).category)
	self.assertEqual(ds.dataseturi_set.get(pk = 1), uri)
        self.assertEqual(ds.geographic_location.geometry.coords, loc.coords)
	self.assertTemplateUsed('dataset_table')
	self.assertIn('<a href=""%s" >ds </a>' %reverse ("output_json"), response.content)

class IndexViewTestCase(TestCase):

    def test_index_view_with_no_datasets(self):
        response = self.client.get(reverse('summary_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no datasets available in the database")
        self.assertQuerysetEqual(response.context['datasets'], [])



