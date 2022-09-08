# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import bs4
import document as document
import requests
from bs4 import BeautifulSoup


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("start")

    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    #print(page.text)
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
        print()

    # python_jobs = results.find_all(
    #     "h2", string=lambda text: "python" in text.lower()
    # )
    #
    # python_job_elements = [
    #     h2_element.parent.parent.parent for h2_element in python_jobs
    # ]
    #
    # for job_element in python_job_elements:
    #     title_element = job_element.find("h2", class_="title")
    #     company_element = job_element.find("h3", class_="company")
    #     location_element = job_element.find("p", class_="location")


