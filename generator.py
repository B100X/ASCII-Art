# pip install pyfiglet
# import pyfiglet module

import pyfiglet

data =
pyfiglet.figlet_format("ASCII Text")
print(data)



# If you want, you can change the font style of your ASCII Art Generator :

import pyfiglet

data = pyfiglet.figlet_format("ASCII Text",font='digital')
print(data)



# If you want to see the list of ASCII Art Font Styles :

import pyfiglet

fonts = pyfiglet.FigletFont.getFonts()
fonts = list(fonts)
print(len(fonts))
