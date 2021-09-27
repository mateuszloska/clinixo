from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import ContactProfile

class ContactListView(ListView):
    queryset = ContactProfile.objects.all()
    context_object_name = 'contact_list'
    paginate_by = 1
    template_name = 'patient_mgm/contact_list.html'