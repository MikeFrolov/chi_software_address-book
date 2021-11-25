from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


from . import forms
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
            )
        else:
            contacts = Contact.objects.all()
        return render(request, self.template_name, {'contacts': contacts})


class AddContactView(CreateView):
    template_name = "address_book/add_new_contact.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy('list_contacts')

    def get_success_url(self) -> str:
        return super().get_success_url()


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
