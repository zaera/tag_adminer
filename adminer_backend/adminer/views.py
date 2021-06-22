from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from adminer.models import Settings, Competition, Group, Runner, Wrist
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from adminer.tools import *
from django.http import JsonResponse
from .forms import WristEditForm
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView, BSModalReadView
# from random import randint
# queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
# for i in queryset_runner:
#     i.runner_group_id = randint(41, 80)
#     i.save()


def handler404(request, exception, template_name="index.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def index_page(request):
    # write_comp_id_to_file()
    # read_comp_id_from_file()
    # write_update_to_file()
    # read_update_from_file()
    return render(request, 'index.html')


class WristReadView(BSModalReadView):
    model = Wrist
    template_name = 'read_wrist.html'


class WristEditView(BSModalUpdateView):
    model = Wrist
    template_name = 'update_wrist.html'
    form_class = WristEditForm
    success_message = 'Success: Wrist was updated.'
    success_url = reverse_lazy('adminer:result-list')


class WristDeleteView(BSModalDeleteView):
    model = Wrist
    template_name = 'delete_wrist.html'
    success_message = 'Success: Wrist was deleted.'
    success_url = reverse_lazy('adminer:result-list')


def result_list(request):
    competition_id = read_comp_id_from_file()
    competition = Competition.objects.filter(id=competition_id)
    queryset_wrist = Wrist.objects.filter(wrist_competition_id=competition_id)
    queryset_group = Group.objects.filter(group_competition_id=competition_id)
    queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
    data = []
    for i in queryset_wrist:
        name = ''
        group = ''
        for runner in queryset_runner:
            if runner.runner_sn == i.wrist_sn:
                name = runner.runner_name
                for group_ in queryset_group:
                    if group_.id == runner.runner_group_id:
                        group = group_.group_name
        sn = i.wrist_sn
        if sn < 10:
            sn = '000' + str(sn)
        elif sn < 100:
            sn = '00' + str(sn)
        elif sn < 1000:
            sn = '0' + str(sn)
        data.append(tuple((i.id, sn, name, group, i.wrist_voltage, i.wrist_passed)))
    context = {
        'data': data,
        'competition': competition[0].comp_name,
    }
    return render(request, 'result_list.html', context=context)
    # return JsonResponse(data, safe=False)


def check_update(request):
    data = read_update_from_file()
    return JsonResponse(data, safe=False)

