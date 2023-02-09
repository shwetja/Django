from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentForm, Student


# Create your views here.
class SimpleClassBasedView(View):
    def get(self, request):
        form = StudentForm()
        template_name = 'app1/add.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        template_name = 'app1/add.html'
        context = {'form': form}
        return render(request, template_name, context)


class Studentview(View):
    def get(self, request):
        obj = Student.objects.all()
        template_name = 'app1/show.html'
        context = {'data': obj}
        return render(request, template_name, context)


class Updateview(View):
    def get(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(instance=obj)
        template_name = 'app1/add.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        template_name = 'app1/add.html'
        context = {'form': form}
        return render(request, template_name, context)


class Deleteview(View):
    def get(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(instance=obj)
        template_name = 'app1/del_confirm.html'
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, pk):
        obj = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=obj)
        obj.delete()
        return redirect('show_url')

