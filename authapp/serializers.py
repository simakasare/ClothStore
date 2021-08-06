from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'})
    class Meta:
        model = Account
        fields = ['email','username','password','password2']
    def save(self):
        account =Account(
        email=self._validated_data['email'],
        username=self._validated_data['username'],
        
        )
        password=self._validated_data['password']
        password2=self._validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        account.set_password(password)
        account.save()
        return account