from rest_framework.serializers import ModelSerializer
from fbvapp.models import Fbv


class FbvSerializers(ModelSerializer):
    class Meta:
        model = Fbv
        fields = '__all__'

