from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # (r'^featuresapp/', include('featuresapp.foo.urls')),
    (r'^$', 'featuresapp.people.views.personal'),
)
