from django.contrib import admin
from .models import Competition, Group, Runner, Wrist
from rangefilter.filters import DateTimeRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CompetitionResource(resources.ModelResource):

    class Meta:
        model = Competition


class CompetitionAdmin(ImportExportModelAdmin):
    list_display = ('comp_name', 'comp_type',)
    list_filter = ('comp_name', 'comp_type',)
    search_fields = ('comp_name', 'comp_type',)
    resource_class = CompetitionResource


class GroupResource(resources.ModelResource):

    class Meta:
        model = Group


class GroupAdmin(ImportExportModelAdmin):
    list_display = ('group_name', 'group_seq', 'group_competition_id',)
    list_filter = ('group_name', 'group_seq', 'group_competition_id',)
    search_fields = ('group_name', 'group_seq', 'group_competition_id',)
    resource_class = GroupResource


class RunnerResource(resources.ModelResource):

    class Meta:
        model = Runner


class RunnerAdmin(ImportExportModelAdmin):
    list_display = ('runner_sn', 'runner_competition_id', 'runner_group_id', 'runner_name', 'runner_club', 'runner_coach', 'runner_skill', 'runner_state',)
    list_filter = ('runner_sn', 'runner_competition_id', 'runner_group_id', 'runner_name', 'runner_club', 'runner_coach', 'runner_skill', 'runner_state',)
    search_fields = ('runner_sn', 'runner_competition_id', 'runner_group_id', 'runner_name', 'runner_club', 'runner_coach', 'runner_skill', 'runner_state',)
    resource_class = RunnerResource


class WristResource(resources.ModelResource):

    class Meta:
        model = Wrist


class WristAdmin(ImportExportModelAdmin):
    list_display = ('wrist_competition_id', 'wrist_serial_number', 'wrist_firmware', 'wrist_voltage', 'wrist_passed', 'wrist_time', 'wrist_points',)
    list_filter = ('wrist_competition_id', 'wrist_serial_number', 'wrist_firmware', 'wrist_voltage', 'wrist_passed', 'wrist_time', 'wrist_points',)
    search_fields = ('wrist_competition_id', 'wrist_serial_number', 'wrist_firmware', 'wrist_voltage', 'wrist_passed', 'wrist_time', 'wrist_points',)
    resource_class = WristResource


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Runner, RunnerAdmin)
admin.site.register(Wrist, WristAdmin)
