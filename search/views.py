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
            tag_list = tag.split(",")
            tagname = tag_list[0]
            url = base_url + "tags/" + tagname + "/media/recent?access_token=260885964.45f1b46.21e98a2bae1a46dab31568d770197a0a"
            resp = requests.get(url)
            
            json = resp.json()
            image_link = []
            
            for data in json['data']:
                present = True
                all_tag = data['tags']
                input_tags = tag_list[1:]
                
                for item in input_tags:
                    if (item not in all_tag):
                        present = False
                        break
                    
                if present:        
                    image_link.append(data['images']['low_resolution']['url'])
        
            return render(request,'search.html',{'image_link':image_link})
        
        else:
            return HttpResponse("Please try again")
