from .models import Sign_Up,Sign_in,Forgot_Password
from rest_framework import serializers 

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign_Up
        fields = ['username','Email','Password','mobile','country','gender']
        extra_kwargs ={
            'Password':{'write_only':True}
        }

    def create(self, validated_data):
     user = Sign_Up.objects.create(
      username=validated_data['username'],
      Email=validated_data['Email'],
      mobile=validated_data['mobile'],
      country=validated_data['country'],
      gender=validated_data['gender'],

    )
    #  Sign_Up.Password(validated_data['Password'])
    #  Sign_Up.save()

     return user

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign_in
        fields = '__all__'

class ForgotpasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forgot_Password
        fields = '__all__'
