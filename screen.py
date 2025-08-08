from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time
import os
from pyfiglet import Figlet
import sys


def loading(range_limit):
    loading_chars = ['|', '/', '-', '\\']
    for _ in range(range_limit):
        for char in loading_chars:
            sys.stdout.write(f'\r{char} [*] - Please wait for the new page...')
            sys.stdout.flush()
            time.sleep(0.1)

def created_banner():
    text1 = "One_Exploit"
    maker = Figlet(font="slant")
    banner = maker.renderText(text1)
    print(banner)
    with open("banner.txt", "w") as file:
        file.write(banner)

def clear():
    os.system("clear")

clear()

def banner():
    created_banner()
    print(f'''
    email: amirhosein@onexploit.app
    dropbox-dropin-btn,
    .dropbox-dropin-btn:link,
    .dropbox-dropin-btn:hover {{
        display: inline-block;
        height: 14px;
        font-family: "Lucida Grande", "Segoe UI", "Tahoma", "Helvetica Neue", "Helvetica", sans-serif;
        font-size: 11px;
        font-weight: 600;
        color: #636363;
        text-decoration: none;
        padding: 1px 7px 5px 3px;
        border: 1px solid #ebebeb;
        border-radius: 2px;
        border-bottom-color: #d4d4d4;
        background: #fcfcfc;
        background: -moz-linear-gradient(top, #fcfcfc 0%, #f5f5f5 100%);
        background: -webkit-linear-gradient(top, #fcfcfc 0%, #f5f5f5 100%);
        background: linear-gradient(to bottom, #fcfcfc 0%, #f5f5f5 100%);
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fcfcfc', endColorstr='#f5f5f5', GradientType=0);
    }}
    ''')

loading(5)
clear()
banner()

chromedriver_path = "chromedriver.exe"

if not chromedriver_path:
    print("Please write your ChromeDriver path.")
    for _ in range(3):
        chromedriver_path = input("Enter your ChromeDriver path: ")
        if chromedriver_path:
            break
    if not chromedriver_path:
        exit()
else:
    print("Welcome")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

url = "file:///C:/Users/Gigabyte/Desktop/web/rezome.html"

driver.get(url)

time.sleep(3)

# Get the page's full height and width
scroll_width = driver.execute_script("return document.body.scrollWidth")
scroll_height = driver.execute_script("return document.body.scrollHeight")

window_width = driver.execute_script("return window.innerWidth")
window_height = driver.execute_script("return window.innerHeight")

# Adjust window size to match content for higher precision
driver.set_window_size(window_width, window_height)

# Increase zoom level for higher resolution (optional but increases quality)
driver.execute_script("document.body.style.zoom='150%'")  # Optional: Adjust zoom level to 150%

screenshots = []

current_position = 0
while current_position < scroll_height:
    screenshot_filename = f"screenshot_{current_position}.png"
    driver.save_screenshot(screenshot_filename)
    screenshots.append(Image.open(screenshot_filename))

    # Scroll the window
    driver.execute_script(f"window.scrollTo(0, {current_position + window_height});")

    time.sleep(1)

    current_position += window_height

# Create the panorama image
total_width = max(s.width for s in screenshots)
total_height = sum(s.height for s in screenshots)

panorama_image = Image.new('RGB', (total_width, total_height))

# Paste the screenshots vertically with higher accuracy
y_offset = 0
for screenshot in screenshots:
    panorama_image.paste(screenshot, (0, y_offset))
    y_offset += screenshot.height

# Save and show the panorama
panorama_image.save("panorama_screenshot_high_res.png")
panorama_image.show()

driver.quit()
