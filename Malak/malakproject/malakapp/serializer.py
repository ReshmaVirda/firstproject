# import email
# from wsgiref import validate
from rest_framework import serializers 
from .models import MyUser
# from rest_framework.exceptions import NotAuthenticated

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sign_Up
#         fields = ['id','username','email','password','mobile','country','gender']
#         extra_kwargs ={
#             'password':{'write_only':True}
#         }

    
#     #  Sign_Up.Password(validated_data['Password'])
#     #  Sign_Up.save()

# def create(self, validated_data):
#         user = Sign_Up.objects.create_user(
#             validated_data['username'], 
#             validated_data['email'], 
#             validated_data['password'],
#             validated_data['mobile'],
#             validated_data['country'],
#             validated_data['gender'],
#             )

        
#         return user

    

# class LoginSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sign_Up
#         fields = ['email', 'password',]
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         if Sign_Up.objects.filter(email=['email'],password=['password']).first:
#             return True
        
#         raise NotAuthenticated

class RegistrationSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = MyUser
        fields = ['email', 'password', 'mobile', 'country', 'gender', 'credits', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, validated_data):
        user = MyUser.objects.create(email=validated_data['email'], mobile=validated_data['mobile'], country=validated_data['country'], gender=validated_data['gender'], credits=validated_data['credit'], username=validated_data['username'])
        password = validated_data['password']
        user.set_password(password)
        user.save()
        print(user, "user is here")
        return user