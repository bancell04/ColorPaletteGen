# Brady Ancell
# CSCI101 - Section F
# Create Project (Color Palette Generator)

import csv
import random
import pygame
import colorsys

black = (1, 1 ,1)
white = (250, 250, 250)
color_database = []
with open('colors.csv', 'r') as file:
    color_reader = csv.reader(file, delimiter=',')
    for row in color_reader:
        color_database.append(row)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def match(user_color):
    red_match = []
    green_match = []
    blue_match = []
    for color in range(1,len(color_database)):
        if user_color[0] >= (int(color_database[color][1]) - 25) and user_color[0] <= (int(color_database[color][1]) + 25):
            red_match.append(color)
        else:
            continue
        if user_color[1] >= (int(color_database[color][2]) - 25) and user_color[1] <= (int(color_database[color][2]) + 25):
            green_match.append(color)
        else:
            continue
        if user_color[2] >= (int(color_database[color][3]) - 25) and user_color[2] <= (int(color_database[color][3]) + 25):
            blue_match.append(color)
        else:
            continue
    matches = []
    for red in red_match:
        for green in green_match:
            for blue in blue_match:
                if red == green and green == blue:
                    matches.append(red)
                    break
    user_color = color_database[matches[0]]
    return user_color

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def name_match(colorName):
    color_match = ''
    for color in range(1,len(color_database)):
        if colorName.lower() == color_database[color][0]:
            #print(color_database[color])
            color_match = [int(color_database[color][1]), int(color_database[color][2]), int(color_database[color][3])]
            break
        else:
            continue
    return color_match

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def complementary(user_color):
    complementary = [(255 - int(user_color[0])), (255 - int(user_color[1])), (255 - int(user_color[2]))]
    return complementary

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def triadic(user_color):
    red = user_color[0]/255
    green = user_color[1]/255
    blue = user_color[2]/255
    hsv_color1 = colorsys.rgb_to_hsv(red, green, blue)
    hue1 = hsv_color1[0]
    saturation = hsv_color1[1]
    value = hsv_color1[2]
    hues = [hue1]
    new_hue = hue1
    for i in range(2):
        new_hue = new_hue + .33
        if new_hue > 1:
            new_hue = new_hue - 1
            hues.append(new_hue)
        else:
            hues.append(new_hue)
    hsv_color2 = [hues[1], saturation, value]
    hsv_color3 = [hues[2], saturation, value]
    rgb_tuple2 = colorsys.hsv_to_rgb(round(hsv_color2[0], 2), round(hsv_color2[1], 2), round(hsv_color2[2], 2))
    #print(rgb_tuple2)
    rgb_tuple3 = colorsys.hsv_to_rgb(round(hsv_color3[0], 2), round(hsv_color3[1], 2), round(hsv_color3[2], 2))
    #print(rgb_tuple3)
    color2 = [round(255*rgb_tuple2[0]), round(255*rgb_tuple2[1]), round(255*rgb_tuple2[2])]
    color3 = [round(255*rgb_tuple3[0]), round(255*rgb_tuple3[1]), round(255*rgb_tuple3[2])]
    return color2, color3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def tetradic(user_color):
    red = user_color[0]/255
    green = user_color[1]/255
    blue = user_color[2]/255
    hsv_color1 = colorsys.rgb_to_hsv(red, green, blue)
    hue1 = hsv_color1[0]
    saturation = hsv_color1[1]
    value = hsv_color1[2]
    hues = [hue1]
    new_hue = hue1
    for i in range(3):
        new_hue = new_hue + .25
        if new_hue > 1:
            new_hue = new_hue - 1
            hues.append(new_hue)
        else:
            hues.append(new_hue)
    #print(hues)
    hsv_color2 = [hues[1], saturation, value]
    hsv_color3 = [hues[2], saturation, value]
    hsv_color4 = [hues[3], saturation, value]
    rgb_tuple2 = colorsys.hsv_to_rgb(round(hsv_color2[0], 2), round(hsv_color2[1], 2), round(hsv_color2[2], 2))
    rgb_tuple3 = colorsys.hsv_to_rgb(round(hsv_color3[0], 2), round(hsv_color3[1], 2), round(hsv_color3[2], 2))
    rgb_tuple4 = colorsys.hsv_to_rgb(round(hsv_color4[0], 2), round(hsv_color4[1], 2), round(hsv_color4[2], 2))
    color2 = [round(255*rgb_tuple2[0]), round(255*rgb_tuple2[1]), round(255*rgb_tuple2[2])]
    color3 = [round(255*rgb_tuple3[0]), round(255*rgb_tuple3[1]), round(255*rgb_tuple3[2])]
    color4 = [round(255*rgb_tuple4[0]), round(255*rgb_tuple4[1]), round(255*rgb_tuple4[2])]
    return color2, color3, color4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def analogous(user_color):
    red = user_color[0]/255
    green = user_color[1]/255
    blue = user_color[2]/255
    hsv_color1 = colorsys.rgb_to_hsv(red, green, blue)
    hue1 = hsv_color1[0]
    saturation = hsv_color1[1]
    value = hsv_color1[2]
    new_hue1 = hue1 + (.083*saturation)
    if new_hue1 > 1:
        new_hue1 = new_hue1 - 1
    new_hue2 = hue1 - (.083*saturation)
    if new_hue2 < 0:
        new_hue2 = new_hue2 + 1
    hsv_color2 = [new_hue1, saturation, value]
    hsv_color3 = [new_hue2, saturation, value]
    rgb_tuple2 = colorsys.hsv_to_rgb(round(hsv_color2[0], 2), round(hsv_color2[1], 2), round(hsv_color2[2], 2))
    rgb_tuple3 = colorsys.hsv_to_rgb(round(hsv_color3[0], 2), round(hsv_color3[1], 2), round(hsv_color3[2], 2))
    color2 = [round(255*rgb_tuple2[0]), round(255*rgb_tuple2[1]), round(255*rgb_tuple2[2])]
    color3 = [round(255*rgb_tuple3[0]), round(255*rgb_tuple3[1]), round(255*rgb_tuple3[2])]
    return color2, color3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def split_complementary(user_color):
    temp_color = complementary(user_color)
    colors = analogous(temp_color)
    return colors[0], colors[1]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# 1 COLOR = COMPLEMENTARY + 1
    # complementary = 255 - NUM

    
# 2 COLOR = Analogous + 2+
    # convert to HSL and then add or subtract HUE (add or subtract more the bigger saturation is)
    
# 3 Triadic + 2
    # convert to HSL and add x to cue and 2x to hue
    # If hue is in middle range: x = hue/2
    # If hue is in right range:  x = hue/3
    # If hue is in left range: x = (360-hue)/3
    
# 4 Split Complementary + 2
    # find complementary. convert to  HSL, add x, subtract x

# 5 Tetradic + 3
    # conver to HSL, add x, 2x, and 3x to hue

print('Welcome to the Python Color Palette Generator!')
Playing = True
while Playing:
    pygame.init()
    user_color = []
    colorName = []
    colorFinal = []
    colors1 = []
    colors2 = []
    color1 = []
    color2 = []
    color3 = []
    color4 = []
    color5 = []
    color6 = []
    user = int(input('Would you like to enter color name or color RGB?\n1 - RGB\n2  - Color Name\n'))
    if user == 1:
        print('Input a color value (RGB) and length of the palette you want and we will do the rest!')
        while True:
            red = int(input('Red: '))
            if red < 0 or red > 256:
                print('Please input a valid RGB value!\n------------------------------')
                continue
            green = int(input('Green: '))
            if green < 0 or green > 256:
                print('Please input a valid RGB value!\n------------------------------')
                continue
            blue = int(input('Blue: '))
            if blue < 0 or blue > 256:
                print('Please input a valid RGB value!\n------------------------------')
                continue
            break
        user_color = [red, green, blue]
            
    elif user == 2:
        while True:
            colorName = input('Enter the name of the color: ')
            match = name_match(colorName)
            if match == '':
                print('There was no match for that color. Please try a different name.')
                continue
            else:
                break
        user_color = match
    while True:
        palette = input('Enter the length of your color palette (between 1-6): ')
        if int(palette) < 1 or int(palette) > 6:
            print('Please input a valid palette size!\n------------------------------')
            continue
        break

    if palette == '1':
        color1 = user_color
        #color1 = match(user_color)
        print(f'Your color palette is {color1}')
        colorFinal = [color1]
        
    if palette == '2':
        color1 = user_color
        #color1 = match(user_color)
        #print(user_color)
        #print(color1)
        color2 = complementary(color1)
        #print(color2)
        #print(f'Your color match was {color1}.')
        colorFinal = [color1, color2]
        print(f'Your color palette is {color1} and {color2}.')
        
    elif palette == '3':
        #color1 = match(user_color)
        color1 = user_color
        colors = triadic(color1)
        color2 = colors[0]
        color3 = colors[1]
        colorFinal = [color1, color2, color3]
        print(f'Your color palette is {color1}, {color2}, and {color3}.')

    elif palette == '4':
        color1 = user_color
        colors = tetradic(color1)
        color2 = colors[0]
        color3 = colors[1]
        color4 = colors[2]
        colorFinal = [color1, color2, color3, color4]
        print(f'Your color palette is {color1}, {color2}, {color3}, and {color4}.')
        
    elif palette == '5':
        color1 = user_color
        colors1 = split_complementary(user_color)
        color2 = colors1[0]
        color3 = colors1[1]
        colors2 = analogous(user_color)
        color4 = colors2[0]
        color5 = colors2[1]
        colorFinal = [color1, color2, color3, color4, color5]
        print(f'Your color palette is {color1}, {color2}, {color3}, {color4}, and {color5}.')

    elif palette == '6':
        color1 = user_color
        colors1 = analogous(user_color)
        color2 = colors1[0]
        color3 = colors1[1]
        colors2 = split_complementary(user_color)
        color4 = colors2[0]
        color5 = colors2[1]
        color6 = complementary(user_color)
        colorFinal = [color1, color2, color3, color4, color5, color6]
        print(f'Your color palette is {color1}, {color2}, {color3}, {color4}, {color5}, and {color6}.')
    else:
        print('Invalid Input')
        continue
    #names = []
    #for i in range(int(palette)):
            #temp_name = match(colorFinal[i])[0]
            #names.append(temp_name)
    #print(names)
        
    #class Button:
        #def __init__(self, text):
            #self.size = self.text.get_size()
            #self.surface = pygame.Surface(self.size)
            #self.surface.blit(self.text, (0, 0))
    #button = Button('Quit')
    display = True
    clock = pygame.time.Clock()
    while display:
        paletteDisplay = pygame.display.set_mode([500,500])
        paletteDisplay.fill([255, 255, 255])
        x = 0
        title = "Brady's Color Palette Generator!"
        width = round((500/int(palette)))
        font = pygame.font.Font(None , 20)
        font2 = pygame.font.Font(None, 35)
        for i in range(int(palette)):
            middle = round(width/2) + x
            font = pygame.font.Font(None , 20)
            font2 = pygame.font.Font(None, 35)
            text1 = font.render(f'{colorFinal[i]}', True, black)
            text2 = font2.render(f'{title}', True, black)
            textRect1 = text1.get_rect()
            textRect1.center = (middle, 475)
            textRect2 = text2.get_rect()
            textRect2.center = (200, 25)
            pygame.draw.rect(paletteDisplay, (colorFinal[i]), (x, 50, width, 400))
            paletteDisplay.blit(text1, textRect1)
            paletteDisplay.blit(text2, textRect2)
            #paletteDisplay.blit(button.surface, (435, 15))
            x += width
            middle += middle
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    display = False
                    break
            if event.type == pygame.QUIT:
                pygame.quit()
                display = False
                break
        if display:
            clock.tick(30)
            pygame.display.flip() # update the screen
        continue
    userI = input('Would you like to generate another palette (Enter: Yes or No)?\n')
    if userI == 'Yes':
        continue
    else:
        break
    
print('Thanks for generating!')


# if palette = 2
    # complementary
# if palette = 3
    # triadic
# if palette 4
    # tetradic
# if pallete = 5
    # split complementary + analogous
# if pallete = 6
    # split complementary + analogous + complementary
    


