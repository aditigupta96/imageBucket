from django.shortcuts import render
import requests
# Create your views here.
access_token = "260885964.45f1b46.21e98a2bae1a46dab31568d770197a0a"
client_secret = "25995932a2534cf09f9be5a87be61001"

base_url = "https://api.instagram.com/v1/"

def search_tag(request):
	resp = requests.get("https://api.instagram.com/v1/tags/lnmiit/media/recent?access_token=260885964.45f1b46.21e98a2bae1a46dab31568d770197a0a")

	json = resp.json()

	image_link = []
	for data in json['data']:
		image_link.append(data['images']['low_resolution']['url'])

	return render(request,'index.html',{'image_link':image_link})