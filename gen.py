import os
import requests
from faker import Faker
from datetime import datetime
from colorama import Fore
from bs4 import BeautifulSoup
import random
import os 



fake = Faker('ru_RU')
R2ST = """

   ▄████████ ███    █▄     ▄████████    ▄████████  ▄█     ▄████████ ███▄▄▄▄           ▄██████▄     ▄████████ ███▄▄▄▄   
  ███    ███ ███    ███   ███    ███   ███    ███ ███    ███    ███ ███▀▀▀██▄        ███    ███   ███    ███ ███▀▀▀██▄ 
  ███    ███ ███    ███   ███    █▀    ███    █▀  ███▌   ███    ███ ███   ███        ███    █▀    ███    █▀  ███   ███ 
 ▄███▄▄▄▄██▀ ███    ███   ███          ███        ███▌   ███    ███ ███   ███       ▄███         ▄███▄▄▄     ███   ███ 
▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ▀███████████ ███▌ ▀███████████ ███   ███      ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ 
▀███████████ ███    ███          ███          ███ ███    ███    ███ ███   ███        ███    ███   ███    █▄  ███   ███ 
  ███    ███ ███    ███    ▄█    ███    ▄█    ███ ███    ███    ███ ███   ███        ███    ███   ███    ███ ███   ███ 
  ███    ███ ████████▀   ▄████████▀   ▄████████▀  █▀     ███    █▀   ▀█   █▀         ████████▀    ██████████  ▀█   █▀  
  ███    ███                                                                                                           
                                    
                                    DEV            : R2ST UWU
                                    SUPPORT SERVER : /MART
                                    OK             : BYE  """


def sdf(details, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for key, value in details.items():
            file.write(f"{key}: {value}\n-----------------------------------\n")

def russian():
    details = {
        'Name': fake.name_female(),
        'Age': fake.random_int(min=18, max=35),
        'City': fake.city(),
        'Phone Number': fake.phone_number(),
        'Email': fake.email(),
        'Address': fake.address(),
        'Occupation': fake.job(),
        'Blood Type': fake.random_element(elements=('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'))
    }

    randirate = fake.random_int(min=6000, max=12000)

    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} [{Fore.LIGHTBLACK_EX}{datetime.now()}{Fore.RESET}] Russian Details:")
    for key, value in details.items():
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} [{Fore.LIGHTBLACK_EX}{datetime.now()}{Fore.RESET}] {Fore.LIGHTCYAN_EX}{key} | {value}")
    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} [{Fore.LIGHTBLACK_EX}{datetime.now()}{Fore.RESET}] Rate in INR: [{Fore.LIGHTBLACK_EX}{randirate}{Fore.RESET}]")

    ct = datetime.now().strftime("%m%d%H%M")
    df = f"dtl.txt"
    sdf(details, df)

    sq = "Russian girl"
    key = "rBLIt4-EseXmsHzTkcG-Njf4Wxh06eDvqnGiw6eDh5o"
    headers = {"Authorization": f"Client-ID {key}"}

    response = requests.get(f"https://api.unsplash.com/search/photos?query={sq}&per_page=10", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data and 'results' in data:
            results = data['results']
            if results:
                index = random.randint(0, len(results) - 1)
                url = results[index]['urls']['regular']
                if url:
                    imgr = requests.get(url)
                    if imgr.status_code == 200:
                        imagefn = f"russian.jpg"
                        with open(imagefn, 'wb') as f:
                            f.write(imgr.content)
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} [{Fore.LIGHTBLACK_EX}{datetime.now()}{Fore.RESET}] Generated Russian Girl Image.")
                        return

    print(f"{Fore.RED}[{datetime.now()}] Failed to generate image link")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.LIGHTRED_EX+R2ST+"\n")
    os.system("title Russian Generator || R2ST")
    russian()
