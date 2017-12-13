#from django.contrib.auth.models import User
from rest_framework import serializers
from models import Employee

class DisplaySerializer(serializers.Serializer):

    display = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

    def get_display(self, instance):
        return {'Employee name': instance.employee_name, 'Employee Email ID': instance.email,
                'Password' : instance.password}
    
class EmployeeSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = Employee
        fields = ('employee_name','email','password')
        def create(self,validated_data):
            return Employee.objects.create(**validated_data)

    def validate(self,instance):
	   print("inside validate")
	   exists = Employee.objects.filter(email=instance['email'])
	   if exists:
		raise serializers.ValidationError("You are no eligible for the job")
	   print instance['email']
	   return instance
	
        
