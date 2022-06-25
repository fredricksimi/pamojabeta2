from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('causes', views.causes_view, name='causes'),
    path('cause-detail', views.cause_detail_view, name='cause-detail'),
    path('blog', views.blog_view, name='blog'),
    path('post', views.PostCreateView.as_view(template_name='mainapp/post.html'), name='write-a-post'),
    path('volunteer', views.volunteer_view, name='volunteer'),
    path('mentor', views.mentor_view, name='mentor'),
    path('impact', views.impact_view, name='impact'),
    path('gallery', views.gallery_view, name='gallery'),
    path('staff', views.staff_view, name='staff'),
    path('contact', views.contact_view, name='contact'),

]