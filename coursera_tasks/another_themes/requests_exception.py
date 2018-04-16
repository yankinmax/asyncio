import sys
import requests


url = sys.argv[1]

try:
	response = requests.get(url, timeout=30)
	response.raise_for_status()			#for HTTPErrors
except requests.Timeout:
	print("error timeout, url:", url)
except requests.HTTPError as err:
	code = err.response.status_code
	print("error url: {0}, code {1}".format(url, code))
except requests.RequestException:
	print("error downloading url", url)
else:
	print(response.content)

#print(response.content)

