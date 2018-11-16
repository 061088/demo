from rest_framework import generics
from rest_framework.mixins import CreateModelMixin

from .serializers import SquadMemberSerializer

from squad.models import SquadMember


class SquadMemberListView(CreateModelMixin, generics.ListAPIView):
	lookup_field = 'slug'
	serializer_class = SquadMemberSerializer

	def get_queryset(self):
		return SquadMember.objects.all()

	def filter_queryset(self, queryset):
		queryset = super(SquadMemberListView, self).filter_queryset(queryset)
		return queryset.order_by('number')

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def get_serializer_context(self):
		"""
		Extra context provided to the serializer class.
		"""
		return {
			'request': self.request,
			'format': self.format_kwarg,
			'view': self
		}


class SquadMemberRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'slug'
	serializer_class = SquadMemberSerializer

	def get_queryset(self):
		return SquadMember.objects.all()
	
	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

