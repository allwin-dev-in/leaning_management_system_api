from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import permissions,authentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from course_management.serializers import AdminSerializer
from course_management.serializers import CourseSerializer
from course_management.models import Course
from course_management.pagination import CustomPagination
from course_management.pagination import LimitOffsetPagination

# Create your views here.

class AdminSignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=AdminSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_superuser(**cleaned_data)
            ser_inst=AdminSerializer(qs)
            return Response(ser_inst.data)
        else:
            return Response(serializer_instance.errors)

# Using Generic Views

class CourseCreateView(CreateAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=CourseSerializer

class CourseListView(ListAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=CourseSerializer
    queryset=Course.objects.all()

    pagination_class=LimitOffsetPagination


    #For Filtering in URls
    def get_queryset(self):

        qs=Course.objects.all()
        query_parameter=self.request.query_params

        if "language" in query_parameter:
            language=query_parameter.get("language")
            qs=qs.filter(language__iexact=language) #case insensitive
        
        if "price" in query_parameter:
            price=query_parameter.get("price")
            qs=qs.filter(price=price)

        if "trainer" in query_parameter:
            trainer=query_parameter.get("trainer")
            qs=qs.filter(trainer=trainer) # cas sensitive

        if "title" in query_parameter:
            title=query_parameter.get("title")
            qs=qs.filter(title__icontains=title)  # mathing cases

        return qs


class CourseRetriveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    serializer_class=CourseSerializer
    queryset=Course.objects.all()



    
# ============================================================


# # Using ViewSet
# class CouseViewSet(ModelViewSet):
#     serializer_class=CourseSerializer
#     queryset=Course.objects.all()