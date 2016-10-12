from django.conf.urls import url
from tictacoe.views import new_invitation, accept_invitation, game_detail, game_do_move

urlpatterns = [
    url(r'^invite/$', new_invitation, name='tictacoe_invite'),
    url(r'^invitation/(?P<pk>\d+)/$', accept_invitation, name='tictacoe_accept_invitation'),
    url(r'^game/(?P<pk>\d+)/$', game_detail, name='tictacoe_game_detail'),
    url(r'^game/(?P<pk>\d+)/do_move$', game_do_move, name='tictacoe_game_do_move')
]
