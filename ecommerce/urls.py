from django.urls import path
from.views import home_page, about_us, contact_us

urlpatterns =[
    path('home/', home_page, name="home"),
    path('about/', about_us, name="about"),
    path('contact/', contact_us, name = "contact"),
]
