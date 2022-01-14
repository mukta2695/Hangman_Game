import pygame
import math
import random

pygame.init()

#SETUP DISPLAY
WIDTH, HEIGHT= 800, 500
#Pygame accepts the input in the form of a tupple. therefore a tupple is passed
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HANGMAN!")

#Colors
WHITE=(255,255,255)
BLACK=(0,0,0)

#BUTTON VARIABLES
RADIUS=20
GAP_SIZE=15
letters=[]
A=65
x_start=round((WIDTH-(RADIUS*2+GAP_SIZE)*13)/2)
y_start=400

for i in range(26):
  x= x_start+GAP_SIZE*2+((RADIUS*2+GAP_SIZE)*(i%13))
  y= y_start+((i//13)*(RADIUS*2+GAP_SIZE))
  letters.append([x,y,chr(A+i), True])

#FONTS 
Letter_font=pygame.font.SysFont('comicsans',40)
Word_font=pygame.font.SysFont('comicsans',45)

#LOAD IMAGES
images=[]
for i in range(7):
  image=pygame.image.load("hangman"+str(i)+".png")  
  images.append(image)

#print(images)
def generate_word(file):
    f=open(file)
    word_list=[]
    for word in f:
        word_list.append(word.split())
    word=random.choice(word_list)[0]
    return word.upper()




def draw(word,guessed,hangman_status):
  window.fill(WHITE)
  #Draw image

  display_word=""
  for letter in word:
    if letter in guessed:
      display_word+=letter+ " "
    else:
      display_word+="_ "

  text=Word_font.render(display_word,1,BLACK) #.render is used to create an image of the text
  window.blit(text, (400, 200))
  for letter in letters:
    x,y,l,visible=letter
    if visible:
      pygame.draw.circle(window,BLACK, (x,y), RADIUS,3)
      text=Letter_font.render(l,1,BLACK)
      window.blit(text,(x-text.get_width()/2, y-text.get_height()/2))

  window.blit(images[hangman_status],(150,100))
  pygame.display.update()

def display_msg(message,won,word):
    pygame.time.delay(1000) #Wait 1 second
    window.fill(WHITE)
    text=Word_font.render(message,1,BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

    if not won:
      pygame.time.delay(1000) #Wait 2 seconds
      window.fill(WHITE)
      text=Word_font.render("The correct word was "+word+"!",1,BLACK)
      window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(3000)


def main():
  #GAME VARIABLES
  hangman_status=0
  word=""
  word=generate_word("words.txt")
  guessed=[]

  #SETUP GAME LOOP
  #Frames per seconds
  FPS=60 #Maximum and const fps
  clock=pygame.time.Clock()
  run=True
  


  while run == True:
    draw(word,guessed,hangman_status)
    clock.tick(FPS) # To make sure that the while loop runs at the FPS speed
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        run= False
      elif event.type==pygame.MOUSEBUTTONDOWN:
        x_position, y_position=pygame.mouse.get_pos() 
        for letter in letters:
          x,y,l,visible=letter 
          if visible:
            distance=math.sqrt((x-x_position)**2 +(y-y_position)**2)

            if distance<RADIUS:
              #print(l)
              letter[3]=False
              guessed.append(l)
              if l not in word:
                hangman_status+=1
        #Get the co-ordinates of the mouse
        #print(position) #top left is 0,0

    
    won=True
    for letter in word:
      if letter not in guessed:
        won=False
        break
    if won:
      display_msg("YOU WON!",won,word)
      break
    if hangman_status==6:
      display_msg("YOU LOST!",won,word)
      break
  
main()
'''
repeat=True
while repeat: 
  pygame.time.delay(1000) #Wait 1 second
  window.fill(WHITE)
  text=Word_font.render("Do you want to play again?",1,BLACK)
  window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/4 - text.get_height()/4))
  options=["YES","NO"]
  cw=1.5
  w=3.1
  RADIUS1=50
  for option in options:
    pygame.draw.circle(window,BLACK, (WIDTH/cw - text.get_width()/cw, HEIGHT/2 - text.get_height()/2), RADIUS1,3)
    text=Word_font.render(option,1,BLACK)
    window.blit(text,(WIDTH/w - text.get_width()/w, HEIGHT/2.1 - text.get_height()/2.1))
    w-=1.5

  clock=pygame.time.Clock()
  clock.tick(60)
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
      x_pos, y_pos=pygame.mouse.get_pos() 
      for option in options:
        dis=math.sqrt(((WIDTH/cw - text.get_width()/cw)-x_pos)**2 +((HEIGHT/2 - text.get_height()/2)-y_pos)**2)

        if dis<RADIUS1:
          if option == "YES":
            main()
          else:
            repeat=False
'''



  
pygame.display.update()
pygame.time.delay(3000)
  
pygame.quit()
