from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup



class person_data(APIView):
    def get(self,request):
        # Get the 'channel_name' from the request
        channel_name = request.GET.get('channel_name')
        print(channel_name)
        import requests

        url = f'https://anitaku.pe/category/{channel_name}'
        print(url)

        r = requests.get(url)
        #print(r.text)
    
        soup = BeautifulSoup(r.text, "html.parser")
        body = soup.body

        # Step 2: Get the third div
        third_div = body.contents[3]
        h=soup.find("div", 'anime_info_body_bg')


        a = h.contents[7]
        type=a.span.next_sibling.next_sibling.text
        descriptions = h.find("div", 'description').text
        b = h.contents[15]
        release=b.text
        c = h.contents[17]
        status=c.span.next_sibling.next_sibling.text
        print("Scraped content:",type)
        print("Scraped content:",descriptions)
        print("Scraped content:",release)
        print("Scraped content:",status)
        data = {
            'type': type,
            'description': descriptions,
            'release': release,
            'status': status
        }

        # Send data as JSON response
        return Response(data)



        







        











# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .scraper_utils import get_youtube_subscribers

# @api_view(['GET'])
# def get_subscriber_count(request):
#     # Get the 'channel_name' from the request
#     channel_name = request.GET.get('channel_name')
#     print(channel_name)
#     if not channel_name:
#         return Response({"error": "You must provide a channel_name"}, status=400)
    
#     # Call the function to scrape subscribers
#     data = get_youtube_subscribers(channel_name)
    
#     return Response(data)
