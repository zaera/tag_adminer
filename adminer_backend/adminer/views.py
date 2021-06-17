from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from adminer.models import Settings, Competition, Group, Runner, Wrist
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from adminer.tools import write_comp_id_to_file, read_comp_id_from_file, write_update_to_file, read_update_from_file


def handler404(request, exception, template_name="index.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def index_page(request):
    write_comp_id_to_file()
    read_comp_id_from_file()
    write_update_to_file()
    read_update_from_file()
    return render(request, 'index.html')
