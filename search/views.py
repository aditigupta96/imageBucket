from django.shortcuts import render
import requests
from django.template.response import TemplateResponse
from django.http import HttpResponse

# Create your views here.
access_token = "260885964.45f1b46.21e98a2bae1a46dab31568d770197a0a"
client_secret = "25995932a2534cf09f9be5a87be61001"

base_url = "https://api.instagram.com/v1/"

def home(request):
	response = TemplateResponse(request, 'index.html',{})
	return response

def search_tag(request):
        if request.method == "POST":
            tag = request.POST.get("tag")
            url = base_url + "tags/" + tag + "/media/recent?access_token=260885964.45f1b46.21e98a2bae1a46dab31568d770197a0a"
            resp = requests.get(url)

            json = resp.json()

            image_link = []
            for data in json['data']:
		image_link.append(data['images']['low_resolution']['url'])

            return render(request,'search.html',{'image_link':image_link})
        
        else:
            return HttpResponse("Please try again")
