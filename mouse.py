import pyautogui
import time

print("30sec for get the position")
time.sleep(20)
x, y = pyautogui.position()
print ("Atual mouse Position:")
print ("x = "+str(x)+" y = "+str(y))


print ("\nIs on Screen?")
resp = pyautogui.onScreen(x, y)
print (str(resp))

input("enter for close")
