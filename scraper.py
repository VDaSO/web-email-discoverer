from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from colorama import Fore, init
import os
import re
import time


init(autoreset=True)


session = requests.Session()
session.cookies.update({'cookie_consent': 'accepted'})
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/123.0.0.0 Safari/537.36'
})

def fetch_page(domain_name):
    try:
        response = session.get(domain_name)
        return response
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED} Error: {e}")
        return None

def extract_links(html, domain_name):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("a")
    url_list = set()

    for link in links:
        href = link.get("href")
        if href and href != "#":
            full_url = urljoin(domain_name, href)
            if domain_name in full_url:
                url_list.add(full_url)

    return url_list

def display_links(links):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Fore.YELLOW}----------- {len(links)} UNIQUE URLS FOUND -----------\n")
    for link in links:
        print(f"{Fore.CYAN}{link}")

def uridiscover(domain_name):
    response = fetch_page(domain_name)
    if response and response.status_code == 200:
        print(f"{Fore.GREEN} PAGE FOUND : {domain_name}")
        links = extract_links(response.text, domain_name)
        display_links(links)
        return links
    elif response:
        print(f"{Fore.RED} Error: Status code {response.status_code} for {domain_name}")
    else:
        print(f"{Fore.RED} Could not reach {domain_name}")
    return set()

def email_match(html):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_list = re.findall(email_pattern, html)
    return email_list

def search_email(urls_list):
    found_emails = {}
    for url in urls_list:
        response = fetch_page(url)
        time.sleep(0.3)  
        if response and response.status_code == 200:
            html = response.text
            email_list = email_match(html)
            if email_list:
                found_emails[url] = email_list
                print(f"\n{Fore.GREEN} Emails found on {url}:")
                for email in email_list:
                    print(f"{Fore.CYAN}  {email}")
        else:
            print(f"{Fore.RED} Failed to fetch {url}")
    return found_emails

def main():
    url = input(f"{Fore.YELLOW} Provide an URL (e.g., https://www.example.fr):\n> ").strip()
    links = uridiscover(url)
    if links:
        print(f"\n{Fore.MAGENTA} Searching emails in discovered pages...\n")
        search_email(links)

if __name__ == "__main__":
    main()
