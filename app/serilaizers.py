from app.models import Person, Pet, Country, Vehicle
from rest_framework import serializers


class PetSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField(source='get_brand')
    class Meta:
        model = Pet
        fields = "__all__"  

    def get_brand(self, obj):
        return str(obj.brand)

class VehicleSerializer(serializers.ModelSerializer):
    person_name = serializers.SerializerMethodField(source='get_person_name')

    pet = PetSerializer(many=True, read_only=True)
    class Meta:
        model = Vehicle 
        fields = "__all__"

    def get_person_name(self, obj):
        return str(obj.person_name)    


class PersonSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField(source='get_country_name')
    
    vehicle = VehicleSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = "__all__"

    def get_country_name(self, obj):
        return str(obj.country_name)       


class CountrySerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = "__all__"

