from rest_framework.views import  APIView
from django.http import JsonResponse
from .apicontroler import Apicontroler
from django.views.decorators.csrf import csrf_exempt
import datetime
import pandas as pd
import json



class TestApi(APIView):

    def get(self, request, format=None):
        try:
            
            data = Apicontroler().get_test_apidata()
            return JsonResponse(data, safe=False)
        except Exception as ex :
            
            return JsonResponse([], safe=False)

