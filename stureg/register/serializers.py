from rest_framework import serializers
from register.models import Student

class studentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Student
            fields = '__all__'