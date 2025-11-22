from pygame import*
from socket import*
from PIL import Image
init()
window=display.set_mode((500,500))
clock=time.Clock()
display.set_caption("LEVEL 2")
window.fill((0,0,0))
player1=image.load("platform.png")
player=transform.scale(player1,(50,100))
player2=image.load("platform2.png")
player2=transform.scale(player2,(50,100))
ball=image.load("ball.png")
ball=transform.scale(ball,(20,20))
def connect_server():
    try:
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(('localhost',8080))
    except:
        print("Connection error")

font_win=font.Font(None,70)
font_main=font.Font(None,56)
score_player1=0
score_player2=0
text1=font_main.render(f"{score_player1}",True,(255,255,255))
text2=font_main.render(f"{score_player2}",True,(255,255,255))
while True:
    for e in event.get():
        if e.type==QUIT:
            quit()
    connect_server()
    window.blit(player,(0,200))
    window.blit(player2,(450,200))
    window.blit(ball,(250,250))
    window.blit(text1,(30,30))
    window.blit(text2,(450,30))
    display.update()
    clock.tick(40)
quit()
