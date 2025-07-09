import pygame
from pygame import mixer
import math

pygame.init()
mixer.init()
mixer.set_num_channels(8)   #8 seperate Channel für Musik erstellen
                                                                                                                                #VARIABLEN DEKLERATION
WHITE = (255,255,255)               #Farbcodes
BLACK = (0,0,0)
RED = (255,0,0)
PURPLE = "#A576F2"
GREY = "#616161"
DARK_YELLOW = "#61611C"
GREEN = "#1CF038"
LIGHT_RED = "#F0342B"
LIGHT_PINK = "#F3CBE0"
LAVENDEL = "#BDB0F3"
LIGHT_GREEN = "#C6F5BF"
LIGHT_CYAN = "#C2EAF5"
LIGHT_PINK = "#F5C8CF"
ORANGE = "#F4A653"
LIGHT_GREY = "#E6E6E6"

BTN_Y = 800    #Button y position
CRC_S = 100    #Kreis Durchmesser (Circle Span)

HIT = pygame.USEREVENT + 1                      #Individuelles Event für treffen des Elements
MISS = pygame.USEREVENT + 2                     #Individuelles Event für vertreffen des Elements
obstacle_timer = pygame.USEREVENT + 3           #Erstellen des Events meines Zeitzählers (timer)
pygame.time.set_timer(obstacle_timer,125)       #Alle 125 Millisekunden wird das timer Event ausgeführt


FPS = 60                                        #Frames per Second
WIDTH, HEIGHT = 1768, 992                       #Bildschirm Breite, Höhe
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  #Bildschirm
pygame.display.set_caption("Falling Buttons")
                                                                                                                                #BUTTON CLASS ERSTELLUNG
class Button():                                        #Button Klasse die individuell anklickbare Buttons erstellt
    def __init__(self, x, y, image, width, height):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

    def draw(self):                         #Checkt ob der Knopf gedrückt wird und malt den Knopf
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action
                                                                                                                                #Bilder erstellung
class Picture():
    def __init__(self, image, width, height):
            self.width = width
            self.height = height
            self.image = pygame.image.load(f"pictures/{image}")
            self.image = pygame.transform.scale(self.image, (width, height))
                                                                                                                                #fonts
font = pygame.font.Font("font/jumpman/Jumpman.ttf", 200)                            
font_back = pygame.font.Font("font/jumpman/Jumpman.ttf", 210)
font_press = pygame.font.Font("font/jumpman/Jumpman.ttf", 100)
font_press_back = pygame.font.Font("font/jumpman/Jumpman.ttf", 101)
font_small1 = pygame.font.Font("font/jumpman/Jumpman.ttf", 50)
font_small2 = pygame.font.Font("font/jumpman/Jumpman.ttf", 80)
font_small2_back = pygame.font.Font("font/jumpman/Jumpman.ttf", 81)
font_pause = pygame.font.Font("font/jumpman/Jumpman.ttf", 200)
font_score = pygame.font.Font("font/jumpman/Jumpman.ttf", 50)
                                                                                #HOMESCREEN (ab hier bis zum Ende von Game werden Texte, Buttons und Bilder erstellt)
HOMESCREEN_BACKGROUND = Picture("HOMESCREEN_BACKGROUND.png", WIDTH, HEIGHT)

HOMESCREEN_TITLE = font.render("Falling  Blocks", False, WHITE)
HOMESCREEN_TITLE_rect = HOMESCREEN_TITLE.get_rect(midtop = (WIDTH//2, 10))              #rect = rectangle
HOMESCREEN_TITLE_BACK = font_back.render("Falling  Blocks", False, BLACK)
HOMESCREEN_TITLE__BACK_rect = HOMESCREEN_TITLE_BACK.get_rect(midtop = (WIDTH//2, 10))

HOMESCREEN_CHOOSEGAME = font_small2.render("Choose your Song by clicking on the Cover!", False, WHITE)
HOMESCREEN_CHOOSEGAME_rect = HOMESCREEN_CHOOSEGAME.get_rect(center = (WIDTH//2, HEIGHT//3))
HOMESCREEN_CHOOSEGAME_BACK = font_small2_back.render("Choose your Song by clicking on the Cover!", False, BLACK)
HOMESCREEN_CHOOSEGAME_BACK_rect = HOMESCREEN_CHOOSEGAME_BACK.get_rect(center = (WIDTH//2, HEIGHT//3))
HOMESCREEN_SPECIALIST = font_small1.render("SPECIALIST - Persona4", False, WHITE)
HOMESCREEN_SPECIALIST_rect = HOMESCREEN_SPECIALIST.get_rect(midtop = (WIDTH//4, HEIGHT//1.3))
HOMESCREEN_GODONLYKNOWS = font_small1.render("GOD ONLY KNOWS - A-One", False, WHITE)
HOMESCREEN_GODONLYKNOWS_rect = HOMESCREEN_GODONLYKNOWS.get_rect(midtop = (WIDTH//1.35, HEIGHT//1.3))
HOMESCREEN_INFESTATION = font_small1.render("INFESTATION - DM DOKURO", False, WHITE)
HOMESCREEN_INFESTATION_rect = HOMESCREEN_INFESTATION.get_rect(midtop = (WIDTH // 2, HEIGHT // 1.67))

HOMESCREEN_MEDIUM = font_small1.render("MEDIUM", False, ORANGE)
HOMESCREEN_MEDIUM_rect = HOMESCREEN_MEDIUM.get_rect(midtop = (WIDTH//4, HEIGHT//1.2))
HOMESCREEN_HARD = font_small1.render("Hard", False, LIGHT_RED)
HOMESCREEN_HARD_rect = HOMESCREEN_HARD.get_rect(midtop = (WIDTH//1.35, HEIGHT//1.2))
HOMESCREEN_EXTREME = font_small1.render("Extreme", False, PURPLE)
HOMESCREEN_EXTREME_rect = HOMESCREEN_EXTREME.get_rect(midtop = (WIDTH // 2, HEIGHT // 1.53))

HOMESCREEN_SPECIALIST_PLAY = pygame.image.load("pictures/Persona4CAT.png")
HOMESCREEN_SPECIALIST_PLAY_BUTTON = Button(WIDTH//4, HEIGHT//1.5, HOMESCREEN_SPECIALIST_PLAY, 200, 200)
HOMESCREEN_SPECIALIST_PLAY_INTERACT = Picture("Persona4CAT_Interact.png", 200, 200)

HOMESCREEN_GODONLYKNOWS_PLAY = pygame.image.load("pictures/GodOnlyKnows.png")
HOMESCREEN_GODONLYKNOWS_PLAY_BUTTON = Button(WIDTH//1.35, HEIGHT//1.5, HOMESCREEN_GODONLYKNOWS_PLAY, 200, 200)
HOMESCREEN_GODONLYKNOWS_PLAY_INTERACT = Picture("GodOnlyKnows_Interact.png", 200, 200)

HOMESCREEN_INFESTATION_PLAY = pygame.image.load("pictures/Infestation.png")
HOMESCREEN_INFESTATION_PLAY_BUTTON = Button(WIDTH//2, HEIGHT// 2, HOMESCREEN_INFESTATION_PLAY, 200, 200)
HOMESCREEN_INFESTATION_PLAY_INTERACT = Picture("Infestation_Interact.png", 200, 200)
                                                                                                                                #MUSIK LAUTSTÄRKE
MUSIC_UP = pygame.image.load("pictures/VolumeUp.png")
MUSIC_UP_BUTTON = Button(WIDTH-50, HEIGHT-105, MUSIC_UP, 50, 50)
MUSIC_UP_INTERACT = Picture("VolumeUp_Interact.png", 50, 50)

MUSIC_DOWN = pygame.image.load("pictures/VolumeDown.png")
MUSIC_DOWN_BUTTON = Button(WIDTH-50, HEIGHT-50, MUSIC_DOWN, 50, 50)
MUSIC_DOWN_INTERACT = Picture("VolumeDown_Interact.png", 50, 50)

MUSIC_SYMBOL = pygame.image.load("pictures/VolumeSymbol.png")
MUSIC_SYMBOL_BUTTON = Button(WIDTH-120, HEIGHT-80, MUSIC_SYMBOL, 50, 50)
MUSIC_SYMBOL_INTERACT = Picture("VolumeSymbol_Interact.png", 50, 50)
                                                                                                                                #PAUSE
PAUSE = font_pause.render("PAUSE", False, WHITE)
PAUSE_rect = PAUSE.get_rect(center = (WIDTH//1.9, HEIGHT//5))

PAUSE_HOME = pygame.image.load("pictures/HOME.png")
PAUSE_HOME_BUTTON = Button(WIDTH//1.9, HEIGHT// 2  + 200, PAUSE_HOME, 550, 110)
PAUSE_HOME_INTERACT = Picture("HOME_INTERACT.png", 550, 110)

PAUSE_CONTINUE = pygame.image.load("pictures/CONTINUE.png")
PAUSE_CONTINUE_BUTTON = Button(WIDTH//1.9, HEIGHT//2, PAUSE_CONTINUE, 550, 110)
PAUSE_CONTINUE_INTERACT = Picture("CONTINUE_INTERACT.png", 550, 110)

PAUSE_RETRY = pygame.image.load("pictures/RETRY.png")
PAUSE_RETRY_BUTTON = Button(WIDTH//1.9, HEIGHT// 2 + 100, PAUSE_RETRY, 275, 110)
PAUSE_RETRY_INTERACT = Picture("RETRY_INTERACT.png", 275, 110)

PAUSE_TRANSPARENCY = Picture("Transparency.png", WIDTH, HEIGHT)
                                                                                                                                #DEATH
DEATH_TRANSPARENCY = Picture("Death_Transparency.png", WIDTH, HEIGHT)

DEATH = font_pause.render("YOU LOST", False, WHITE)
DEATH_rect = DEATH.get_rect(center = (WIDTH//1.9, HEIGHT//5))
                                                                                                                                #WIN
WON = font_pause.render("YOU PASSED", False, WHITE)
WON_rect = WON.get_rect(center = (WIDTH//1.9, HEIGHT//5))

WON_BACKGROUND = Picture("WON_BACKGROUND.png", WIDTH, HEIGHT)
                                                                                                                                #GAME
GAME_BACKGROUND1 =  Picture("Persona4.png", WIDTH, HEIGHT)
GAME_BACKGROUND2 = Picture("GodOnlyKnowsBackground.png", WIDTH, HEIGHT) 
GAME_BACKGROUND3 = Picture("InfestationBackground.png", WIDTH, HEIGHT)

GAME_BTN1 = pygame.Rect(round(WIDTH * 0.2), BTN_Y, CRC_S, CRC_S)     #BTN = Button
GAME_BTN2 = pygame.Rect(round(WIDTH * 0.4), BTN_Y, CRC_S, CRC_S)
GAME_BTN3 = pygame.Rect(round(WIDTH * 0.6), BTN_Y, CRC_S, CRC_S)
GAME_BTN4 = pygame.Rect(round(WIDTH * 0.8),  BTN_Y, CRC_S, CRC_S)

font_key = pygame.font.Font("font/jumpman/Jumpman.ttf", 75)

GAME_KEY1 = font_key.render("V", False, LIGHT_GREEN)
GAME_KEY2 = font_key.render("B", False, LIGHT_PINK)
GAME_KEY3 = font_key.render("N", False, LAVENDEL)
GAME_KEY4 = font_key.render("M", False, LIGHT_CYAN)
GAME_KEY1_rec = GAME_KEY1.get_rect(center = (round(WIDTH * 0.2) + CRC_S / 2 + 2, BTN_Y + CRC_S / 2 - 2))
GAME_KEY2_rec = GAME_KEY2.get_rect(center = (round(WIDTH * 0.4) + CRC_S / 2 + 2, BTN_Y + CRC_S / 2 - 2))
GAME_KEY3_rec = GAME_KEY3.get_rect(center = (round(WIDTH * 0.6) + CRC_S / 2 + 2, BTN_Y + CRC_S / 2 - 2))
GAME_KEY4_rec = GAME_KEY4.get_rect(center = (round(WIDTH * 0.8) + CRC_S / 2 + 2, BTN_Y + CRC_S / 2 - 2))

GAME_BTN1O = pygame.Rect(round(WIDTH * 0.2), BTN_Y, CRC_S, CRC_S)    #Indikator für Knopf drücke (visuel)
GAME_BTN2O = pygame.Rect(round(WIDTH * 0.4), BTN_Y, CRC_S, CRC_S)
GAME_BTN3O = pygame.Rect(round(WIDTH * 0.6), BTN_Y, CRC_S, CRC_S)
GAME_BTN4O = pygame.Rect(round(WIDTH * 0.8), BTN_Y, CRC_S, CRC_S)

GAME_LINE1 = pygame.Rect(round(WIDTH * 0.2) - 20, -20, CRC_S + 40, 1100)
GAME_LINE2 = pygame.Rect(round(WIDTH * 0.4) - 20, -20, CRC_S + 40, 1100)
GAME_LINE3 = pygame.Rect(round(WIDTH * 0.6) - 20, -20, CRC_S + 40, 1100)
GAME_LINE4 = pygame.Rect(round(WIDTH * 0.8) - 20, -20, CRC_S + 40, 1100)

GAME_READY = font_pause.render("READY?", False, WHITE,)
GAME_READY_rect = GAME_READY.get_rect(center = (WIDTH//1.9, HEIGHT//2))
GAME_3 = font_back.render("3", False, WHITE,)
GAME_2 = font_back.render("2", False, WHITE,)
GAME_1 = font_back.render("1", False, WHITE,)
GAME_1_rect = GAME_1.get_rect(center = (WIDTH//1.9, HEIGHT//2))

GAME_SKIP = font_score.render("SKIP? (E)", False, WHITE,)
GAME_SKIP_rect = GAME_SKIP.get_rect(midright = (WIDTH, HEIGHT - 30))

MISS_TRANSPERENCY_GAME1 = Picture("MISS_Transperency_game1.png", WIDTH, HEIGHT)
MISS_TRANSPERENCY_GAME2 = Picture("MISS_Transperency_game2.png", WIDTH, HEIGHT)
MISS_TRANSPERENCY_GAME3 = Picture("MISS_Transperency_game3.png", WIDTH, HEIGHT)

GAME_BAR_OUTLINE = Picture("BAR.png", 100, 600)
GAME_BAR_OUTLINE_rect = GAME_BAR_OUTLINE.image.get_rect(bottomright = (WIDTH // 5.5, HEIGHT))

GAME_Piechart = Picture("Circle.png", 104, 102)
                                                                                #_music funktion lässt Musik einmal abspielen
def overtake_music(OVERTAKE, MUSIK_LAUTSTARKE, SOUND):
    if OVERTAKE:
        mixer.music.load(f"music/{SOUND}")
        mixer.music.set_volume(MUSIK_LAUTSTARKE)
        mixer.music.play()
                                                                                #Alle Funktionen mit _draw sind für das malen der verschiedenen Screens
def death_draw(transparency_check):
    if transparency_check:                            #Setzt transparenz einmal falls der Deathscreen angezeigt wird
        WIN.blit(DEATH_TRANSPARENCY.image,(0,0))
    WIN.blit(DEATH, DEATH_rect)

    pos = pygame.mouse.get_pos() 
    if MUSIC_UP_BUTTON.rect.collidepoint(pos):                        #Weitere Interaktionen mit Knöpfen
        WIN.blit(MUSIC_UP_INTERACT.image, MUSIC_UP_BUTTON.rect)
    if MUSIC_DOWN_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_DOWN_INTERACT.image, MUSIC_DOWN_BUTTON.rect)
    if MUSIC_SYMBOL_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_SYMBOL_INTERACT.image, MUSIC_SYMBOL_BUTTON.rect)
    if PAUSE_HOME_BUTTON.rect.collidepoint(pos):                   
        WIN.blit(PAUSE_HOME_INTERACT.image,PAUSE_HOME_BUTTON.rect)
    if PAUSE_RETRY_BUTTON.rect.collidepoint(pos):
        WIN.blit(PAUSE_RETRY_INTERACT.image, PAUSE_RETRY_BUTTON.rect)
    pygame.display.update()

def won_draw(WON_SCORE, HIT_counter, ELEMENT_counter, WON_FINISH):
    if not WON_FINISH:
        WIN.blit(WON_BACKGROUND.image,(0,0))              #Malt den Hintergrund währen der Score lädt

    WIN.blit(WON, WON_rect)

    if WON_FINISH:                                  #Wenn der Score geladen hat werden die Knöpfe freigeschalten     
        pos = pygame.mouse.get_pos() 
        if MUSIC_UP_BUTTON.rect.collidepoint(pos):
            WIN.blit(MUSIC_UP_INTERACT.image, MUSIC_UP_BUTTON.rect)
        if MUSIC_DOWN_BUTTON.rect.collidepoint(pos):
            WIN.blit(MUSIC_DOWN_INTERACT.image, MUSIC_DOWN_BUTTON.rect)
        if MUSIC_SYMBOL_BUTTON.rect.collidepoint(pos):
            WIN.blit(MUSIC_SYMBOL_INTERACT.image, MUSIC_SYMBOL_BUTTON.rect)
        if PAUSE_HOME_BUTTON.rect.collidepoint(pos):
            WIN.blit(PAUSE_HOME_INTERACT.image,PAUSE_HOME_BUTTON.rect)
        if PAUSE_RETRY_BUTTON.rect.collidepoint(pos):
            WIN.blit(PAUSE_RETRY_INTERACT.image, PAUSE_RETRY_BUTTON.rect)

    SCORE_TEXT = font_press.render("Total Score : " + str(WON_SCORE), False, LAVENDEL)  #Zeigt den Score an
    SCORE_TEXT_rect = SCORE_TEXT.get_rect(center = (WIDTH// 1.9, HEIGHT // 2.7))
    WIN.blit(SCORE_TEXT, SCORE_TEXT_rect)
    if ELEMENT_counter > 0:                                                             #Zeigt die Prozentanzahl an
        PERCENTAGE = round(HIT_counter / ELEMENT_counter * 100, 1)
        PERCENTAGE_TEXT = font_press.render(str(PERCENTAGE) + "%", False, LIGHT_PINK)
        PERCENTAGE_TEXT_rect = PERCENTAGE_TEXT.get_rect(center = (WIDTH// 1.9, HEIGHT // 2.1))
        WIN.blit(PERCENTAGE_TEXT, PERCENTAGE_TEXT_rect)
    pygame.display.update()

def homescreen_draw(homescreen_check):
    if homescreen_check:
        WIN.blit(HOMESCREEN_BACKGROUND.image,(0,0))
    WIN.blit(HOMESCREEN_TITLE_BACK, HOMESCREEN_TITLE__BACK_rect)
    WIN.blit(HOMESCREEN_TITLE, HOMESCREEN_TITLE_rect)
    WIN.blit(HOMESCREEN_CHOOSEGAME_BACK, HOMESCREEN_CHOOSEGAME_BACK_rect)
    WIN.blit(HOMESCREEN_CHOOSEGAME,HOMESCREEN_CHOOSEGAME_rect)
    WIN.blit(HOMESCREEN_SPECIALIST, HOMESCREEN_SPECIALIST_rect)
    WIN.blit(HOMESCREEN_GODONLYKNOWS, HOMESCREEN_GODONLYKNOWS_rect)
    WIN.blit(HOMESCREEN_INFESTATION,HOMESCREEN_INFESTATION_rect)
    WIN.blit(HOMESCREEN_MEDIUM, HOMESCREEN_MEDIUM_rect)
    WIN.blit(HOMESCREEN_HARD,HOMESCREEN_HARD_rect)
    WIN.blit(HOMESCREEN_EXTREME,HOMESCREEN_EXTREME_rect)
    
    pos = pygame.mouse.get_pos()                    #Interaktionen mit Knöpfen
    if MUSIC_UP_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_UP_INTERACT.image, MUSIC_UP_BUTTON.rect)
    if MUSIC_DOWN_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_DOWN_INTERACT.image, MUSIC_DOWN_BUTTON.rect)
    if MUSIC_SYMBOL_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_SYMBOL_INTERACT.image, MUSIC_SYMBOL_BUTTON.rect)

    if HOMESCREEN_SPECIALIST_PLAY_BUTTON.rect.collidepoint(pos):
        WIN.blit(HOMESCREEN_SPECIALIST_PLAY_INTERACT.image, HOMESCREEN_SPECIALIST_PLAY_BUTTON.rect)
    if HOMESCREEN_GODONLYKNOWS_PLAY_BUTTON.rect.collidepoint(pos):
        WIN.blit(HOMESCREEN_GODONLYKNOWS_PLAY_INTERACT.image, HOMESCREEN_GODONLYKNOWS_PLAY_BUTTON.rect)
    if HOMESCREEN_INFESTATION_PLAY_BUTTON.rect.collidepoint(pos):
        WIN.blit(HOMESCREEN_INFESTATION_PLAY_INTERACT.image, HOMESCREEN_INFESTATION_PLAY_BUTTON.rect)
    pygame.display.update()

def pause_draw(transparency_check):
    if transparency_check:                  #Setzt transparenz falls Pause gedrückt wurde
        WIN.blit(PAUSE_TRANSPARENCY.image,(0,0))
    
    pos = pygame.mouse.get_pos() 
    if PAUSE_HOME_BUTTON.rect.collidepoint(pos):                      #Weitere Interaktionen mit Knöpfen
        WIN.blit(PAUSE_HOME_INTERACT.image,PAUSE_HOME_BUTTON.rect)
    if PAUSE_CONTINUE_BUTTON.rect.collidepoint(pos):
        WIN.blit(PAUSE_CONTINUE_INTERACT.image,PAUSE_CONTINUE_BUTTON.rect)
    if PAUSE_RETRY_BUTTON.rect.collidepoint(pos):
        WIN.blit(PAUSE_RETRY_INTERACT.image, PAUSE_RETRY_BUTTON.rect)
    
    if MUSIC_UP_BUTTON.rect.collidepoint(pos):                          
        WIN.blit(MUSIC_UP_INTERACT.image, MUSIC_UP_BUTTON.rect)
    if MUSIC_DOWN_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_DOWN_INTERACT.image, MUSIC_DOWN_BUTTON.rect)
    if MUSIC_SYMBOL_BUTTON.rect.collidepoint(pos):
        WIN.blit(MUSIC_SYMBOL_INTERACT.image, MUSIC_SYMBOL_BUTTON.rect)

    WIN.blit(PAUSE, PAUSE_rect)
    pygame.display.update()

def game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, game, MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart):
    if game == "game1":                     #Checkt in welchem Spiel wir uns befinden und setzt anhand dessen andere Hintergründe und MISS Effekte
        WIN.blit(GAME_BACKGROUND1.image,(0,0))
        if MISS_check > 0:
            WIN.blit(MISS_TRANSPERENCY_GAME1.image,(0,0))

    if game == "game2":
        WIN.blit(GAME_BACKGROUND2.image,(0,0))
        if MISS_check > 0:
            WIN.blit(MISS_TRANSPERENCY_GAME2.image,(0,0))
    
    if game == "game3":
        WIN.blit(GAME_BACKGROUND3.image,(0,0))
        if MISS_check > 0:
            WIN.blit(MISS_TRANSPERENCY_GAME3.image,(0,0))

    pygame.draw.arc(WIN, LIGHT_GREY, [WIDTH - 148, 50, 98, 100], 0, piechart, 100)      #Malt den Fortschritt anhand eines Kreises
    pygame.draw.arc(WIN, LIGHT_GREY, [WIDTH - 149, 50, 99, 100], 0, piechart, 100)
    pygame.draw.arc(WIN, LIGHT_GREY, [WIDTH - 150, 50, 100, 100], 0, piechart, 100)
    WIN.blit(GAME_Piechart.image, (WIDTH - 153, 49))


    pygame.draw.ellipse(WIN, BLACK, GAME_BTN1)              #Die Spielknöpfe
    pygame.draw.ellipse(WIN, BLACK, GAME_BTN2)
    pygame.draw.ellipse(WIN, BLACK, GAME_BTN3)
    pygame.draw.ellipse(WIN, BLACK, GAME_BTN4)

    pygame.draw.rect(WIN, BLACK, GAME_LINE1,5)              #Die Spiel Linien
    pygame.draw.rect(WIN, BLACK, GAME_LINE2,5)
    pygame.draw.rect(WIN, BLACK, GAME_LINE3,5)
    pygame.draw.rect(WIN, BLACK, GAME_LINE4,5)

    WIN.blit(GAME_KEY1, GAME_KEY1_rec)
    WIN.blit(GAME_KEY2, GAME_KEY2_rec)
    WIN.blit(GAME_KEY3, GAME_KEY3_rec)
    WIN.blit(GAME_KEY4, GAME_KEY4_rec)

    MULTIPLIER_TEXT = font_score.render("Multiplier : " + str(MULTIPLIER) + "x", False, WHITE)  #Alle Statistiken im Spiel
    WIN.blit(MULTIPLIER_TEXT, [10,10])
    SCORE_TEXT = font_score.render("Score : " + str(SCORE), False, WHITE)
    WIN.blit(SCORE_TEXT, [10,50])
    if ELEMENT_counter > 0:
        PERCENTAGE = round(HIT_counter / ELEMENT_counter * 100, 1)
        PERCENTAGE_TEXT = font_score.render(str(PERCENTAGE) + "%", False, WHITE)
        PERCENTAGE_TEXT_rect = PERCENTAGE_TEXT.get_rect(center = (WIDTH//1.9, HEIGHT // 6))
        WIN.blit(PERCENTAGE_TEXT, PERCENTAGE_TEXT_rect)

    GAME_BAR = pygame.Rect(0,0,50, LIFES * 5.4)             #Umrandung der Lebensanzeige
    GAME_BAR.bottomright = (WIDTH // 5.5 - 25,HEIGHT - 30) 

    
    if LIFES <= 80 and LIFES * 5.4 > 50:                #Lebensanzeige die aktualisiert
        pygame.draw.rect(WIN,ORANGE, GAME_BAR)
    if LIFES <= 50:
        pygame.draw.rect(WIN,RED, GAME_BAR)
    if LIFES > 80 :
        pygame.draw.rect(WIN,GREEN, GAME_BAR)
    WIN.blit(GAME_BAR_OUTLINE.image, GAME_BAR_OUTLINE_rect)


    if keys_pressed[pygame.K_v]:                                #Umrandung der Spielknöpfe faöös gedrückt
        pygame.draw.ellipse(WIN, LIGHT_GREEN, GAME_BTN1O, 4)
    if keys_pressed[pygame.K_b]:
         pygame.draw.ellipse(WIN, LIGHT_PINK, GAME_BTN2O, 4)
    if keys_pressed[pygame.K_n]:
        pygame.draw.ellipse(WIN, LAVENDEL, GAME_BTN3O, 4)
    if keys_pressed[pygame.K_m]:
        pygame.draw.ellipse(WIN, LIGHT_CYAN, GAME_BTN4O, 4)
        
    for OBJECTS1 in LINE1:                                 #Malt die Elemente
        pygame.draw.ellipse(WIN, LIGHT_GREEN, OBJECTS1)
    for OBJECTS2 in LINE2:
        pygame.draw.ellipse(WIN, LIGHT_PINK, OBJECTS2)
    for OBJECTS3 in LINE3:
        pygame.draw.ellipse(WIN, LAVENDEL, OBJECTS3)
    for OBJECTS4 in LINE4:
        pygame.draw.ellipse(WIN, LIGHT_CYAN, OBJECTS4)

    if timer > -1 and timer < 14:
        WIN.blit(GAME_SKIP,GAME_SKIP_rect)
    if timer > 5 and timer < 8:                #Die Indikatoren das dass Speil beginnt
        WIN.blit(GAME_READY, GAME_READY_rect)
    if timer == 14:
        WIN.blit(GAME_3, GAME_1_rect)
    if timer == 15:
        WIN.blit(GAME_2, GAME_1_rect)
    if timer == 16:
        WIN.blit(GAME_1, GAME_1_rect)

    pygame.display.update()

def game_handle_lines(LINE1,LINE2,LINE3,LINE4, keys_pressed, CHECK1,CHECK2,CHECK3,CHECK4, VEL):  #Alle Linien auf Kollisionen Checken und danach Aktualisieren
    STRAT1 = True
    STRAT2 = True
    STRAT3 = True
    STRAT4 = True
    
    for OBJECTS1 in LINE1:
        OBJECTS1.y += VEL
        if GAME_BTN1.colliderect(OBJECTS1) and keys_pressed[pygame.K_v] and CHECK1:     #Check ob wir das Element getroffen haben (HIT EVENT)
            pygame.event.post(pygame.event.Event(HIT))
            LINE1.remove(OBJECTS1)
            STRAT1 = False
        elif OBJECTS1.y > HEIGHT:                                       #Check falls Element nicht getroffen ob das Element unter der Y achse ist und entfernt werden muss (MISS EVENT)  
            LINE1.remove(OBJECTS1)
            pygame.event.post(pygame.event.Event(MISS))
            STRAT1 = False
        elif not GAME_BTN1.colliderect(OBJECTS1) and keys_pressed[pygame.K_v] and CHECK1 and STRAT1:                 #Falls auch das nicht Check ob Knopf gedrückt wird ohne Element im Radius (MISS EVENT)                                 
            pygame.event.post(pygame.event.Event(MISS))
            STRAT1 = False
    if len(LINE1) == 0 and STRAT1:                                      #Wenn der Knopf gedrückt wird obwohl kein Objekt in der Linie ist wird hier auch das MISS event ausgeführt
        if keys_pressed[pygame.K_v] and CHECK1:
            pygame.event.post(pygame.event.Event(MISS))
            

    for OBJECTS2 in LINE2:
        OBJECTS2.y += VEL
        if GAME_BTN2.colliderect(OBJECTS2) and keys_pressed[pygame.K_b] and CHECK2:
            pygame.event.post(pygame.event.Event(HIT))
            LINE2.remove(OBJECTS2)
            STRAT2 = False
        elif OBJECTS2.y > HEIGHT:
            LINE2.remove(OBJECTS2)
            pygame.event.post(pygame.event.Event(MISS))
            STRAT2 = False
        elif not GAME_BTN2.colliderect(OBJECTS2) and keys_pressed[pygame.K_b] and CHECK2 and STRAT2:
            pygame.event.post(pygame.event.Event(MISS))
            STRAT2 = False
    if len(LINE2) == 0 and STRAT2:
        if keys_pressed[pygame.K_b] and CHECK2:
            pygame.event.post(pygame.event.Event(MISS))
    
    for OBJECTS3 in LINE3:
        OBJECTS3.y += VEL
        if GAME_BTN3.colliderect(OBJECTS3) and keys_pressed[pygame.K_n] and CHECK3:
            pygame.event.post(pygame.event.Event(HIT))
            LINE3.remove(OBJECTS3)
            STRAT3 = False
        elif OBJECTS3.y > HEIGHT:
            LINE3.remove(OBJECTS3)
            pygame.event.post(pygame.event.Event(MISS))
            STRAT3 = False
        elif not GAME_BTN3.colliderect(OBJECTS3) and keys_pressed[pygame.K_n] and CHECK3 and STRAT3:
            pygame.event.post(pygame.event.Event(MISS))
            TRAT3 = False
    if len(LINE3) == 0 and STRAT3:
        if keys_pressed[pygame.K_n] and CHECK3:
            pygame.event.post(pygame.event.Event(MISS))

    for OBJECTS4 in LINE4:
        OBJECTS4.y += VEL
        if GAME_BTN4.colliderect(OBJECTS4) and keys_pressed[pygame.K_m] and CHECK4:
            pygame.event.post(pygame.event.Event(HIT))
            LINE4.remove(OBJECTS4)
            STRAT4 = False
        elif OBJECTS4.y > HEIGHT:
            LINE4.remove(OBJECTS4)
            pygame.event.post(pygame.event.Event(MISS))
            STRAT4 = False
        elif not GAME_BTN4.colliderect(OBJECTS4) and keys_pressed[pygame.K_m] and CHECK4 and STRAT4:
            pygame.event.post(pygame.event.Event(MISS))
            STRAT4 = False
    if len(LINE4) == 0 and STRAT4:
        if keys_pressed[pygame.K_m] and CHECK4:
            pygame.event.post(pygame.event.Event(MISS))


def main():
    
    LINE1 = []          #1. Spiel Reihe
    LINE2 = []          #2. Spiel Reihe
    LINE3 = []          #3. Spiel Reihe
    LINE4 = []          #4. Spiel Reihe
    HOMESCREEN = True   #Ob der Homescreen angezeigt wird
    OVERTAKE_HOMESCREEN = True     #Zum Musik abspielen
    OVERTAKE_GAME = True
    wait = False        #Ob der Wartescreen angezeigt wird
    CHECK1 = True        #Um 1maligen Knopfdruck zu gewähren
    CHECK2 = True
    CHECK3 = True
    CHECK4 = True
    timer = 0         #Timer initialisieren
    game1 = False
    game2 = False
    game3 = False
    homescreen_check = True
    MISS_check = 0
    VEL = 15                        #Velocity
    MULTIPLIER = 1
    SCORE = 0
    WON_SCORE = 0
    MUSIK_LAUTSTARKE = 0.1
    LIFES = 100
    LIFES_MULTI = 1
    LIFES_counter = 0
    ELEMENT_counter = 0
    HIT_counter = 0
    fade = False
    fade_count = 0
    death = False
    OVERTAKE_DEATH = True
    won = False
    piechart = 0
    piechartnum = 0
    countHit = 1
    countMiss = 1
    generator1check = True      #Für die Levelerstellung
    generator2check = True
    generator3check = True
    generator4check = True
    test1 = []                  #Für die Levelerstellung
    test2 = []
    test3 = []
    test4 = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                                                                            #Alles ab hier spawnt meine Elemente
            if event.type == obstacle_timer:                                            
                    if not HOMESCREEN and not wait and game1:                                                                   #Game1 spawner
                        timer += 0.125
                        if timer in [15.875, 18.25, 19.625, 20.625, 23.625, 24.75, 27.125, 28.25, 29.375, 33.0, 33.625, 36.5, 37.625, 38.25, 38.625, 38.75, 39.0, 40.875, 42.375, 44.125, 45.0, 48.5, 49.375, 50.375, 51.875, 53.25, 53.875, 57.125, 58.375, 61.375, 62.125, 65.5, 66.5, 66.75, 68.875, 71.125, 72.0, 73.125, 73.875, 74.0, 75.625, 77.125, 78.0, 79.625, 81.75, 84.75, 86.0, 86.875, 89.75, 92.25, 95.625, 97.875, 99.0, 101.375, 102.0, 103.5, 104.375, 106.625, 107.5, 108.125, 110.0, 110.875, 113.25, 115.625, 118.375, 119.125, 119.75, 120.125, 122.875, 124.375, 125.375, 128.0, 129.375, 130.25, 132.5, 133.875]: #Line 1
                            OBJECTS1 = pygame.Rect(round(WIDTH * 0.2 + 10), 0, 80, 80)
                            LINE1.append(OBJECTS1)
                        if timer in [16.25, 17.5, 18.75, 20.125, 21.25, 24.0, 25.375, 26.25, 27.5, 29.0, 32.0, 34.125, 35.5, 36.875, 38.25, 38.625, 38.75, 39.0, 39.625, 41.25, 43.125, 44.625, 47.375, 48.75, 49.625, 50.75, 52.125, 53.5, 54.5, 55.0, 55.375, 55.875, 56.25, 56.75, 57.625, 59.125, 61.0, 62.125, 63.125, 65.0, 66.125, 68.5, 69.875, 70.5, 72.375, 74.25, 74.75, 76.0, 77.25, 78.5, 80.125, 81.0, 83.375, 83.75, 85.5, 87.25, 88.25, 88.75, 89.0, 93.125, 93.625, 95.125, 96.5, 98.375, 99.75, 101.625, 102.875, 103.875, 107.0, 107.875, 108.625, 110.375, 111.625, 111.875, 114.0, 116.5, 117.75, 118.875, 120.5, 122.125, 123.375, 124.625, 124.875, 125.875, 128.5, 128.75, 130.0, 131.0, 133.375, 135.375]: #Line 2
                            OBJECTS2 = pygame.Rect(round(WIDTH * 0.4 + 10), 0, 80, 80)
                            LINE2.append(OBJECTS2)
                        if timer in [16.125, 17.25, 18.625, 20.375, 21.625, 23.75, 25.0, 26.125, 28.0, 29.125, 30.625, 31.0, 32.5, 33.875, 34.625, 35.75, 36.125, 36.75, 39.375, 39.875, 40.375, 41.125, 41.625, 42.625, 44.375, 45.625, 46.875, 47.75, 49.0, 49.625, 51.0, 51.5, 52.375, 53.625, 54.25, 55.5, 56.375, 57.375, 58.625, 59.375, 61.125, 62.375, 63.5, 64.5, 64.75, 65.125, 66.875, 68.5, 69.625, 71.0, 72.875, 74.375, 74.75, 76.25, 77.125, 78.5, 79.875, 81.375, 83.5, 84.625, 85.875, 87.125, 88.125, 89.25, 92.75, 94.125, 96.0, 97.375, 100.0, 100.625, 101.5, 102.375, 103.25, 104.125, 105.125, 105.5, 105.875, 106.75, 107.625, 108.375, 109.0, 109.5, 110.625, 111.375, 112.375, 113.5, 115.125, 117.5, 118.625, 121.0, 121.75, 122.5, 124.5, 124.875, 125.625, 126.625, 128.75, 129.625, 131.875, 133.625, 134.875]: #Line 3
                            OBJECTS3 = pygame.Rect(round(WIDTH * 0.6 + 10), 0, 80, 80)
                            LINE3.append(OBJECTS3)
                        if timer in [16.5, 17.875, 19.875, 21.0, 22.0, 23.25, 25.625, 27.375, 28.5, 29.875, 30.625, 31.0, 34.375, 34.75, 35.875, 37.125, 39.5, 40.125, 40.625, 41.5, 43.875, 45.375, 46.875, 50.625, 51.25, 54.75, 55.25, 56.0, 56.875, 58.875, 59.875, 60.75, 62.75, 63.625, 64.5, 64.75, 65.875, 68.25, 70.25, 70.5, 72.25, 73.375, 76.0, 77.75, 79.375, 80.5, 80.75, 81.75, 83.125, 83.75, 84.875, 87.875, 88.75, 89.0, 91.75, 94.625, 96.875, 100.375, 101.875, 102.75, 103.75, 105.0, 105.375, 105.75, 107.25, 108.75, 109.25, 110.125, 111.125, 112.125, 113.0, 114.5, 117.0, 117.875, 120.75, 121.125, 121.75, 126.25, 128.25, 129.125, 132.25, 134.125]: #Line 4
                            OBJECTS4 = pygame.Rect(round(WIDTH * 0.8 + 10), 0, 80, 80)
                            LINE4.append(OBJECTS4)
                    if not HOMESCREEN and not wait and game2:                                                                   #Game2 spawner
                        timer += 0.125
                        timer = round(timer,3)
                        if timer in [16.125, 17.625, 18.625, 19.375, 21.125, 21.5, 22.125, 23.625, 25.625, 26.75, 27.75, 29.25, 30.375, 31.625, 32.0, 35.0, 36.375, 37.25, 40.125, 40.75, 44.625, 47.125, 49.125, 49.625, 51.375, 54.25, 55.0, 55.625, 56.75, 58.625, 59.375, 59.625, 62.125, 63.0, 63.625, 64.75, 65.5, 67.25, 68.375, 69.25, 70.875, 72.125, 73.375, 73.5, 74.375, 74.875, 76.0, 81.125, 81.375, 81.75, 82.125, 82.5, 82.875, 83.125, 83.5, 85.125, 85.5, 85.875, 86.125, 86.5, 86.75, 87.125, 87.5, 87.75, 90.375, 91.625, 92.125, 93.125, 94.5, 94.875, 95.25, 97.0, 99.125, 100.5, 100.875, 103.0, 106.5, 107.625, 109.0, 109.625, 112.25, 113.25, 114.25, 115.125, 117.125, 117.75, 120.25, 121.0, 121.75, 122.5, 124.125, 125.5, 126.5, 127.625, 128.0, 128.375, 128.75, 129.125, 129.25, 130.0, 131.5, 133.625, 135.375, 136.25, 137.0, 137.375, 138.875, 141.125, 141.75, 144.125, 144.5, 149.875, 150.25, 150.5, 150.875, 151.25, 151.5, 151.875, 152.25, 152.625, 152.875, 153.25, 153.625, 153.875, 156.125, 156.5, 158.125, 160.25, 160.875, 161.375, 161.875, 163.5, 164.625, 164.875, 166.0, 169.125, 170.625, 172.0, 173.75, 175.125, 175.75, 176.25, 177.125, 178.625, 179.375, 179.625, 182.5, 183.375, 184.25, 184.625, 185.625, 187.75, 188.75, 191.375, 192.75, 196.25, 196.75, 197.25, 197.75, 198.25, 199.0, 199.625, 200.0, 201.875, 203.25, 205.75, 207.75, 209.375, 211.0, 212.25, 213.375, 215.625, 219.125, 220.625, 223.625, 224.375, 225.5, 225.875, 226.75, 229.625, 229.875, 231.875, 232.5, 232.875, 234.25, 235.625, 236.75, 239.0, 239.5, 240.5, 242.25, 244.0, 245.375, 245.75, 246.125, 246.5, 249.875, 250.125, 250.5, 250.875, 251.25, 251.625, 252.0, 252.25, 255.5, 255.75, 256.125, 256.5, 257.5, 257.75, 258.25, 258.625, 259.0, 259.25, 259.75, 260.125, 260.375, 260.75, 261.125, 261.375, 261.75, 262.125, 262.5, 262.875, 263.25, 263.5, 265.25, 265.625, 266.0, 266.375, 266.75, 267.0, 267.375, 267.75, 268.625, 269.0, 269.375, 270.75, 271.5, 272.125, 273.625, 274.375, 275.125, 277.125, 277.875, 279.25]: #Line 1
                            OBJECTS1 = pygame.Rect(round(WIDTH * 0.2 + 10), 0, 80, 80)
                            LINE1.append(OBJECTS1)
                        if timer in [16.875, 18.375, 20.0, 21.125, 21.5, 22.875, 24.625, 25.625, 26.375, 27.125, 29.625, 31.25, 32.375, 34.125, 35.875, 36.875, 37.875, 38.75, 39.75, 40.125, 41.5, 43.875, 45.75, 48.625, 49.125, 49.625, 50.25, 52.375, 54.25, 55.0, 56.25, 57.25, 58.125, 58.875, 59.375, 59.625, 60.5, 62.375, 63.25, 64.75, 66.125, 67.875, 68.75, 70.0, 71.75, 72.75, 75.25, 77.375, 77.75, 78.25, 78.625, 79.0, 79.25, 79.625, 80.0, 80.375, 80.75, 85.25, 85.625, 86.0, 86.375, 88.625, 89.0, 91.375, 92.125, 93.875, 96.0, 98.75, 100.25, 102.0, 103.875, 105.375, 107.625, 108.625, 110.75, 111.5, 113.5, 116.0, 117.125, 118.875, 119.875, 122.5, 123.5, 124.875, 126.25, 127.0, 129.625, 130.625, 132.875, 134.25, 134.75, 134.875, 136.0, 136.75, 137.625, 139.625, 140.0, 140.5, 141.5, 142.75, 144.875, 145.25, 147.0, 147.375, 147.75, 148.125, 148.5, 148.75, 149.125, 149.5, 154.25, 154.625, 155.0, 155.375, 157.5, 158.625, 159.625, 160.75, 161.25, 162.25, 163.0, 164.0, 165.25, 166.5, 167.0, 167.5, 167.875, 168.75, 169.875, 170.75, 171.625, 173.0, 174.5, 175.5, 176.125, 176.5, 177.625, 179.0, 180.0, 180.375, 180.75, 181.0, 181.375, 181.75, 182.0, 182.75, 185.0, 186.0, 186.875, 188.25, 189.25, 189.5, 189.875, 190.25, 190.625, 193.5, 193.75, 196.375, 196.875, 197.5, 198.0, 198.5, 199.25, 199.75, 200.25, 202.125, 204.375, 206.625, 208.875, 210.375, 212.125, 214.125, 216.5, 218.375, 219.75, 221.125, 221.5, 222.25, 222.875, 223.625, 224.875, 226.25, 227.5, 228.375, 228.875, 230.375, 231.25, 233.5, 234.875, 236.375, 237.5, 238.625, 239.625, 241.25, 241.5, 241.75, 243.125, 244.75, 247.0, 247.375, 247.75, 248.125, 248.375, 248.75, 249.125, 249.5, 252.625, 253.0, 253.375, 253.625, 256.75, 257.125, 261.125, 261.375, 261.75, 262.125, 263.875, 264.25, 264.625, 265.0, 268.625, 269.0, 270.125, 270.75, 272.125, 275.75, 277.875, 280.5]: #Line 2
                            OBJECTS2 = pygame.Rect(round(WIDTH * 0.4 + 10), 0, 80, 80)
                            LINE2.append(OBJECTS2)
                        if timer in [17.25, 19.0, 20.375, 20.75, 21.125, 21.5, 24.125, 26.75, 28.5, 29.625, 31.625, 32.0, 34.5, 35.875, 37.25, 39.0, 40.75, 42.875, 43.25, 43.375, 43.875, 46.75, 47.625, 48.25, 51.875, 53.5, 55.0, 56.0, 57.125, 58.0, 58.75, 60.125, 61.25, 62.75, 64.0, 65.5, 66.875, 68.0, 69.5, 69.75, 70.125, 71.375, 72.125, 73.0, 76.625, 77.0, 79.5, 79.875, 80.25, 80.5, 80.875, 81.25, 81.625, 82.0, 83.75, 84.125, 84.375, 84.75, 89.375, 89.75, 91.125, 92.125, 93.25, 94.875, 95.25, 96.0, 97.25, 98.75, 99.875, 101.625, 103.375, 103.75, 104.5, 105.875, 108.125, 110.875, 113.75, 114.625, 118.5, 121.0, 121.75, 122.375, 123.875, 125.0, 125.75, 126.125, 127.625, 128.0, 128.375, 129.75, 131.125, 134.25, 134.75, 134.875, 135.5, 137.5, 138.875, 140.375, 141.25, 143.5, 145.625, 146.0, 146.375, 146.75, 151.375, 151.75, 152.125, 152.375, 155.5, 155.875, 157.875, 159.125, 159.5, 160.375, 162.0, 162.625, 163.625, 164.75, 165.0, 165.875, 166.75, 167.375, 167.75, 168.5, 170.25, 171.25, 171.875, 173.375, 174.0, 174.375, 174.875, 175.375, 176.0, 177.875, 178.375, 179.5, 179.875, 180.875, 181.25, 182.25, 183.125, 185.375, 186.125, 186.625, 188.0, 189.0, 189.375, 189.75, 192.0, 195.125, 195.5, 195.875, 200.5, 200.75, 201.125, 201.5, 203.0, 203.875, 205.25, 206.0, 208.5, 210.375, 211.75, 214.5, 216.0, 217.875, 218.375, 220.125, 222.25, 223.0, 223.625, 224.75, 226.125, 227.75, 229.25, 229.875, 230.875, 231.0, 231.625, 231.75, 232.5, 232.75, 234.875, 236.625, 238.0, 238.25, 238.75, 239.5, 240.875, 242.125, 243.75, 245.375, 245.75, 246.875, 247.25, 247.625, 247.875, 251.125, 251.375, 251.75, 252.125, 254.0, 254.375, 254.75, 255.125, 255.625, 256.0, 256.375, 258.125, 258.5, 258.875, 259.125, 262.25, 262.75, 263.0, 263.375, 263.75, 265.125, 265.5, 265.875, 266.25, 266.5, 268.0, 268.375, 268.625, 269.0, 270.125, 270.75, 271.5, 273.625, 275.125, 276.375, 277.125, 279.25]: #Line 3
                            OBJECTS3 = pygame.Rect(round(WIDTH * 0.6 + 10), 0, 80, 80)
                            LINE3.append(OBJECTS3)
                        if timer in [16.5, 18.0, 19.75, 20.375, 20.75, 21.875, 24.0, 25.0, 26.375, 27.5, 28.5, 30.625, 32.75, 33.125, 33.5, 35.5, 35.875, 38.375, 38.75, 41.125, 42.25, 45.375, 46.25, 48.25, 51.0, 52.75, 53.5, 54.25, 55.0, 56.625, 57.5, 58.0, 60.875, 61.5, 61.75, 62.25, 66.125, 67.625, 68.5, 70.75, 71.375, 72.5, 73.625, 74.0, 74.25, 74.875, 78.125, 78.375, 78.75, 79.125, 82.25, 82.625, 83.0, 83.25, 83.875, 84.25, 84.625, 84.875, 86.625, 87.0, 87.25, 87.625, 88.0, 88.375, 91.125, 92.5, 93.25, 94.25, 96.0, 96.75, 97.75, 98.125, 98.75, 99.5, 99.875, 102.5, 104.75, 105.875, 107.25, 110.375, 111.5, 112.875, 115.75, 116.625, 119.375, 121.75, 122.5, 123.125, 124.375, 124.625, 125.75, 126.125, 127.125, 128.75, 129.125, 129.25, 130.25, 130.5, 132.25, 134.25, 134.75, 134.875, 136.0, 138.25, 138.375, 139.25, 140.0, 140.875, 141.875, 142.375, 145.75, 146.125, 146.5, 146.875, 147.125, 147.625, 147.875, 148.25, 148.625, 149.0, 149.25, 149.625, 150.0, 150.375, 150.75, 151.0, 152.75, 153.125, 153.375, 153.75, 154.125, 154.5, 154.75, 155.125, 156.875, 158.375, 159.0, 159.25, 159.875, 161.75, 162.5, 163.125, 164.25, 165.375, 166.375, 168.125, 169.5, 171.0, 171.5, 172.25, 173.875, 174.125, 174.625, 175.0, 175.625, 177.375, 178.25, 180.25, 180.5, 181.625, 181.875, 182.625, 183.625, 185.625, 186.375, 187.0, 188.5, 190.125, 190.5, 193.375, 193.625, 195.125, 195.5, 195.875, 198.625, 203.875, 204.625, 207.125, 210.0, 212.75, 215.125, 217.0, 217.25, 217.875, 218.375, 223.0, 223.625, 225.375, 227.0, 227.375, 228.25, 228.875, 230.5, 233.5, 234.25, 236.0, 237.125, 237.375, 238.0, 238.25, 240.125, 241.75, 242.5, 242.75, 243.0, 246.125, 246.5, 248.25, 248.625, 248.875, 249.25, 249.625, 250.0, 250.375, 250.75, 251.125, 251.5, 251.75, 252.125, 252.5, 252.875, 253.125, 253.5, 253.875, 254.25, 254.625, 254.875, 255.25, 259.5, 259.875, 260.25, 260.625, 260.875, 261.25, 261.625, 262.0, 264.125, 264.5, 264.75, 266.875, 267.25, 267.625, 269.375, 270.125, 271.5, 272.25, 273.625, 274.375, 275.75, 277.125, 277.875, 279.25, 280.5]: #Line 4
                            OBJECTS4 = pygame.Rect(round(WIDTH * 0.8 + 10), 0, 80, 80)
                            LINE4.append(OBJECTS4)
                    if not HOMESCREEN and not wait and game3:                                                                   #Game3 spawner
                        timer += 0.125
                        timer = round(timer,3)
                        if timer in [17.125, 17.375, 18.625, 19.0, 19.375, 19.75, 20.25, 20.5, 21.0, 21.25, 21.75, 22.125, 22.625, 22.875, 23.25, 23.5, 23.625, 24.125, 24.5, 25.75, 26.0, 26.625, 26.875, 27.25, 27.625, 28.125, 28.5, 29.75, 30.0, 30.5, 30.75, 31.25, 31.5, 32.0, 32.375, 32.875, 33.125, 33.625, 33.875, 35.875, 36.125, 36.375, 36.75, 37.125, 37.5, 37.875, 38.375, 38.75, 39.125, 40.625, 41.0, 41.375, 41.875, 42.375, 43.5, 44.875, 45.75, 47.5, 48.25, 50.0, 51.625, 53.375, 54.125, 55.0, 55.75, 57.25, 57.875, 59.625, 60.875, 62.0, 62.375, 63.25, 64.75, 67.125, 67.625, 67.875, 68.375, 68.75, 69.875, 70.625, 71.125, 71.875, 72.625, 73.0, 73.375, 74.25, 74.625, 75.0, 75.75, 76.625, 77.0, 77.375, 77.75, 78.125, 78.5, 78.875, 79.375, 80.125, 80.5, 80.875, 81.25, 82.125, 82.5, 83.25, 84.375, 86.375, 86.75, 87.125, 88.0, 88.75, 89.125, 90.0, 91.5, 92.375, 93.25, 94.375, 94.75, 95.5, 96.25, 97.0, 97.625, 98.375, 99.0, 99.25, 99.75, 101.125, 101.5, 101.875, 102.625, 103.25, 103.875, 105.125, 105.625, 106.5, 107.375, 107.875, 109.0, 109.75, 110.375, 111.125, 111.625, 111.875, 112.375, 113.625, 114.375, 116.125, 117.0, 117.75, 118.375]: #Line 1
                            OBJECTS1 = pygame.Rect(round(WIDTH * 0.2 + 10), 0, 80, 80)
                            LINE1.append(OBJECTS1)
                        if timer in [17.875, 18.25, 20.0, 21.75, 22.125, 23.5, 23.625, 24.875, 25.25, 27.25, 27.625, 28.875, 29.25, 30.5, 30.75, 32.0, 32.375, 34.375, 34.75, 35.125, 35.5, 36.125, 36.375, 38.375, 38.75, 39.25, 39.5, 41.375, 41.875, 43.125, 44.25, 45.25, 46.625, 47.875, 49.375, 50.5, 51.0, 52.625, 54.5, 56.125, 57.75, 59.25, 60.5, 62.875, 64.0, 65.5, 66.0, 66.75, 68.0, 69.125, 70.625, 71.5, 72.25, 73.875, 74.25, 74.625, 75.375, 76.125, 78.125, 78.5, 78.875, 79.625, 80.875, 81.75, 82.875, 83.625, 85.25, 86.0, 86.75, 87.625, 88.375, 89.5, 90.375, 91.875, 93.625, 94.625, 95.25, 95.375, 95.875, 96.625, 97.25, 98.125, 98.625, 99.5, 100.375, 101.125, 101.625, 102.25, 103.0, 103.625, 104.5, 105.375, 106.375, 106.875, 107.5, 108.125, 108.5, 108.75, 109.375, 110.0, 110.25, 110.625, 111.5, 112.125, 113.125, 113.375, 113.875, 114.625, 115.125, 115.375, 115.75, 116.75, 117.375, 119.125]: #Line 2
                            OBJECTS2 = pygame.Rect(round(WIDTH * 0.4 + 10), 0, 80, 80)
                            LINE2.append(OBJECTS2)
                        if timer in [17.125, 17.375, 19.375, 19.75, 21.0, 21.25, 22.625, 22.875, 24.125, 24.5, 25.75, 26.0, 26.5, 27.25, 27.625, 28.875, 29.25, 29.75, 30.0, 31.25, 31.25, 32.75, 33.625, 33.875, 35.125, 35.5, 36.125, 36.375, 37.5, 37.875, 39.125, 39.875, 40.25, 42.25, 43.375, 44.125, 45.125, 47.0, 48.0, 48.875, 50.375, 51.375, 53.75, 55.375, 56.25, 57.5, 58.25, 60.0, 61.0, 63.625, 65.125, 67.625, 67.875, 68.75, 69.5, 70.375, 71.125, 71.5, 72.25, 73.0, 73.375, 74.25, 74.625, 75.375, 76.125, 77.0, 77.375, 77.75, 78.5, 78.875, 80.125, 80.5, 80.875, 81.75, 82.5, 83.75, 84.75, 85.25, 86.0, 86.75, 87.625, 88.375, 90.0, 90.75, 91.125, 93.0, 93.75, 94.5, 94.875, 95.5, 96.0, 96.5, 97.125, 97.375, 98.25, 98.75, 99.125, 99.375, 99.875, 100.375, 101.0, 101.5, 101.75, 102.5, 103.125, 103.75, 104.875, 105.5, 105.875, 106.0, 106.75, 107.5, 107.875, 108.875, 109.5, 110.625, 111.25, 112.125, 112.875, 113.625, 114.5, 115.375, 115.75, 116.0, 116.875, 117.625, 118.75]: #Line 3
                            OBJECTS3 = pygame.Rect(round(WIDTH * 0.6 + 10), 0, 80, 80)
                            LINE3.append(OBJECTS3)
                        if timer in [17.125, 17.375, 18.625, 19.0, 20.25, 20.5, 21.0, 21.25, 21.75, 22.125, 22.625, 22.875, 23.5, 23.625, 24.875, 25.25, 25.75, 26.0, 26.625, 26.875, 28.125, 28.5, 28.875, 29.25, 29.625, 30.5, 30.75, 31.25, 31.5, 32.0, 32.375, 32.875, 33.125, 34.375, 34.75, 35.125, 35.5, 36.75, 37.125, 38.375, 38.75, 39.25, 39.5, 41.375, 41.875, 42.75, 43.75, 44.75, 46.125, 48.5, 49.75, 52.125, 53.0, 56.0, 56.75, 56.875, 58.75, 60.625, 61.625, 64.25, 66.375, 67.625, 67.875, 69.125, 69.875, 70.625, 71.5, 71.875, 72.625, 73.0, 73.375, 73.875, 75.0, 75.75, 76.625, 77.75, 78.125, 78.5, 78.875, 79.375, 79.75, 80.125, 80.5, 81.25, 81.75, 82.125, 83.25, 84.0, 84.375, 85.625, 86.0, 86.375, 87.125, 87.625, 88.0, 89.125, 90.375, 90.75, 91.125, 92.625, 92.875, 93.5, 93.875, 94.125, 94.625, 95.75, 96.25, 96.625, 96.875, 97.375, 97.875, 98.0, 98.5, 99.625, 100.0, 100.125, 100.625, 100.875, 101.25, 102.125, 102.75, 103.375, 104.0, 104.25, 105.375, 105.75, 106.5, 107.0, 107.25, 107.625, 109.125, 109.875, 110.5, 110.75, 111.0, 112.0, 112.375, 113.625, 114.0, 114.25, 114.75, 115.0, 116.25, 116.5, 117.25, 118.0, 119.5]: #Line 4
                            OBJECTS4 = pygame.Rect(round(WIDTH * 0.8 + 10), 0, 80, 80)
                            LINE4.append(OBJECTS4)
                                                        #Alle Funktionen die passieren wenn man ein Element trifft
            if event.type == HIT:               
                MULTIPLIER += 1
                SCORE += 1 * MULTIPLIER
                HIT_counter += 1
                if LIFES < 100:
                    LIFES += 2

                LIFES_counter -= 1
                ELEMENT_counter += 1

                if countHit == 1:
                    mixer.Channel(0).set_volume(MUSIK_LAUTSTARKE)               #Hit Sounds
                    mixer.Channel(0).play(mixer.Sound("music/HitSound.mp3"))
                    countHit = 2
                elif countHit == 2:
                    mixer.Channel(1).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(1).play(mixer.Sound("music/HitSound.mp3"))
                    countHit = 3
                elif countHit == 3:
                    mixer.Channel(2).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(2).play(mixer.Sound("music/HitSound.mp3"))
                    countHit = 4
                elif countHit == 4:
                    mixer.Channel(3).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(3).play(mixer.Sound("music/HitSound.mp3"))
                    countHit = 1

            if MISS_check > 0:
                MISS_check -= 1
                                                                #Alle Funktionen die passieren wenn man vertrifft
            if event.type == MISS:          
                MULTIPLIER = 1
                MISS_check = 2
                if LIFES_counter <= 0:
                    LIFES_MULTI = 2
                else:
                    LIFES_MULTI *= 2
                LIFES -= 1 * LIFES_MULTI                                                                                                                                                                           
                LIFES_counter = 3
                ELEMENT_counter += 1

                if countMiss == 1:
                    mixer.Channel(4).set_volume(MUSIK_LAUTSTARKE)               #Miss Sounds
                    mixer.Channel(4).play(mixer.Sound("music/MissSound.wav"))
                    countMiss = 2
                elif countMiss == 2:
                    mixer.Channel(5).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(5).play(mixer.Sound("music/MissSound.wav"))
                    countMiss = 3
                elif countMiss == 3:
                    mixer.Channel(6).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(6).play(mixer.Sound("music/MissSound.wav"))
                    countMiss = 4
                elif countMiss == 4:
                    mixer.Channel(7).set_volume(MUSIK_LAUTSTARKE)
                    mixer.Channel(7).play(mixer.Sound("music/MissSound.wav"))
                    countMiss = 1

        keys_pressed = pygame.key.get_pressed()

                                                                                         #Mein Level ersteller
        """
        #cnt = 1.375
        #cnt = 0.875
        cnt = 0.625
        if keys_pressed[pygame.K_v] and generator1check:                                        
            generator1check = False
            a = (timer - cnt)
            test1.append(a)
            print("LINE 1 = ")
            print(test1)
        if not keys_pressed[pygame.K_v]:
             generator1check = True
        if keys_pressed[pygame.K_b] and generator2check:
            generator2check = False
            b = (timer - cnt)
            test2.append(b)
            print("LINE 2 = ")
            print(test2)
        if not keys_pressed[pygame.K_b]:
            generator2check = True
        if keys_pressed[pygame.K_n] and generator3check:
            generator3check = False
            c = (timer - cnt)
            test3.append(c)
            print("LINE3 : ")
            print(test3)
        if not keys_pressed[pygame.K_n]:
            generator3check = True
        if keys_pressed[pygame.K_m] and generator4check:
            generator4check = False
            d = (timer - cnt)
            test4.append(d)
            print("LINE 4 :")
            print(test4)
        if not keys_pressed[pygame.K_m]:
            generator4check = True
        """
                                                                                        #FADE SCREEN (Übergabg von Pause ins Spiel)
        if fade:                                                                                            
            if keys_pressed[pygame.K_ESCAPE] and pause_check == True:       
                pause_check = False
                fade = False
                transparency_check = True
            if not keys_pressed[pygame.K_ESCAPE]:
                pause_check = True

            fade_count += 1
            if fade_count == 1:
                game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, game, MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)
                WIN.blit(GAME_3, GAME_1_rect)
            elif fade_count == 60:
                game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, game, MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)
                WIN.blit(GAME_2, GAME_1_rect)
            elif fade_count == 120:
                game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, game, MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)
                WIN.blit(GAME_1, GAME_1_rect)
            
            if fade_count >= 180:
                wait = False
                fade = False
                fade_count = 0
                transparency_check = True
                mixer.music.unpause()
            
            pygame.display.update()
                                                                                             #DEATH SCREEN  
        elif death:                                                                                                        
            overtake_music(OVERTAKE_DEATH, MUSIK_LAUTSTARKE,"FiestaDeGuerra.mp3")
            OVERTAKE_DEATH = False

            death_draw(transparency_check)
            transparency_check = False

            if MUSIC_UP_BUTTON.draw():      #Buttons für die Lautstärke Regelung
                MUSIK_LAUTSTARKE += 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_DOWN_BUTTON.draw():      
                MUSIK_LAUTSTARKE -= 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_SYMBOL_BUTTON.draw():
                MUSIK_LAUTSTARKE = 0.1
                mixer.music.set_volume(MUSIK_LAUTSTARKE)

            if PAUSE_HOME_BUTTON.draw():        #Homebutton
                death = False
                HOMESCREEN = True
                homescreen_check = True
                game1 = False
                game2 = False
                game3 = False
                OVERTAKE_HOMESCREEN = True
            if PAUSE_RETRY_BUTTON.draw():       #Retry button
                death = False
                MULTIPLIER = 1
                SCORE = 0
                piechart = 0
                piechartnum = 0
                OVERTAKE_GAME = True
                timer = 0                                                                                         
                LINE1 = []
                LINE2 = []
                LINE3 = []
                LINE4 = []
                transparency_check = True
                LIFES = 100
                LIFES_MULTI = 1
                LIFES_counter = 0
                HIT_counter = 0
                ELEMENT_counter = 0
                                                                                             #WIN SCREEN
        elif won:                                
            WON_FINISH = False                                      #Score Zähler
            if WON_SCORE < SCORE - 10000:
                WON_SCORE += 9999
            elif WON_SCORE < SCORE - 1000:
                WON_SCORE += 99
            elif WON_SCORE < SCORE - 100:
                WON_SCORE += 19
            elif WON_SCORE < SCORE - 10:
                WON_SCORE += 4
            elif WON_SCORE < SCORE:
                WON_SCORE += 1
            else: 
                WON_FINISH = True
            
            overtake_music(OVERTAKE_HOMESCREEN, MUSIK_LAUTSTARKE, "MISTER.mp3")
            OVERTAKE_HOMESCREEN = False
            won_draw(WON_SCORE, HIT_counter, ELEMENT_counter, WON_FINISH)

            if MUSIC_UP_BUTTON.draw():
                MUSIK_LAUTSTARKE += 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_DOWN_BUTTON.draw():      
                MUSIK_LAUTSTARKE -= 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_SYMBOL_BUTTON.draw():
                MUSIK_LAUTSTARKE = 0.1
                mixer.music.set_volume(MUSIK_LAUTSTARKE)

            if WON_FINISH:
                if PAUSE_HOME_BUTTON.draw():
                    won = False
                    HOMESCREEN = True
                    homescreen_check = True
                    game1 = False
                    game2 = False
                    game3 = False
                    WON_SCORE = 0
                if PAUSE_RETRY_BUTTON.draw():
                    won = False
                    MULTIPLIER = 1
                    SCORE = 0
                    piechart = 0
                    piechartnum = 0
                    OVERTAKE_GAME = True
                    timer = 0                                                                                         
                    LINE1 = []
                    LINE2 = []
                    LINE3 = []
                    LINE4 = []
                    transparency_check = True
                    LIFES = 100
                    LIFES_MULTI = 1
                    LIFES_counter = 0
                    HIT_counter = 0
                    ELEMENT_counter = 0
                    WON_SCORE = 0
                                                                                    #WAIT SCREEN
        elif wait:                          
            mixer.music.pause()

            pause_draw(transparency_check)
            transparency_check = False
            
            if MUSIC_UP_BUTTON.draw():      #Buttons für die Lautstärke Regelung
                MUSIK_LAUTSTARKE += 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_DOWN_BUTTON.draw():      
                MUSIK_LAUTSTARKE -= 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_SYMBOL_BUTTON.draw():
                MUSIK_LAUTSTARKE = 0.1
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
                
            if PAUSE_HOME_BUTTON.draw():
                wait = False
                HOMESCREEN = True
                homescreen_check = True
                game1 = False
                game2 = False
                game3 = False
                OVERTAKE_HOMESCREEN = True
            if PAUSE_CONTINUE_BUTTON.draw():        #Continue button
                if timer > 17:
                    fade = True
                    fade_count = 0
                else:
                    wait = False
                    pause_check = False
                    transparency_check = True
                    mixer.music.unpause()

            if PAUSE_RETRY_BUTTON.draw():
                wait = False
                MULTIPLIER = 1
                SCORE = 0
                piechart = 0
                piechartnum = 0
                OVERTAKE_GAME = True
                timer = 0                                                                                         
                LINE1 = []
                LINE2 = []
                LINE3 = []
                LINE4 = []
                transparency_check = True
                LIFES = 100
                LIFES_MULTI = 1
                LIFES_counter = 0
                HIT_counter = 0
                ELEMENT_counter = 0

            elif  keys_pressed[pygame.K_ESCAPE] and pause_check == True:        #Macht den fade falls Escape nochmal gedrückt wird
                if timer > 17:
                    pause_check = False
                    fade = True
                    fade_count = 0
                else:
                    wait = False
                    pause_check = False
                    transparency_check = True
                    mixer.music.unpause()

            if not keys_pressed[pygame.K_ESCAPE]:
                pause_check = True
                                                                                                    #HOME SCREEN
        elif HOMESCREEN:        
            overtake_music(OVERTAKE_HOMESCREEN, MUSIK_LAUTSTARKE, "MISTER.mp3")
            OVERTAKE_HOMESCREEN = False
            homescreen_draw(homescreen_check)
            if homescreen_check:
                homescreen_check = False

            if HOMESCREEN_SPECIALIST_PLAY_BUTTON.draw():        #Input ob Game1 gestartet wird
                HOMESCREEN = False
                mixer.music.stop()
                OVERTAKE_GAME = True
                timer = 0
                LINE1 = []
                LINE2 = []
                LINE3 = []
                LINE4 = []
                game1 = True
                game = "game1"
                transparency_check = True
                LIFES = 100
                LIFES_MULTI = 1
                LIFES_counter = 0
                MULTIPLIER = 1
                SCORE = 0
                piechart = 0
                piechartnum = 0
                HIT_counter = 0
                ELEMENT_counter = 0
            if HOMESCREEN_GODONLYKNOWS_PLAY_BUTTON.draw():      #Input ob Game2 gestartet wird
                HOMESCREEN = False
                mixer.music.stop()
                OVERTAKE_GAME = True
                timer = 0                                                                                         
                LINE1 = []
                LINE2 = []
                LINE3 = []
                LINE4 = []
                game2 = True
                game = "game2"
                transparency_check = True
                LIFES = 100
                LIFES_MULTI = 1
                LIFES_counter = 0
                MULTIPLIER = 1
                SCORE = 0
                piechart = 0
                piechartnum = 0
                HIT_counter = 0
                ELEMENT_counter = 0
            if HOMESCREEN_INFESTATION_PLAY_BUTTON.draw():       #Input ob Game3 gestartet wird
                HOMESCREEN = False
                mixer.music.stop()
                OVERTAKE_GAME = True
                timer = 0                                                                                         
                LINE1 = []
                LINE2 = []
                LINE3 = []
                LINE4 = []
                game3 = True
                game = "game3"
                transparency_check = True
                LIFES = 100
                LIFES_MULTI = 1
                LIFES_counter = 0
                MULTIPLIER = 1
                SCORE = 0
                piechart = 0
                piechartnum = 0
                HIT_counter = 0
                ELEMENT_counter = 0
            
            if MUSIC_UP_BUTTON.draw():      #Buttons für die Lautstärke Regelung
                MUSIK_LAUTSTARKE += 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_DOWN_BUTTON.draw():      
                MUSIK_LAUTSTARKE -= 0.02
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            if MUSIC_SYMBOL_BUTTON.draw():
                MUSIK_LAUTSTARKE = 0.1
                mixer.music.set_volume(MUSIK_LAUTSTARKE)
            

                                                                                                   #GAME1 SCREEN
        elif game1:    
            if keys_pressed[pygame.K_ESCAPE] and pause_check == True:       #Ob Pause gedrückt wird
                wait = True
                pause_check = False
            if not keys_pressed[pygame.K_ESCAPE]:
                pause_check = True
            
            overtake_music(OVERTAKE_GAME,MUSIK_LAUTSTARKE, "Persona_4_Specialist.mp3")
            OVERTAKE_GAME = False

            game_handle_lines(LINE1,LINE2,LINE3,LINE4, keys_pressed, CHECK1,CHECK2,CHECK3,CHECK4, VEL)      #Elemente verarbeiten
            if keys_pressed[pygame.K_v]: CHECK1 = False
            else: CHECK1 = True
            if keys_pressed[pygame.K_b]: CHECK2 = False
            else: CHECK2 = True
            if keys_pressed[pygame.K_n]: CHECK3 = False
            else: CHECK3 = True
            if keys_pressed[pygame.K_m]: CHECK4 = False
            else: CHECK4 = True
            
            if keys_pressed[pygame.K_e] and timer < 14:     #Skip Funktion
                timer = 14
                mixer.music.set_pos(14)

            if piechartnum >= 139:                      #Anzeige wie weit man im spiel (piechart)
                piechart = 2 * math.pi
                piechartnum = 1000
                won = True
                OVERTAKE_HOMESCREEN = True
                transparency_check = True
            elif timer >= piechartnum:
                piechart += 1/50 * math.pi
                piechartnum += 1/100 * 139

            game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, "game1", MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)

            if LIFES <= 0:          #Tod Funktion
                death = True
                OVERTAKE_DEATH = True
                                                                                                    #GAME2 SCREEN
        elif game2:    
            if keys_pressed[pygame.K_ESCAPE] and pause_check == True:
                wait = True
                pause_check = False
            if not keys_pressed[pygame.K_ESCAPE]:
                pause_check = True

            overtake_music(OVERTAKE_GAME,MUSIK_LAUTSTARKE,"God_only_knows.mp3")
            OVERTAKE_GAME = False

            game_handle_lines(LINE1,LINE2,LINE3,LINE4, keys_pressed, CHECK1,CHECK2,CHECK3,CHECK4, VEL)
            if keys_pressed[pygame.K_v]: CHECK1 = False
            else: CHECK1 = True
            if keys_pressed[pygame.K_b]: CHECK2 = False
            else: CHECK2 = True
            if keys_pressed[pygame.K_n]: CHECK3 = False
            else: CHECK3 = True
            if keys_pressed[pygame.K_m]: CHECK4 = False
            else: CHECK4 = True

            if keys_pressed[pygame.K_e] and timer < 14:
                timer = 270
                mixer.music.set_pos(14)

            if piechartnum >= 285:
                piechart = 2 * math.pi
                piechartnum = 1000
                won = True
                OVERTAKE_HOMESCREEN = True
                transparency_check = True
            elif timer >= piechartnum:
                piechart += 1/50 * math.pi
                piechartnum += 1/100 * 285

            game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, "game2", MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)

            if LIFES <= 0:
                death = True
                OVERTAKE_DEATH = True
                                                                                                   #GAME3 SCREEN
        elif game3:                                                                                                
            if keys_pressed[pygame.K_ESCAPE] and pause_check == True:
                wait = True
                pause_check = False
                VEL = 15
            if not keys_pressed[pygame.K_ESCAPE]:
                pause_check = True
                VEL = 20 

            overtake_music(OVERTAKE_GAME,MUSIK_LAUTSTARKE, "Infestation.mp3")
            OVERTAKE_GAME = False

            game_handle_lines(LINE1,LINE2,LINE3,LINE4, keys_pressed, CHECK1,CHECK2,CHECK3,CHECK4, VEL)
            if keys_pressed[pygame.K_v]: CHECK1 = False
            else: CHECK1 = True
            if keys_pressed[pygame.K_b]: CHECK2 = False
            else: CHECK2 = True
            if keys_pressed[pygame.K_n]: CHECK3 = False
            else: CHECK3 = True
            if keys_pressed[pygame.K_m]: CHECK4 = False
            else: CHECK4 = True

            if keys_pressed[pygame.K_e] and timer < 14:
                timer = 14
                mixer.music.set_pos(14)

            if piechartnum >= 125:
                piechart = 2 * math.pi
                piechartnum = 1000
                won = True
                OVERTAKE_HOMESCREEN = True
                transparency_check = True
            elif timer >= piechartnum:
                piechart += 1/50 * math.pi
                piechartnum += 1/100 * 125

            game_draw(keys_pressed, LINE1,LINE2,LINE3,LINE4, MULTIPLIER, SCORE, timer, "game3", MISS_check, LIFES, HIT_counter, ELEMENT_counter, piechart)

            if LIFES <= 0:
                VEL = 15
                death = True
                OVERTAKE_DEATH = True
            
    """print("----------------------------") #Level ersteller Output
    print("LINE 1 = ")
    print(test1)
    print("LINE 2 = ")
    print(test2)
    print("LINE 3 = ")
    print(test3)
    print("LINE 4 = ")
    print(test4)"""

    pygame.quit()
if __name__ == "__main__":
    main()