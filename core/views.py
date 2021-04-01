from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Host, Participant, Contact
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


def about(request):
    template_name = "core/about.html"
    return render(request, template_name)


def projects(request):
    template_name = "core/projects.html"
    projects = Participant.objects.all()
    context = {"projects": projects}
    return render(request, template_name, context)


def contact(request):
    template_name = "core/contact.html"
    return render(request, template_name)


@csrf_exempt
def add_contact(request):
    if request.method == "POST":
        Full_Name = request.POST["name"]
        Email_Address = request.POST["email"]
        Message = request.POST["message"]
        Contact.objects.create(
            Full_Name=Full_Name,
            Email_Address=Email_Address,
            Message=Message,
        )
        messages.success(request, "Your message is successfully sent!")

    return redirect("contact")


def host(request):
    template_name = "core/host.html"

    return render(request, template_name)


@csrf_exempt
def add_host(request):
    username = request.user.get_username()
    if request.method == "POST":
        full_name = request.POST["name"]
        email = request.POST["email"]
        org = request.POST["org"]
        type_org = request.POST["type"]
        designation = request.POST["designation"]
        phone = request.POST["phone"]
        purpose = request.POST["purpose"]
        detail = request.POST["detail"]
        theme = request.POST["theme"]
        guidelines = request.POST["guidelines"]
        elig_cri = request.POST["age"]
        last_sub = request.POST["last_sub"]
        Host.objects.create(
            username=username,
            full_name=full_name,
            email=email,
            org=org,
            type_org=type_org,
            designation=designation,
            phone=phone,
            purpose=purpose,
            detail=detail,
            theme=theme,
            guidelines=guidelines,
            elig_cri=elig_cri,
            last_sub=last_sub,
        )

    return redirect("/")


def host_dashboard(request, username):
    username = username
    host_obj = Host.objects.get(username=username)
    host_id = host_obj.id
    projects = Participant.objects.all().filter(host_id=host_id)
    template_name = "core/dashboard.html"
    context = {"host_obj": host_obj, "projects": projects}
    return render(request, template_name, context)


def delete_host(request, username):
    host_obj = Host.objects.get(username=username)
    host_obj.delete()

    return redirect("/")


@csrf_exempt
def add_participant(request, host_id):
    host_id = host_id
    username = request.user.get_username()
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        url = fs.url(filename)
        new_participant = Participant(
            username=username,
            School_Name=request.POST["school_name"],
            School_Phone_no=request.POST["school_phone"],
            School_Email_address=request.POST["school_email"],
            School_Address=request.POST["school_address"],
            State=request.POST["school_state"],
            Student_Name=request.POST["name"],
            Contact_no=request.POST["phone"],
            Email_address=request.POST["email"],
            House_Address=request.POST["address"],
            Gender=request.POST["gender"],
            Title_of_your_project=request.POST["title"],
            Question_or_Problem=request.POST["question"],
            Hypothesis_or_possible_solution=request.POST["solution"],
            Materials_needed=request.POST["material"],
            Results=request.POST["results"],
            Image_of_Project=url,
            Link_of_your_project=request.POST["link"],
            host_id=host_id,
        )
        new_participant.save()
        return redirect("projects")


def detail(request):
    template_name = "core/detail.html"
    hosts = Host.objects.all()
    context = {"hosts": hosts}
    return render(request, template_name, context)


def applyto(request, host_id):
    host_id = host_id
    template_name = "core/applyto.html"
    host_obj = Host.objects.get(pk=host_id)
    context = {"host_obj": host_obj, "host_id": host_id}
    return render(request, template_name, context)


def participant(request, host_id):
    host_id = host_id
    template_name = "core/participant.html"
    context = {"host_id": host_id}

    return render(request, template_name, context=context)


def project_details(request, project_id):
    template_name = "core/project_details.html"
    project_obj = Participant.objects.get(pk=project_id)
    context = {"project_obj": project_obj}
    return render(request, template_name, context)


def project_view(request, project_id):
    template_name = "core/project_view.html"
    project_obj = Participant.objects.get(pk=project_id)
    context = {"project_obj": project_obj}
    return render(request, template_name, context)