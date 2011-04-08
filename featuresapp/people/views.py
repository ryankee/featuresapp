from django.views.generic.simple import direct_to_template
from featuresapp.features.models import Feature

def personal(request):
    extra_context = {
        'high_priority': Feature.objects.all()[:5]
    }
    return direct_to_template(request, 'people/personal.html', extra_context=extra_context)
