from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        # app_icon=None,
        app_icon="C://Users//AYeddula//OneDrive - DXC Production//Desktop//Pythonlang//Covid Notify//Virus.ico",
        timeout=4
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    # notifyMe("Tyro", "Let's All Stop The Spread Of This Virus!!")
    myHTMLData = getData("https://www.mohfw.gov.in/")

    soup = BeautifulSoup(myHTMLData, 'html_parser')
    # print(myHTMLData)
    # print(soup.prettify())

    for table in soup.find_all('table'):
        print(table)
