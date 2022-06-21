from django.shortcuts import render

def home_view(request):
    return render(request, 'mainapp/index.html')

def about_view(request):
    return render(request, 'mainapp/about.html')

def causes_view(request):
    return render(request, 'mainapp/causes.html')

def blog_view(request):
    return render(request, 'mainapp/blog.html')

def volunteer_view(request):
    return render(request, 'mainapp/volunteer.html')

def impact_view(request):
    return render(request, 'mainapp/impact.html')

def gallery_view(request):
    return render(request, 'mainapp/gallery.html')

def staff_view(request):
    return render(request, 'mainapp/staff.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')