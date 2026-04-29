from django.shortcuts import render, redirect, get_object_or_404
from .models import Voter
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import re
from django.contrib import messages


def home(request):
    data = Voter.objects.all()
    return render(request, 'home.html', {'data': data})


def add(request):
    if request.method == "POST":
        voter_no = request.POST['voter_no'].upper()  # convert to uppercase
        pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
        if not re.match(pattern, voter_no):
            messages.error(request, "Invalid Voter Number (Format: ABCDE1234F)")
            return render(request, 'form.html')
        Voter.objects.create(
            name=request.POST['name'],
            father_name=request.POST['father_name'],
            gender=request.POST['gender'],
            dob=request.POST['dob'],
            voter_no=voter_no,
            photo=request.FILES.get('photo')
        )
        return redirect('/')
    return render(request, 'form.html')



def edit(request, id):
    voter = get_object_or_404(Voter, id=id)
    if request.method == "POST":
        voter.name = request.POST['name']
        voter.father_name = request.POST['father_name']
        voter.gender = request.POST['gender']
        voter.dob = request.POST['dob']
        voter.voter_no = request.POST['voter_no']
        if 'photo' in request.FILES:
            voter.photo = request.FILES['photo']
        voter.save()
        return redirect('/')
    return render(request, 'form.html', {'voter': voter})


def delete(request, id):
    voter = get_object_or_404(Voter, id=id)
    voter.delete()
    return redirect('/')


def view(request, id):
    voter = get_object_or_404(Voter, id=id)
    return render(request, 'view.html', {'voter': voter})


