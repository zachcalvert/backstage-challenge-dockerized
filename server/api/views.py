from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from api import functions
from api.models import DifferenceRequest, PythagoreanTripletRequest


def difference(request):
    """Returns the difference between:
    1. The sum of the squares of the first n natural numbers
    2. The square of the sum of the same first n natural numbers"""
    try:
        number = int(request.GET.get("number"))
    except ValueError:
        return HttpResponse(status=400)

    if last_request := DifferenceRequest.objects.filter(number=number).first():
        difference = last_request.difference
        last_datetime = last_request.created_at
    else:
        sum_of_squares = functions.sum_of_squares(number)
        square_of_sums = functions.square_of_sums(number)
        difference = abs(sum_of_squares - square_of_sums)
        last_datetime = None

    difference_request = DifferenceRequest.objects.create(number=number, difference=difference)
    occurrences = DifferenceRequest.objects.filter(number=number).count()

    return JsonResponse({
        "datetime": difference_request.created_at,
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

    if last_request := PythagoreanTripletRequest.objects.filter(
        a=a,
        b=b,
        c=c
    ).first():
        is_triplet = last_request.is_triplet
        product = last_request.product
        last_datetime = last_request.created_at
    else:
        is_triplet = functions.is_pythagorean_triplet(a,b,c)
        product = functions.product_of_three(a,b,c)
        last_datetime = None

    pythagorean_request = PythagoreanTripletRequest.objects.create(
        a=a,
        b=b,
        c=c,
        is_triplet=is_triplet,
        product=product
    )
    occurrences = PythagoreanTripletRequest.objects.filter(a=a, b=b, c=c).count()

    return JsonResponse({
        "datetime": pythagorean_request.created_at,
        "is_triplet": is_triplet,
        "last_datetime": last_datetime,
        "occurrences": occurrences,
        "product": product,
    })
