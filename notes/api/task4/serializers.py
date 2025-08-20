from rest_framework.serializers import ModelSerializer
from api.task4.models import Order

class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"