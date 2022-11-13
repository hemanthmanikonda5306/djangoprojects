from rest_framework.serializers import ModelSerializer
from cbvapp.models import Cbv


class CbvSerializers(ModelSerializer):
    class Meta:
        model = Cbv
        fields = '__all__'
