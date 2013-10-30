from bs4 import BeautifulSoup as bs
from django.utils.encoding import smart_str
import requests

def extract(number):
	base_url = "http://projecteuler.net/problem="
	path = ".//project_euler//problem_"

	req = requests.get(base_url + smart_str(number));
	soup = bs(req.content)

	write = ["/*" + "\n"]
	write.append(smart_str(soup.h2.text) + "\n")
	write.append(smart_str(soup.h3.text) + "\n\n")
	
	for string in  soup.findAll('p'):
		write.append(smart_str(string.text) + "\n")

	write.append("*/")
	
	with open(path + smart_str(number) + ".cpp",'wb') as f:
		f.writelines(write)

	print "Done writing problem", number 

if __name__ == "__main__":
	max_int = 436
	start = 25
	for i in range(start,max_int):
		extract(i)
