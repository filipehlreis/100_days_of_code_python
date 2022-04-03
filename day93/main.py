import pyautogui
from time import sleep

sleep(2)
pyautogui.press('space')

i = 0
while True:
    screen = pyautogui.screenshot()

    tree_low1 = screen.getpixel((375, 480))
    tree_low2 = screen.getpixel((400, 480))

    tree_high1 = screen.getpixel((375, 440))
    tree_high2 = screen.getpixel((400, 440))

    if tree_low1[0] != 255 or tree_low2[0] != 255 or \
            tree_high1[0] != 255 or tree_high2[0] != 255:
        # save screenshot to analyse
        i += 1
        screen.save(f"day93\\{i}.jpg")

        # press the 'space' to jump
        pyautogui.press('space')
        print('Espaço pressionado.')
        sleep(0.0001)
