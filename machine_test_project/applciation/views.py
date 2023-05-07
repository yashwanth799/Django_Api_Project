from django.http import HttpResponse
import http
from pstats import Stats
import statistics
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .forms import ProjectForm
from .forms import ClientForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Project, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import AddClientSerializers, ClientSerializer, ProjectSerializer
from .models import Client
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from applciation.models import Client, Project
from applciation.serializers import ProjectSerializer


def home(request):
    return render(request, 'base.html')


@api_view()
def add_clients(request, id):
    client = get_object_or_404(Client, pk=id)
    serializers = AddClientSerializers(client)
    return Response(serializers.data)


# @api_view()
# def clients_list(request, id):
#     seralizer
#     clients = Client.objects.all()
#     return render(request, 'client_list.html', {'clients': clients})


# class BookApiView(APIView):
#     serializer_class = BookSerializer

#     def get(self, request):
#         allBooks = Book.objects.all().values()
#         return Response({"Message": "List of Books", "Book List": allBooks})


# class BookApiView(APIView):
#     serializer_class = BookSerializer
#     def get(self, request):
#         allBooks = Book.objects.all().values()
#         return Response({"Message": "List of Books", "Book List": allBooks})

    # def post(self, request):
    #     print('Request data is : ', request.data)
    #     serializer_obj = BookSerializer(data=request.data)
    #     if (serializer_obj.is_valid()):

    #         Book.objects.create(id=serializer_obj.data.get("id"),
    #                             title=serializer_obj.data.get("title"),
    #                             author=serializer_obj.data.get("author")
    #                             )

    #     book = Book.objects.all().filter(id=request.data["id"]).values()
    #     return Response({"Message": "New Book Added!", "Book": book})

# retriving and adding the clients in the database
class ClientApiView(APIView):
    serializer_class = AddClientSerializers

    def get(self, request):
        allClients = Client.objects.all().values()
        return Response({"Message": "List of Clients", "Client List": allClients})

    def post(self, request):
        print('Request data is : ', request.data)
        serializer_obj = AddClientSerializers(data=request.data)
        if (serializer_obj.is_valid()):

            Client.objects.create(name=serializer_obj.data.get("name"),
                                  email=serializer_obj.data.get("email"),
                                  phone=serializer_obj.data.get("phone"),
                                  address=serializer_obj.data.get("address"),
                                  created_by=serializer_obj.data.get(
                                      "created_by"),
                                  created_at=serializer_obj.data.get(
                                      "created_at"),
                                  )

        allClients = Client.objects.all().values()
        return Response({"Message": "List of Clients", "Client List": allClients})

# it is used to show the client data with the project assigned using id


class ClientView(APIView):
    def post(self, request):
        serializer_obj = AddClientSerializers(data=request.data)
        if serializer_obj.is_valid():
            client = Client.objects.create(**serializer_obj.validated_data)
            return Response(ClientSerializer(client).data)
        return Response(serializer_obj.errors)

    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class ClientViewUpdate(APIView):
    def get(self, request, id):
        client = get_object_or_404(Client, pk=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client = get_object_or_404(Client, pk=id)
        serializer_obj = ClientSerializer(client, data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        else:
            return Response(serializer_obj.errors, status=400)


class ClientViewDelete(APIView):
    def delete(self, request, id):
        client = get_object_or_404(Client, pk=id)
        client.delete()
        return Response(status=204)


class ProjectView(APIView):
    serializer_class = ProjectSerializer

    def get(self, request):
        allProject = Project.objects.all().values()
        return Response({"Message": "List of Projects", "Project List": allProject})

    def post(self, request):
        serializer_obj = ProjectSerializer(data=request.data)
        if serializer_obj.is_valid():
            client = get_object_or_404(Client, id=id)
            project = serializer_obj.save(client=client)
            users = User.objects.filter(id__in=request.data.getlist('users'))
            project.users.set(users)
            return Response(ProjectSerializer(project).data, status=Stats.HTTP_201_CREATED)
        return Response(serializer_obj.errors, status=statistics.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer_obj = ProjectSerializer(data=request.data)
    #     if serializer_obj.is_valid():
    #         client = get_object_or_404(Client, id=id)
    #         project = serializer_obj.save(client=client)
    #         users = request.data.getlist('users')
    #         project.users.set(users)
    #         return Response(ProjectSerializer(project).data, status=Stats.HTTP_201_CREATED)
    #     return Response(serializer_obj.errors, status=statistics.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     serializer_obj = ProjectSerializer(data=request.data)
    #     print('Request data is : ', request.data)
    #     serializer_obj = ProjectSerializer(data=request.data)
    #     if (serializer_obj.is_valid()):

    #         Project.objects.create(name=serializer_obj.data.get("name"),
    #                                #    client=serializer_obj.data.get("client"),
    #                                users=serializer_obj.data.get(
    #             "users"),
    #         )

    #     allProjects = Project.objects.all().values()
    #     return Response({"Message": "List of Projects", "Project List": allProjects})

# class ProjectView(APIView):
#     def post(self, request, id):
#         client = get_object_or_404(Client, pk=id)
#         serializer_obj = ProjectSerializer(data=request.data)
#         if serializer_obj.is_valid():
#             project = serializer_obj.save(client=client)
#             return Response({"Message": "Project created successfully", "Project ID": project.id})
#         else:
#             return Response(serializer_obj.errors, status=400)

    # def get(self, request, id):
    #     client = get_object_or_404(Client, id)
    #     serializer = ClientSerializer(client)
    #     clients = Client.objects.prefetch_related('projects')
    #     serializer = ClientSerializer(clients, many=True)
    #     return Response(serializer.data)


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form, 'client': client})


def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'delete_client.html', {'client': client})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'delete_project.html', {'project': project})


def add_project(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            return redirect('project_list')
    else:
        form = ProjectForm(initial={'users': users})
    return render(request, 'add_project.html', {'form': form})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(username=username, password=password)
            user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'delete_user.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin-dashboard')
            elif user.is_not_superuser:
                return redirect('user-dashboard')
        else:
            return HttpResponse("okay")
    else:
        return render(request, 'login.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
def user_dashboard(request):
    user_data = request.user
    return render(request, 'user_dashboard.html', {'user_data': user_data})
