from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

user=get_user_model()

# serializers.Serializer ModelSerializer HyperlinkedModelSerializer ListSerializer BaseSerializer

class Serializerview(serializers.ModelSerializer):
    password=serializers.CharField(required=True)
    password2=serializers.CharField(required=True)
    class Meta:
        model = user
        fields=[
            "id",
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs={
            'password':{"write_only":True},
            'password2':{"write_only":True},
        }
    def create(self, validated_data):
        username=validated_data.get('username')
        email=validated_data.get('email')
        password=validated_data.get('password')
        password2=validated_data.get('password2')
        if password==password2:
            users=user(username=username,email=email)
            users.set_password(password)
            users.save()
            return user
        else:
            raise serializers.ValidationError({
                'error':'both password not match',
            }
            )
class Loginserializers(serializers.Serializer):
    username=serializers.CharField(max_length=30)
    password=serializers.CharField(max_length=50)
    
    def validate(self, values):
        username= values.get("username")
        password= values.get("password")
        
        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                values['user']=user
            else:
                raise serializers.ValidationError("incorrect username or password")
        else:
            raise serializers.ValidationError("Both Username and Password are need")
        return values
    
class Userviewserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "id",
            'username',
            'email',
        ]