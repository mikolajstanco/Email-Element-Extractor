import os
import base64
import json
from bs4 import BeautifulSoup
import re
import csv


import GoogleAuth
import GoogleManagment as GM


def main(): 
    file_path = "./results.csv"
    settings_path = "./settings.json"

    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            subject = settings['Subject']['Theme']
            style = settings['Style']
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {settings_path}")
        return
    
    processed_count = 0

    service = GoogleAuth.authenticate_gmail()
    query = f'is:unread subject:"{subject}"'
    
    while True:

        messages = GM.search_messages(service, query)

        if len(messages) == 0:
            break

        for message in messages:
            msg_id = message['id']
            msg = GM.get_message(service, msg_id)

            found_element = "Not_Found"

            for p in msg["payload"]["parts"]:
                if p["mimeType"] in ["text/html"]:
                    data = base64.urlsafe_b64decode(p["body"]["data"]).decode("utf-8")
                    soup = BeautifulSoup(data, "html.parser")
                    try:
                        found_element = soup.find_all('td', attrs={'style': f'{style}'})[0].get_text()
                    except Exception as e:
                        print(f"Error occured while parsing Email {msg_id}: {e}")

            msg_subject = ''
            msg_date = ''
            
            headers = msg['payload']['headers']
            
            for header in headers:                 
                if header['name'] == 'To':
                    msg_to_raw = header['value']
                elif header['name'] == "Date":
                    msg_date = header['value']
                
            msg_to = "Nieznany adres"
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', msg_to_raw)
            if email_match:
                msg_to = email_match.group(0)

            file_exists = os.path.isfile(file_path)

            with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:
                    writer.writerow(['Email', 'Element', 'Date'])
                writer.writerow([msg_to, found_element, msg_date])
            
            print(msg_to, found_element)
            
            GM.mark_as_read(service, msg_id)

            processed_count+=1
 
    print(f"Found: {processed_count} elements")

if __name__ == "__main__":
    main()