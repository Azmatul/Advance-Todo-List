from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.db.models import Q

from .models import *
from TodoList.models import *


def add_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        # Create a new task using the 'objects' manager
        Tasks.objects.create(
            title=title,
            description=description,
        )
        return redirect("home")

    return render(request, "add_list.html")


def tasks_list(request):
    filter_option = request.GET.get('filter', 'all')
    search_query = request.GET.get('search_task', '')  # Get the search input

    if filter_option == 'active':
        tasks = Tasks.objects.filter(is_achieve=False)
    elif filter_option == 'achieve':
        tasks = Tasks.objects.filter(is_achieve=True)
    else:
        tasks = Tasks.objects.all()

    # Apply search filter on top of the above query
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    context = {
        'tasks': tasks,
        'filter_option': filter_option,
        'search_task': search_query,
    }

    return render(request, 'home.html', context)


def mark_achieved(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.is_achieve = True
    task.save()
    return redirect('home')


def unmark_achieved(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.is_achieve = False
    task.save()
    return redirect('home')


def update(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')

        task.save()

        return redirect('home')
    return render(request, "update.html", {"task": task})


def delete(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.delete()
    return redirect('home')
