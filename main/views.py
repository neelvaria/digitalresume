from typing import Any
from django.shortcuts import render
from django.contrib import messages
from . models import *
from django.views import generic
from .forms import Contactform
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        testimonial = Testimonial.objects.filter(is_active=True)
        cerificate = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        context['testimonials'] = testimonial
        context['certificate'] = cerificate
        context['blogs'] = blogs
        context['portfolio'] = portfolio
        return context

class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = Contactform
    success_url = "/"
    
    def form_valid(self,form):
        form.save()
        messages.success(self.request,'Thank You.We will be in touch soon!!')
        return super().form_valid(form)

class portfolioview(generic.FormView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filters(is_active=True)
    
class portfoliodetialview(generic.DeleteView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"

class Blogview(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True) 

class blogdetailview(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"   
    

