from django.shortcuts import render
from .models import Shoe
from requests.models import Response


def index(request: Response) -> render:
    """Render index page for shoe site."""
    shoe_list = Shoe.objects.all()
    return render(request, 'listing/listing_base.html', {
        'shoe_list': shoe_list
    })
