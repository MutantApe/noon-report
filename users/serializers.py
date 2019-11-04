
from rest_framework import serializers
from users.models import Student


class StudentSerializer(serializers.ModelSerializer):
    #teacher_serial = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model   = Student
        fields  =   [
                'name',
                'roll',
                'date'

        ]
'''class TeacherSerializer(serializers.ModelSerializer):
    teacher_serial = serializers.RelatedField(many=True)
    class Meta:
        model   = Teacher
        fields  =   [

                'name',
                'teacher_serial',
                'roll',

        ]'''
