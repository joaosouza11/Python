import urllib
import urllib.request

try:
  site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError :
  print("Error. The 'pudim' website is currently unavailable")
else:
  print("The 'pudim' website was successfully accessed.")
  #print(site.read())