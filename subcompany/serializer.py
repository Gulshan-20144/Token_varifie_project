from rest_framework import serializers
from subcompany.models import Users,company
from django.contrib.auth.models import User
# from accounts.serializer import Userviewserializers

class Userdetailserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email',]
class Userserializers(serializers.ModelSerializer):
    gmail=serializers.EmailField()
    class Meta:
        model=Users
        fields=['user_id','name','mobile','gmail','age']
        
        
    def validate_name(self,valuse):
        if len(valuse)>20:
            raise serializers.ValidationError("Name must les then 20 character")
        return valuse
    def validate_mobile(self,values):
        string=str(values)
        if len(string)==10:
            return values
        else:
            raise serializers.ValidationError("Mobile Number is must 10 Digits")


class companyserializes(serializers.ModelSerializer):
    # user=Userserializers(read_only=True)
    adminuser=Userdetailserializers(read_only=True)
    class Meta:
        model=company
        fields=['id','c_name','adminuser']