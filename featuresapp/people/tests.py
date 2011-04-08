from django.test import TestCase

HTTP_SUCCESS=200

class PersonalPageTest(TestCase):
    def testCanAccessPersonalPage(self):
        response = self.client.get('/')
        self.assertEquals(HTTP_SUCCESS, response.status_code)

    def testUsesPersonalTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'people/personal.html')
