from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('causes', views.causes_view, name='causes'),
    path('blog', views.blog_view, name='blog'),
    path('volunteer', views.volunteer_view, name='volunteer'),
    path('impact', views.impact_view, name='impact'),
    path('gallery', views.gallery_view, name='gallery'),
    path('staff', views.staff_view, name='staff'),
    path('contact', views.contact_view, name='contact'),

]