
from django.urls import path
from .import views

urlpatterns = [

    path('',views.home,name='home'),

    path('signup/',views.signup,name='signup'),

    path('loginpage/',views.loginpage,name='loginpage'),

    path('course_page',views.course_page,name='course_page'),

    path('student_page',views.student_page,name='student_page'),

    path('about/',views.about,name='about'),

    path('logout_page',views.logout_page,name='logout_page'),

    path('show',views.show,name='show'),

    path('add_course',views.add_course,name="add_course"),

    path('add_student',views.add_student,name="add_student"),

    path('usercreate/',views.usercreate,name="usercreate"),

    path('login/',views.login,name="login"),

    path('logout/',views.logout,name="logout")

    

]
