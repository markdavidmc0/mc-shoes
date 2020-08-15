from django.shortcuts import render


def index(request):
    return render(request, 'listing/listing_base.html', {})
