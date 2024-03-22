import webbrowser 
import urllib.parse

url = "https://github.com/Gaming32/Superpack/releases/download/v0.3/superpack-0.3.jar"

if webbrowser.get('windows-default').open(url):
  print("Opened browser")
else:
  print("Unable to open browser")