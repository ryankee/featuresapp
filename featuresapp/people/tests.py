from django.test import TestCase
from featuresapp.features.models import Feature

HTTP_SUCCESS=200

class PersonalPageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def testCanAccessPersonalPage(self):
        self.assertEquals(HTTP_SUCCESS, self.response.status_code)

    def testUsesPersonalTemplate(self):
        self.assertTemplateUsed(self.response, 'people/personal.html')

class PersonalPageHighPriorityTest(TestCase):
    def testPersonalPageHighPriorityWithNoFeatures(self):
        features = Feature.objects.all()
        self.response = self.client.get('/')
        self.assertItemsEqual(features, self.response.context['high_priority'])

    def testPersonalPageHighPriority(self):
        Feature.objects.create()
        features = Feature.objects.all()
        self.response = self.client.get('/')
        self.assertItemsEqual(features, self.response.context['high_priority'])

    def testPersonalPageHighPriorityOnlyShows5(self):
        [Feature.objects.create() for i in range(5)]
        self.response = self.client.get('/')
        self.assertEquals(5, len(self.response.context['high_priority']))
