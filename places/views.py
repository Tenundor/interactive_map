from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse


from places.models import Place


def serialise_place_geojson(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude],
        },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('place_api', kwargs={'place_id': place.id}),
        }
    }


def serialise_place_details(place):
    images = place.images.all()
    return {
        "title": place.title,
        "imgs": [image.file.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }


def index(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()
    context = {
        "places": {
            "type": "FeatureCollection",
            "features": [serialise_place_geojson(place) for place in places],
        }
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place_api(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    content = serialise_place_details(place)
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
