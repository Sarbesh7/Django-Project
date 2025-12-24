
from .models import Student
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse


class Home(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'home.html', {'students': students})




   

class Create(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')  # FIXED

        if not all([name, age, email, address]):
            return render(request, 'create.html', {
                'error': 'All fields are required'
            })
        
        if Student.objects.filter(email=email).exists():
            return render(request, 'error.html', {
                'error': 'Email already exists'
            })
       

        Student.objects.create(
            name=name,
            age=int(age),
            email=email,
            address=address 
        )

        return redirect('home')



    

class Delete(View):
    def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
        except Student.DoesNotExist:
            pass
        return redirect('home')


class Update(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        return render(request, 'update.html', {'student': student})

    def post(self, request, id):
        student = Student.objects.get(id=id)
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')

        if not all([name, age, email, address]):
            return render(request, 'update.html', {
                'student': student,
                'error': 'All fields are required'
            })

        student.name = name
        student.age = age
        student.email = email
        student.address = address
        student.save()
        return redirect('home')




