from django.forms import ModelForm
from tictacoe.models import Invitation


class InvitationForm(ModelForm):

    class Meta:
        model = Invitation
        fields = '__all__'
        exclude = ['from_user']
