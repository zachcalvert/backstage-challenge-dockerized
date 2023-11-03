from django.db import models


class ApiRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class DifferenceRequest(ApiRequest):
    number = models.IntegerField(null=False)
    difference = models.IntegerField()


class PythagoreanTripletRequest(ApiRequest):
    a = models.IntegerField(null=False)
    b = models.IntegerField(null=False)
    c = models.IntegerField(null=False)
    is_triplet = models.BooleanField(default=False)
    product = models.IntegerField()
