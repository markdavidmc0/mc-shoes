from django.shortcuts import render


def index(request):
    title = "MC Shoes"
    return render(request, 'listing/listing_base.html', {'title': title})
