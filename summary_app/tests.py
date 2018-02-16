# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from geospaas.catalog.models import Dataset 

class DatasetIndexViewTests(TestCase): 

    def test_index_view_with_no_datasets(self):
        response = self.client.get(reverse('summary_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no datasets available")
        self.assertQuerysetEqual(response.context['datasets'], [])





    



