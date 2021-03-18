# 1st step: install "ip2geotools"
# 2ns step: import socket & DbIpCity
# 3rd step: ask a url from user
# 4th step: try to understand the code

import socket
from ip2geotools.databases.noncommercial  import DbIpCity

url_link = input("Insert a URL: ")
IP = socket.gethostbyname(url_link)
response = DbIpCity.get(IP, api_key='free')
print("IP: ", IP)
print("City: ", response.city)
print("Region: ", response.region)
print("Country ", response.country)
print("Latitude: ", response.latitude)
print("Longtitude: ", response.longitude)