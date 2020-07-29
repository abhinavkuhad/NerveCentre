from rest_framework import serializers
from .models import ResourceCentre
from .models import Journalist
from .models import NewsCentre


class NewsCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCentre
        fields = ('id', 'source_name', 'author', 'title', 'description', 'news_url', 'publish_date','content')


class JournalistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journalist
        fields = ('id', 'first_name', 'last_name')


class ResourceCentreSerializer(serializers.ModelSerializer):
    newscentre = NewsCentreSerializer()
    journalist = JournalistSerializer()


    class Meta:
        model = ResourceCentre
        fields = ('id','journalist_fname','journalist_lname','current_status','assigned_date','newscentre','journalist')
