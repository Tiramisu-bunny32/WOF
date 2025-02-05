import pygame
import sys








pygame.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

text_font=pygame.font.Font("Hey Comic.ttf",90)






DARK_BROWN=(150, 112, 109)
CYAN=(3, 252, 239)
GREEN=(47, 232, 172)
YELLOW=(252, 232, 3)
BLACK=(25, 30, 54)
PURPLE=(198, 3, 252)
LIGHT_BLUE=(3, 148, 252)
VERY_LIGHT_BLUE=(184, 255, 255)
DARK_GREEN=(7, 179, 79)
BLUE=(5, 150, 247)
ROYAL_BLUE=(5, 156, 250)
ICEWING_LIGHT_BLUE=(193, 246, 247)
SANDWING_YELLOW=(250, 241, 90)
PINK=(242, 119, 218)
WHITE=(255,255,255)
COLORS={"Clay":DARK_BROWN,
        "Tsunami":CYAN,
        "Glory":GREEN,
        "Kinkajou":YELLOW,
        "Moon":BLACK,
        "Tamarin":PURPLE,
        "Riptide":LIGHT_BLUE,
        "Anemone":VERY_LIGHT_BLUE,
        "Auklet":DARK_GREEN,
        "Webs":BLUE,
        "Queen_Coral":ROYAL_BLUE,
        "Winter":ICEWING_LIGHT_BLUE,
        "Qibli":SANDWING_YELLOW,
        "Narrator":PINK}
       

character_image_paths={"Clay":"WOF dragon images/Clay.png",
                       "Tsunami":"WOF dragon images/Tsunami.png",
                       "Glory":"WOF dragon images/Glory.png",
                       "Kinkajou":"WOF dragon images/Kinkajou.png",
                       "Moon":"WOF dragon images/Moon.png",
                       "Tamarin":"WOF dragon images/Tamarin.png",
                       "Riptide":"WOF dragon images/Riptide.png",
                       "Anemone":"WOF dragon images/Anemone.png",
                       "Auklet":"WOF dragon images/Auklet.png",
                       "Webs":"WOF dragon images/Webs.png",
                       "Queen_Coral":"WOF dragon images/Queen_Coral.png",
                       "Winter":"WOF dragon images/Winter.png",
                       "Qibli":"WOF dragon images/Qibli.png",
    
}



def load_dragons():
    images={}
    for character,path in character_image_paths.items():
        try:
            image=pygame.image.load(path)
            images[character]=pygame.transform.scale(image,(150,150))
        except:
            surface=pygame.Surface((150,150))
            surface.fill(COLORS.get(character,WHITE))
            images[character]=surface
    return images
#load character images
character_images=load_dragons()
#list of dragon characters

        
story=[{"speaker":"Moon","text":"We have three months off from school; we might as well do something.","previous_speaker":None},
      {"speaker": "Kinkajou", "text":"truth or dare?"},
      {"speaker":"Glory", "text":"Nope, let's play that when I'm in a more dangerous mood for dares. But I have one devious idea..."},
      {"speaker":"Moon", "text":"This won't be harmful, will it?"},
      {"speaker":"Glory","text":"Relax, we're only rating our friends."},
      {"speaker":"Moon","text":"Won't that make them feel bad?"},
      {"speaker":"Glory","text":"Not if we don't tell them."},
      {"speaker":"Glory","text":"Relax, we're only rating our friends."},
      {"speaker":"Kinkajou","text":"I'll start! how about Winter? he's always so grouchy around Moon. Actully, he's grouchy around anyone! Though he is a pretty shiny Icewing..."},
      {"speaker":"Moon","text":"He's so weird and devious. I'd rate him a 2/10"},
      {"speaker":"Glory","text":"I've only met him once. He seemed really obsessed with finding Icicle. I'll rate him a 4/10."},
      {"speaker":"Kinkajou","text":"Nah, more like a 3/10."},
      {"speaker":"Moon","text":"What about Tsunami?"},
      {"speaker":"Kinkajou","text":"so we're rating our teachers now? Maybe a 9?"},
      {"speaker":"Glory","text":"noo, she was always so bossy. Don't underestimate her. She needs more common sense. How about a 1/10?"},
      {"speaker":"Moon","text":"I thought she was your friend? She's not so bad though, I'd rate her a 8/10? don't tell her I said that..."},
      {"speaker":"Glory","text":"How about loyal Clay? *rolling eyes*I guess I'll rate him a 9/10"},
      {"speaker":"Moon","text":"I barely know him..."},
      {"speaker":"Kinkajou","text":"ohh, yeah, isn't that our teacher who's obsessed with food? decent 8/10"},
      {"speaker":"Moon","text":"9/10 I guess."},
      {"speaker":"Kinkajou","text":"ohh, yeah, isn't that our teacher who's obsessed with food? decent 8/10"},
      ]

def display_text_and_images(speaker1,text1,speaker2=None,text2=None):
    screen.fill(WHITE)
    if speaker1 !="narrator":
        image1=character_images[speaker1]
        screen.blit(image1,(200,300))
    if speaker2 and speaker2 !="narrator":
        image2=character_images[speaker2]
        screen.blit(image2,(600,300))
    color1=COLORS.get(speaker1,WHITE)
    #speaker1's color is stored in color1
    speaker1_name=text_font.render(f"{speaker1}",True,color1)
    screen.blit(speaker1_name,(200,250))
    dialouge=text1.split("\n")
    y_offset=500
    for line in dialouge:
        display_text=text_font.render(line,True,color1)
        screen.blit(display_text,(200,y_offset))
        y_offset+=40
    
    




running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(CYAN)
    pygame.display.flip()




pygame.quit()
sys.exit()























