from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Student
from users.serializers import StudentSerializer
from rest_framework import filters
from datetime import datetime,timedelta



@api_view(['GET',])
def student_datewise_list(request):
    vardate = datetime.today().date()
    #var_start_date=datetime.today().date()
    #var_end_date=var_start_date-timedelta(30)

    try:
        date = request.GET.get("date", str(vardate))
        print(date)
        #start_date = request.GET.get("date1", str(var_start_date))
        # end_date = request.GET.get("date2", str(var_end_date))
        # print(start_date)
        # print(end_date)

        student_datewise = Student.objects.filter(date=date)
        # student_date_range =  Student.objects.filter(date__gte=end_date,date__lte=start_date)

        serializer = StudentSerializer(student_datewise, many=True)
        #response= student.values('name','teacher','roll')
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={"success": False, "error": e})

@api_view(['GET'])
def student_date_rangewise_list(request):
    var_end_date = datetime.today().date()
    var_start_date = var_end_date - timedelta(30)
    try:
        start_date = request.GET.get("date1", str(var_start_date))
        end_date = request.GET.get("date2", str(var_end_date))
        print(start_date)
        print(end_date)

        student_date_range = Student.objects.filter(date__gte=start_date, date__lte=end_date).order_by('-date')

        serializer = StudentSerializer(student_date_range, many=True)
        # response= student.values('name','teacher','roll')
        if start_date<=end_date:
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response('Invalid Date Range')

    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={"success": False, "error": e})
'''@api_view(['GET',])
def teacher_list():

    try:
        teacher = Teacher.objects.all()
        serializer = StudentSerializer(teacher, many=True)
        #response= student.values('name','teacher','roll')
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data={"success": False, "error": e})
                        '''