from django.urls import path
from .views import result_list, check_update, WristEditView, WristDeleteView, WristReadView


app_name = 'adminer'

urlpatterns = [
    path('result_list/', result_list, name='result-list'),
    path('check_update/', check_update, name='check-update'),
    path('update_wrist/<int:pk>', WristEditView.as_view(), name='update-wrist'),
    path('delete_wrist/<int:pk>', WristDeleteView.as_view(), name='delete-wrist'),
    path('read_wrist/<int:pk>', WristReadView.as_view(), name='read-wrist'),
]
