from rest_framework import serializers

from myapp.models import Asset1

class AssetSerializer(serializers.ModelSerializer):
   class Meta:
       model = Asset1
       fields =  '__all__'
