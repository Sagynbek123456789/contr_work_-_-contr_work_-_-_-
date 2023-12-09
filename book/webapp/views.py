from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices
from webapp.validate_char_field import task_validate
from webapp.forms import TaskForm, AuthorSearchForm


def index_view(request):
    search_form = AuthorSearchForm(request.GET)
    tasks = Task.objects.filter(status='active').order_by('-created_at')

    if search_form.is_valid() and 'author' in search_form.cleaned_data:
        author_name = search_form.cleaned_data['author']
        tasks = Task.objects.filter(author__icontains=author_name, status='active').order_by('-created_at')

    return render(request, 'index.html', {'tasks': tasks, 'search_form': search_form})


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_create.html', {'status_choices': status_choices, 'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)

        if form.is_valid():
            task = Task.objects.create(
                author=form.cleaned_data.get('author'),
                mail=form.cleaned_data.get('mail'),
                description=form.cleaned_data.get('description'),
                # status=form.cleaned_data.get('status')

            )
            return redirect('index')
        else:
            return render(request, 'task_create.html', {'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task_update.html', {'status_choices': status_choices, 'task': task, 'form': form})
    elif request.method == 'POST':
        author = request.POST.get('author')
        mail = request.POST.get('mail')
        description = request.POST.get('description')
        # status = request.POST.get('status')
        errors = task_validate(task.author, task.mail, task.description, task.status)

        if errors:
            return render(request, 'task_update.html',
                          {'status_choices': status_choices, 'errors': errors, 'task': task})
        else:
            task.author = author
            task.mail = mail
            task.description = description
            # task.status = status
            task.save()
            return redirect('index')


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
