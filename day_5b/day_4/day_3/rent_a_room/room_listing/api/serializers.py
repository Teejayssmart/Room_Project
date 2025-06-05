from rest_framework import serializers

# (1)create a serializser to map all the values
class RoomSerializer(serializers.Serializer):
    title =serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    location = serializers.CharField()
    available_from = serializers.DateField()
    owner = serializers.CharField()