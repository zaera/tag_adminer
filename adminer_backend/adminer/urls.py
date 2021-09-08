from django.urls import path
from .views import(
    # result_list,
    check_update,
    WristEditView,
    WristDeleteView,
    WristReadView,
    GroupEditView,
    GroupDeleteView,
    GroupReadView,
    RunnerEditView,
    RunnerDeleteView,
    RunnerReadView,
    resultlist,
)


app_name = 'adminer'

urlpatterns = [
    path('resultlist/', resultlist, name='result-list'),
    # path('result_list/', result_list, name='result-list'),
    path('check_update/', check_update, name='check-update'),

    path('update_wrist/<int:pk>', WristEditView.as_view(), name='update-wrist'),
    path('delete_wrist/<int:pk>', WristDeleteView.as_view(), name='delete-wrist'),
    path('read_wrist/<int:pk>', WristReadView.as_view(), name='read-wrist'),

    path('update_group/<int:pk>', GroupEditView.as_view(), name='update-group'),
    path('delete_group/<int:pk>', GroupDeleteView.as_view(), name='delete-group'),
    path('read_group/<int:pk>', GroupReadView.as_view(), name='read-group'),

    path('update_runner/<int:pk>', RunnerEditView.as_view(), name='update-runner'),
    path('delete_runner/<int:pk>', RunnerDeleteView.as_view(), name='delete-runner'),
    path('read_runner/<int:pk>', RunnerReadView.as_view(), name='read-runner'),
]
