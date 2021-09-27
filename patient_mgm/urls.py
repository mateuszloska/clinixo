from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import ContactListView

app_name = 'patient_mgm'

urlpatterns = [
    path('',TemplateView.as_view(template_name="patient_mgm/base.html"), name='main_page'),
    path('contacts', ContactListView.as_view(), name='contact_list'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]