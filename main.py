from json import dumps
from random import choice, randint
from string import ascii_letters, digits
from time import sleep
import httpx

WARP_ID = input("Enter WARP ID:\n")

if not WARP_ID:
    exit("WARP ID not found!")

def genString(stringLength):
    try:
        letters = ascii_letters + digits
        return ''.join(choice(letters) for _ in range(stringLength))
    except Exception as error_code:
        print(error_code)

def digitString(stringLength):
    try:
        digit = digits
        return ''.join(choice(digit) for _ in range(stringLength))
    except Exception as error_code:
        print(error_code)

url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"

SUCCESS_COUNT = 0

while True:
    try:
        install_id = genString(22)
        body = {
            "key": f"{genString(43)}=",
            "install_id": install_id,
            "fcm_token": f"{install_id}:APA91b{genString(134)}",
            "referrer": WARP_ID,
            "warp_enabled": False,
        }
        data = dumps(body).encode("utf8")
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1"
        }
        response = httpx.post(url, data=data, headers=headers).status_code
    except Exception as error_code:
        print(error_code)

    if response == 200:
        SUCCESS_COUNT += 1
        print(f"\033[32mPassed:\033[0m +1GB (total: {SUCCESS_COUNT}GB)")
    else:
        print(f"\033[31mFailed: {response}\033[0m")

    pause_time = randint(1, 20)
    print(f"Pause: {pause_time} seconds.")
    sleep(pause_time)