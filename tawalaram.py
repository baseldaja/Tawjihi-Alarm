import time
from urllib.request import urlopen

def check_website(url):
    try:
        response = urlopen(url)
        return response.getcode() == 200
    except:
        return False

def main():
    website_url = "https://www.tawjihi.jo/?fbclid=IwAR2xqr6CdO5-SrQ6Jf1lFN8OSTIDWKhjp3a3uN_h9BbSnfC4gvNhRKsfOAc"
    check_interval = 10

    website_live = False

    while True:
        while not website_live and not check_website(website_url):
            print("Website is not live. Checking again in {} seconds.".format(check_interval))
            time.sleep(check_interval)

        if not website_live:
            print("Website is live!")
            website_live = True

        time.sleep(check_interval) 
