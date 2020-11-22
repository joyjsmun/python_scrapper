import requests

from bs4 import BeautifulSoup


URL = f"https://stackoverflow.com/jobs?q=react&pg="


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)
 


def extract_job(html):
  title = html.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).find("a")["title"]
  company, location = html.find("h3",{"class":"fc-black-700 fs-body1 mb4"}).find_all("span",recursive=False)
  company = company.get_text(strip=True).strip("\n")
  location =location.get_text(strip=True).strip("\r").strip("-").strip("\n")

  return {
    "title" : title,
    "company" : company,
    "location" : location
  }




 
def extract_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    #print(f"scrapping {page +1}")
    result = requests.get(f"{URL}&pg{page+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"-job"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)
    


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return []
