from django.conf.urls import url
from industrydetailsapp import views
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [

    url(r'^$', views.Signin, name='Login'),
    # url(r'^$', views.Details_Form, name='Details_Form'),
    url(r'^Signup', views.Signup, name='Signup'),
    url(r"^Signin", views.Signin, name='Signin'),
    url(r'^ssignupdetails', views.ssignupdetails, name='ssignupdetails'),
    url(r'^ssignindetails', views.ssignindetails, name='ssignindetails'),
    url(r'^Details_Form', views.Details_Form, name='Details_Form'),
    url(r'^submitdetails', views.submitdetails, name='submitdetails'),
    # url(r'^ssignin', views.ssignindetails, name='ssignindetails'),

]
