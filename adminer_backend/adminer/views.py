from random import randrange
import hashlib
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from adminer.models import Settings, Competition, Group, Runner, Wrist
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from adminer.tools import *
from django.http import JsonResponse
from .forms import WristEditForm, GroupEditForm, RunnerEditForm
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalDeleteView, BSModalReadView
from django.core.files.storage import default_storage
# from random import randint
# queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
# for i in queryset_runner:
#     i.runner_group_id = randint(41, 80)
#     i.save()
import os

from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


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


class RunnerReadView(BSModalReadView):
    model = Runner
    template_name = 'read_runner.html'


class RunnerEditView(BSModalUpdateView):
    model = Runner
    template_name = 'update_runner.html'
    form_class = RunnerEditForm
    success_message = 'Success: Runner was updated.'
    success_url = reverse_lazy('adminer:result-list')


class RunnerDeleteView(BSModalDeleteView):
    model = Runner
    template_name = 'delete_runner.html'
    success_message = 'Success: Runner was deleted.'
    success_url = reverse_lazy('adminer:result-list')


class GroupReadView(BSModalReadView):
    model = Group
    template_name = 'read_group.html'


class GroupEditView(BSModalUpdateView):
    model = Group
    template_name = 'update_group.html'
    form_class = GroupEditForm
    success_message = 'Success: Group was updated.'
    success_url = reverse_lazy('adminer:result-list')


class GroupDeleteView(BSModalDeleteView):
    model = Group
    template_name = 'delete_group.html'
    success_message = 'Success: Group was deleted.'
    success_url = reverse_lazy('adminer:result-list')


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


@query_debugger
def resultlist(request):
    # Group.objects.all().filter(competition__id=5)[0].group_name
    # https://medium.com/@dwernychukjosh/sha256-encryption-with-python-bf216db497f9
    hash_string = str(randrange(1000))
    text = hashlib.sha256(hash_string.encode()).hexdigest()
    f = open(os.path.join(settings.BASE_DIR, 'adminer/static/upd.txt'), 'w')
    f.write(str(text))
    f.close()

    data = []
    wrists = Wrist.objects.prefetch_related('competition').filter(competition__id=1)
    runners = Runner.objects.select_related('competition', 'group').filter(competition__id=1)
    groups = Group.objects.select_related('competition').filter(competition__id=1)

    for wrist in wrists:
        runner_name = ''
        runner_group = 0
        group_name = ''
        for runner in runners:
            if runner.runner_sn == wrist.wrist_sn:
                runner_name = runner.runner_name
                runner_group = runner.group
        for group in groups:
            if group == runner_group:
                group_name = group.group_name

        data.append(list((
            wrist.wrist_sn,
            runner_name,
            group_name,
            wrist.wrist_voltage,
            wrist.wrist_seq,

        )))

    count = len(data)
    context = {
        'data': data,
        'count': count,
    }

    return render(request, 'result_list_.html', context=context)


# def result_list(request):
#     # competition_id = read_comp_id_from_file()
#     # competition = Competition.objects.filter(id=competition_id)
#     # queryset_wrist = Wrist.objects.filter(wrist_competition_id=competition_id)
#     # queryset_group = Group.objects.filter(group_competition_id=competition_id)
#     # queryset_runner = Runner.objects.filter(runner_competition_id=competition_id)
#     # data = []
#     # for i in queryset_wrist:
#     #     runner_name = ''
#     #     runner_id = ''
#     #     group_name = ''
#     #     group_id = ''
#     #     for runner in queryset_runner:
#     #         if runner.runner_sn == i.wrist_sn:
#     #             runner_name = runner.runner_name
#     #             runner_id = runner.id
#     #             for group_ in queryset_group:
#     #                 if group_.id == runner.runner_group_id:
#     #                     group_name = group_.group_name
#     #                     group_id = group_.id
#     #                     group_seq = group_.group_seq
#     #     sn = i.wrist_sn
#     #     if sn < 10:
#     #         sn = '000' + str(sn)
#     #     elif sn < 100:
#     #         sn = '00' + str(sn)
#     #     elif sn < 1000:
#     #         sn = '0' + str(sn)
#     #     voltage = i.wrist_voltage
#     #     if 75 < voltage:
#     #         voltage = '<i class="fa fa-battery-full" aria-hidden="true"></i>'
#     #     elif 60 < voltage < 76:
#     #         voltage = '<i class="fa fa-battery-three-quarters" aria-hidden="true"></i>'
#     #     elif 40 < voltage < 61:
#     #         voltage = '<i class="fa fa-battery-half" aria-hidden="true"></i>'
#     #     elif 15 < voltage < 41:
#     #         voltage = '<i class="fa fa-battery-quarter" aria-hidden="true"></i>'
#     #     elif 0 < voltage < 16:
#     #         voltage = '<i class="fa fa-battery-empty" aria-hidden="true"></i>'
#     #     # data.append(tuple((i.id, sn, runner_id, runner_name.replace(" ", "<br>"), convert_time(i.wrist_total_time), group_id, group_name, voltage, i.wrist_passed)))
#     #     result = calculate_classic(i.wrist_seq, i.wrist_punches, group_seq, 2)
#     #
#     #     # print (result)
#     #     res = result[0]
#     #     result_passed = res[0]
#     #     result_total_time = res[1]
#     #     result_points = res[2]
#     #     judge_seq = res[3]
#     #     # print(res)
#     #     del result[0]
#     #     # print(result)
#     #     data.append(tuple((i.id, sn, runner_id, runner_name.replace(" ", "<br>"), convert_time(result_total_time),
#     #                        group_id, group_name, voltage, result_passed, result_points, judge_seq, result)))
#     context = {
#         'data': 'data',
#         'competition': 'competition[0].comp_name',
#     }
#
#     return render(request, 'result_list.html', context=context)
#     # return JsonResponse(data, safe=False)


def check_update(request):
    data = read_update_from_file()
    return JsonResponse(data, safe=False)
