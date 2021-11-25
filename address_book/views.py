from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Contact


class HomePageView(TemplateView):
    template_name = "address_book/home.html"


class ListContactsView(ListView):
    model = Contact
    template_name = "address_book/list_contacts.html"

    def get(self, request, **kwargs):
        query = self.request.GET.get('q')
        if query:
            contacts = Contact.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(phone__icontains=query)
            ).order_by('first_name')
        else:
            contacts = Contact.objects.all().order_by('first_name')
        return render(request, self.template_name, {'contacts': contacts})


class AddContactView(CreateView):
    template_name = "address_book/add_new_contact.html"
    model = Contact
    fields = ['first_name',
              'last_name',
              'country',
              'city',
              'street',
              'house_number',
              'url',
              'phone',
              'profile_pic']
    success_url = reverse_lazy('list_contacts')


class EditContactView(UpdateView):
    template_name = 'address_book/edit_contact.html'
    model = Contact
    fields = ['first_name',
              'last_name',
              'country',
              'city',
              'street',
              'house_number',
              'url',
              'phone',
              'profile_pic']
    success_url = reverse_lazy('list_contacts')


class DeleteContactView(DeleteView):
    template_name = 'address_book/contact_confirm_delete.html'
    model = Contact
    success_url = reverse_lazy('list_contacts')
