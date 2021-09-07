from django.contrib import admin
from .models import Settings, Competition, Group, Runner, Wrist
# from rangefilter.filters import DateTimeRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

# python manage.py gen_data


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'printer_ip', 'printer_autoprint', 'current_comp_id', 'version',)
    list_filter = ('printer_ip', 'printer_autoprint', 'current_comp_id', 'version',)
    search_fields = ('printer_ip', 'printer_autoprint', 'current_comp_id', 'version',)


class CompetitionResource(resources.ModelResource):
    class Meta:
        model = Competition


class CompetitionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comp_name', 'comp_type', 'comp_data',)
    list_filter = ('comp_name', 'comp_type',)
    search_fields = ('comp_name', 'comp_type', 'comp_data',)
    resource_class = CompetitionResource


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group


class GroupAdmin(ImportExportModelAdmin):
    list_display = ('id', 'group_name', 'group_seq', 'competition',)
    list_filter = ('group_name', 'group_seq', 'competition',)
    search_fields = ('group_name', 'group_seq', 'competition',)
    resource_class = GroupResource


class RunnerResource(resources.ModelResource):
    class Meta:
        model = Runner


class RunnerAdmin(ImportExportModelAdmin):
    list_display = ('id',
                    'runner_sn',
                    'runner_name',
                    'runner_club',
                    'runner_coach',
                    'runner_skill',
                    'runner_state',)
    list_filter = ('runner_sn',
                   'runner_name',
                   'runner_club',
                   'runner_coach',
                   'runner_skill',
                   'runner_state',)
    search_fields = ('runner_sn',
                     'runner_name',
                     'runner_club',
                     'runner_coach',
                     'runner_skill',
                     'runner_state',)
    resource_class = RunnerResource


class WristResource(resources.ModelResource):
    class Meta:
        model = Wrist


class WristAdmin(ImportExportModelAdmin):
    list_display = ('id',
                    'wrist_sn',
                    'wrist_firmware',
                    'wrist_voltage',
                    # 'wrist_passed',
                    # 'wrist_total_time',
                    # 'wrist_points',
                    'wrist_seq',
                    'wrist_punches',)
    list_filter = ('wrist_firmware',
                   'wrist_voltage',
                   # 'wrist_passed',
                   )
    search_fields = (
        'wrist_sn',
        'wrist_firmware',
        'wrist_voltage',
        'wrist_passed',
        'wrist_total_time',
        'wrist_points',
        'wrist_seq',
        'wrist_punches',)
    resource_class = WristResource


admin.site.register(Settings, SettingsAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Runner, RunnerAdmin)
admin.site.register(Wrist, WristAdmin)
