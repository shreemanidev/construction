from django.shortcuts import render

def homePage(Request):
    return render(Request,"index.html")

def aboutPage(Request):
     return render(Request,"about.html")
def servicesPage(Request):
     return render(Request,"services.html")
def projectPage(Request):
     return render(Request,"projects.html")
def blogPage(Request):
     return render(Request,"blog.html")
def blogdetailsPage(Request):
     return render(Request,"blog-details.html")
def contactPage(Request):
     return render(Request,"contact.html")
def carrierPage(Request):
     return render(Request,"carrier.html")
def harryPage(Request):
     return render(Request,"harry.html")