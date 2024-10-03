import pygame
import math
import sys
from pygame.locals import*
from pygame import mixer
import pygame as py 

py.init() 
pygame.init()
mixer.init()

#variables

run=True
start= True
game= False
end=True

credit=False
# leveles or modes

# counting
counting=[False,False,False,False,False,False,False,False,False,False]

#  alphabets

alphabets=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

# colors
color_names=[False,False,False,False,False,False,False,False,False,False]

# fruit names
fruit_names=[False,False,False,False,False,False,False,False,False,False]

# clock
clock=pygame.time.Clock()

# font

font=pygame.font.SysFont(None,35)
arsh=font.render('V1PASH',True,(0,0,255))
arsh.set_alpha(60)

#screen info
# full_size= [pygame.display.Info().current_w,pygame.display.Info().current_h]

# width=1000
# height=400

width=pygame.display.Info().current_w

height=pygame.display.Info().current_h

full_size=[width,height]

window=pygame.display.set_mode((full_size),pygame.RESIZABLE)

pygame.display.set_caption("Brainstorm ideas & ways")

print(full_size)

pygame_icon = pygame.image.load('asset/logo.png')
pygame.display.set_icon(pygame_icon)

# assets

# buttons
play= pygame.image.load("asset/play_button.png")
play=pygame.transform.scale(play,(width/7.68,height/5.08))
playimg= play.get_rect()
playimg.center=(width/2,height/1.8)

home=pygame.image.load("asset/home.png")
home=pygame.transform.scale(home,(width/21.94,height/12.34))
home_img=home.get_rect()
home_img.center=(width/17,height/18)

quit=pygame.image.load("asset/close.png")
quit=pygame.transform.scale(quit,(width/21.94,height/12.34))
quitimg=quit.get_rect()
quitimg.topright=(width,height/35)

credits=pygame.image.load("asset/credit.png")
credits=pygame.transform.scale(credits,(width/5.12,height/5.76))
credit_img=credits.get_rect()
credit_img.center=(width/2,height/1.2)

back_button=pygame.image.load("asset/back.png")
back_button=pygame.transform.scale(back_button,(width/21.94,height/12.34))
back_button_image=back_button.get_rect()
back_button_image.center=(width/17,height/18)

next_button=pygame.image.load("asset/next.png")
next_button=pygame.transform.scale(next_button,(width/7.68,height/9.6))
next_button_image=back_button.get_rect()
next_button_image.center=(width/1.462,height/1.393)

previous_button=pygame.image.load("asset/previous.png")
previous_button=pygame.transform.scale(previous_button,(width/7.68,height/9.6))
previous_button_image=previous_button.get_rect()
previous_button_image.center=(width/4.571,height/1.393)


audio_button=pygame.image.load("asset/audio.png")
audio_button=pygame.transform.scale(audio_button,(width/7.68,height/5.76))
audio_button_image=audio_button.get_rect()
audio_button_image.center=(width/2,height/1.393)

# cursor image
curser=pygame.image.load("asset/curser.png")
curser=pygame.transform.scale(curser,(width/17.066,height/10.8))
curser_image=curser.get_rect()
pygame.mouse.set_visible(False)

# start background
backgroundimg= pygame.image.load("asset/start_bg.jpg")
backgroundimg=pygame.transform.scale(backgroundimg,(width,height))
background=backgroundimg.get_rect()
background.center=(width/2,height/2)

title=pygame.image.load("asset/title.png")
title=pygame.transform.scale(title,(width/1.706,height/4.32))
title_img=title.get_rect()
title_img.center=(width/2,height/4)

# modes

alpha=pygame.image.load("asset/modes/alphabets/alphabets.png")
alpha=pygame.transform.scale(alpha,(width/3.84,height/4.32))
alpha_img=alpha.get_rect()
alpha_img.center=(width/2.9,height/3.5)

count=pygame.image.load("asset/modes/counting/count.png")
count=pygame.transform.scale(count,(width/3.84,height/4.32))
count_img=count.get_rect()
count_img.center=(width/1.536,height/3.5)

color=pygame.image.load("asset/modes/color/color.png")
color=pygame.transform.scale(color,(width/3.84,height/4.32))
color_img=color.get_rect()
color_img.center=(width/2.9,height/1.570)

fruit=pygame.image.load("asset/modes/fruit/fruit.png")
fruit=pygame.transform.scale(fruit,(width/3.84,height/4.32))
fruit_img=color.get_rect()
fruit_img.center=(width/1.536,height/1.570)

# game screen img

game_bg=pygame.image.load("asset/game_bg.jpg")
game_bg=pygame.transform.scale(game_bg,(width,height))
game_bg_img=game_bg.get_rect()
game_bg_img.center=(width/2,height/2)

# credits

name=pygame.image.load("asset/credit/credit.png")
name=pygame.transform.scale(name,(width/1.92,height/1.329))
name_img=name.get_rect()
name_img.center=(width/2,height/2)

# counting

one=pygame.image.load("asset/modes/counting/images/1.png")
one=pygame.transform.scale(one,(width/3.072,height/1.728))
one_i=one.get_rect()
one_i.center=(width/2,height/3)


two=pygame.image.load("asset/modes/counting/images/2.png")
two=pygame.transform.scale(two,(width/3.072,height/1.728))
two_i=two.get_rect()
two_i.center=(width/2,height/3)

three=pygame.image.load("asset/modes/counting/images/3.png")
three=pygame.transform.scale(three,(width/3.072,height/1.728))
three_i=three.get_rect()
three_i.center=(width/2,height/3)

four=pygame.image.load("asset/modes/counting/images/4.png")
four=pygame.transform.scale(four,(width/3.072,height/1.728))
four_i=four.get_rect()
four_i.center=(width/2,height/3)

five=pygame.image.load("asset/modes/counting/images/5.png")
five=pygame.transform.scale(five,(width/3.072,height/1.728))
five_i=five.get_rect()
five_i.center=(width/2,height/3)

six=pygame.image.load("asset/modes/counting/images/6.png")
six=pygame.transform.scale(six,(width/3.072,height/1.728))
six_i=six.get_rect()
six_i.center=(width/2,height/3)

seven=pygame.image.load("asset/modes/counting/images/7.png")
seven=pygame.transform.scale(seven,(width/3.072,height/1.728))
seven_i=seven.get_rect()
seven_i.center=(width/2,height/3)

eight=pygame.image.load("asset/modes/counting/images/8.png")
eight=pygame.transform.scale(eight,(width/3.072,height/1.728))
eight_i=eight.get_rect()
eight_i.center=(width/2,height/3)

nine=pygame.image.load("asset/modes/counting/images/9.png")
nine=pygame.transform.scale(nine,(width/3.072,height/1.728))
nine_i=nine.get_rect()
nine_i.center=(width/2,height/3)

ten=pygame.image.load("asset/modes/counting/images/10.png")
ten=pygame.transform.scale(ten,(width/3.072,height/1.728))
ten_i=ten.get_rect()
ten_i.center=(width/2,height/3)


# alphabets
a=pygame.image.load("asset/modes/alphabets/images/a.png")
a=pygame.transform.scale(a,(width/3.072,height/1.728))
a_i=a.get_rect()
a_i.center=(width/2,height/3)

b=pygame.image.load("asset/modes/alphabets/images/b.png")
b=pygame.transform.scale(b,(width/3.072,height/1.728))
b_i=b.get_rect()
b_i.center=(width/2,height/3)

c=pygame.image.load("asset/modes/alphabets/images/c.png")
c=pygame.transform.scale(c,(width/3.072,height/1.728))
c_i=c.get_rect()
c_i.center=(width/2,height/3)

d=pygame.image.load("asset/modes/alphabets/images/d.png")
d=pygame.transform.scale(d,(width/3.072,height/1.728))
d_i=c.get_rect()
d_i.center=(width/2,height/3)

e=pygame.image.load("asset/modes/alphabets/images/e.png")
e=pygame.transform.scale(e,(width/3.072,height/1.728))
e_i=e.get_rect()
e_i.center=(width/2,height/3)

f=pygame.image.load("asset/modes/alphabets/images/f.png")
f=pygame.transform.scale(f,(width/3.072,height/1.728))
f_i=f.get_rect()
f_i.center=(width/2,height/3)

g=pygame.image.load("asset/modes/alphabets/images/g.png")
g=pygame.transform.scale(g,(width/3.072,height/1.728))
g_i=g.get_rect()
g_i.center=(width/2,height/3)

h=pygame.image.load("asset/modes/alphabets/images/h.png")
h=pygame.transform.scale(h,(width/3.072,height/1.728))
h_i=h.get_rect()
h_i.center=(width/2,height/3)

iss=pygame.image.load("asset/modes/alphabets/images/i.png")
iss=pygame.transform.scale(iss,(width/3.072,height/1.728))
i_i=iss.get_rect()
i_i.center=(width/2,height/3)

j=pygame.image.load("asset/modes/alphabets/images/j.png")
j=pygame.transform.scale(j,(width/3.072,height/1.728))
j_i=j.get_rect()
j_i.center=(width/2,height/3)

k=pygame.image.load("asset/modes/alphabets/images/k.png")
k=pygame.transform.scale(k,(width/3.072,height/1.728))
k_i=k.get_rect()
k_i.center=(width/2,height/3)

l=pygame.image.load("asset/modes/alphabets/images/l.png")
l=pygame.transform.scale(l,(width/3.072,height/1.728))
l_i=l.get_rect()
l_i.center=(width/2,height/3)

m=pygame.image.load("asset/modes/alphabets/images/m.png")
m=pygame.transform.scale(m,(width/3.072,height/1.728))
m_i=m.get_rect()
m_i.center=(width/2,height/3)

n=pygame.image.load("asset/modes/alphabets/images/n.png")
n=pygame.transform.scale(n,(width/3.072,height/1.728))
n_i=n.get_rect()
n_i.center=(width/2,height/3)

o=pygame.image.load("asset/modes/alphabets/images/o.png")
o=pygame.transform.scale(o,(width/3.072,height/1.728))
o_i=o.get_rect()
o_i.center=(width/2,height/3)

p=pygame.image.load("asset/modes/alphabets/images/p.png")
p=pygame.transform.scale(p,(width/3.072,height/1.728))
p_i=p.get_rect()
p_i.center=(width/2,height/3)

q=pygame.image.load("asset/modes/alphabets/images/q.png")
q=pygame.transform.scale(q,(width/3.072,height/1.728))
q_i=q.get_rect()
q_i.center=(width/2,height/3)

r=pygame.image.load("asset/modes/alphabets/images/r.png")
r=pygame.transform.scale(r,(width/3.072,height/1.728))
r_i=r.get_rect()
r_i.center=(width/2,height/3)

s=pygame.image.load("asset/modes/alphabets/images/s.png")
s=pygame.transform.scale(s,(width/3.072,height/1.728))
s_i=s.get_rect()
s_i.center=(width/2,height/3)

t=pygame.image.load("asset/modes/alphabets/images/t.png")
t=pygame.transform.scale(t,(width/3.072,height/1.728))
t_i=t.get_rect()
t_i.center=(width/2,height/3)

u=pygame.image.load("asset/modes/alphabets/images/u.png")
u=pygame.transform.scale(u,(width/3.072,height/1.728))
u_i=u.get_rect()
u_i.center=(width/2,height/3)

v=pygame.image.load("asset/modes/alphabets/images/v.png")
v=pygame.transform.scale(v,(width/3.072,height/1.728))
v_i=v.get_rect()
v_i.center=(width/2,height/3)

w=pygame.image.load("asset/modes/alphabets/images/w.png")
w=pygame.transform.scale(w,(width/3.072,height/1.728))
w_i=w.get_rect()
w_i.center=(width/2,height/3)

x=pygame.image.load("asset/modes/alphabets/images/x.png")
x=pygame.transform.scale(x,(width/3.072,height/1.728))
x_i=x.get_rect()
x_i.center=(width/2,height/3)

y=pygame.image.load("asset/modes/alphabets/images/y.png")
y=pygame.transform.scale(y,(width/3.072,height/1.728))
y_i=y.get_rect()
y_i.center=(width/2,height/3)

z=pygame.image.load("asset/modes/alphabets/images/z.png")
z=pygame.transform.scale(z,(width/3.072,height/1.728))
z_i=z.get_rect()
z_i.center=(width/2,height/3)

# colours name

red=pygame.image.load("asset/modes/color/images/red.jpg")
red=pygame.transform.scale(red,(width/3.072,height/1.728))
red_i=red.get_rect()
red_i.center=(width/2,height/3)

blue=pygame.image.load("asset/modes/color/images/blue.jpg")
blue=pygame.transform.scale(blue,(width/3.072,height/1.728))
blue_i=blue.get_rect()
blue_i.center=(width/2,height/3)

black=pygame.image.load("asset/modes/color/images/black.jpg")
black=pygame.transform.scale(black,(width/3.072,height/1.728))
black_i=black.get_rect()
black_i.center=(width/2,height/3)

brown=pygame.image.load("asset/modes/color/images/brown.jpg")
brown=pygame.transform.scale(brown,(width/3.072,height/1.728))
brown_i=brown.get_rect()
brown_i.center=(width/2,height/3)

green=pygame.image.load("asset/modes/color/images/green.jpg")
green=pygame.transform.scale(green,(width/3.072,height/1.728))
green_i=green.get_rect()
green_i.center=(width/2,height/3)

grey=pygame.image.load("asset/modes/color/images/grey.jpg")
grey=pygame.transform.scale(grey,(width/3.072,height/1.728))
grey_i=grey.get_rect()
grey_i.center=(width/2,height/3)

orange=pygame.image.load("asset/modes/color/images/orange.jpg")
orange=pygame.transform.scale(orange,(width/3.072,height/1.728))
orange_i=orange.get_rect()
orange_i.center=(width/2,height/3)

pink=pygame.image.load("asset/modes/color/images/pink.jpg")
pink=pygame.transform.scale(pink,(width/3.072,height/1.728))
pink_i=pink.get_rect()
pink_i.center=(width/2,height/3)

purple=pygame.image.load("asset/modes/color/images/purple.jpg")
purple=pygame.transform.scale(purple,(width/3.072,height/1.728))
purple_i=purple.get_rect()
purple_i.center=(width/2,height/3)

yellow=pygame.image.load("asset/modes/color/images/yellow.jpg")
yellow=pygame.transform.scale(yellow,(width/3.072,height/1.728))
yellow_i=yellow.get_rect()
yellow_i.center=(width/2,height/3)

# fruits name
apple=pygame.image.load("asset/modes/fruit/images/apple.png")
apple=pygame.transform.scale(apple,(width/3.072,height/1.728))
apple_i=apple.get_rect()
apple_i.center=(width/2,height/3)

banana=pygame.image.load("asset/modes/fruit/images/banana.png")
banana=pygame.transform.scale(banana,(width/3.072,height/1.728))
banana_i=banana.get_rect()
banana_i.center=(width/2,height/3)

cherry=pygame.image.load("asset/modes/fruit/images/cherry.png")
cherry=pygame.transform.scale(cherry,(width/3.072,height/1.728))
cherry_i=cherry.get_rect()
cherry_i.center=(width/2,height/3)

kiwi=pygame.image.load("asset/modes/fruit/images/kiwi.png")
kiwi=pygame.transform.scale(kiwi,(width/3.072,height/1.728))
kiwi_i=kiwi.get_rect()
kiwi_i.center=(width/2,height/3)

mango=pygame.image.load("asset/modes/fruit/images/mango.png")
mango=pygame.transform.scale(mango,(width/3.072,height/1.728))
mango_i=mango.get_rect()
mango_i.center=(width/2,height/3)

orangef=pygame.image.load("asset/modes/fruit/images/orange.png")
orangef=pygame.transform.scale(orangef,(width/3.072,height/1.728))
orangef_i=orangef.get_rect()
orangef_i.center=(width/2,height/3)

pear=pygame.image.load("asset/modes/fruit/images/pear.png")
pear=pygame.transform.scale(pear,(width/3.072,height/1.728))
pear_i=pear.get_rect()
pear_i.center=(width/2,height/3)

pineapple=pygame.image.load("asset/modes/fruit/images/pineapple.png")
pineapple=pygame.transform.scale(pineapple,(width/3.072,height/1.728))
pineapple_i=pineapple.get_rect()
pineapple_i.center=(width/2,height/3)

strawberry=pygame.image.load("asset/modes/fruit/images/strawberry.png")
strawberry=pygame.transform.scale(strawberry,(width/3.072,height/1.728))
strawberry_i=strawberry.get_rect()
strawberry_i.center=(width/2,height/3)

watermelon=pygame.image.load("asset/modes/fruit/images/watermelon.png")
watermelon=pygame.transform.scale(watermelon,(width/3.072,height/1.728))
watermelon_i=watermelon.get_rect()
watermelon_i.center=(width/2,height/3)

# scroll

scroll=0

FrameHeight = pygame.display.Info().current_h
FrameWidth = pygame.display.Info().current_w

tiles = math.ceil(FrameWidth / backgroundimg.get_width()) + 1
    
if start:
 mixer.music.load("asset/start.wav")
 mixer.music.play()
 
      
while run:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
        if event.type==KEYDOWN and event.key in[K_ESCAPE]:
            run=False
            
# start screen
    while start:
        mouse=pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                start=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                start=False
                run=False
# play button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.27<= mouse[0] <=width/1.78 and  height/2.17 <= mouse[1]<height/1.54:
                    game=True
                    start=False
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()
                    start=False
                    run=False
# credit button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.481<= mouse[0] <=width/1.676  and  height/1.339 <= mouse[1]<=height/1.09:
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()            
                    credit=True
                    start=False
            
        i = 0
        while(i < tiles): 
            window.blit(backgroundimg, (backgroundimg.get_width()*i 
                                        + scroll, 0)) 
            i += 1
    # FRAME FOR SCROLLING 
        scroll -= 2
  
    # RESET THE SCROLL FRAME 
        if abs(scroll) > backgroundimg.get_width(): 
            scroll = 0
                
        clock.tick(120)
        window.blit(play,playimg)
        window.blit(quit,quitimg)
        window.blit(title,title_img)
        window.blit(credits,credit_img)
        window.blit(arsh,(width/1.080,height/1.04))
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()
        
# game screen
    while game:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == QUIT:
                game=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                game=False
                run=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    game=False
                    run=False  
# back button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    start=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    game=False
                    
# counting mode button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.835<= mouse[0] <=width/1.317   and   height/4.721<= mouse[1]<=height/2.823:
                    counting[0]=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()
                    mixer.music.load("asset/modes/counting/audio/one.mp3")
                    mixer.music.play()
                    game=False            
# alphabets mode button
            if event.type==MOUSEBUTTONDOWN:
                if width/4.208<= mouse[0] <=width/2.21  and   height/4.721<= mouse[1]<=height/2.823:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()     
                    game=False
                    
# colors mode button
            if event.type==MOUSEBUTTONDOWN:
                if width/4.208<= mouse[0] <=width/2.21  and   height/1.77<= mouse[1]<=height/1.423:
                    color_names[0]=True
                    mixer.music.load("asset/modes/color/audio/red.mp3")
                    mixer.music.play()   
                    game=False
                    
# fruits mode button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.835<= mouse[0] <=width/1.317  and   height/1.77<= mouse[1]<=height/1.423:
                    fruit_names[0]=True
                    mixer.music.load("asset/modes/fruit/audio/apple.mp3")
                    mixer.music.play()       
                    game=False

        
        window.blit(game_bg,game_bg_img)
        window.blit(alpha,alpha_img)
        window.blit(count,count_img)
        window.blit(color,color_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(fruit,fruit_img)
        window.blit(back_button,back_button_image)
        window.blit(quit,quitimg)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

# counting game screen
    while counting[0]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[0]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[0]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[0]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[0]=False
                    run=False 
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/one.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP1]:
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[1]=True
                    mixer.music.load("asset/modes/counting/audio/two.mp3")
                    mixer.music.play()
                    counting[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[0]=False
# skip screen
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[0]=False
                
            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[0]=False

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[0]=False         

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[0]=False 

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[0]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[0]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[0]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[0]=False
                
# till here skip screen             
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(one,one_i)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[1]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[1]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[1]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[1]=False
# audio button           
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/two.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP2]:
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[1]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[2]=True
                    mixer.music.load("asset/modes/counting/audio/three.mp3")
                    mixer.music.play()
                    counting[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[1]=False
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[0]=True
                    mixer.music.load("asset/modes/counting/audio/one.mp3")
                    mixer.music.play()
                    counting[1]=False


            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[0]=True
                    mixer.music.load("asset/modes/counting/audio/one.mp3")
                    mixer.music.play()
                    counting[1]=False
# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[1]=False
                
            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[1]=False

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[1]=False         

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[1]=False 

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[1]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[1]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[1]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[1]=False
                
# till here skip screen             
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        window.blit(two,two_i)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[2]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[2]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[2]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[2]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[2]=False
                    run=False 
# audio button           
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/three.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP3]:
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[3]=True
                    mixer.music.load("asset/modes/counting/audio/four.mp3")
                    mixer.music.play()
                    counting[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[3]=True
                    mixer.music.load("asset/modes/counting/audio/four.mp3")
                    mixer.music.play()
                    counting[2]=False
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[1]=True
                    mixer.music.load("asset/modes/counting/audio/two.mp3")
                    mixer.music.play()
                    counting[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[1]=True
                    mixer.music.load("asset/modes/counting/audio/two.mp3")
                    mixer.music.play()
                    counting[2]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[2]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[2]=False

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[2]=False         

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[2]=False 

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[2]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[2]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[2]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[2]=False
                
# till here skip screen             
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        window.blit(next_button,next_button_image)
        window.blit(three,three_i)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[3]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[3]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[3]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[3]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[3]=False
                    run=False 
# audio button           
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/four.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP4]:
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[4]=True
                    mixer.music.load("asset/modes/counting/audio/five.mp3")
                    mixer.music.play()
                    counting[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[4]=True
                    mixer.music.load("asset/modes/counting/audio/five.mp3")
                    mixer.music.play()
                    counting[3]=False
# previous button 
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[2]=True
                    mixer.music.load("asset/modes/counting/audio/three.mp3")
                    mixer.music.play()
                    counting[3]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[2]=True
                    mixer.music.load("asset/modes/counting/audio/three.mp3")
                    mixer.music.play()
                    counting[3]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[3]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[3]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[3]=False         

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[3]=False 

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[3]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[3]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[3]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[3]=False
                
# till here skip screen       
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(four,four_i)
        window.blit(audio_button,audio_button_image)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[4]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[4]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[4]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[4]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[4]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[5]=True
                    mixer.music.load("asset/modes/counting/audio/six.mp3")
                    mixer.music.play()
                    counting[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[5]=True
                    mixer.music.load("asset/modes/counting/audio/six.mp3")
                    mixer.music.play()
                    counting[4]=False
# audio button           
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/five.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP5]:
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[3]=True
                    mixer.music.load("asset/modes/counting/audio/four.mp3")
                    mixer.music.play()
                    counting[4]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[3]=True
                    mixer.music.load("asset/modes/counting/audio/four.mp3")
                    mixer.music.play()
                    counting[4]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[4]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[4]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[4]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[4]=False 

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[4]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[4]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[4]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[4]=False
                
# till here skip screen
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(five,five_i)
        window.blit(audio_button,audio_button_image)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[5]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[5]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[5]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[5]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[5]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[6]=True
                    mixer.music.load("asset/modes/counting/audio/seven.mp3")
                    mixer.music.play()
                    counting[5]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[6]=True
                    mixer.music.load("asset/modes/counting/audio/seven.mp3")
                    mixer.music.play()
                    counting[5]=False

# audio button           
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/six.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP6]:
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[4]=True
                    mixer.music.load("asset/modes/counting/audio/five.mp3")
                    mixer.music.play()
                    counting[5]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[4]=True
                    mixer.music.load("asset/modes/counting/audio/five.mp3")
                    mixer.music.play()
                    counting[5]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[5]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[5]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[5]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[5]=False 

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[5]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[5]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[5]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[5]=False
                
# till here skip screen
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(six,six_i)
        window.blit(audio_button,audio_button_image)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[6]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[6]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[6]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[6]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[6]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[7]=True
                    mixer.music.load("asset/modes/counting/audio/eight.mp3")
                    mixer.music.play()
                    counting[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[7]=True
                    mixer.music.load("asset/modes/counting/audio/eight.mp3")
                    mixer.music.play()
                    counting[6]=False
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/seven.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP7]:
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[5]=True
                    mixer.music.load("asset/modes/counting/audio/six.mp3")
                    mixer.music.play()
                    counting[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[5]=True
                    mixer.music.load("asset/modes/counting/audio/six.mp3")
                    mixer.music.play()
                    counting[6]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[6]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[6]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[6]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[6]=False 

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[6]=False

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[6]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[6]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[6]=False
                
# till here skip screen

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        window.blit(seven,seven_i)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[7]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[7]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[7]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[7]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[7]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[8]=True
                    mixer.music.load("asset/modes/counting/audio/nine.mp3")
                    mixer.music.play()
                    counting[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[8]=True
                    mixer.music.load("asset/modes/counting/audio/nine.mp3")
                    mixer.music.play()
                    counting[7]=False
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/eight.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP8]:
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[6]=True
                    mixer.music.load("asset/modes/counting/audio/seven.mp3")
                    mixer.music.play()
                    counting[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[6]=True
                    mixer.music.load("asset/modes/counting/audio/seven.mp3")
                    mixer.music.play()
                    counting[7]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[7]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[7]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[7]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[7]=False 

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[7]=False

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[7]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[7]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[7]=False
                
# till here skip screen
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        window.blit(eight,eight_i)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[8]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[8]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[8]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[8]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[8]=False
                    run=False 
# next button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    counting[9]=True
                    mixer.music.load("asset/modes/counting/audio/ten.mp3")
                    mixer.music.play()
                    counting[8]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    counting[9]=True
                    mixer.music.load("asset/modes/counting/audio/ten.mp3")
                    mixer.music.play()
                    counting[8]=False
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/nine.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE,K_KP9]:
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[7]=True
                    mixer.music.load("asset/modes/counting/audio/eight.mp3")
                    mixer.music.play()
                    counting[8]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[7]=True
                    mixer.music.load("asset/modes/counting/audio/eight.mp3")
                    mixer.music.play()
                    counting[8]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[8]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[8]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[8]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[8]=False 

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[8]=False

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[8]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[8]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[8]=False
                
# till here skip screen
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(previous_button,previous_button_image)
        window.blit(nine,nine_i)
        window.blit(audio_button,audio_button_image)
        window.blit(next_button,next_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while counting[9]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                counting[9]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                counting[9]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    counting[9]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    counting[9]=False
                    run=False 
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/counting/audio/ten.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/counting/audio/ten.mp3")
                mixer.music.play()
                
# previous button
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    counting[8]=True
                    mixer.music.load("asset/modes/counting/audio/nine.mp3")
                    mixer.music.play()
                    counting[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    counting[8]=True
                    mixer.music.load("asset/modes/counting/audio/nine.mp3")
                    mixer.music.play()
                    counting[9]=False
# skip screen
            if event.type==KEYDOWN and event.key in[K_KP1]:
                counting[0]=True
                mixer.music.load("asset/modes/counting/audio/one.mp3")
                mixer.music.play()
                counting[9]=False
                
            if event.type==KEYDOWN and event.key in[K_KP2]:
                counting[1]=True
                mixer.music.load("asset/modes/counting/audio/two.mp3")
                mixer.music.play()
                counting[9]=False

            if event.type==KEYDOWN and event.key in[K_KP3]:
                counting[2]=True
                mixer.music.load("asset/modes/counting/audio/three.mp3")
                mixer.music.play()
                counting[9]=False         

            if event.type==KEYDOWN and event.key in[K_KP4]:
                counting[3]=True
                mixer.music.load("asset/modes/counting/audio/four.mp3")
                mixer.music.play()
                counting[9]=False 

            if event.type==KEYDOWN and event.key in[K_KP5]:
                counting[4]=True
                mixer.music.load("asset/modes/counting/audio/five.mp3")
                mixer.music.play()
                counting[9]=False

            if event.type==KEYDOWN and event.key in[K_KP6]:
                counting[5]=True
                mixer.music.load("asset/modes/counting/audio/six.mp3")
                mixer.music.play()
                counting[9]=False

            if event.type==KEYDOWN and event.key in[K_KP7]:
                counting[6]=True
                mixer.music.load("asset/modes/counting/audio/seven.mp3")
                mixer.music.play()
                counting[9]=False

            if event.type==KEYDOWN and event.key in[K_KP8]:
                counting[7]=True
                mixer.music.load("asset/modes/counting/audio/eight.mp3")
                mixer.music.play()
                counting[9]=False

            if event.type==KEYDOWN and event.key in[K_KP9]:
                counting[8]=True
                mixer.music.load("asset/modes/counting/audio/nine.mp3")
                mixer.music.play()
                counting[9]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(audio_button,audio_button_image)
        window.blit(ten,ten_i)
        window.blit(previous_button,previous_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

# alphabets
    while alphabets[0]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[0]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[0]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[0]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[0]=False
                    run=False 
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_a]:
                mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[0]=False
        
# skip screen
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[0]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[0]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[0]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[0]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[0]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[0]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[0]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[0]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[0]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[0]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[0]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[0]=False    
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(a,a_i)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[1]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[1]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[1]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[1]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[1]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_b]:
                mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[1]=False
# skip screen
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[1]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[1]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[1]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[1]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[1]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[1]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[1]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[1]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[1]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[1]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[1]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[1]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[1]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(b,b_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()
        
    while alphabets[2]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[2]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[2]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[2]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[2]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_c]:
                mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[2]=False

# skip
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[2]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[2]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[2]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[2]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[2]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[2]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[2]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[2]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[2]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[2]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[2]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[2]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[2]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[2]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(c,c_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[3]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[3]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[3]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[3]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[3]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_d]:
                mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[3]=False
# skip screen
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[3]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[3]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[3]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[3]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[3]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[3]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[3]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[3]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[3]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[3]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[3]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[3]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[3]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[3]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(d,d_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[4]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[4]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[4]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[4]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[4]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_e]:
                mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[4]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[1]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[4]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[4]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[4]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[4]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[4]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[4]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[4]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[4]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[4]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[4]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[4]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[4]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[4]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[4]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(e,e_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[5]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[5]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[5]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[5]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[5]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_f]:
                mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[5]=False

# skip screen
            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[0]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[5]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[5]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[5]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[5]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[5]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[5]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[5]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[5]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[5]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[5]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[5]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[5]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[5]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(f,f_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[6]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[6]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[6]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[6]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[6]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_g]:
                mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[6]=False
# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[6]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[6]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[6]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[6]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[6]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[6]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[6]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[6]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[6]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[6]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[6]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[6]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[6]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[6]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(g,g_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[7]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[7]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[7]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[7]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[7]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_h]:
                mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[7]=False
# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[7]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[0]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[7]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[7]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[7]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[7]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[7]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[7]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[7]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[7]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[7]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[7]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[7]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[7]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(h,h_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[8]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[8]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[8]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[8]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[8]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_i]:
                mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[8]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[8]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[8]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[0]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[8]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[8]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[8]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[8]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[8]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[8]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[8]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[8]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[8]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[8]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[8]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(iss,i_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[9]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[9]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[9]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[9]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[9]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_j]:
                mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[9]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[9]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[9]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[9]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[9]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[9]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[9]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[9]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[9]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[9]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[9]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[9]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[9]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[9]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[9]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(j,j_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[10]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[10]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[10]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[10]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[10]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_k]:
                mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[10]=False
# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[10]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[10]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[10]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[0]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[10]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[10]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[10]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[10]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[10]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[10]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[10]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[10]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[10]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[10]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(k,k_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[11]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[11]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[11]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[11]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[11]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_l]:
                mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[11]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[11]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[11]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[11]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[11]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[11]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[11]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[11]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[11]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[11]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[11]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[11]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[11]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[11]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[11]=False
                
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(l,l_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[12]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[12]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[12]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[12]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[12]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_m]:
                mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[12]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[12]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[12]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[12]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[12]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[0]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[12]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[12]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[12]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[12]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[12]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[12]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[12]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[12]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[12]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(m,m_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[13]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[13]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[13]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[13]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[13]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_n]:
                mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[13]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[13]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[13]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[13]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[13]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[13]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[0]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[13]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[13]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[13]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[13]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[13]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[13]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[13]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[13]=False
       
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(n,n_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[14]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[14]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[14]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[14]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[14]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_o]:
                mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[14]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[14]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[14]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[14]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[14]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[14]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[14]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[0]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[14]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[14]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[14]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[14]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[14]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[14]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[14]=False
       
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(o,o_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[15]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[15]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[15]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[15]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[15]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_p]:
                mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[15]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[15]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[15]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[15]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[15]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[15]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[15]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[15]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[15]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[15]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[15]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[15]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[15]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[15]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[15]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(p,p_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[16]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[16]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[16]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[16]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[16]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_q]:
                mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[16]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[16]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[16]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[16]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[16]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[16]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[16]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[16]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[16]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[0]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[16]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[16]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[16]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[16]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[16]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[16]=False
                
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(q,q_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[17]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[17]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[17]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[17]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[17]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_r]:
                mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[17]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[17]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[17]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[17]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[17]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[17]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[17]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[17]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[17]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[17]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[17]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[17]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[17]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[17]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[17]=False
   
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(r,r_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[18]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[18]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[18]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[18]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[18]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_s]:
                mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[19]=True
                    mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[19]=True
                    mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                    mixer.music.play()
                    alphabets[18]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[18]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[18]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[18]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[18]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[18]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[18]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[18]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[18]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[0]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[18]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[18]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[18]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[18]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[18]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(s,s_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[19]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[19]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[19]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[19]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[19]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_t]:
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[20]=True
                    mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[20]=True
                    mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                    mixer.music.play()
                    alphabets[19]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[19]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[19]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[19]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[19]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[19]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[19]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[19]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[19]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[19]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[19]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[19]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[19]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[19]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[19]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(t,t_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[20]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[20]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[20]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[20]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[20]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[19]=True
                    mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                    mixer.music.play()
                    alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[19]=True
                    mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_u]:
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[21]=True
                    mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[21]=True
                    mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                    mixer.music.play()
                    alphabets[20]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[20]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[20]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[20]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[20]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[20]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[20]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[20]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[20]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[20]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[0]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[20]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[20]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[20]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[20]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(u,u_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[21]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[21]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[21]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[21]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[21]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[20]=True
                    mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                    mixer.music.play()
                    alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[20]=True
                    mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_v]:
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[22]=True
                    mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[22]=True
                    mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                    mixer.music.play()
                    alphabets[21]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[21]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[21]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[21]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[21]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[21]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[21]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[21]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[21]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[21]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[21]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[21]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[21]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[21]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[21]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(v,v_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[22]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[22]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[22]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[22]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[22]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[21]=True
                    mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                    mixer.music.play()
                    alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[21]=True
                    mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_w]:
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[23]=True
                    mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[23]=True
                    mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                    mixer.music.play()
                    alphabets[22]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[22]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[22]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[22]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[22]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[22]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[22]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[22]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[22]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[22]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[22]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[0]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[22]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[22]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[22]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(w,w_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[23]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[23]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[23]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[23]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[23]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[22]=True
                    mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                    mixer.music.play()
                    alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[22]=True
                    mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_x]:
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[24]=True
                    mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[24]=True
                    mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                    mixer.music.play()
                    alphabets[23]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[23]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[23]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[23]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[23]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[23]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[23]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[23]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[23]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[23]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[23]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[23]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[0]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[23]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[23]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(x,x_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[24]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[24]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[24]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[24]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[24]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[23]=True
                    mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                    mixer.music.play()
                    alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[23]=True
                    mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_y]:
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    alphabets[25]=True
                    mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    alphabets[25]=True
                    mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                    mixer.music.play()
                    alphabets[24]=False

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[24]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[24]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[24]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[24]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[24]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[24]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[24]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[24]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[24]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[24]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[24]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[24]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[24]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[0]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[24]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(next_button,next_button_image)
        window.blit(y,y_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while alphabets[25]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                alphabets[25]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                alphabets[25]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    alphabets[25]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    alphabets[25]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    alphabets[24]=True
                    mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                    mixer.music.play()
                    alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    alphabets[24]=True
                    mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()

            if event.type==KEYDOWN and event.key in[K_z]:
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()

# skip screen

            if event.type==KEYDOWN and event.key in[K_a]:
                    alphabets[0]=True
                    mixer.music.load("asset/modes/alphabets/audio/a.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_b]:
                    alphabets[1]=True
                    mixer.music.load("asset/modes/alphabets/audio/b.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_c]:
                    alphabets[2]=True
                    mixer.music.load("asset/modes/alphabets/audio/c.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_d]:
                    alphabets[3]=True
                    mixer.music.load("asset/modes/alphabets/audio/d.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_e]:
                    alphabets[4]=True
                    mixer.music.load("asset/modes/alphabets/audio/e.mp3")
                    mixer.music.play()
                    alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_f]:
                    alphabets[5]=True
                    mixer.music.load("asset/modes/alphabets/audio/f.mp3")
                    mixer.music.play()
                    alphabets[25]=False
 
            if event.type==KEYDOWN and event.key in[K_g]:
                    alphabets[6]=True
                    mixer.music.load("asset/modes/alphabets/audio/g.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_h]:
                    alphabets[7]=True
                    mixer.music.load("asset/modes/alphabets/audio/h.mp3")
                    mixer.music.play()
                    alphabets[25]=False         

            if event.type==KEYDOWN and event.key in[K_i]:
                    alphabets[8]=True
                    mixer.music.load("asset/modes/alphabets/audio/i.mp3")
                    mixer.music.play()
                    alphabets[25]=False     

            if event.type==KEYDOWN and event.key in[K_j]:
                    alphabets[9]=True
                    mixer.music.load("asset/modes/alphabets/audio/j.mp3")
                    mixer.music.play()
                    alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_k]:
                    alphabets[10]=True
                    mixer.music.load("asset/modes/alphabets/audio/k.mp3")
                    mixer.music.play()
                    alphabets[25]=False     
                                    
            if event.type==KEYDOWN and event.key in[K_l]:
                    alphabets[11]=True
                    mixer.music.load("asset/modes/alphabets/audio/l.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_m]:
                    alphabets[12]=True
                    mixer.music.load("asset/modes/alphabets/audio/m.mp3")
                    mixer.music.play()
                    alphabets[25]=False    
    
            if event.type==KEYDOWN and event.key in[K_n]:
                    alphabets[13]=True
                    mixer.music.load("asset/modes/alphabets/audio/n.mp3")
                    mixer.music.play()
                    alphabets[25]=False 

            if event.type==KEYDOWN and event.key in[K_o]:
                    alphabets[14]=True
                    mixer.music.load("asset/modes/alphabets/audio/o.mp3")
                    mixer.music.play()
                    alphabets[25]=False   

            if event.type==KEYDOWN and event.key in[K_p]:
                    alphabets[15]=True
                    mixer.music.load("asset/modes/alphabets/audio/p.mp3")
                    mixer.music.play()
                    alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_q]:
                    alphabets[16]=True
                    mixer.music.load("asset/modes/alphabets/audio/q.mp3")
                    mixer.music.play()
                    alphabets[25]=False
                    
            if event.type==KEYDOWN and event.key in[K_r]:
                    alphabets[17]=True
                    mixer.music.load("asset/modes/alphabets/audio/r.mp3")
                    mixer.music.play()
                    alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_s]:
                    alphabets[18]=True
                    mixer.music.load("asset/modes/alphabets/audio/s.mp3")
                    mixer.music.play()
                    alphabets[25]=False 
                    
            if event.type==KEYDOWN and event.key in[K_t]:
                alphabets[19]=True
                mixer.music.load("asset/modes/alphabets/audio/t.mp3")
                mixer.music.play()
                alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_u]:
                alphabets[20]=True
                mixer.music.load("asset/modes/alphabets/audio/u.mp3")
                mixer.music.play()
                alphabets[25]=False
                
            if event.type==KEYDOWN and event.key in[K_v]:
                alphabets[21]=True
                mixer.music.load("asset/modes/alphabets/audio/v.mp3")
                mixer.music.play()
                alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_w]:
                alphabets[22]=True
                mixer.music.load("asset/modes/alphabets/audio/w.mp3")
                mixer.music.play()
                alphabets[25]=False     

            if event.type==KEYDOWN and event.key in[K_x]:
                alphabets[23]=True
                mixer.music.load("asset/modes/alphabets/audio/x.mp3")
                mixer.music.play()
                alphabets[25]=False 

            if event.type==KEYDOWN and event.key in[K_y]:
                alphabets[24]=True
                mixer.music.load("asset/modes/alphabets/audio/y.mp3")
                mixer.music.play()
                alphabets[25]=False

            if event.type==KEYDOWN and event.key in[K_z]:
                alphabets[25]=True
                mixer.music.load("asset/modes/alphabets/audio/z.mp3")
                mixer.music.play()
                alphabets[0]=False

        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(z,z_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

# fruit names
    while fruit_names[0]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[0]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[0]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[0]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[0]=False
                    run=False 
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/apple.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/apple.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[1]=True
                    mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                    mixer.music.play()
                    fruit_names[0]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[1]=True
                    mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                    mixer.music.play()
                    fruit_names[0]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(apple,apple_i)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()
        
    while fruit_names[1]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[1]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[1]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[1]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[1]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[0]=True
                    mixer.music.load("asset/modes/fruit/audio/apple.mp3")
                    mixer.music.play()
                    fruit_names[1]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[0]=True
                    mixer.music.load("asset/modes/fruit/audio/apple.mp3")
                    mixer.music.play()
                    fruit_names[1]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[2]=True
                    mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                    mixer.music.play()
                    fruit_names[1]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[2]=True
                    mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                    mixer.music.play()
                    fruit_names[1]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(banana,banana_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[2]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[2]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[2]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[2]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[2]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[1]=True
                    mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                    mixer.music.play()
                    fruit_names[2]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[1]=True
                    mixer.music.load("asset/modes/fruit/audio/banana.mp3")
                    mixer.music.play()
                    fruit_names[2]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[3]=True
                    mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                    mixer.music.play()
                    fruit_names[2]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[3]=True
                    mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                    mixer.music.play()
                    fruit_names[2]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(cherry,cherry_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[3]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[3]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[3]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[3]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[3]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[2]=True
                    mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                    mixer.music.play()
                    fruit_names[3]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[2]=True
                    mixer.music.load("asset/modes/fruit/audio/cherry.mp3")
                    mixer.music.play()
                    fruit_names[3]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[4]=True
                    mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                    mixer.music.play()
                    fruit_names[3]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[4]=True
                    mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                    mixer.music.play()
                    fruit_names[3]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(kiwi,kiwi_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[4]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[4]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[4]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[4]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[4]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[3]=True
                    mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                    mixer.music.play()
                    fruit_names[4]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[3]=True
                    mixer.music.load("asset/modes/fruit/audio/kiwi.mp3")
                    mixer.music.play()
                    fruit_names[4]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[5]=True
                    mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                    mixer.music.play()
                    fruit_names[4]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[5]=True
                    mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                    mixer.music.play()
                    fruit_names[4]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(mango,mango_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[5]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[5]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[5]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[5]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[5]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[4]=True
                    mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                    mixer.music.play()
                    fruit_names[5]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[4]=True
                    mixer.music.load("asset/modes/fruit/audio/mango.mp3")
                    mixer.music.play()
                    fruit_names[5]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[6]=True
                    mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                    mixer.music.play()
                    fruit_names[5]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[6]=True
                    mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                    mixer.music.play()
                    fruit_names[5]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(orangef,orangef_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[6]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[6]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[6]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[6]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[6]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[5]=True
                    mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                    mixer.music.play()
                    fruit_names[6]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[5]=True
                    mixer.music.load("asset/modes/fruit/audio/orange.mp3")
                    mixer.music.play()
                    fruit_names[6]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[7]=True
                    mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                    mixer.music.play()
                    fruit_names[6]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[7]=True
                    mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                    mixer.music.play()
                    fruit_names[6]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(pear,pear_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[7]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[7]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[7]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[7]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[7 ]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[6]=True
                    mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                    mixer.music.play()
                    fruit_names[7]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[6]=True
                    mixer.music.load("asset/modes/fruit/audio/pear.mp3")
                    mixer.music.play()
                    fruit_names[7]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[8]=True
                    mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                    mixer.music.play()
                    fruit_names[7]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[8]=True
                    mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                    mixer.music.play()
                    fruit_names[7]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(pineapple,pineapple_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[8]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[8]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[8]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[8]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[8]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[7]=True
                    mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                    mixer.music.play()
                    fruit_names[8]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[7]=True
                    mixer.music.load("asset/modes/fruit/audio/pineapple.mp3")
                    mixer.music.play()
                    fruit_names[8]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    fruit_names[9]=True
                    mixer.music.load("asset/modes/fruit/audio/watermelon.mp3")
                    mixer.music.play()
                    fruit_names[8]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    fruit_names[9]=True
                    mixer.music.load("asset/modes/fruit/audio/watermelon.mp3")
                    mixer.music.play()
                    fruit_names[8]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(strawberry,strawberry_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while fruit_names[9]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                fruit_names[9]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                fruit_names[9]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    fruit_names[9]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    fruit_names[9]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    fruit_names[8]=True
                    mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                    mixer.music.play()
                    fruit_names[9]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    fruit_names[8]=True
                    mixer.music.load("asset/modes/fruit/audio/strawberry.mp3")
                    mixer.music.play()
                    fruit_names[9]=False                   
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/fruit/audio/watermelon.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/fruit/audio/watermelon.mp3")
                mixer.music.play()
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(watermelon,watermelon_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()
# color names
    while color_names[0]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[0]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[0]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[0]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[0]=False
                    run=False 
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/red.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/red.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[1]=True
                    mixer.music.load("asset/modes/color/audio/blue.mp3")
                    mixer.music.play()
                    color_names[0]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[1]=True
                    mixer.music.load("asset/modes/color/audio/blue.mp3")
                    mixer.music.play()
                    color_names[0]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(red,red_i)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[1]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[1]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[1]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[1]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[1]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[0]=True
                    mixer.music.load("asset/modes/color/audio/red.mp3")
                    mixer.music.play()
                    color_names[1]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[0]=True
                    mixer.music.load("asset/modes/color/audio/red.mp3")
                    mixer.music.play()
                    color_names[1]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/blue.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/blue.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[2]=True
                    mixer.music.load("asset/modes/color/audio/yellow.mp3")
                    mixer.music.play()
                    color_names[1]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[2]=True
                    mixer.music.load("asset/modes/color/audio/yellow.mp3")
                    mixer.music.play()
                    color_names[1]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(blue,blue_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[2]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[2]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[2]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[2]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[2]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[1]=True
                    mixer.music.load("asset/modes/color/audio/blue.mp3")
                    mixer.music.play()
                    color_names[2]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[1]=True
                    mixer.music.load("asset/modes/color/audio/blue.mp3")
                    mixer.music.play()
                    color_names[2]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/yellow.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/yellow.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[3]=True
                    mixer.music.load("asset/modes/color/audio/pink.mp3")
                    mixer.music.play()
                    color_names[2]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[3]=True
                    mixer.music.load("asset/modes/color/audio/pink.mp3")
                    mixer.music.play()
                    color_names[2]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(yellow,yellow_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[3]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[3]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[3]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[3]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[3]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[2]=True
                    mixer.music.load("asset/modes/color/audio/yellow.mp3")
                    mixer.music.play()
                    color_names[3]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[2]=True
                    mixer.music.load("asset/modes/color/audio/yellow.mp3")
                    mixer.music.play()
                    color_names[3]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/pink.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/pink.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[4]=True
                    mixer.music.load("asset/modes/color/audio/brown.mp3")
                    mixer.music.play()
                    color_names[3]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[4]=True
                    mixer.music.load("asset/modes/color/audio/brown.mp3")
                    mixer.music.play()
                    color_names[3]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(pink,pink_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[4]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[4]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[4]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[4]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[4]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[3]=True
                    mixer.music.load("asset/modes/color/audio/pink.mp3")
                    mixer.music.play()
                    color_names[4]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[3]=True
                    mixer.music.load("asset/modes/color/audio/pink.mp3")
                    mixer.music.play()
                    color_names[4]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/brown.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/brown.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[5]=True
                    mixer.music.load("asset/modes/color/audio/black.mp3")
                    mixer.music.play()
                    color_names[4]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[5]=True
                    mixer.music.load("asset/modes/color/audio/black.mp3")
                    mixer.music.play()
                    color_names[4]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(brown,brown_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[5]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[5]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[5]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[5]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[5]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[4]=True
                    mixer.music.load("asset/modes/color/audio/brown.mp3")
                    mixer.music.play()
                    color_names[5]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[4]=True
                    mixer.music.load("asset/modes/color/audio/brown.mp3")
                    mixer.music.play()
                    color_names[5]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/black.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/black.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[6]=True
                    mixer.music.load("asset/modes/color/audio/green.mp3")
                    mixer.music.play()
                    color_names[5]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[6]=True
                    mixer.music.load("asset/modes/color/audio/green.mp3")
                    mixer.music.play()
                    color_names[5]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(black,black_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[6]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[6]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[6]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[6]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[6]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[5]=True
                    mixer.music.load("asset/modes/color/audio/black.mp3")
                    mixer.music.play()
                    color_names[6]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[5]=True
                    mixer.music.load("asset/modes/color/audio/black.mp3")
                    mixer.music.play()
                    color_names[6]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/green.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/green.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[7]=True
                    mixer.music.load("asset/modes/color/audio/orange.mp3")
                    mixer.music.play()
                    color_names[6]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[7]=True
                    mixer.music.load("asset/modes/color/audio/orange.mp3")
                    mixer.music.play()
                    color_names[6]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(green,green_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[7]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[7]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[7]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[7]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[7]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[6]=True
                    mixer.music.load("asset/modes/color/audio/green.mp3")
                    mixer.music.play()
                    color_names[7]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[6]=True
                    mixer.music.load("asset/modes/color/audio/green.mp3")
                    mixer.music.play()
                    color_names[7]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/orange.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/orange.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[8]=True
                    mixer.music.load("asset/modes/color/audio/purple.mp3")
                    mixer.music.play()
                    color_names[7]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[8]=True
                    mixer.music.load("asset/modes/color/audio/purple.mp3")
                    mixer.music.play()
                    color_names[7]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(orange,orange_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[8]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[8]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[8]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[8]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[8]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[7]=True
                    mixer.music.load("asset/modes/color/audio/orange.mp3")
                    mixer.music.play()
                    color_names[8]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[7]=True
                    mixer.music.load("asset/modes/color/audio/orange.mp3")
                    mixer.music.play()
                    color_names[8]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/purple.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/purple.mp3")
                mixer.music.play()
# next screen
            if event.type==MOUSEBUTTONDOWN:
                if width/1.49<= mouse[0] <=width/1.284  and   height/1.45 <= mouse[1]<=height/1.29:
                    color_names[9]=True
                    mixer.music.load("asset/modes/color/audio/grey.mp3")
                    mixer.music.play()
                    color_names[8]=False

            if event.type==KEYDOWN and event.key in[K_RIGHT]:
                    color_names[9]=True
                    mixer.music.load("asset/modes/color/audio/grey.mp3")
                    mixer.music.play()
                    color_names[8]=False
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(purple,purple_i)
        window.blit(previous_button,previous_button_image)
        window.blit(next_button,next_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

    while color_names[9]:
        mouse=pygame.mouse.get_pos()
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                color_names[9]=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                run=False
                color_names[9]=False
# home button
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    game=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play()       
                    color_names[9]=False
# exit button
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    color_names[9]=False
                    run=False 
# previous
            if event.type==MOUSEBUTTONDOWN:
                if width/6.04<= mouse[0] <=width/3.67  and   height/1.48 <= mouse[1]<=height/1.319:
                    color_names[8]=True
                    mixer.music.load("asset/modes/color/audio/purple.mp3")
                    mixer.music.play()
                    color_names[9]=False

            if event.type==KEYDOWN and event.key in[K_LEFT]:
                    color_names[8]=True
                    mixer.music.load("asset/modes/color/audio/purple.mp3")
                    mixer.music.play()
                    color_names[9]=False
                    
# audio button
            if event.type==MOUSEBUTTONDOWN:
                if width/2.282<= mouse[0] <=width/1.786 and  height/1.573<= mouse[1]<=height/1.252:
                    mixer.music.load("asset/modes/color/audio/grey.mp3")
                    mixer.music.play()
                    
            if event.type==KEYDOWN and event.key in[K_SPACE]:
                mixer.music.load("asset/modes/color/audio/grey.mp3")
                mixer.music.play()
        
        window.blit(game_bg,game_bg_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(quit,quitimg)
        window.blit(home,home_img)
        window.blit(grey,grey_i)
        window.blit(previous_button,previous_button_image)
        window.blit(audio_button,audio_button_image)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()

# credit screen
    while credit:
        mouse=pygame.mouse.get_pos()

        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                credit=False
                run=False
            
            if event.type==KEYDOWN and event.key in[K_ESCAPE]:
                credit=False
                run=False
                
 # exit button  
            if event.type==MOUSEBUTTONDOWN:
                if width/1.044<= mouse[0] <=width/1.0019    and   height/27.87 <= mouse[1]<=height/9.81:
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play() 
                    credit=False
                    run=False
# back button                 
            if event.type==MOUSEBUTTONDOWN:
                if width/26.03<= mouse[0] <=width/12.90   and   height/50.82<= mouse[1]<=height/11.52:
                    start=True
                    mixer.music.load("asset/click_sound.wav")
                    mixer.music.play() 
                    credit=False
      
        if credit:     
            title=pygame.transform.scale(title,(800,200))
            title_img.center=(width/1.7,height/8)
            
        window.blit(game_bg,game_bg_img)
        window.blit(title,title_img)
        window.blit(name,name_img)
        window.blit(arsh,(width/1.080,height/1.04))
        window.blit(back_button,back_button_image)
        window.blit(quit,quitimg)
        curser_image.topleft=pygame.mouse.get_pos()
        window.blit(curser,curser_image)
        pygame.display.update()
        
    pygame.display.update()
pygame.quit()
