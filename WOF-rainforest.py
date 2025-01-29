

player_choice = ""


class colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    ORANGE = "\033[38;2;255;165;0m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    MAGENTA = "\033[35m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"





class Dragon:
    def __init__(self, name, look, personality, abilities):
        self.name=name
        self.look=look
        self.personality=personality
        self.abilities_list=abilities
    def display_abilities(self):
        if self.abilities_list:
            print("ability_list contains: ")
            for ability in self.abilities_list:
                print(f"{ability}")
Moon_abilities=["telepathy","telling the future","breathing fire"]
Moon=Dragon("speaker": "Moon", "text":"black scales with silver scales like stars on wings and silver teardrop shaped scales next to eyes","shy, loves scrolls so much she spends more time reading than talking to other dragons",Moon_abilities)
Moon.display_abilities()
Kinkajou_abilities=["spits a deadly venom from fangs","color-changing scales"]
Kinkajou=Dragon("speaker":"Kinkajou", "text": "bright scales that change colors based on mood with a curled tail","usually energetic, friendly and bubbly, very protective of friends such as Moon and Glory",Kinkajou_abilities)
Glory_abilities=["spits a deadly venom from fangs","color-changing scales"]
Glory=Dragon("speaker":"Glory", "text": "bright scales that change colors based on mood with a curled tail","Sarcastic, loyal",Glory_abilities)
Clay=Dragon("speaker":"Clay", "text": "ark brown scales with a flat head and amber underscales","friendly, constantly hungrey","Fire-resistant scales")
Tsunami_abilities=["lighting up stripes on body","creating one big wave with a splash of her strong tail"]
Tsunami=Dragon("speaker":"Tsunami", "text": "Blue scales with light-up stripes along body","bossy, loyal, sometimes over-confident",Tsunami_abilities)
Anemone=Dragon("speaker":"Anemone", "text": "very pale blue with hints of pink along wings","bossy, spoiled","animus powers, which means a dragon can enchant and object to do whatever they want just by telling it to")
Riptide_abilities=["lighting up stripes on body","creating one big wave with a splash of his strong tail"]
Riptide=Dragon("speaker":"Riptide", "text": "lue scales with light-up stripes along body","",Riptide_abilities)
Auklet_abilities=["lighting up stripes on body","creating one big wave with a splash of her strong tail"]
Auklet=Dragon("speaker":"Auklet", "text": "Green scales with light-up stripes along body","energetic, only a baby dragonet",Auklet_abilities)
Tamarin_abilities=["spits a deadly venom from fangs","color-changing scales"]
Tamarin=Dragon("speaker":"Tamarin", "text": "bright scales that change colors based on mood with a curled tail","intellegent, confident in her abilities even though she's blind","Tamarin_abilities")
Queen_Coral_abilities=["lighting up stripes on body","creating one big wave with a splash of her strong tail"]
Queen_Coral=Dragon("speaker":"Queen Coral", "text": "elegant with pearls around horns and wings, a horn with a wicked point attached to tail, Blue scales with light-up stripes along body","protective of her daughters, can sometimes be violent",Queen_Coral_abilities)
Webs_abilities=["lighting up stripes on body","creating one big wave with a splash of his strong tail"]
Webs=Dragon("speaker":"Webs", "text": "Blue scales with light-up stripes along body","intellegent, constantly sleeping",Webs_abilities)
Sunny=Dragon("Sunny","golden scales and green eyes with no scorpian barb at the end of her tail unlike a real sandwing","optimistic, always tries to be nice to random dragons, kind but dislikes when her friends call her sweet","can breathe fire but her fire isn't too strong")
   
def say(name_or_color,text):
    color=name_or_color
    name=""
    if name_or_color=="speaker":"Clay":
"text : "       color=colors.DARK_GRAY
        name="Clay: "
    elif name_or_color=="speaker": "Moon":
        color=colors.BLUE
        name="Moon: "
    elif name_or_color=="speaker":"Kinkajou":
"text":         color=colors.YELLOW
        name="Kinkajou: "
    elif name_or_color=="speaker":"Glory":
"text":         color=colors.GREEN
        name="Glory: "
    elif name_or_color=="speaker":"Tsunami":
"text":         color=colors.CYAN
        name="Tsunami: "
    elif name_or_color=="speaker":"Seawing selling smoothies":
        color=colors.CYAN
        name="Seawing selling smoothies: "
    elif name_or_color=="speaker":"Seawing":
"text":         color=colors.CYAN
        name="Seawing: "
    elif name_or_color=="speaker":"Anemone":
"text":         color=colors.MAGENTA
        name="Anemone: "
    elif name_or_color=="speaker":"Auklet":
"text":         color=colors.LIGHT_GREEN
        name="Auklet: "
    elif name_or_color=="speaker":"Tamarin":
"text":         color=colors.LIGHT_PURPLE
        name="Tamarin: "
    elif name_or_color=="speaker":"Riptide":
"text : "       color=colors.LIGHT_BLUE
        name="Riptide: "
    elif name_or_color=="speaker":"Queen Coral":
"text":         color=colors.RED
        name="Queen Coral: "
    elif name_or_color=="speaker":"Coral":
"text":         color=colors.RED
        name="Coral: "
    elif name_or_color=="speaker":"random dragon chef":
"text":         color=colors.ORANGE
        name="random dragon chef: "
    elif name_or_color=="speaker":"Webs":
"text":         color=colors.LIGHT_BLUE
        name="Webs: "
    elif name_or_color=="Winter":
        color=colors.CYAN
        name="Qibli: "  
    elif name_or_color=="Qibli":
        color=colors.ORANGE
        name="Qibli:  "    
    print(color, end="")
    print(name, end="")
    print(text, end="")
    print(colors.END)




def start():
    print("Episode one: Summer break in Pyrhia")
    say("speaker": "Moon", "text":"We have three months off from school; we migt as well do something.")
    say("speaker":"Kinkajou", "text": "truth or dare?")
    say("speaker":"Glory", "text": "Nope, let's play that when I'm in a more dangerous mood for dares. But I have one devious idea...")
    say("speaker": "Moon", "text": "This won't be harmful, will it?")
    say("speaker":"Glory", "text": "Relax, we're only rating our friends.")
    say("speaker": "Moon", "text": "Won't that make them feel bad?")
    say("speaker":"Glory", "text": "not if we don't tell them.")
    say("speaker":"Kinkajou", "text": "I'll start! how about Winter? he's always so grouchy around Moon. Actully, he's grouchy around anyone! Though he is a pretty shiny Icewing...")
    say("speaker": "Moon", "text": "He's so weird and devious. I'd rate him a 2/10")
    say("speaker":"Glory", "text": "I've only met him once. he seemed really obsessed with Icicle. I'll rate him an 4/10")
    say("speaker":"Kinkajou", "text": "nah, more like a 3/10")
    say("speaker": "Moon", "text": "What about Tsunami?")
    say("speaker":"Kinkajou", "text": "so we're rating our teachers now? maybe a 9?")
    say("speaker":"Glory", "text": "noo, she was always so bossy. Don't underestimate her. She needs more common sense. How about a 1/10?")
    say("speaker": "Moon", "text": "I thought she was your friend? She's not so bad though, I'd rate her a 8/10? don't tell her I said that...")
    say("speaker":"Glory", "text": "How about loyal Clay? *rolling eyes*I guess I'll rate him a 9/10")
    say("speaker": "Moon", "text": "I barely know him...")
    say("speaker":"Kinkajou", "text": "ohh, yeah, isn't that our teacher who's obsessed with food? decent 8/10")
    say("speaker": "Moon", "9/10 I guess")
    say("speaker":"Kinkajou", "text": "what about Anemone? She must have taken after Tsunami, she's too bossy!")
    say("speaker":"Glory", "text": "Oh yeah. Tsunami's obsessed with protecting her from becoming evil. I don't know her.")
    say("speaker": "Moon", "text": "well, she did whack me with a broom, so I don't consider her a friend...I know she was only jealous of me. 4/10.")
    say("speaker":"Kinkajou", "text": "She's such a spoiled brat! Plus she hurt Moon! -1,000/10!")
    say("speaker":"Glory", "text": "there's no point in having a scale from 1-10 if your just going to break it.")
    say("speaker":"Kinkajou", "text": "Ughh, fine. 1/10.")
    say("speaker": "Moon", "text": "what about Qibli? He always tries to impress me, but I secretly hate him. I don't know i I would call him a 'friend'. 1/10.")
    say("speaker":"Kinkajou", "text": "eh, 2/10.")
    say("speaker":"Glory", "text": "I DON'T EVEN KNOW THESE DRAGONS. But, hey, isn't QIbli obsessed with Sunny?")
    say("speaker":"Kinkajou", "text": "yeah, no, I don't know about that. He's fine with Moon, but the first time he met Sunny he thought she was a tresspasser in Thorn's quote and quote palace. ")
    say("speaker": "Moon", "text": "I think that's enough rating for today. Maybe we should go to the cafe in Jade mountain.")
    say("speaker":"Kinkajou", "text": "there's a cafe in our school?")
    say("speaker": "Moon", "text": "I heard it was recently added with meals for every tribes based on what they enjoy.")
    say("speaker":"Glory", "text": "nah. Too far from the rainforest. I'm kind of in charge of it, you know;I need to be close by to help out in case a nightwing steals a rainwing's pinapple or something.")
    say("speaker": "Moon", "text": "umm, ok. the beach?")
    say("speaker":"Glory", "text": "also too far, but Tsunami and Anemone are there currently. Maybe we can visit to bug Tsunami. Ugh, fine, I'll ask Deathbringer to substitute for me-not that I trust him to rule the rainforest.")
    say("speaker": "Moon", "text": "maybe we should let the player decide: cafe or beach?")
    say("speaker":"Kinkajou", "text": "huh? We have a player? What sport are we playing? A game called rainwings are the best?")
    say("speaker": "Moon", "text": "hey...")
    say("speaker":"Glory", "text": "You really need to pay attention, Kinkajou. You didn't notice that we're trapped in a screen on an app called python? YES, WE HAVE A PLAYER!")
    say("speaker":"Kinkajou", "text": "I don't know what an app is. Sounds like something a scavenger would use, but we have plenty of pythons here in the rainforest!They all deserve to die!")
    say("speaker":"Glory", "text": "forget it. I'm done explaining to you. Player that Kinkajou is oblivious to, where do you think we should go?")
    player_choice=input("Choose one: the cafe or beach?")
    if player_choice=="cafe":
        cafe()
    elif player_choice=="beach":
        beach()



def cafe():
    say("speaker": "Moon", "text": "Maybe we could get one large plate of fruit?")
    say("speaker":"Kinkajou", "text": "I have enough room for one whole pinapple!")
    say("speaker":"Glory", "text": "yeah, right. hey, there's Clay.")
    say("speaker":"Clay", "text": "oh! hi, Glory. thought you were in the rainforest!")
    say("speaker":"Glory", "text": "I had to work up the courage to ask Deathbringer to sub for me. *eyeroll*")
    say("speaker":"Clay", "text": "I might order a boar. Or maybe ten cows with a whale on the side.")
    say("speaker":"Glory", "text": "Don't yoou work at this place?")
    say("speaker":"Clay", "text": "chefs need to eat too!")
    say("speaker":"Kinkajou", "text": "hii, clay! I rated you a 8/10 eariler today!")
    say("speaker": "Moon", "text": "I thought we weren't suposed to tell them about the rating game!")
    say("speaker":"Clay", "text": "???")
    say("speaker":"Kinkajou", "text": "sorry...")
    say("speaker":"random dragon chef", "text": "GET BACK TO WORK!")
    say("speaker":"Clay", "text": "oops. gotta run. the main chef wants to make snake sandwhiches. Guess my boar ice cream will have to wait.")
    say("speaker":"Glory", "text": "grosss.....")
    say("speaker":"Clay", "text": "byye. also, Moon and Kinkajou, Webs wants you students to know you have a history test after summer break. I think it's on the scortching to the present?")
    say("speaker":"Kinkajou", "text": "noooo!")
    say("speaker": "Moon", "text": "yes! I studies for months!")
    say("speaker":"Kinkajou", "text": "hmm...I feel like playing a game after lunch.")
    say("speaker":"Glory", "text": "What I'm in the mood for is something dangerous.")
    say("speaker": "Moon", "text":"dangerous?")
    say("speaker":"Glory", "text": "you know, truth or dare.")
    say("speaker": "Moon", "text":"I thought weren't in the mood!")
    say("speaker":"Glory", "text": "Moods can change. *smirks*")
    say("speaker": "Moon", "text": "truth or dare sounds a little dangerous...Why don't we just play something peacful like chess?")
    say("speaker":"Kinkajou", "text": "Chess! I love chess! I'm champion at loosing!")
    say("speaker":"Glory", "text": "another debate!")
    player_choice=input("choose one, truth or dare or chess?")
    if player_choice=="truth or dare":
        truth_or_dare()
    elif player_choice=="chess":
        chess()





def beach():
    say("speaker":"Kinkajou", "text": "Wow, this place is perfact for our suntime!")
    say("speaker": "Moon", "text": "Maybe we should order smoothies while we look for Tsunami.")
    print("two minutes later:")
    say("speaker":"Glory", "text": "I'll take a guava smoothie, please.")
    say("speaker":"Kinkajou", "text": "I'll take a strawberry delight please make it quick please I'M STARVING!")
    say("speaker":"Seawing selling smoothies", "text": "BE PATIENT!")
    say("speaker": "Moon", "text": "*whispers* umm...I'll take a blueberry with extra sugar...")
    say("speaker":"Seawing", "text": "huh? speak up please!")
    say("speaker":"Kinkajou", "text": "*whispering to Glory* the Seawing's voice sounds familier...Do you reconize the Seawing's face?")
    say("speaker":"Glory", "text": "Of course not. The dragon's face is covered with a hat. I can't see past that fat brim.")
    say("speaker":"Kinkajou", "text": "C'mon, Moon! You can do it! Try to order your drink louder!")
    say("speaker": "Moon", "text": "umm, I'd take a suger smoothie with extra blueberries please.")
    say("speaker":"Kinkajou", "text": "oops! Moon, I think you mixed up your words.")
    say("speaker": "Moon", "text": "*blushes*")
    say("speaker":"Seawing", "text": "LOOK, IF YOU WON'T SPEAK UP YOU WON'T GET YOUR SMOOTHIE!I've had a long day and this is exausting! *runs away* *hat falls off* ")
    say("speaker":"Glory", "text": "Tsunami??? Why did you block your face with a stupid hat? And since when did you sell smoothies? Aren't you supposed to enjoy your day off from school? *cracks up*")
    say("speaker":"Kinkajou", "text": "Tsunami? selling smoothies sounds like the wrong job for you. You had the nerve to not give Moon a smoothie!!! It's ok, Moon. You can have mine. I've lost apetite. The only thing I'm hungry for right now is REVENGE against Tsunami for being rude to you!")
    say("speaker":"Glory", "text": "Don't be so hot-headed, Kinkajou. You don't answer bullying with yelling. Ya answer it with teasing, like this!*stomps over to Tsunami* HEY, THESE ARE YOUR STUDENTS YOUR SNAPPING AT, LAZY, SNORING MANATEE! ")
    say("speaker":"Tsunami", "text": "I'm going to choose to ignore that...MELONBRAIN!")
    say("speaker":"Kinkajou", "text": "Hey! nobody talks to the queen that way! not even my teacher...")
    say("speaker": "Moon", "text": "Umm... why DID you start selling smoothies??")
    say("speaker":"Tsunami", "text": "long story....")
    say("speaker":"Anemone", "text": "*rolls eyes* Auklet made her.")
    say("speaker":"Auklet", "text": "smooooothie. *pours smoothie on Tsunami's head.*")
    say("speaker":"Anemone", "text": "I told Tsunami that if she didn't listen to Auklet I would enchant her scales to turn pink.")
    say("speaker":"Glory", "text": "well, Tsunami wouldn't want to get mistaken for Jambu *snickers*")
    say("speaker":"Anemone", "text": "Duh, she'd be too embarrassed if she was pink, so she had no choice but to listen to Auklet and start a smoothie stand. Of course, my whimp of a sister wanted to hide her face with a hat because she was embarrassed to let every dragon know it was her who was selling smoothies.")
    say("speaker": "Moon", "text": "umm...you didn't need to force her to start a buisness.")
    say("speaker":"Anemone", "text": "too late!")
    say("speaker":"Clay", "text": "*runs over* smoothies--! Tsunami??? why are you wearing a weird hat?")
    say("speaker":"Tamarin", "text": "Hi Kinkajou! Hi Anemone! Umm...Is Tsunami starting a smoothie stand?")
    say("speaker":"Tsunami", "text": "*grabs a sign and glues it to the front of the smoothie stand*")
    say("speaker":"Clay", "text": "a sign that says 'closed'?? That's my least favorite kind of sign!")
    say("speaker":"Anemone", "text": "*whispering to Tamarin* Hiiii, Tamarin! My sister's so touchy...")
    say("speaker":"Tsunami", "text": "I.")
    say("speaker": "Moon", "text": "???")
    say("speaker":"Tsunami", "text": "I heard that, Anemone!!")
    say("speaker":"Riptide", "text": "*walks over* Tsunami's selling smoothies? that's new...")
    say("speaker":"Tsunami", "text": "Riptide? *blushes* your good, how am I?")
    say("speaker":"Riptide", "text": "Don't you mean 'I'm good, how are you?'")
    say("speaker":"Anemone", "text": "*to Tamarin* when my sister mixes up her words it's never a good sign.")
    say("speaker":"Riptide", "text": "is...everything ok? I'd love to order a smoothie from this stand!")
    say("speaker":"Tsunami", "text": "*nods rapidly and tears off the CLOSED sign* *starts blending a smoothie *")
    say("speaker":"Tsunami", "text": "*starts blending so fast she accedently pours hot sauce inside*")
    say("speaker":"Anemone", "text": "ooohh. She mixed up the ingredients!")
    say("speaker":"Kinkajou", "text": "You're willing to blend a drink for Riptide but not Moon? Geez!")
    print("*the hot sauce and icing spills and mixes together on the counter*")
    say("speaker": "Moon", "text": "*sees the mess* It's ok, Kinkajou. I don't know if I'm hungry anymore... ")
    say("speaker":"Tsunami", "text": "donehereyougoriptide!")
    say("speaker":"Riptide", "text": "*sips it anxiously* Woow, that's...*runs away and rinses with water*")
    print("...............")
    say("speaker":"Riptide", "text": "*runs back* SPICY. ")
    say("speaker":"Anemone", "text": "HA! Tsunami didn't notice the huge glob of hot sauce landing in Riptide's smoothie! ")
    say("speaker":"Tsunami", "text": "There was h-hot sauce? In the smoothie? *blushes and starts wobbling* *FAINTS*")
    say("speaker":"Riptide", "text": "*catches her* Are you sure this is actully Tsunami?")
    say("speaker":"Queen Coral", "text": "*walks over* Hello, daughters! *stares at Riptide* Riptide! You've contamenated my daughter! You even made her faint?")
    say("speaker":"Glory", "text": "Greetings, your majesty. May I ask why you're at the beach and not at your palace?")
    say("speaker":"Coral", "text": "I flew over to the beach because Morray told me all three of my daughters are here. I wanted to have a chat with them, but instead I see THAT dragon.*glares at Riptide*")
    say("speaker":"Anemone", "text": ".....TSUNAMI'S SELLING SMOOTHIES.")
    say("speaker":"Coral", "text": "And did Riptide order one? *fuming*")
    say("speaker": "Moon", "text": "umm...kind of.")
    say("speaker":"Coral", "text": "she didn't...GIVE HIM one...right?")
    say("speaker":"Auklet", "text": "sissy gave the smoothie!")
    say("speaker":"Coral", "text": "and did he    drink    it?")
    say("speaker":"Tamarin", "text": "Mayybe.")
    say("speaker":"Coral", "text": "come on, daughters! Wre're going back to the Deep Palace! *storms off*")
    say("speaker":"Anemone", "text": "*rolls eyes*")
    say("speaker":"Auklet", "text": "Tsunami and Wiptide sitting in a twee! ")
    say("speaker":"Clay", "text": "....Umm...I'd beter go back to Jade Mountain Academy. I'm suposed to teach the next class.")
    say("speaker":"Glory", "text": "CLAY, IT'S SUMMER BREAK!...Oh. Your just looking for an excuse to leave.")
    say("speaker":"Kinkajou", "text": "Some beach day *glares at Tsunami*.")
    say("speaker": "Moon", "text": "Maybe we should go to the Kingdom of Sand instead.")
    say("speaker":"Kinkajou", "text": "nooo, the way Qibli describes the scorpian den gives me the creeps.")
    say("speaker":"Glory", "text": "Maybe we should play another game...*smirks at Tsunami*")
    say("speaker":"Tsunami", "text": "Whaaat...?")
    say("speaker":"Glory", "text": "Moon, Kinkajou, Let's get out of here. We need to talk in priiivate.")
    print(".....")
    say("speaker":"Kinkajou", "text": "ok, what did you want to talk to us about in priiivate?")
    say("speaker":"Glory", "text": "We might as well play truth or dare. I'll get Riptide and Clay so we have more players.")
    say("speaker": "Moon", "text": "truth or dare sounds a little dangerous...Why don't we just play something peacful like chess?")
    say("speaker":"Kinkajou", "text": "Chess! I love chess! I'm champion at loosing!")
    say("speaker":"Glory", "text": "another debate!")
    player_choice=input("choose one, truth or dare or chess?")
    if player_choice=="truth or dare":
        truth_or_dare()
    elif player_choice=="chess":
        chess()
       
def truth_or_dare():
    say("speaker": "Moon", "text": "I still think this is a bad idea...")
    say("speaker":"Glory", "text": "too bad! It's what the player chose.")
    say("speaker": "Moon", "text": "do we have to do dares?")
    say("speaker":"Kinkajou", "text": "How about we do dares, but not on Moon?")
    say("speaker":"Glory", "text": "Good job breaking the rules of truth or dare!")
    say("speaker":"Kinkajou", "text": "I'm just trying to help Moon!")
    say("speaker":"Glory", "text": "fiine. Kinkajou, truth or dare?")
    say("speaker":"Kinkajou", "text": "dare! bring it!")
    say("speaker":"Glory", "text": "if you insiiist.")
    say("speaker":"Kinkajou", "text": "of course I insiiist.")
    say("speaker":"Glory", "text": "*whispers dare to Kinkajou*")
    say("speaker":"Kinkajou", "text": "*GAAASPP*")
    say("speaker":"Glory", "text": "what are you waiting for? Do it, you BRAVE dragon!")
    say("speaker":"Kinkajou", "text": "....")
    say("speaker":"Glory", "text": "You don't want to disappoint your queen...")
    say("speaker":"Kinkajou", "text": "*akwardly walks over to Moon*")
    say("speaker": "Moon", "text": "...yes?")
    say("speaker":"Kinkajou", "text": "*touches Moon*")
    say("speaker":"Glory", "text": "Harder!")
    say("speaker":"Kinkajou", "text": "Moon, what I'm about to do is forced by Glory.")
    print("....")
    say("speaker":"Kinkajou", "text": "*slaps Moon*")
    say("speaker": "Moon", "text": "!!!!!")
    say("speaker":"Kinkajou", "text": "Sorry!")
    say("speaker": "Moon", "text": "Glory, why would you dare her to do that?!")
    say("speaker":"Glory", "text": "sssorry. But truth or dare isn't truth or dare without a good prank.")
    say("speaker": "Moon", "text": "It's....It's...ok. Kinkajou, come with me. *drags Kinkajou away*")
    print("....")
    say("speaker":"Kinkajou", "text": "what is it Moon? sorry Glory did that to you...")
    say("speaker": "Moon", "text": "Well, I'm going to get her back.")
    say("speaker":"Kinkajou", "text": "are you sure? I mean, I'm not disagreeing with you; I think that's a great idea, but Glory can get pissed off reallly easily.")
    say("speaker": "Moon", "text": "yes. Very sure. *walks back to Glory*")
    say("speaker":"Glory", "text": "*looks bored* yes?")    
    say("speaker": "Moon", "text": "Kinkajou, truth or dare?")  
    say("speaker":"Kinkajou", "text": "DARE DARE DARE DARE--")
    say("speaker": "Moon", "text": "calm down! calm down! *whispers dare to Kinkajou*")
    say("speaker":"Kinkajou", "text": "Sorry, amazing Queen Glory! I'll forever regret this! *goes into camaflouge* ")
    say("speaker":"Glory", "text": "huh? I thought this was truth or dare; not hide and seek. *rolls eyes* ")
    say("speaker":"Kinkajou", "text": "*POKE* ")
    say("speaker":"Glory", "text": "OW!")
    say("speaker":"Kinkajou", "text": "sorry!")
    say("speaker": "Moon", "text": "sorry, I just had to get you back.")
    say("speaker":"Glory", "text": "*thinking* time to get revenge on both of them.")
    say("speaker":"Glory", "text": "Kinkajou! look over there! It's a bird with an apple for a head!")
    say("speaker":"Kinkajou", "text": "WHERE? WHERE? *looks away from Glory*")
    say("speaker":"Glory", "text": "*pushes Kinkajou into the ocean*")
    say("speaker":"Kinkajou", "text": "ACK!--*glug glug*")
    say("speaker": "Moon", "text": "Kinkajou! *jumps into the sea*")
    say("speaker":"Glory", "text": "sorry? *smiles evily*")
    say(colors.ITALIC,"under the sea:")
    say("speaker": "Moon", "text": "*grabs Kinkajou and swims her back to the surface*")
    say("speaker": "Moon", "text": "*swims over to Glory* Glory! I'm sorry I made Kinkajou poke you, but you were the one who made her slap me!")
    say("speaker":"Kinkajou", "text": "*coughs* I love swimming in the lakes in the rainforest, but in the ocean? at the beach? TOO SALTY! *coughs*")
    say("speaker": "Moon", "text": "I knew truth or dare was a bad idea! Why can't we play something...better? less dangerous maybe?")
    say("speaker":"Glory", "text": "*tosses a sand ball at Moon*")
    say("speaker":"Kinkajou", "text": "HOW DARE YOU HIT MOON! this means war!! *scales turn red* ")
    say("speaker": "Moon", "text": "Be careful!")
    say(colors.ITALIC, "*sand flies everywhere*")
    say("speaker":"Anemone", "text": "??? I snuck away from Mother to check on you guys and I see a major sand fight?")
    say("speaker":"Kinkajou", "text": "This is none of your buisness, PRINCESS.")
    say("speaker": "Moon", "text": "*dodges a sand ball* Wait, you ran away from Coral? Isn't she looking for you?")
    say("speaker":"Anemone", "text": "*rolls eyes* YEah, yeah. I enchanted Auklet's harness to keep her away from me though. I came over to look for you three. Surely what you guys are doing is more interesting than going back to the deap palace with my Mother.")
    say("speaker":"Glory", "text": "Leave us alone!....please?")
    say("speaker":"Anemone", "text": "So whyy are you three throwing sand? Can I help?")
    say("speaker":"Coral", "text": "(from a distance) Anemone?")
    say("speaker":"Anemone", "text": "My enchantment on Auklet's harness failed? three moons, what did I say wrong??")
    say("speaker":"Glory", "text": "Ohh, look! Your Mom is looking for you. Guess you better leave now! *throws a sand ball at her*")
    say("speaker":"Anemone", "text": "Hey! I'm a princess, you know!")
    say("speaker":"Glory", "text": "Who cares? Tsunami is royalty and I bully her all the time! *throws a sand ball at Kinkjou*")
    say("speaker":"Kinkajou", "text": "Ok, PRINCESS who put a love spell on me and is only two years old, kindly leave us alone to fight in peace.")
    say("speaker":"Glory", "text": "You can't fight in peace.")
    say("speaker":"Kinkajou", "text": "details!")
    say("speaker":"Anemone", "text": "Kinkajou! I told you! I'm sorry for the love spell! Why can't you just forgive me?! Also, I'm ending your fighting once and for all! *picks up a seashell* I enchant this seashell to bring Clay over here...NOW!")
    say("speaker":"Tsunami", "text": "*apears* Where am I? Anemone?")
    say("speaker":"Anemone", "text": "UGHH, why is animus magic glitching?! I said CLAY not my sister! Seashell, put Tsunami back at her smoothie stand.")
    say("speaker":"Tsunami", "text": "HEY! I'm not done interrogating you--*disapears*")
    say("speaker":"Anemone", "text": "Ok, let's try this again. Seashell, bring Clay here or else!")
    say("speaker":"Kinkajou", "text": "Why do you need Clay? *sand ball hits her* Glory! OUCH!")
    say("speaker":"Anemone", "text": "SEASHELL! THIS IS THE LAST STRAW! bring Clay-oof!")
    say("speaker":"Clay", "text": "*lands on her*")
    say("speaker":"Anemone", "text": "....Oof!")
    say("speaker":"Clay", "text": "oh! sorry. *stands up* How did I get here? Why are two of my students and one of my friends throwing sand at each other?")
    say("speaker": "Moon", "text": "Wasn't MY idea. *sand ball bounces off her wing*")
    say("speaker":"Anemone", "text": "I need you to stop their argument. I know how great you are at bringing peace to fighting dragons. I've seen enough!  bye! *runs away*")
    say("speaker":"Clay", "text": "Umm...Did she enchant something to bring me here?")
    say("speaker":"Glory", "text": "*accidently hits him with a sand ball* sorry! and yes she did!")
    say("speaker":"Clay", "text": "umm...ok? calm down and stop fighting!")
    say("speaker":"Kinkajou", "text": "*falls into the ocean*")
    say("speaker": "Moon", "text": "*falls into the ocean*")
    say("speaker":"Clay", "text": "Glory! did you push--")
    say("speaker":"Glory", "text": "I did nothing!")
    say("speaker":"Kinkajou", "text": "*crawls back onto the beach soaking wet and coughing* Glory! How could you?!")
    say("speaker":"Glory", "text": "sorry...")
    say("speaker":"Kinkajou", "text": "I don't know if I accept your apology, your HIGHNESS.")
    say("speaker": "Moon", "text":"Me neither...but you don't have to be so rude about it, Kinkajou.")
    say("speaker":"Clay", "text": "everyone calm down! You should try to forgive each other, being friends and all.")
    say("speaker":"Glory", "text": "Three moons, Clay. Don't try to persuade us into being all sweet and mushy.")
    say("speaker": "Moon", "text":"Ok. I'll forgive Glory as long as we get to play chess instead.")
    say("speaker":"Kinkajou", "text": "Me too, as long as Queen Glory doesn't push us into the ocean or hurt Moon. I almost sprayed venom at you, but stopped myself, remembering how painful venom felt when I got some on my wing.")
    say("speaker":"Glory", "text": "well, thanks for forgiving me I SUPOSE, but we can't play chess because there's three of us.")
    say("speaker": "Moon", "text":"It's okay. You can play with Kinkajou and I'll watch.")
    say("speaker":"Kinkajou", "text": "I love chess! The rainwings play it everyday!")
    say("speaker":"Glory", "text": "Nice joke, Kinkajou, but I've never in my rein of queen seen a rainwing playing chess.")
    say("speaker":"Kinkajou", "text": "Well then, maybe you're not as observent as you think you are, YOUR MAGESTY!")
    say("speaker":"Glory", "text": "*throws up her talons* Fine then! It's clear you don't want me to teach you chess! I'll just let Moon do it.")
    say("speaker":"Kinkajou", "text": DEAL!")
    print("restart the game and type in chess instead of truth or dare if you want to know what happens dering the chess game.")
    say(colors.ITALIC,"The next day at school:")
    say("speaker":"Kinakjou", "text": "Moon, get out your chess board and teach me some more!")
    say("speaker": "Moon", "text": "Sorry, we have to take our history test now.")
    say("speaker":"Kinakjou", "text": "*freazes in terror*")
    say("speaker": "Moon", "text": "You should have studied.")
    say("speaker":"Kinkajou", "text": "C-can't you just help me on the test?")
    say("speaker": "Moon", "text": "Sorry, Kinkajou. It's a test. I offered to help you study.")
    say("speaker":"Kinkajou", "text": "I don't even know what the scorching is!!!")
    say("speaker": "Moon", "text": "Maybe Webs will tell you.")
    say("speaker":"Kinkajou", "text": "pssh. Yeah, or yell at me for not studying.")
    say("speaker": "Moon", "text": "I don't know what to tell you, Kinkajou. You should have-")
    say("speaker":"Kinkajou", "text": "I know, I know! I should have studied! Three moons! Why am I such a bad student? *turnes blue and orange* *storms down the hall*")
    say("speaker": "Moon", "text": "Kinkajou, wait! Your not a bad stu...")
    say("speaker": "Moon", "text": "*thinking:* Wow. I've never seen Kinkajou this unhappy about school...")
    print("In class:")
    say("speaker":"Webs", "text": "*starts passing out the test*")
    say("speaker":"Webs", "text": "I assumed you all studied about the scorching to the present.")
    say("speaker":"Kinkajou", "text": "*Looks guiltily at Moon")
    say("speaker":"Webs", "text": "you have thirty minutes to fill ou your scroll. 80% and below, is an F.")
    say("speaker":"Kinkajou", "text": "GEEZ. *turns orange*")
    print("after the text begins:")
   
    print("Kinkajou's work:")
    print("#1. Why did the dragons decide to wipe out the scavengers?")
    print("Kinkajou's answer: because the scavengers were using the dragons as trampolines? How should I know?!")
    print("#2. How did Queen Oasis die?")
    print("Kinkajou's answer: Oh! that one's easy. A pesky scavenger killed her. Even I know that!")
    print("#3. Which one of the three Sandwing sisters turned their fight for the throne into a word war?")
    print("Kinkajou's answer: What's her name? Blaster? Blubber? melon-nose? papaya-face?")
    print("#4. There was a monument in the courtyard of the Sandwing stronghold before Thorn took it down. It was made of black stone and stands in the sand above the exact spot Queen Oasis was buried. What does the gravestone say?")
    print("Kinkajou's answer: Three moons! Why is this quesion so complicated?! ummm, ok! guessing time!")
    print("Kinkajou's guess: Queen Oasis was a very good queen, but got killed. Tea, anyone?")
    print("#5. Why did the dragonets or destiny decide to make Jade Mountain a school?")
    print("Kinkajou's answer: Oh, this one is the easiest! Jade mountain was made because The dragonets wanted a school for all the tribes! ")
    print("#6. What were Queen Scarlet's two daughters named?")
    print("Kinkajou's answer: Ummm...IDK. What's a Skywing name? Cloudtail and Windhead?")
    print("later:")
    print("#20. Name at least three of the Icewing animus gifts.")
    print("Kinkajou's answer: Hmmm...Winter told us about those. One is the gift of darkness, a tree with light globes growing from it. One is the gift of Weakness, an ice cliff that protects the ice kingdom from any other tribe--wait. Didn't Queen Snwfall take it down? Eh. Whatever. A third gift is the gift of cheese, where snowflakes fall inside the Icewing palace. Wait, does any of that make sense?")
    print("#21. How do you say SQUID-BRAIN in Aquatic?")
    print("Kinkajou's answer: WHAT? how am I suposed to know? I never asked Turtle! *thinks of Turtle and blushes*. Ok, I'll just guess.")
    print("Kinkajou's guess: A flash on the head, a flash on the wing and a flash on the mouth")
    say("speaker":"Webs", "text": "time's up, dragonets!*collects the tests*")
    print("the next day:")
    say("speaker":"Webs", "text": "And I will give you back your tests and show you your scores.")
    say("speaker":"Kinkajou", "text": "noooo!")
    print("The Scorching to the Present-test #1  Name: Moon the Rainwing")
    print("Score: 100%")
    print("Teacher's feedback: Great job studying!-Webs")
    print("The Scorching to the Present-test #1  Name: Kinkajou the Rainwing")
    print("score: 3%")
    print("Teacher's Feedback: Kinkajou, please see me after class.-Webs ")
    say("speaker":"Kinkajou", "text": "Three moons! He always falls asleep after teaching! *bangs head on desk*")
    say("speaker": "Moon", "text": "Kinkajou, it's time to hunt at the feasting grounds with Clay.")
    print("At the feasting grounds")
    say("speaker":"Clay", "text": "Kinkajou, why aren't you gathering your fruit? Don't you like mangoes?")
    say("speaker":"Kinkajou", "text": "*smashes a scavenger*")
    say("speaker":"Clay", "text": "Okkkkay...")
    print("after lunch at the dorms:")
    say("speaker": "Moon", "text":"Kinkajou, aren't you going to go see Webs?")
    say("speaker":"Kinkajou", "text": "HA! If he's asleep you owe me a mango.")
    say("speaker": "Moon", "text":"I thought you weren't hungrey...")
    say("speaker":"Kinkajou", "text": "*storms into Web's classroom and sees Webs snoring*")
    say("speaker": "Moon", "text":"Fine. Here's your mango.")
    say("speaker":"Kinkajou", "text": "*devours the mango*")
        say("speaker": "Moon", "text":"Kinkajou, If you need help studying you can always ask for help.")
    say("speaker":"Kinkajou", "text": "FINE. I'll study.")




def chess():
    say("speaker":"Kinkajou", "text": "Umm... what's chess again?")
    say("speaker": "Moon", "text": "Kinkajou, didn't you just say that the Rainwings play it every day?")
    say("speaker":"Kinkajou", "text": "huh? I did?")
    say("speaker":"Glory", "text": "Rainwings are not nearly intellegent enough to play a complicated game like chess.")
    say("speaker":"Kinkajou", "text": "Hey! You're insulting yourself, me and your entire tribe!")
    say("speaker":"Glory", "text": "I meant Rainwings BESIDES us.")
    say("speaker": "Moon", "text": "Basically in chess you have a board with black and white peices. Your supposed to attack your opponent with your peices--")
    say("speaker":"Kinkajou", "text": "What? but I would never attack you!")
    say("speaker": "Moon", "text": "not litatally attacking. It's a game!")
    say("speaker":"Glory", "text": "Sorry to interupt but are you SURE Kinkajou will be able to understand the concept of chess? Even I'm not that good.")
    say("speaker":"Kinkajou", "text": "I can learn...")
    say("speaker": "Moon", "text": "Are you sure, Kinkajou? There are a lot of peices that each do different things.")
    say("speaker":"Kinkajou", "text": "of course I'm sure.")
    say("speaker": "Moon", "text": "OK. Do you want to be white or black?")
    say("speaker":"Kinkajou", "text": "both? *turns her scales black and white*")
    say("speaker": "Moon", "text": "no, I mean do you want the white or black peices?")
    say("speaker":"Kinkajou", "text": "well, your scales are already black so I guess I'll be white.*turns white and grabs the white peices*")
    say("speaker":"Glory", "text": "Isn't white the color of sickness or pain for a Rainwing?")
    say("speaker":"Kinkajou", "text": "oh, right. *turns pink and yellow*")
    say("speaker": "Moon", "text": "The object of this game is to capture your opponent's peices.")
    say("speaker":"Kinkajou", "text": "OK? so we have to steal each other's peices? That's easy. *steals all of Moon's peices*")
    say("speaker": "Moon", "text": "NO! Each peice does a different thing. This is a game about being careful and smart. You have to use your peices to capture the other dragon's peices. But you have to be careful because the other dragon could steal yours.")
    say("speaker":"Kinkajou", "text": "ohh, got it.")
    say("speaker": "Moon", "text": "This peice is called the king. It's your most valuable peice. This peice can move around the board in whatever direction he wants, but only by one space. If your peice captured my king you would win. But right before Your peice attacks my king you have to say check to give my king a chance to escape from your peice. The king can move away from the attacker, attack the peice, or--")
    say("speaker":"Kinkajou", "text": "Ok, got it. What about the other peices?")
    say("speaker": "Moon", "text": "OK. All of these peices are pawns.")
    say("speaker":"Kinkajou", "text": "but why do they all look the same? They look like mini scavendgers!")
    say("speaker": "Moon", "text": "Umm...that's just how it is. Each of them can only move forward one space during their turn.")
    say("speaker":"Kinkajou", "text": "Ok, what about the castle?")
    say("speaker": "Moon", "text": "that's called a rook.")
    say("speaker":"Glory", "text": "*whispers to Moon* Are you sure she can handle this?")
    say("speaker": "Moon", "text": "I'm not sure...but can't we give her a chance?")
    say("speaker":"Kinkajou", "text": "What is this suposed to do? It looks like a deformed dragon.")
    say("speaker": "Moon", "text": "Don't you know what a horse is? Scavengers ride them.")
    say("speaker":"Kinkajou", "text": "No. Why? is this what a horse looks like? Umm...what does the peice do?")
    say("Moon:", "It can move 2 spaces up or down and then one to the side. Like an L shape. It's called a knight.")
    say("speaker":"Kinkajou", "text": "??? Since when do knights move in an L shape?")
    say("speaker": "Moon", "text": "Kinkajou, maybe I can teach you more tomorrow. I'm getting tired of explaining to you.")
    say("speaker":"Kinkajou", "text": "WHY?")
    say("speaker": "Moon", "text": "*starts packing up the peices and board*")
    say("speaker":"Kinkajou", "text": "MOON! What about this weird peice with a crack in the top? If it's broken, shouldn't we fix it?")
    say("speaker": "Moon", "text": "Kinkajou! Put away the glue and give me the bishup!")
    say("speaker":"Glory", "text": "Looks like we've had quite the day already. Come on, Kinkajou, I have to go back to the rainforest. I don't trust Deathbringer to rule the tribe for me.")
    say("speaker": "Moon", "text": "Three moons! Kinkajou! don't snap the board in half! Go study for our history test. I can help.")
    say("speaker":"Kinkajou", "text": "I don't even know what the scalding is!")
    say("speaker": "Moon", "text": "It's the SCORCHING. Webs told us about it, like a month ago.")
    say("speaker":"Glory", "text": "Alright, I'm going.")
    say("speaker":"Kinkajou", "text": "*turns orange")
    say("speaker":"Glory", "text": "Don't worry, Kinkajou. Moon will play with you tomorrow.")
    print("...")
    say(colors.ITALIC,"after summer break at school:")
    say("speaker":"Kinakjou", "text": "Moon, get out your chess board and teach me some more!")
    say("speaker": "Moon", "text": "Sorry, we have to take our history test now.")
    say("speaker":"Kinakjou", "text": "*freazes in terror*")
    say("speaker": "Moon", "text": "You should have studied.")
    say("speaker":"Kinkajou", "text": "C-can't you just help me on the test?")
    say("speaker": "Moon", "text": "Sorry, Kinkajou. It's a test. I offered to help you study.")
    say("speaker":"Kinkajou", "text": "I don't even know what the scorching is!!!")
    say("speaker": "Moon", "text": "Maybe Webs will tell you.")
    say("speaker":"Kinkajou", "text": "pssh. Yeah, or yell at me for not studying.")
    say("speaker": "Moon", "text": "I don't know what to tell you, Kinkajou. You should have-")
    say("speaker":"Kinkajou", "text": "I know, I know! I should have studied! Three moons! Why am I such a bad student? *turnes blue and orange* *storms down the hall*")
    say("speaker": "Moon", "text": "Kinkajou, wait! Your not a bad stu...")
    say("speaker": "Moon", "text": "*thinking:* Wow. I've never seen Kinkajou this unhappy about school...")
    print("In class:")
    say("speaker":"Webs", "text": "*starts passing out the test*")
    say("speaker":"Webs", "text": "I assumed you all studied about the scorching to the present.")
    say("speaker":"Kinkajou", "text": "*Looks guiltily at Moon")
    say("speaker":"Webs", "text": "you have thirty minutes to fill ou your scroll. 80% and below, is an F.")
    say("speaker":"Kinkajou", "text": "GEEZ. *turns orange*")
    print("after the text begins:")
   
    print("Kinkajou's work:")
    print("#1. Why did the dragons decide to wipe out the scavengers?")
    print("Kinkajou's answer: because the scavengers were using the dragons as trampolines? How should I know?!")
    print("#2. How did Queen Oasis die?")
    print("Kinkajou's answer: Oh! that one's easy. A pesky scavenger killed her. Even I know that!")
    print("#3. Which one of the three Sandwing sisters turned their fight for the throne into a word war?")
    print("Kinkajou's answer: What's her name? Blaster? Blubber? melon-nose? papaya-face?")
    print("#4. There was a monument in the courtyard of the Sandwing stronghold before Thorn took it down. It was made of black stone and stands in the sand above the exact spot Queen Oasis was buried. What does the gravestone say?")
    print("Kinkajou's answer: Three moons! Why is this quesion so complicated?! ummm, ok! guessing time!")
    print("Kinkajou's guess: Queen Oasis was a very good queen, but got killed. Tea, anyone?")
    print("#5. Why did the dragonets or destiny decide to make Jade Mountain a school?")
    print("Kinkajou's answer: Oh, this one is the easiest! Jade mountain was made because The dragonets wanted a school for all the tribes! ")
    print("#6. What were Queen Scarlet's two daughters named?")
    print("Kinkajou's answer: Ummm...IDK. What's a Skywing name? Cloudtail and Windhead?")
    print("later:")
    print("#20. Name at least three of the Icewing animus gifts.")
    print("Kinkajou's answer: Hmmm...Winter told us about those. One is the gift of darkness, a tree with light globes growing from it. One is the gift of Weakness, an ice cliff that protects the ice kingdom from any other tribe--wait. Didn't Queen Snwfall take it down? Eh. Whatever. A third gift is the gift of cheese, where snowflakes fall inside the Icewing palace. Wait, does any of that make sense?")
    print("#21. How do you say SQUID-BRAIN in Aquatic?")
    print("Kinkajou's answer: WHAT? how am I suposed to know? I never asked Turtle! *thinks of Turtle and blushes*. Ok, I'll just guess.")
    print("Kinkajou's guess: A flash on the head, a flash on the wing and a flash on the mouth")
    say("speaker":"Webs", "text": "time's up, dragonets!*collects the tests*")
    print("the next day:")
    say("speaker":"Webs", "text": "And I will give you back your tests and show you your scores.")
    say("speaker":"Kinkajou", "text": "noooo!")
    print("The Scorching to the Present-test #1  Name: Moon the Rainwing")
    print("Score: 100%")
    print("Teacher's feedback: Great job studying!-Webs")
    print("The Scorching to the Present-test #1  Name: Kinkajou the Rainwing")
    print("score: 3%")
    print("Teacher's Feedback: Kinkajou, please see me after class.-Webs ")
    say("speaker":"Kinkajou", "text": "Three moons! He always falls asleep after teaching! *bangs head on desk*")
    say("speaker": "Moon", "text": "Kinkajou, it's time to hunt at the feasting grounds with Clay.")
    print("At the feasting grounds")
    say("speaker":"Clay", "text": "Kinkajou, why aren't you gathering your fruit? Don't you like mangoes?")
    say("speaker":"Kinkajou", "text": "*smashes a scavenger*")
    say("speaker":"Clay", "text": "Okkkkay...")
    print("after lunch at the dorms:")
    say("speaker": "Moon", "text":"It's ok, Kinkajou. It's just a test.")
    say("Winter","Three moons, Kinkajou! Stop moping!")
    say("Qibli","Winter, be nice.")
    say("speaker": "Moon", "text":"Kinkajou, aren't you going to go see Webs?")
    say("speaker":"Kinkajou", "text": "HA! If he's asleep you owe me a mango.")
    say("speaker": "Moon", "text":"I thought you weren't hungrey...")
    say("speaker":"Kinkajou", "text": "*storms into Web's classroom and sees Webs snoring*")
    say("speaker": "Moon", "text":"Fine. Here's your mango.")
    say("speaker":"Kinkajou", "text": "*devours the mango*")
    say("speaker": "Moon", "text":"Kinkajou, If you need help studying you can always ask for help.")
    say("speaker":"Kinkajou", "text": "FINE. I'll study.")








    print("Episode two: Secret Dragon (Christmas addition)")
    say("Kinkjou","Merry Christmas!")
    say("speaker": "Moon", "text":"What's Christmas exactly?")
    say("speaker":"Kinkajou", "text": "I read it in a scroll about scavengers. It's a holiday that they celebrate.")
    say("speaker": "Moon", "text":"Oh, yeah. I remember reading that scroll about a year ago, but I'd forgotten what the holiday was called. Scavengers can actully celebrate!")
    say("Winter","*pops his head in* of course they can! Remember that time we saw them building a house? They're incredibly clever for animals.")
    say("speaker":"Kinkajou", "text": "Why should we let animals have all the fun? We could celebrate too! According to the scroll, Christmas is where scavengers have a certain day to exchange presents. Some baby scavengers are actually naive enough to think the presents from their parents are from some scavenger with a beard who wears red. I think its name is Sanatizer? ")
    say("speaker": "Moon", "text":"I guess we could try celebrating that. Exchanging presents sound fun.")
    say("Kinkjou","We have to put the gifts under a tree in boxes so they'll be hidden and each dragon will be suprised when they open their boxes. Of course, we can also write wist lists for each other so we know what everyone wants for a present. Can we not do that? I want to be suprised, especially by Winter.")
    say("speaker": "Moon", "text":"Wow. This holiday sounds fun.")
    say("Winter","More like a waste of time.")
    say("speaker":"Kinkajou", "text": "Well, if you don't want to do it me and Moon will do it ourselves this afternoon.")
    say("Winter","FINE. But we won't be able to find gifts by this afternoon.")
    say("speaker":"Kinkajou", "text": "Huh. Good catch. I'll give you one day to make a gift.")
    say("Winter","ONE DAY?!")
    say("speaker":"Kinkajou", "text": "WHAT? do you have trouble thinking of gifts in one day's time?!")
    say("speaker": "Moon", "text":"Winter's right. We need at least a week to think about presents to give to each other, especially if we're making the present.")
    say("speaker":"Kinkajou", "text": "Ugh, FINE! Ooh! I have an idea!! We should do secret dragon! Scavengers do it, but they don't call it secret dragon obviously.")
    say("speaker": "Moon", "text":"Won't we need more dragons for that?")
    say("Winter","What in the moons is secret dragon?")
    say("speaker":"Kinkajou", "text": "It's when we write our names on tiny slips of paper and slip them in a box. Then, we'll take turns reaching into the box withouht looking and the name we pull out is the dragon we give gifts to.")
































































   








































   
























start()















