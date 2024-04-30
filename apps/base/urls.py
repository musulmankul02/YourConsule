from django.urls import path
from apps.base.views import *
urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),    
    path('blog/', blog, name="blog"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),
    path('case_study_details/', case_study_details, name="case-study-details"),
    path('blog_details/', blog_details, name="blog_details"),

]