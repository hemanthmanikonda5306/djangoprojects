from rest_framework.serializers import ModelSerializer
from simplejwt.models import Simple


class Simple_Serializers(ModelSerializer):
    class Meta:
        model = Simple
        fields = '__all__'
