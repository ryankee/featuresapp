from django.shortcuts import render_to_response

def personal(request):
    return render_to_response('people/personal.html')
