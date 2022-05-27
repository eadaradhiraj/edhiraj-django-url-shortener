from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from uritemplate import partial
from . import serializers
from .models import UrlData
from rest_framework import status
import random
import string
from django.shortcuts import redirect


def urlRedirect(request, slug):
    data = UrlData.objects.get(slug=slug)
    return redirect(data.url)


class Urls(APIView):

    def get(self, _):
        return Response(
            serializers.UrlSerializer(
                UrlData.objects.all(), many=True
            ).data
        )

    def post(self, request):
        slug = ''.join(random.choice(string.ascii_letters)
                       for x in range(10))
        url = request.data.get("url")
        # print(3*'*', url)
        serializer = serializers.UrlSerializer(data={"url": url, "slug": slug})
        print("****", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # Get object with this pk
        req_url = request.data.get('url')
        url = get_object_or_404(
            UrlData.objects.filter(url=req_url))
        url.delete()
        return Response({"message": "Url with id `{}` has been deleted.".format(req_url)}, status=204)
