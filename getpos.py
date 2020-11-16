import pyautogui
while True:
    x, y = pyautogui.position()
    string_position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    pixelcolor = pyautogui.screenshot().getpixel((x, y))
    string_position += '      RGB: (' + str(pixelcolor[0]).rjust(3)
    string_position += ', ' + str(pixelcolor[1]).rjust(3)
    string_position += ', ' + str(pixelcolor[2]).rjust(3) + ')'
    print(string_position, end='')
    print('\b' * len(string_position), end='', flush=True)

