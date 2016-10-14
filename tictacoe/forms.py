from django.core.exceptions import ValidationError
from django.forms import ModelForm, HiddenInput
from tictacoe.models import Invitation, Move, BOARD_SIZE


class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        #fields = '__all__'
        exclude = ['from_user']


class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = ['game', 'by_first_player', 'comment', 'timestamp']
        #widgets = {'x': HiddenInput(), 'y': HiddenInput()}

    def clean(self):
        game = self.instance.game
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        if not game or not game.status == 'A' or not game.is_empty(x, y):
            raise ValidationError('Illegal move')
        return self.cleaned_data
