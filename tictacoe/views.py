from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from tictacoe.models import Invitation, Game
from tictacoe.forms import InvitationForm


# Create your views here.

@login_required
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(data=request.POST, instance=invitation)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = InvitationForm()
    return render(request, 'tictacoe/new_invitation.html', {'form': form})


@login_required
def accept_invitation(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == "POST":
        if 'accept' in request.POST:
            game = Game.objects.new_game(invitation)
            game.save()
            invitation.delete()
            return redirect(game)
            #return HttpResponse('Invitation accepted')
        else:
            invitation.delete()
            return redirect('user_home')
    else:
        return render(request, 'tictacoe/accept_invitation.html', {'invitation': invitation })



@login_required
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game.is_users_move(request.user):
        return redirect('tictacoe_game_do_move', pk=pk)
    return render(request, 'tictacoe/game_detail.html', {'game': game})


@login_required
def game_do_move(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if not game.is_users_move(request.user):
        #return redirect('tictacoe_game_do_move', pk=pk)
        raise PermissionDenied
    return render(request, 'tictacoe/game_do_move.html', {'game': game})
