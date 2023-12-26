from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('about/',views.aboutPage),
    path('services/',views. servicesPage),
    path('projects/',views. projectPage),
    path('blog/',views. blogPage),
    path('carrier/',views. carrierPage),
    path('harry/',views.harryPage),
    path('blog-details/',views.blogdetailsPage),
 
    path('contact/',views.contactPage), 
    
    
    
    
  
] 