# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json 
from django.test import TestCase 
from django.test.client import Client
from django.core.urlresolvers import reverse

from geospaas.catalog.models import * 
from geospaas.vocabularies.models import *



class DatasetTableViewTestCase(TestCase):
    fixtures = ['summary_app/fixtures/vocabularies.json','summary_app/fixtures/catalog.json']

    def setUp(self):
	self.ds = Dataset.objects.all().get(pk = 1)
    
    def test_view_dataset_table(self):
	client = Client()
	loc = GeographicLocation.objects.all().get(pk = 1)
	uri = DatasetURI.objects.all().get(pk = 1)
	resp = self.client.get('/summary_app/1/')
	self.assertEqual(resp.status_code, 200)
	self.assertEqual(resp.context['dataset'].pk, 1)
	self.assertTrue(str(self.ds.ISO_topic_category) in resp.content)
	self.assertTrue(str(self.ds.data_center) in resp.content)
	self.assertContains(resp, str(self.ds.data_center))
	self.assertContains(resp, str(self.ds.ISO_topic_category))
	self.assertContains(resp, str(self.ds.source.platform))
	self.assertTrue(str(self.ds.source.platform) in resp.content)
	self.assertTrue(str(self.ds.source.instrument) in resp.content)
	#self.assertEqual(str(self.ds.gcmd_location.category), Location.objects.all().get(pk = 1).category)
	self.assertEqual(self.ds.dataseturi_set.get(pk = 1), uri)
        #self.assertEqual(self.ds.geographic_location.geometry, loc.coords)
	self.assertTemplateUsed('dataset_table')
	self.assertIn('<a href="%s">Json </a>' %reverse ('summary_app:output_json', kwargs = {'pk': 1}), resp.content)

class IndexViewTestCase(TestCase):

    def test_index_view_with_no_datasets(self):
        response = self.client.get(reverse('summary_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no datasets available in the database")
        self.assertQuerysetEqual(response.context['datasets'], [])



