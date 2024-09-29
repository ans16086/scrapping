import requests

# 20.24.43.214
# 20.24.43.214
# 20.24.43.214
# url = 'https://www.youtube.com/PewDiePie'



# http_proxy  = "193.233.83.181:8085"
# https_proxy = "193.233.83.181:8085"
# ftp_proxy   = "193.233.83.181:8085"

# proxies = { 
#               "http"  : http_proxy, 
#               "https" : https_proxy, 
#               "ftp"   : ftp_proxy
#             }

# r = requests.get(url)
# print(r.text)




from requests_html import HTMLSession

# Initialize the session
session = HTMLSession()

# Load the dynamic page
url = 'https://www.instagram.com/ahmedaliakbarofficial/'
response = session.get(url)

# Render the page, executing JavaScript
response.html.render(timeout=20)