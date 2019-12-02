import time
import pyautogui
import pyperclip
import os
import random

def mapping_img(img,click):
    box_location = pyautogui.locateOnScreen(img)
    center = pyautogui.center(box_location)
    if click == 'double':
        pyautogui.doubleClick(center)
    else:
        pyautogui.leftClick(center)
    time.sleep(1)

def chat_user(user):
    if user != '':
        mapping_img('search.png', 'single')
        pyautogui.typewrite(user)
        time.sleep(1)
        pyautogui.moveRel(xOffset=0,yOffset=80)
        pyautogui.click()
        time.sleep(1)
    else:
        mapping_img('xiaoyu.png','single')
        mapping_img('chat.png', 'single')

def read_txt(txt):
    hellofile = open(txt,"r",encoding="UTF-8")
    hellocontent = hellofile.readlines()
    print(len(hellocontent))
    number = random.randint(0,len(hellocontent)-1)
    print('line number is{}',format(number))
    pyperclip.copy(hellocontent[number])
    pyautogui.hotkey('ctrl','v')
    hellofile.close()

def read_img(img_name):
    mapping_img('pic,png','single')
    img_path = 'E:/wecharttest/venv' + img_name
    pyautogui.typewrite(img_path)
    pyautogui.press('enter')

def main():
    os.chdir('E:/wecharttest/venv')
    print(os.getcwd())
    # TODO Login Wechat
    mapping_img('login.PNG','double')
    # TODO search chat user
    chat_user('')
    # TODO start chatting
    read_txt('hello.txt')
    pyautogui.press('enter')
    time.sleep(1)
    read_txt('yulu.txt')
    pyautogui.press('enter')
    time.sleep(1)
    read_img('sunshine.PNG')
    pyautogui.press('enter')
    time.sleep(1)

print('ok')
main()
