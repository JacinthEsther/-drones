from rest_framework import serializers

from drones.models import DroneCategory, Drone


# The DroneCategorySerializer class declares a drones attribute that holds an instance of
# serializers.HyperlinkedRelatedField with many and read_only equal to True. This way, the code defines a one-to-many
# relationship that is read- only.

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(many=True,
                                                 read_only=True,
                                                 view_name='drone-detail')

    class Meta:
        model = DroneCategory
        fields = ('url', 'pk', 'name', 'drones')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # Display the category name
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = ('url', 'name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp')
