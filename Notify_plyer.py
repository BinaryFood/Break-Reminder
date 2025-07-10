from plyer import notification

import time


if __name__ == '__main__':
    while True:
        notification.notify(title="~ ~ Take a break ~ ~", 
                        message="YOUR ATTENDENCE IS MARKED!!\nMentally Absent, Emotionally Shattered.",
                        app_icon="D:/Documents/Downloads/sad-cat.ico",
                        timeout=5
                        )
        
        time.sleep(10)