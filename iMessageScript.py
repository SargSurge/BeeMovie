import pyautogui

file = open('beeMovie.txt')
script = file.read()

for x in script.split():
    pyautogui.write(x)
    pyautogui.press('enter')

