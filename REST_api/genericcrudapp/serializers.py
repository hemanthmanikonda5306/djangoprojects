from rest_framework.serializers import ModelSerializer
from genericcrudapp.models import Gen


class GvSerializers(ModelSerializer):
    class Meta:
        model = Gen
        fields='__all__'

