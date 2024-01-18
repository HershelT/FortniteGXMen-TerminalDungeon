import time
import os
from AsciiAnimations import *
from keyboardListener import *


clear_command = 'cls' if os.name == 'nt' else 'clear'
os.system(clear_command)

def waitForInput(char):
    user_input = None
    while (user_input != char):
        user_input = input()
#turns text to 2d arrays
def createArrayinArray(text: str):
    rows = text.splitlines()
    # If the first line is empty, skip it
    if rows and not rows[0]:
        rows = rows[1:]
    # If the last line is empty, skip it
    if rows and not rows[-1]:
        rows = rows[:-1]
    newText = [list(row) for row in rows]
    return newText

#prints given display to screen fast
def printScreen(screen, clear = True):
    if clear: os.system(clear_command)
    for row in screen:
        print(''.join(row),flush=True)
    # print('\033[?25h', end='')

#Adds text to overwrite over main screen with a specific row from most bottom of text being rowIndex from bottom of screen and column from left
def addLinesToSreen(lines, screen, rowIndex=0, colIndex=0, color='\033[m'):
    newLines = createArrayinArray(lines)
    for i, row in enumerate(newLines):
        for j, char in enumerate(row):
            screen[len(screen) - (len(newLines)+rowIndex)+i][colIndex+j] = color + char + '\033[0m'
#Use this after addlinestotext to erase a line written on previously
def createEmptyString(screenList : list):
    emptyString = ''.join(' ' if char != '\n' else '\n' for char in screenList)
    return emptyString

#Moves a character left or right (entity, screen it should be on,row want to be on, column want to be on, how much to move by, color if want)

def moveLeftorRight(entity:str,fullScreen, rowIndex, colIndex, stepMoveBy, jumpMoveBy, color='\033[0m'):
    key_listener = MyKeyListener()
    listener = keyboard.Listener(
        on_press=key_listener.on_press,
        on_release=key_listener.on_release)
    listener.start()
    keyboard.Controller().release(keyboard.Key.enter)
    longest_row=len(max(createArrayinArray(entity), key=len))
    addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
    printScreen(fullScreen)
    while not key_listener.is_enter_pressed():
        if key_listener.is_right_arrow_pressed() and (colIndex+longest_row+stepMoveBy)<=(len(fullScreen[2])-1):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            colIndex += stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_left_arrow_pressed() and (colIndex-stepMoveBy>=5):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            colIndex -= stepMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_up_arrow_pressed() and (rowIndex+len(createArrayinArray(entity))+jumpMoveBy)<(len(fullScreen)):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            rowIndex += jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
        elif key_listener.is_down_arrow_pressed() and (rowIndex-jumpMoveBy>0):
            addLinesToSreen(createEmptyString(entity), fullScreen, rowIndex, colIndex, color='\033[0m')
            rowIndex -= jumpMoveBy
            addLinesToSreen(entity, fullScreen, rowIndex, colIndex, color)
            key_listener.keys_pressed.discard(all); 
            printScreen(fullScreen)
            time.sleep(0.15)
    listener.stop()
    del key_listener

#hides the cursor in the begining from screen
print('\033[?25l', end='')


#defining full screens
startScreenArray =createArrayinArray(startScreen)
clearScreenArray= createArrayinArray(clearScreen)

#defining things to add (deprecated)
# creditsArray=createArrayinArray(credits)
# settingsArray = createArrayinArray(settings)
# ManWalkingArray = createArrayinArray(ManWalking)

#initlizes the startscreen
addLinesToSreen(pressEnter, startScreenArray, 8, 36, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')

#Add credits to main screen
addLinesToSreen(credits, startScreenArray, 1, 36, '\033[1m\033[90m')
printScreen(startScreenArray)
waitForInput('')

#Add settings index and erase previously written extra writings to allow users to set their screen size
addLinesToSreen(createEmptyString(credits), startScreenArray, 1, 36, '\033[0m')
addLinesToSreen(createEmptyString(pressEnter), startScreenArray, 8, 36, '\033[1m\033[90m')
addLinesToSreen(settings, startScreenArray, 3, 12, '\033[1;31m')
addLinesToSreen("Press 'Enter' To Continue", startScreenArray, 1, colIndex=8, color='\033[1;31m')
printScreen(startScreenArray)
waitForInput('')


#set charcter position and establish movement
manCol = 50
addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[90m')
moveLeftorRight(ManWalking, clearScreenArray, 1, manCol,stepMoveBy=5,jumpMoveBy=3,color='\033[0m')

#reset screen
startScreenArray =createArrayinArray(startScreen)
addLinesToSreen(loadGame, startScreenArray, 7, 36, '\033[33m')
sleepTime = 0.3
for i in range(1,40):
    addLinesToSreen(loadGame, startScreenArray, 7, 36, '\033[33m')
    addLinesToSreen(createEmptyString(loadBar), startScreenArray, 4, 25, '\033[0m')
    if i == 10: loadGame = prepAssets;sleepTime=0.2
    elif i == 20: loadGame = prepGraphics; sleepTime=0.1
    addLinesToSreen(loadBar, startScreenArray, 4, 26, '\033[1;31m')
    loadBar += "#"
    printScreen(startScreenArray)
    time.sleep(sleepTime)
addLinesToSreen("Game is Starting!  ", startScreenArray, 7, 36, '\033[33m')
printScreen(startScreenArray)
time.sleep(2)

#reprints cursor
print('\033[?25h', end='')

#debugger to test a one by one charcter for bounding
# clearScreenArray = createArrayinArray(clearScreen)
# addLinesToSreen(arrowKeysMessage, clearScreenArray, rowIndex=12, colIndex=manCol-20, color='\033[33m')
# moveLeftorRight(testOneByOne, clearScreenArray, 10, 30,stepMoveBy=1,jumpMoveBy=1,color='\033[0m')

# debugger to get length of entity and screen
# os.system(clear_command)
# print(len(createArrayinArray(TestOneByOne)), len(createArrayinArray(clearScreen)))
# time.sleep(5)


#charcter moves right


# waitForInput('')




