import json
from pygame import*
init()
window=display.set_mode((800,600))
window.fill((233,196,247))
clock=time.Clock()
game=True
#Дані які зберігаються в json
filename="settings.json"
levels=["Легкий","Середній","Важкий"]
index=0
class Button():
    def __init__(self,x,y,width,height,text,color,text_color=(12,7,3)):
        self.rect=Rect(x,y,width,height)
        self.text=text 
        self.color=color
        self.font=font.Font(None,28)
        self.text_color=text_color
    def draw(self,surface):
        draw.rect(window,self.color,self.rect)
        text_button=self.font.render(self.text,True,self.text_color)
        rect_text=text_button.get_rect(center=self.rect.center)
        surface.blit(text_button,rect_text)
    def clicked(self,event):
        return event.type==MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    

play=Button(200,80,200,50,"Грати",(105,90,74))
settings=Button(200,150,200,50,"Складність",(12,7,3))
exit_button=Button(200,220,200,50,"Вийти",(105,90,74))
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if play.clicked(e):
        print("Гра запускається")
    if settings.clicked(e):
        index=index+1%(len(levels))
        with open (filename,"w") as f:
            json.dump({"level":levels[index]},f)
    if exit_button.clicked(e):
        print("Вихід з гри")
        game=False
    play.draw(window)
    settings.draw(window)
    exit_button.draw(window)
    display.update()
    clock.tick(60)
quit()
