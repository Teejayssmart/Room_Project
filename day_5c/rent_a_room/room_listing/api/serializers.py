from rest_framework import serializers
from room_listing.models import Room
# from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        #fields = ['id', 'title', 'description', 'price', 'location', 'available_from']
        #exclude = ['owner', 'active'] 



















#validators
# def title_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Tilte is too short.")
#     else:
#         return value

# (1)create a serializser to map all the values
# class RoomSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title =serializers.CharField(validators=[title_length])
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     location = serializers.CharField()
#     available_from = serializers.DateField()
#     owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     active = serializers.BooleanField()
    
    # def create(self, validated_data):
    #     return Room.objects.create(**validated_data)
    
    # #instance = old value validate_data = new value
    # def update(self, instance, validated_data):
    #         instance.title = validated_data.get('title')
    #         instance.description = validated_data.get('description')
    #         instance.price = validated_data.get('price')
    #         instance.location = validated_data.get('location')
    #         instance.available_from = validated_data.get('available_from')
    #         instance.owner = validated_data.get('owner')
    #         instance.active = validated_data.get('active')
    #         instance.save()
    #         return instance
            
            
            #filed-level validation
    # def validate_title(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name should be at least 5 characters long.")
    #     else:
    #         return value
        
        #object-level validation
    def validate(self, attrs):
        if attrs['title'] == attrs['description']:
            raise serializers.ValidationError("Title and Description cannot be same.")
        else:
            return attrs
        
        