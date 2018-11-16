from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from squad.models import SquadMember


class SquadMemberAPITestCase(APITestCase):
	def setUp(self):
		SquadMember.objects.create(
			name='Mark Noble',
			slug='mark-noble',  
			nationality='English',  
			number=16, 
			position='Midfield',
			appearances=6, 
			minutes=496,
			goals=0, 
			assists=2, 
			yellow_cards=1, 
			red_cards=0, 
			shots_per_game=0.5,
			key_passes=0.7, 
			rating=6.5
		)

	def test_player_name(self):
		mark_noble = SquadMember.objects.get(name='Mark Noble')
		self.assertEqual(mark_noble.name, 'Mark Noble')