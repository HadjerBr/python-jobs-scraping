from bs4 import BeautifulSoup
import requests
page_num = 0
jobsFile = open("jobs.txt", "w") 
while (page_num <= 235//50):
    
    result = requests.get(f"https://www.kariyer.net/is-ilanlari?kw=python&cp={page_num}").content
    soup = BeautifulSoup(result, "lxml")
    jobs = soup.find_all("div", class_ = "list-items")

    
    for job in jobs:
        publication = job.find("span", class_ = "ad-date").text.strip()
        if "Bugün" in publication: # Bugünkü ilanlar
            job_title = job.find("h3", class_="kad-card-title").text.strip()
            company_name = job.find("span", class_ = "kad-card-subtitle").text.strip()
            location = job.find("div", class_ = "kad-card-location").text.strip()
            

            link = job.a["href"]
            result1 = requests.get("https://www.kariyer.net" + link).content
            soup1 = BeautifulSoup(result1, "lxml")
            tecrube = soup1.find("p", class_ = "mb-0").text.strip()

            jobsFile.write(f"Job Title: {job_title}\nCompany name: {company_name}\nnJob Location: {location}\nDate: {publication}\nLink: https://www.kariyer.net/{link}\nTecrube: {tecrube}\n")
            jobsFile.write("\n")
    page_num += 1
    print("page switched")




