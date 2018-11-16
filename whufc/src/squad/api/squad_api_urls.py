from django.urls import path
from django.conf.urls import url

from .views  import SquadMemberListView, SquadMemberRUDView

app_name = 'squad_api'
urlpatterns = [
	url(r'^$', SquadMemberListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/', SquadMemberRUDView.as_view(), name='detail'),
]