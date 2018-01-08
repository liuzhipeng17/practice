class ResearchSerializer(serializers.ModelSerializer):
    templates = serializers.SerializerMethodField()

    class Meta:
        model = Research
        fields = ('id', 'created', 'speaker', 'body', 'templates')

    def get_templates(self, obj):
        values = obj.get_values() # whatever your filter values are. obj is the Research instance
        templates = ResearchTemplate.objects.filter(mergefields__contained_by=values) # Or whatever queryset filter
        return ResearchTemplateSerializer(templates, many=True).data
		
		
# 官网的做法
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days、
		
# 官网地址 http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
