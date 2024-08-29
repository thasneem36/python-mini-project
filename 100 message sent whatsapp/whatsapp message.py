import pyautogui
import time
import random
import pyperclip  

message_list = ['😁','🙂','😊','☺️','😒','🫂','😭','🤗','😇','🥹','🤣']

message_count = int(input("Message Count: "))

time.sleep(5)
for i in range(message_count):
    random_message = random.choice(message_list)
    pyperclip.copy(random_message)  
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(1)
    print(f"Message {i+1}/{message_count} sent.")

print("All messages sent.")
