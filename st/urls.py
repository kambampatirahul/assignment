from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('addassignment', views.addassignment, name='addassignment'),
    path('assignments', views.assignments, name='assignments'),
    path('showassignment', views.showassignment, name='showassignment'),
    path(r'solassignment/(?p<title>[0-9]+)$', views.solassignment, name='solassignment'),
    path(r'ass/(?p<title>[0-9]+)$', views.ass, name='ass'),
    path(r'rewords/(?p<title>[0-9]+)/(?p<id>[0-9]+)$', views.rewords, name='rewords'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home')
]