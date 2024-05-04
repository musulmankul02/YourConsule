from django.urls import path
from apps.base.views import *
from . import views
urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),    
    path('blog/', blog, name="blog"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('case_study_details/<int:id>/', views.case_study_details, name='case-study-details'),
    path('blog/<int:id>/', blog_details, name="blog_details"),
    path('subscribe/', subscribe, name='subscribe'),
]