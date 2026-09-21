import requests
from bs4 import BeautifulSoup
#The page to learn html on w3schools
url ="https://w3schools.com"

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

}
try:
    print("getting data from w3schhol ")
    response = requests.get(url,headers=headers, timeout=10)

    if response.status_code ==200:
        soup = BeautifulSoup(response.text , "html.parser")
        # step 1- finding the <h1> tag of the main topic on the page
        main_heading = soup.find('h1')

        #step 2: find the first <p> tag on the webpage
        first_paragraph = soup.find('p')

        #step 3 - printing the retrieved information
        print("\n Data collect succussfully: \n ")

        if main_heading:
            print(f" Main topic: {main_heading.text.strip()}")

        if first_paragraph:
            print(f" First paragraph: {first_paragraph.text.strip()}")

        print("\n --------------------")

    else:
        print(f"\n Cant connect web page .Error code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"\n Internet connection Error :{e}")