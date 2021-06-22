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
            'wrist_passed',
            'wrist_total_time',
            'wrist_points',
            'wrist_seq',
            'wrist_punches',
                ]
