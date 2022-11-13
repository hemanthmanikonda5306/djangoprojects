from rest_framework.serializers import ModelSerializer
from Modelviewsetcrudapp.models import Model_crud

class Model_serializers(ModelSerializer):
    class Meta:
        model = Model_crud
        fields = '__all__'
