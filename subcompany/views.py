from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response
from accounts.serializer import user
from subcompany.serializer import Userserializers,companyserializes
from subcompany.models import Users,company
from django.contrib.auth.models import User
from subcompany import status
import logging
from django.db.models import Q

logger=logging.getLogger("get_Company")
# Create your views here.
class Userclass(APIView):
    serializer_class=Userserializers
    def get(self,request,user_id=None):
        try:
            logger.info(
            f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n Retreive Data of User_Id= {user_id}\n\n")
            self.id=user_id
            if self.id is not None:
                queryset=Users.objects.get(user_id=self.id)
                serializers=self.serializer_class(queryset)
                status_code=status.OK
                response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"One Data Get Successfully",
                    "Data":serializers.data
                }
            else:
                data=Users.objects.all()
                serializers=self.serializer_class(data,many=True)
                status_code=status.OK
                response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Data Get Successfully",
                    "Data":serializers.data
                }
            if not serializers:
                raise Exception
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Exception as e:
            status_code=status.BAD_REQUEST
            response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Something went Wrong",
                    "error":str(e)
                }
            logger.error(
            f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {str(e)}\n\n",exc_info=True)
        return Response(response,status=status_code)
        
    def post(self,request):
        try:
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {request.data}\n\n")
            serializers=self.serializer_class(data=request.data)
            if serializers.is_valid():
                serializers.save()
                status_code=status.CREATED
                response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Data Create Successfully",
                    "Data":serializers.data
                }
            elif serializers.errors:
                status_code=status.INTERNAL_SERVER_ERROR
                response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Internal Error",
                    "Error":str(serializers.errors)
                }
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Exception as e:
            status_code=status.BAD_REQUEST
            response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Something went Wrong",
                    "error":str(e)
                }
            logger.error(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {str(e)}\n\n",exc_info=True)
        return Response(response,status=status_code)
        
    def patch(self,request,user_id=None):
        try:
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {user_id}\n\n")
            id=user_id
            data=Users.objects.get(user_id=id)
            serializers=self.serializer_class(data,data=request.data)
            if serializers.is_valid():
                serializers.save()
                status_code=status.PARTIAL_CONTENT
                response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Data Partially Updated Successfully",
                    "Data":serializers.data
                }
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Users.DoesNotExist as e:
            status_code=status.BAD_REQUEST
            response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Something Went Wrong",
                    "Error":str(e)
                }
            logger.error(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {str(e)}\n\n")
        return Response(response,status=status_code)
        
    def put(self,request,user_id=None):
        try:
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {user_id}\n\n")
            self.id=user_id
            data=Users.objects.get(user_id=self.id)
            serializers=self.serializer_class(data,data=request.data)
            if serializers.is_valid():
                serializers.save()
                status_code=status.RESET_CONTENT
                response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Data Updated Successfully",
                    "Data":serializers.data
                }
            elif serializers.errors:
                status_code=status.INTERNAL_SERVER_ERROR
                response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Internal Error",
                    "Erorr":str(serializers.errors)
                }
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Exception as e:
            status_code=status.BAD_REQUEST
            response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Something Went Wrong",
                    "Erorr":str(e)
                }
            logger.error(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        return Response(response,status=status_code)
    def delete(self,request,user_id=None):
        try:
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {user_id}\n\n")
            id=user_id
            queryset=User.objects.get(user_id=id)
            queryset.delete()
            status_code=status.OK
            response={
                    "success":True,
                    "status_code":status_code,
                    "massage":"Data Deleted Successfully",
                }
            logger.info(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Exception as e:
            status_code=status.BAD_REQUEST
            response={
                    "success":False,
                    "status_code":status_code,
                    "massage":"Something Went Wrong",
                    "Erorr":str(e)
                }
            logger.error(
                f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {str(e)}\n\n")
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
class companyclass(generics.ListAPIView):
    queryset=company.objects.all()
    serializer_class=companyserializes
    authentication_classes=[JWTAuthentication]
    # authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
    # def get(request):
    def get(self, request):
        logger.info(
            f"Enter log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n Retrieving all details ")
        try:
            user_id=request.user.id
            # user=request.user
            # print(user)
            print(user_id,"_______user_id_")
            # model = company.objects.filter().prefetch_related("adminuser")
            companies = company.objects.filter(Q(adminuser__id=user_id)).first()
            # model=company.objects.get(user_id=user_id)
            print(companies,"____data_______")
            serializer = companyserializes(companies)
            status_code = status.OK
            response = {
                'success': True,
                'status_code': status_code,
                'message': 'Entry fetched successfully',
                'data': serializer.data
            }
            logger.info(
                f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n {response}\n\n")
        except Exception as e:
            status_code = status.BAD_REQUEST
            response = {
                'success': False,
                'status_code': status.BAD_REQUEST,
                'message': "Something is Wrong.",
                'error': str(e)
            }
            logger.error(
                f"Exit log: Requesting {request.build_absolute_uri()} \n\n additionalInfo:\n\n  {str(e)}")
        return Response(response, status=status_code)