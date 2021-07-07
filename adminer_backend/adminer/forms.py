from bootstrap_modal_forms.forms import BSModalModelForm
from adminer.models import Settings, Competition, Group, Runner, Wrist


class WristEditForm(BSModalModelForm):
    class Meta:
        model = Wrist
        fields = [
            'wrist_competition_id',
            'wrist_sn',
            'wrist_firmware',
            'wrist_voltage',
            # 'wrist_passed',
            # 'wrist_total_time',
            # 'wrist_points',
            'wrist_seq',
            'wrist_punches',
                ]


class GroupEditForm(BSModalModelForm):
    class Meta:
        model = Group
        fields = [
            'group_competition_id',
            'group_name',
            'group_seq',
                ]


class RunnerEditForm(BSModalModelForm):
    class Meta:
        model = Runner
        fields = [
            'runner_competition_id',
            'runner_group_id',
            'runner_sn',
            'runner_name',
            'runner_club',
            'runner_coach',
            'runner_skill',
            'runner_state',
                ]

