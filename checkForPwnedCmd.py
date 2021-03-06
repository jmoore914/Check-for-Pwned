import checkForPwnedShared
import tkinter as tk
from tkinter import filedialog
import os
import sys
import time


def inputWithInterrupt(msg):
    try:
        return input(msg)
    except KeyboardInterrupt:
        print('Process interrupted by user.')
        raise SystemExit


while True:
    try:
        while True:
            try:
                fileName = inputWithInterrupt(
                    'File location (enter "browse" to open file dialog):\n')
                if fileName == 'browse':
                    root = tk.Tk()
                    root.withdraw()
                    fileName = filedialog.askopenfilename()
                    print(fileName)
                    root.destroy()
                if not os.path.isfile(fileName):
                    raise ValueError('Not a real file.')
            except ValueError:
                print('Invalid file path. Please try again.')
                print('')
                continue
            break
        print('')
        while True:
            try:
                accountCol = int(input('Account name col: '))
                if accountCol < 0:
                    raise ValueError('Value must be positive.')
            except ValueError:
                print('Invalid number. Please try again.')
                print('')
                continue
            break
        print('')
        while True:
            try:
                pwCol = int(input('Password col: '))
                if accountCol < 0:
                    raise ValueError('Value must be positive.')
            except ValueError:
                print('Invalid number. Please try again.')
                print('')
                continue
            break
        print('')

        while True:
            try:
                headerRow = input('Header row (y/n): ')
                if headerRow == 'y':
                    headerRow = True
                elif headerRow == 'n':
                    headerRow = False
                else:
                    raise ValueError('Invalid input entered.')
            except ValueError:
                print('Value must be "y" or "n". Please try again.')
                print('')
                continue
            break
        print('')

        print(checkForPwnedShared.checkCSV(
            fileName, accountCol, pwCol, headerRow))
        print('')
        input('Press ENTER to exit...')
    except ValueError as e:
        print(str(e) + ' Please try again.')
        print('')
        continue
    break
