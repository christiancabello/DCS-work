

import requests 
from bs4 import BeautifulSoup as Soup

URL = "https://www.cs.hmc.edu/~dodds/demo_cats.html"
page = requests.get(URL) 
html = page.text 

with open("dodds_page.html", "w") as outfile: 
    outfile.write(html) 

with open("dodds_page.html", "r") as infile: 
    html = infile.read()
    
soup = Soup(html, 'html.parser')  
all_ol = soup.find_all('ol') 
first_ol = all_ol[0]
print(first_ol) 
some_lis = first_ol.find_all('li')
print(some_lis)
'''
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content") 

for job_element in job_elements:  
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location") 
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip()) 
    print('\t')

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
) 

print(len(python_jobs))'''