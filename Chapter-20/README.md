## Chapter-20
### Practice questions
1. How can you trigger PyAutoGUI’s fail-safe to stop a program?\
**ANswer:**\
Move the mouse to any of the corners.

2. What function returns the current resolution()?\
**Answer:**\
pyautogui.size()

3. What function returns the coordinates for the mouse cursor’s current position?\
**ANswer:**\
pyautogui.position()

4. What is the difference between pyautogui.moveTo() and pyautogui.move()?\
**Answer:**\
moveto() moves to absolute coordinates of the screen and move() to the relative posiyion of the mouse.

5. What functions can be used to drag the mouse?\
**Answer:**\
pyautogui.dragTo() and pyautogui.drag()

6. What function call will type out the characters of "Hello, world!"?\
**Answer:**\
pyautogui.typewrite('Hello, world!')

7. How can you do keypresses for special keys such as the keyboard’s left arrow key?\
**Answer:**\
pyautogui.press('left')

8. How can you save the current contents of the screen to an image file named screenshot.png?\
**Answer:**\
pyautogui.screenshot('screenshot.png')

9. What code would set a two-second pause after every PyAutoGUI function call?\
**Answer:**\
pyautogui.PAUSE = 2

10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?\
**Answer:**\
Selenium

11. What makes PyAutoGUI error-prone?\
**ANswer:**\
It clicks and types into windows blindly and we cannot find where if we are doing it right .

12. How can you find the size of every window on the screen that includes the text Notepad in its title?\
**Answer:**\
pyautogui.getWindowsWithTitle('Notepad')

13. How can you make, say, the Firefox browser active and in front of every other window on the screen?\
**Answer:**\
w = pyatuogui.getWindowsWithTitle('Firefox')\
w.activate()



