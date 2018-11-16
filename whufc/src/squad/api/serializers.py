from rest_framework import serializers

from squad.models import SquadMember


class SquadMemberSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField(read_only=True)
	image_url = serializers.SerializerMethodField()
	class Meta:
		model = SquadMember
		fields = [
			'url','name','slug', 'image','image_url', 
			'nationality', 'flag', 'number', 'position',
			'appearances', 'minutes','goals', 
			'assists', 'yellow_cards', 'red_cards', 
			'shots_per_game','key_passes', 'rating'
		]
		read_only_fields = ['user']

	def get_url(self,obj):
		request = self.context.get('request')
		return obj.get_api_url(request=request)

	def get_image_url(self, obj):
		if obj.image:
			print(obj.image.url)
			return obj.image.url
		else:
			return None

