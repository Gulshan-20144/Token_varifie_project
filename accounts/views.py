from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializer import Serializerview,Loginserializers
from subcompany import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
import logging
# Create your views here.
logger=logging.getLogger("get_Company")

class ragistrations(APIView):
   serializers_class=Serializerview
   def post(self,request):
      try:
         logger.info(
            f"Enetr log: Requesting {request.build_absolute_uri()}\n\n additionalInfo:\n\n {request.data}\n\n,",exc_info=True)
         serializers=self.serializers_class(data=request.data)
         if serializers.is_valid():
               serializers.save()
               status_code=status.CREATED
               response= {
                  "success":True,
                  "massage":" User Ragister Successfully",
                  "status_code":status_code,
               }
               # serializer_data=serializers.data
         elif serializers.errors:
                status_code=status.INTERNAL_SERVER_ERROR
                response={
                  "success":False,
                  "status_code":status_code,
                  "massage":"Internal Error",
                  "Error":str(serializers.errors)
                }
         logger.info(
            f"Enetr log: Requesting {request.build_absolute_uri()}\n\n additionalInfo:\n\n {response}\n\n,",exc_info=True)
         # if serializers.errors:
         #    raise Exception
      except Exception as e:
         status_code=status.BAD_REQUEST
         response = {
            "success":False,
            "status_code":status_code,
            "message":"somthing went wrong",
            "error": str(e)
         }
         logger.error(
            f"Enetr log: Requesting {request.build_absolute_uri()}\n\n additionalInfo:\n\n {response}\n\n,",exc_info=True)
      return Response(response,status=status_code)
   
class loginview(APIView):
   permission_classes = [AllowAny]
   def post(self,request):
      logger.info(
         f"Log Enter:Requesting {request.build_absolute_uri()}\n\n additionalInfo\n\n{request.data}"
      )
      try:
         serializers=Loginserializers(data=request.data)
         if serializers.is_valid():
            user=serializers.validated_data['user']
            refresh = RefreshToken.for_user(user)
            status_code=status.CREATED
            response={
               "success":True,
               "status_code":status_code,
               "massege":"Token Created Successfully",
               "refresh":str(refresh),
               "Token":str(refresh.access_token)
            }
         logger.info(
         f"Log Enter:Requesting {request.build_absolute_uri()}\n\n additionalInfo\n\n{response}"
      )
      except Exception as e:
         status_code=status.OK
         response={
            "success":False,
            "status_code":status.BAD_REQUEST,
            "massege":"Somthing went wrong",
            "Error":str(e)
         }
         logger.error(
         f"Log Enter:Requesting {request.build_absolute_uri()}\n\n additionalInfo\n\n{response}"
         )
      return Response(response,status=status_code)