from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def abduvahob(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']


		try:
			Contact.objects.create(name = name , email = email , subject = subject , message = message)
			messages.add_message(request , messages.SUCCESS , 'boldi')
			return HttpResponseRedirect(reverse('soon:abduvahob'))
		except:
			messages.add_message(request , messages.WARNING , 'tugadi pishtiz yozmadi bansiz hakkerga uchradiz')
			return HttpResponseRedirect(reverse('soon:abduvahob'))
	return render(request, 'index.html')


