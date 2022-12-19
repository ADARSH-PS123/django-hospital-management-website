from django.urls import path
from . import views
urlpatterns =[
    path("",views.home,name='home'),
    path('about',views.about,name='about'),
    path("doctors",views.doctors,name="doctors"),
    path("bookings",views.booking,name="booking"),
    path("contact",views.contact,name="contact"),
    path("departments",views.departmets,name="departments"),
    path('appointment',views.createAppointment,name='createAppointment'),


]