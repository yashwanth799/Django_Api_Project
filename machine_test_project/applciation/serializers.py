from rest_framework import serializers
from rest_framework import serializers
from applciation.models import Client, Project, User


class AddClientSerializers(serializers.Serializer):
    # id = serializers.IntegerField(label="Enter Client Id")
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    created_by = serializers.CharField(max_length=255)


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ('id', 'name')

class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=True)
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users']

    # def create(self, validated_data):
    #     project = Project.objects.create(
    #         name=validated_data['name'],
    #         client=validated_data['client'],
    #     )
    #     assigned_users = validated_data.get('assigned_users', [])
    #     project.assigned_users.set(assigned_users)
    #     return project


class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'projects', 'email', 'phone', 'address',
                  'created_by', 'created_at')

    def update(self, instance, validated_data):
        projects_data = validated_data.pop('projects', None)
        if projects_data:
            for project_data in projects_data:
                project_id = project_data.pop('id', None)
                project = Project.objects.get(id=project_id)
                for key, value in project_data.items():
                    setattr(project, key, value)
                project.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
