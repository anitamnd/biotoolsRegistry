from rest_framework import serializers
from elixir.models import Domain

# just get the names and the id's
class SubdomainNameSerializer(serializers.ModelSerializer):
	resourcesCount = serializers.SerializerMethodField()

	class Meta:
		model = Domain
		fields = ('name', 'resourcesCount')

	def get_resourcesCount(self, obj):
		return obj.domainresource_set.count()


# class DomainSerializer(serializers.ModelSerializer):
# 	name = serializers.CharField(min_length=1, max_length=50, allow_blank=False, validators=[IsStringTypeValidator], required=True)
	
