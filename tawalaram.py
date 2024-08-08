import time
from urllib.request import urlopen

def check_website(url):
    try:
        response = urlopen(url)
        return response.getcode() == 200
    except:
        return False

def main():
    website_url = "https://www.tawjihi.jo/"
    check_interval = 10

    website_live = False

    while True:
        if not website_live:
            if check_website(website_url):
                print("Website is live!")
                website_live = True
            else:
                print(f"Website is not live. Checking again in {check_interval} seconds.")
        else:
            if not check_website(website_url):
                print("Website has gone down.")
                website_live = False
            else:
                print(f"Website is still live. Checking again in {check_interval} seconds.")

        time.sleep(check_interval)

if __name__ == "__main__":
    main()

