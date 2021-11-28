import mouse
import pyautogui
#getting position of the mouse
x = mouse.get_position()
print(x)
#opens menu
def kpop():
    pyautogui.moveTo(192, 1064, duration = .01)
    mouse.click('left')
    #opens groove
    pyautogui.moveTo(658, 380, duration = .25)
    mouse.click('left')
    #hits kpop
    pyautogui.moveTo(54, 504, duration = 2.5)
    mouse.click('left')
    #hits play all
    pyautogui.moveTo(801, 308, duration = 1)
    mouse.click('left')
