from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import VolunteerForm, MentorForm, MailListForm, ContactPageForm
from .models import Volunteer, Post
from django.contrib import messages
from django.views.generic import CreateView

def home_view(request):
    if request.method == 'POST':
        form = MailListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email was submitted successfully')
            return redirect('mainapp:home')
    else:
        form = MailListForm()
    context = {'form':form}
    return render(request, 'mainapp/index.html', context)

def about_view(request):
    return render(request, 'mainapp/about.html')

def causes_view(request):
    return render(request, 'mainapp/causes.html')

def cause_detail_view(request):
    return render(request, 'mainapp/cause-detail.html')

def blog_view(request):
    return render(request, 'mainapp/blog.html')

def volunteer_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:volunteer')
    else:
        form = VolunteerForm()
    context = {'form':form} 
    return render(request, 'mainapp/volunteer.html', context)

def mentor_view(request):
    if request.method == 'POST':
        form = MentorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:mentor')
    else:
        form = MentorForm()
    context = {'form':form}
    return render(request, 'mainapp/mentor.html', context)

def impact_view(request):
    return render(request, 'mainapp/impact.html')

def gallery_view(request):
    return render(request, 'mainapp/gallery.html')

def staff_view(request):
    return render(request, 'mainapp/staff.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactPageForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were submitted successfully')
            return redirect('mainapp:contact')
    else:
        form = ContactPageForm()
    context = {'form':form}
    return render(request, 'mainapp/contact.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('mainapp:blog')