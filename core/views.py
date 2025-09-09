from django.shortcuts import render, redirect
from .models import Project, Skill, Experience, Testimonial
from .forms import ContactForm
from django.contrib import messages

def home(request):
    projects = Project.objects.order_by('order')[:6]
    skills = Skill.objects.all()
    experiences = Experience.objects.order_by('-start_date')
    testimonials = Testimonial.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent — thank you!")
            return redirect('home')
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'testimonials': testimonials,
        'form': form,
    })
