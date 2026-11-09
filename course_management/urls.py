from django.urls import path



from course_management.views import AdminSignupView
from course_management.views import CourseCreateView
from course_management.views import CourseListView
from course_management.views import CourseRetriveUpdateDelete




urlpatterns=[
    path("admin/",AdminSignupView.as_view()),
    path("add/",CourseCreateView.as_view()),
    path("all/",CourseListView.as_view()),
    path("<int:pk>/",CourseRetriveUpdateDelete.as_view()),
    
]