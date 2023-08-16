import time
import subprocess
from urllib.request import urlopen

def check_website(url):
    try:
        response = urlopen(url)
        return response.getcode() == 200
    except:
        return False

def play_alarm():
    # Adjust the command based on your system and the sound file you want to play
    subprocess.run(["aplay", "path/to/your/alarm_sound.wav"])  # Replace with the actual sound file path

def main():
    website_url = " https://www.reflexmama.com/products?features=83,75,85," 
    check_interval = 10  # Set the interval for checking the website in seconds

    website_live = False

    while True:
        while not website_live and not check_website(website_url):
            print("Website is not live. Checking again in {} seconds.".format(check_interval))
            time.sleep(check_interval)

        if not website_live:
            print("Website is live!")
            website_live = True
            play_alarm()

        time.sleep(check_interval)

if __name__ == "__main__":
    main()