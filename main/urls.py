from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('portfolio',views.portfolioview.as_view(),name="portfolio"),
    path('portfolio/<slug:slug>',views.portfoliodetialview.as_view(),name="portfoliodetail"),
    path('blog/',views.Blogview.as_view(),name="blogs"),
    path('blog/<slug:slug>',views.blogdetailview.as_view(),name="blog"),
]
