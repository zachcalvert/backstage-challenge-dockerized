from django.core.cache import cache

from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from api import functions


def difference(request):
    """Returns the difference between:
    1. The sum of the squares of the first n natural numbers
    2. The square of the sum of the same first n natural numbers"""

    try:
        number = int(request.GET.get("number"))
    except ValueError:
        return HttpResponse(status=400)

    request_time = timezone.now()

    cache_key = f'difference_{number}'
    if cached_value := cache.get(cache_key):
        difference = cached_value['difference']
        last_datetime = cached_value['last_datetime']
        occurrences = cached_value['occurrences'] + 1
    else:
        sum_of_squares = functions.sum_of_squares(number)
        square_of_sums = functions.square_of_sums(number)
        difference = abs(sum_of_squares - square_of_sums)
        last_datetime = None
        occurrences = 1

    cache.set(
        key=cache_key,
        value={
            'difference': difference,
            'last_datetime': request_time,
            'occurrences': occurrences
        }
    )

    return JsonResponse({
        "datetime": request_time,
        "difference": difference,
        "last_datetime": last_datetime,
        "number": number,
        "occurrences": occurrences
    })


def pythagorean_triplet(request):
    """Given a sequence of three integers as query params a, b and c, this view returns:
    1. Whether the three numbers together form a Pythagorean triplet
    2. The product of these three numbers"""
    try:
        a = int(request.GET.get("a", ''))
        b = int(request.GET.get("b", ''))
        c = int(request.GET.get("c", ''))
    except ValueError:
        return HttpResponse(status=400)

    # They should be sorted, but just in case
    a, b, c = sorted([a, b, c])

    request_time = timezone.now()

    cache_key = f'pythagorean_{a}_{b}_{c}'
    if cached_value := cache.get(cache_key):
        # read current cache state
        is_triplet = cached_value['is_triplet']
        last_datetime = cached_value['last_datetime']
        occurrences = cached_value['occurrences'] + 1
        product = cached_value['product']
    else:
        is_triplet = functions.is_pythagorean_triplet(a,b,c)
        product = functions.product_of_three(a,b,c)
        last_datetime = None
        occurrences = 1

    cache.set(
        key=cache_key,
        value={
            'is_triplet': is_triplet,
            'last_datetime': request_time,
            'occurrences': occurrences,
            'product': product,
        }
    )

    return JsonResponse({
        "datetime": request_time,
        "is_triplet": is_triplet,
        "last_datetime": last_datetime,
        "occurrences": occurrences,
        'product': product
    })
