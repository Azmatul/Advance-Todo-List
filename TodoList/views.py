from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import *
from TodoList.models import *

@login_required
def add_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        # Create a new task using the 'objects' manager
        Tasks.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )
        return redirect("home")

    return render(request, "add_list.html")


@login_required
def tasks_list(request):
    filter_option = request.GET.get('filter', 'all')
    search_query = request.GET.get('search_task', '')

    # Start by filtering tasks that belong only to the logged-in user
    tasks = Tasks.objects.filter(created_by=request.user)

    # Then filter based on achievement status
    if filter_option == 'active':
        tasks = tasks.filter(is_achieve=False)
    elif filter_option == 'achieve':
        tasks = tasks.filter(is_achieve=True)

    # Apply search filter on top of all above
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


@login_required
def mark_achieved(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.is_achieve = True
    task.save()
    return redirect('home')

@login_required
def unmark_achieved(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.is_achieve = False
    task.save()
    return redirect('home')

@login_required
def update(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')

        task.save()

        return redirect('home')
    return render(request, "update.html", {"task": task})

@login_required
def delete(request, task_id):
    task = get_object_or_404(Tasks, uid=task_id)
    task.delete()
    return redirect('home')
