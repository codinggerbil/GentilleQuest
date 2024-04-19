#Instructions: Copy and paste this code into the https://www.onlinegdb.com/online_python_compiler. Then, press the run button and then the fullscreen #button. (Also there’s an annoying white bar at the bottom of the page, try reloading if there’s not an ad on it.)

#GentilleQuest v1.1.2
#By ActonWoods









#Status effects index: 0-Poison, 1-Regen, 2-Weak, 3-Strength, 4-Slow, 5-Haste, 6-Void Poison, 7-Burning, 8-Thorns, 9-Dodge
from json import loads
from random import randint
from time import sleep
from math import floor
from math import ceil
def interpret(code):
    global inventory
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global mainhand
    global offhand
    global pp
    global phealth
    holder=''
    index=0
    current=''
    while True:
        current=code[index]
        index+=1
        if not current=='{':
            holder+=current
        else:
            break
    pp=int(holder)
    holder=''
    
    
    
    
    
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[0]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    h_bonus=loads(holder)
    holder=''

    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[1]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    c_bonus=loads(holder)
    holder=''

    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[2]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    l_bonus=loads(holder)
    holder=''
    
    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[3]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    f_bonus=loads(holder)
    holder=''
    
    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[4]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    ha_bonus=loads(holder)
    holder=''
    
    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[5]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    mainhand=loads(holder)
    holder=''
    
    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current=='[':
            holder+=current
        else:
            break
    inventory[6]=holder
    holder=''
    while True:
        current=code[index]
        index+=1
        if not current==']':
            holder+=current
        else:
            break
    holder='['+holder+']'
    offhand=loads(holder)
    holder=''
    
    
    
    index+=2
    while True:
        current=code[index]
        index+=1
        if not current==',':
            holder+=current
        else:
            break
    name=holder
    holder=''
    
    
    
    
    while True:
        current=code[index]
        index+=1
        if not current==',':
            holder+=current
        else:
            break
    souls=int(holder)
    holder=''
    
    
    
    
    while True:
        current=code[index]
        index+=1
        if not current=='*':
            holder+=current
        else:
            break
    phealth=int(holder)
    holder=''
if True:
    
    global magesmith_location 
    magesmith_location= 1000000000
    global shop_location 
    shop_location= 1000000000
    global sage_position
    sage_position=1000000000
    global map
    map='############################################################'
    for i in range(5):
        map+=('############################################################')
    global pp
    pp=0
    global ip
    global actual_events
    ip=[randint(10,359),randint(10,359),randint(10,359),randint(10,359),randint(10,359),randint(10,359)]
    actual_events=['Shop','Magesmith','Chest','Chest','Sage','Healer']
    global gp
    gp=359
    global collect_chance
    global encounter_chance
    collect_chance=10
    encounter_chance=10
    global phealth
    global mainhand
    global offhand
    global souls
    global player_effects
    global hand_print
    global armor_print
    souls=1
    mainhand=[5,0,0,0,0]
    offhand=[0,6,0,0,0]
    phealth=30
    player_effects=[0,0,0,0,0,0,0]
    armor_print=['  Defense: ','    Buff type: ','  Buff power: ']
    hand_print=['   Damage: ','   Block: ','    Effect target: ','  Effect name: ','   Effect power: ']
    global enemy_effects
    enemy_effects=[0,0,0,0,0,0]
    global enemy_buff
    global enemy_debuff
    enemy_buff=[0,0]
    enemy_debuff=[0,0]
    global player_buff
    global player_debuff
    player_buff=[0,0]
    player_debuff=[0,0]
    global player_current_damage
    player_current_damage=0
    global player_current_block
    player_current_block=0
    global inventory
    global effect_names
    global effect_print
    effect_names=['Poison', 'Regen','Weak','Strength','Slow','Haste','Void Poison']
    effect_print=['Poison: ','Regen: ','Weak: ','Strength: ','Slow: ','Haste: ']
    #
    #
    #Order of inventory index: 1-Headgear, 2-Chestgear, 3-Leggear, 
    #4-Footgear, 5-Handgear, 6-Mainhand, 7-Offhand
    #
    #
    global inventorder
    global inventory
    inventorder=('Headgear: ','Chestgear: ','Leggear: ','Footgear: ','Handgear: ','Mainhand: ','Offhand: ',
    'Money: ')
    inventory=['None','Old Madison shirt','Shorts','None','None','Pencil','Notebook',0]
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    h_bonus=[0,0,0]
    c_bonus=[0,0,0]
    l_bonus=[0,0,0]
    f_bonus=[0,0,0]
    ha_bonus=[0,0,0]
    if ha_bonus[1]!=[0]:
        pass
    global enemy_names
    global enemy_print
    enemy_names=('Ms Ohem', 'Benito Mussolini','Joey Joey Joey','Joseph Stalin','Deoxyribonucleic Acid',
    'Donald Trump','Jose Delgado','Mr McCullock','Bob, the demon that lives in the walls','a gremlin',
    'a gremlin','Dolores Umbrige','Lucas Chang','Dynamite Bill','Ms Defilippi','Ms Firetag','Mr Luango',
    'The electoral college','Dihydrogen Monoxide','Aaron Burr')
    enemy_print=('Health: ',"Damage: ",'Defense: ')
answer=input('Do you have a save code? (y or n)')
if answer=='y':
    ploof=input('Enter save code:')
    interpret(ploof)
    print('Save code loaded succesfully! =)')
else:
    name=str(input('What is your name?'))
sleep(1)
turns=1
def story():
    print('Long ago, a school was built unknowingly on a portal to the demon realm.')
    sleep(2)
    print('''The portal corrupted a janitor\'s closet in the school, turning it into a dark pocket dimension 
called the gremlin closet.''')
    sleep(2)
    print('The closet was eventually covered by a coat of paint, and they thought the problem was solved.')
    sleep(2)
    print('50 years later, today, you were walking through the halls with your final engineering project.')
    sleep(2)
    print('You tripped, dropping your project through the paint and into the closet.')
    sleep(2)
    print('Unable to become a Gentille power student without it, you jumped into the closet after it to get it.')
    sleep(2)
    print('Your goal: To find the project and make it out alive.')
    sleep(3)
story()
title=['   _____                  _     _   _   _           ____                         _   ',
'  / ____|                | |   (_) | | | |         / __ \                       | |  ',
' | |  __    ___   _ __   | |_   _  | | | |   ___  | |  | |  _   _    ___   ___  | |_ ',
' | | |_ |  / _ \ | \'_ \  | __| | | | | | |  / _ \ | |  | | | | | |  / _ \ / __| | __|',
' | |__| | |  __/ | | | | | |_  | | | | | | |  __/ | |__| | | |_| | |  __/ \__ \ | |_ ',
'  \_____|  \___| |_| |_|  \__| |_| |_| |_|  \___|  \___\_\  \__,_|  \___| |___/  \__|',
'Made by ActonWoods coding =)']
for i in title:
    print(i)
    sleep(0.5)
sleep(0.5)
input('Press enter to start'.center(106))
headgear_all=[['None',0,0,0],['Baseball Cap',1,3,2],['Sweatband',2,5,2],['Headphones',1,1,1],['Wolf Ears',5,5,1]]
chestgear_all=[['Old Madison Shirt',0,0,0],['Black Tee Shirt',2,5,1],['Basketball Jersey',3,3,1],['Gamer Hoodie',7,0,0],['Wolf Shirt',2,5,1]]
leggear_all=[['Shorts',0,0,0],['Typical Jeans',3,1,1],['Basketball Shorts',2,3,1],['Gamer Pants',5,0,0],['Wolf Tail',3,5,1]]
footgear_all=[['None',0,0,0],['Crocs',1,3,1],['Sneakers',1,3,1],['Pink Slippers',3,5,1],['Wolf Paws',0,5,1]]
handgear_all=[['None',0,0,0],['Black Gloves',1,3,1],['Many Bracelets',1,5,1],['Watch',4,0,0],['Wolf Paws',0,5,1]]
held_items_all=[['Pencil',5,0,0,0,0],['Notebook',0,6,0,0,0],['Broom',4,0,2,2,2],['Spellbook',3,3,2,0,3],['Rusty Knife',3,0,2,0,2],
['Trash can lid',0,8,0,0,0],['Syringe',1,0,2,0,4],['Medicine Bottle',0,0,1,1,3],['Handgun',10,0,1,2,2],['Energy Shield',0,1,1,5,2]]
items_collectable=[
    ['Baseball Cap',1,3,2,'h'],['Sweatband',2,5,2,'h'],['pair of headphones',1,1,1,'h'],['pair of wolf ears',5,5,1,'h']
    ,['Black Tee Shirt',2,5,1,'c'],['Basketball Jersey',3,3,1,'c'],['Gamer Hoodie',7,0,0,'c'],['Wolf Shirt',2,5,1,'c'],['Ravens Jersey',3,5,2]
    ,['pair of typical jeans',3,1,1,'l'],['pair of basketball shorts',2,3,1,'l'],['pair of gamer pants',5,0,0,'l'],['Wolf Tail',3,5,1,'l']
    ,['pair of crocs',1,3,1,'f'],['pair of sneakers',1,3,1,'f'],['pair of pink slippers',3,5,1,'f'],['pair of wolf paws',0,5,1,'f']
    ,['pair of black gloves',1,3,1,'ha'],['collection of many bracelets',1,5,1,'ha'],['Watch',4,0,0,'ha'],['pair of wolf paws',0,5,1,'ha'],
    ['Pencil',5,0,0,0,0,'w'],['Notebook',0,6,0,0,0,'w'],['Broom',4,0,2,2,2,'w'],['Spellbook',3,3,2,0,3,'w'],['Rusty Knife',3,0,2,0,2,'w'],
    ['Trash can lid',0,8,0,0,0,'w'],['Syringe',1,0,2,0,4,'w'],['Medicine Bottle',0,0,1,1,3,'w'],['Handgun',10,0,1,2,2,'w'],
    ['Energy Shield',0,1,1,5,2,'w']
]
putdown=('You left it behind.','You threw it on the ground like the piece of trash it is.','You gingerly put it down.',
'You deserted it.','You had an argument and stormed away from it.')
shop=[randint(0,len(items_collectable)-1),randint(0,len(items_collectable)-1),randint(0,len(items_collectable)-1),
randint(0,len(items_collectable)-1),randint(0,len(items_collectable)-1),randint(0,len(items_collectable)-1)]
purchasable_items=['1','2','3','4','5','6']
adjective=('cool','great','incredible','fine','bargain-price','rare','sturdy','fire','sick','old')
heal_position=1000000000
spellbook=[]
#Spell index: Name, Element, Mana Cost, Damage, Block, Target, Effect, Effect Level
spells_obtainable=[
    ['Fireball','f',1,2,0,0,6,4],['Ice Bolt','w',1,4,0,0,0,0],['Mighty Wind','a',1,2,4,0,0,0],['Rock Wall','e',1,0,6,1,5,3],
    ['Flaming Wall','f',3,0,5,1,8,3],['Healing','w',2,0,0,1,1,5],['Evasion','a',1,0,0,1,9,0],['Boulder','e',3,10,0,0,0,0],
    ['Lightning Zappity Doo','f',5,30,0,1,2,5]]

def render():
    global map
    global magesmith_location
    global shop_location
    global pp
    global ip
    global gp
    global sage_position
    map=''
    for i in range(6):
        map+=('............................................................')
    place=''
    for mp in range(360):
        if pp==mp:
            place+='@'
        elif mp==0:
            place+='&'
        elif mp==shop_location:
            place+='$'
        elif mp==magesmith_location:
            place+='M'
        elif mp==sage_position:
            place+='S'
        elif mp in ip:
            place+='?'
        elif mp==gp:
            place+='%'
        else:
            place+=map[mp]
    map=place
    for mult in range(6):
        print(map[int((mult*60)):int((mult*60)+60)])
def asktick():
    annoyance=0
    answer=''
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global mainhand
    global offhand
    global ip
    global phealth
    global souls
    global name
    global inventory
    while True:
        answer=str(input('Enter an action (h for help): ')).lower()
        if answer=='h':
            print('i for inventory, w for up, a for left, s for down, d for right, and save for a save code.')
        elif answer in 'i w a s d dev save'.split():
            break
        else:
            annoyance+=1
            if annoyance > 10:
                print('''The computer got annoyed at you. 
You have died.''')
                quit()
            else:
                print('Invalid action key. Please try again.')
    global pp
    global inventory
    global inventorder
    global targetdecision
    targetdecision=['Self','Enemy']
    if answer=='dev':
        answer=input('What dev command would you like to use?')
        if answer=='coins':
            inventory[7]+=999
        elif answer=='shop':
            pp=ip[0]
        elif answer=='mage':
            pp=ip[1]
        elif answer=='sage':
            pp=ip[4]
        elif answer=='tp':
            pp=int(input('Where do you want to go?'))
        elif answer=='colchance':
            collect_chance=int(input('What would you like the collect chance to be?'))
        elif answer=='encchance':
            encounter_chance=int(input('What would you like the encounter chance to be?'))
        elif answer=='loadout':
            inventory[0]='Top Hat'
            h_bonus=[10,5,2]
            inventory[1]='Nice Tux'
            c_bonus=[20,3,2]
            inventory[2]='Fancypants'
            l_bonus=[5,5,2]
            inventory[3]='Shiny Shoes'
            f_bonus=[2,1,10]
            inventory[4]='Fancy Gloves'
            h_bonus=[0,3,20]
            inventory[5]='Gentleman\'s Sniper Rifle'
            mainhand=[30,0,0,0,0]
            inventory[6]='Perfect Parrying'
            offhand=[0,99999,0,0,0]
        elif answer=='heal':
            pp=ip[5]
            
    elif answer=='save':
        #Position, gear, name, money, health
        print(str(pp)+'{'+inventory[0]+str(h_bonus)+'}'+'{'+inventory[1]+str(c_bonus)+'}'+'{'+inventory[2]+str(l_bonus)+'}'+'{'+inventory[3]+str(f_bonus)+'}'+'{'+inventory[4]+str(ha_bonus)+'}'+'{'+inventory[5]+str(mainhand)+'}'+'{'+inventory[6]+str(offhand)+'}'+name+','+str(inventory[7])+','+str(phealth)+'*')
    elif answer=='i':
        print('Health: '+str(phealth))
        print('Headgear: '+inventory[0])
        sleep(0.3)
        print('   Block: '+str(h_bonus[0]))
        sleep(0.3)
        if not h_bonus[1]==0:
            print('   Effect: '+effect_names[h_bonus[1]])
            sleep(0.3)
            print('   Power: '+str(h_bonus[2]))
            sleep(0.3)
        print('Chestpiece: '+inventory[1])
        sleep(0.3)
        print('   Block: '+str(c_bonus[0]))
        sleep(0.3)
        if not c_bonus[1]==0:
            print('   Effect: '+effect_names[c_bonus[1]])
            sleep(0.3)
            print('   Power: '+str(c_bonus[2]))
            sleep(0.3)
        print('Leggear: '+inventory[2])
        sleep(0.3)
        print('   Block: '+str(l_bonus[0]))
        sleep(0.3)
        if not l_bonus[1]==0:
            print('   Effect: '+effect_names[l_bonus[1]])
            sleep(0.3)
            print('   Power: '+str(l_bonus[2]))
            sleep(0.3)
        print('Footgear: '+inventory[3])
        sleep(0.3)
        print('   Block: '+str(f_bonus[0]))
        sleep(0.3)
        if not f_bonus[1]==0:
            print('   Effect: '+effect_names[f_bonus[1]])
            sleep(0.3)
            print('   Power: '+str(f_bonus[2]))
            sleep(0.3)
        print('Handgear: '+inventory[4])
        sleep(0.3)
        print('   Block: '+str(ha_bonus[0]))
        sleep(0.3)
        if not ha_bonus[1]==0:
            sleep(0.3)
            print('   Effect: '+effect_names[ha_bonus[1]])
            sleep(0.3)
            print('   Power: '+str(ha_bonus[2]))
            sleep(0.3)
        print('Mainhand: '+inventory[5])
        sleep(0.3)
        print('   Damage: '+str(mainhand[0]))
        sleep(0.3)
        print('   Block: '+str(mainhand[1]))
        sleep(0.3)
        if not mainhand[2]==0:
            print('   Target: '+targetdecision[mainhand[2]-1])
            sleep(0.3)
            print('   Effect: '+effect_names[mainhand[3]])
            sleep(0.3)
            print('   Power: '+effect_names[mainhand[4]])
        print('Offhand: '+inventory[6])
        sleep(0.3)
        print('   Damage: '+str(offhand[0]))
        sleep(0.3)
        print('   Block: '+str(offhand[1]))
        sleep(0.3)
        if not offhand[2]==0:
            print('   Target: '+targetdecision[offhand[2]-1])
            sleep(0.3)
            print('   Effect: '+effect_names[offhand[3]])
            sleep(0.3)
            print('   Power: '+effect_names[offhand[4]])
    elif (answer=='w') and (pp>59):
        pp-=60
    elif (answer=='a') and (pp>0) and not (pp==60 or pp==120 or pp==180 or pp==240):
        pp-=1
    elif (answer=='s') and (pp<300):
        pp+=60
    elif (answer=='d') and (pp<359) and not (pp==59 or pp==119 or pp==179 or pp==239):
        pp+=1
def detect():
    global collect_chance
    global encounter_chance
    global pp
    global ip
    if pp in ip:
        special_event()
        pass
    elif pp==359:
        final_battle()
    else:
        if randint(0,1)==1:
            if randint(0,99)<collect_chance:
                collect()
        else:
            if randint(0,99)<encounter_chance:
                encounter()
                pass
def special_event():
    global actual_events
    global ip
    global pp
    holder=0
    for i in range(6):
        if ip[i]==pp:
            holder=i
            break
    if actual_events[i]=='Magesmith':
        magesmith_encounter()
    elif actual_events[i]=='Shop':
        shop_encounter()
    elif actual_events[i]=='Chest':
        chest(holder)
    elif actual_events[i]=='Sage':
        sage_encounter()
    elif actual_events[i]=='Healer':
        healer()
def magesmith_encounter():
    global inventory
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global h_bonus
    global mainhand
    global offhand
    global inventorder
    global magesmith_location
    global pp
    global targetdecision
    print('"Hi!"')
    sleep(1)
    print('"I\'m Hunter, the Magesmith."')
    sleep(1)
    print('"I can upgrade your gear!"')
    sleep(1)
    print('"For the low price of 5 coins, I can upgrade a piece of gear for you!"')
    sleep(1)
    print('"You have '+str(inventory[7])+' coins."')
    answer=input('"So, is it a yes? (y or n)"')
    while True:
        answer=input('"So, is it a yes? (y or n)"')
        if answer=='y' or answer=='n':
            break
    if answer=='y':
        if inventory[7]>=5:
            inventory[7]-=5
            print('Great!')
            sleep(1)
            print('So, what peice will it be?')
            sleep(1)
            if True:
                print('Headgear: '+inventory[0])
                sleep(0.3)
                print('   Block: '+str(h_bonus[0]))
                sleep(0.3)
                if not h_bonus[1]==0:
                    print('   Effect: '+effect_names[h_bonus[1]])
                    sleep(0.3)
                    print('   Power: '+str(h_bonus[2]))
                    sleep(0.3)
                print('Chestpiece: '+inventory[1])
                sleep(0.3)
                print('   Block: '+str(c_bonus[0]))
                sleep(0.3)
                if not c_bonus[1]==0:
                    print('   Effect: '+effect_names[c_bonus[1]])
                    sleep(0.3)
                    print('   Power: '+str(c_bonus[2]))
                    sleep(0.3)
                print('Leggear: '+inventory[2])
                sleep(0.3)
                print('   Block: '+str(l_bonus[0]))
                sleep(0.3)
                if not l_bonus[1]==0:
                    print('   Effect: '+effect_names[l_bonus[1]])
                    sleep(0.3)
                    print('   Power: '+str(l_bonus[2]))
                    sleep(0.3)
                print('Footgear: '+inventory[3])
                sleep(0.3)
                print('   Block: '+str(f_bonus[0]))
                sleep(0.3)
                if not f_bonus[1]==0:
                    print('   Effect: '+effect_names[f_bonus[1]])
                    sleep(0.3)
                    print('   Power: '+str(f_bonus[2]))
                    sleep(0.3)
                print('Handgear: '+inventory[4])
                sleep(0.3)
                print('   Block: '+str(ha_bonus[0]))
                sleep(0.3)
                if not ha_bonus[1]==0:
                    sleep(0.3)
                    print('   Effect: '+effect_names[ha_bonus[1]])
                    sleep(0.3)
                    print('   Power: '+str(ha_bonus[2]))
                    sleep(0.3)
                print('Mainhand: '+inventory[5])
                sleep(0.3)
                print('   Damage: '+str(mainhand[0]))
                sleep(0.3)
                print('   Block: '+str(mainhand[1]))
                sleep(0.3)
                if not mainhand[2]==0:
                    print('   Target: '+targetdecision[mainhand[2]-1])
                    sleep(0.3)
                    print('   Effect: '+effect_names[mainhand[3]])
                    sleep(0.3)
                    print('   Power: '+effect_names[mainhand[4]])
                print('Offhand: '+inventory[6])
                sleep(0.3)
                print('   Damage: '+str(offhand[0]))
                sleep(0.3)
                print('   Block: '+str(offhand[1]))
                sleep(0.3)
                if not offhand[2]==0:
                    print('   Target: '+targetdecision[offhand[2]-1])
                    sleep(0.3)
                    print('   Effect: '+effect_names[offhand[3]])
                    sleep(0.3)
                    print('   Power: '+effect_names[offhand[4]])
            answer=input('''Type in h for headgear, c for chestpiece, l for legpiece, f for footgear, ha for handgear, m for mainhand, 
            and o for offhand.''')
            while not answer in 'h c l f ha m o'.split():
                print('"Try again, bozo."')
                sleep(1)
                answer=input('''Type in h for headgear, c for chestpiece, l for legpiece, f for footgear, ha for handgear, m for mainhand, 
                and o for offhand.''')
                sleep(1)
            if answer=='h':
                h_bonus[0]+=5
                inventory[0]+=' (upgraded)'
                print('K, I upgraded your headgear!')
            elif answer=='c':
                c_bonus[0]+=5
                inventory[1]+=' (upgraded)'
                print('K, I upgraded your chestpiece!')
            elif answer=='l':
                l_bonus[0]+=5
                inventory[2]+=' (upgraded)'
                print('K, I upgraded your legpiece!')
            elif answer=='f':
                f_bonus[0]+=5
                inventory[3]+=' (upgraded)'
                print('K, I upgraded your footgear!')
            elif answer=='ha':
                ha_bonus[0]+=5
                inventory[4]+=' (upgraded)'
                print('K, I upgraded your handgear!')
            elif answer=='m':
                mainhand[0]+=3
                mainhand[1]+=3
                inventory[5]+=' (upgraded)'
                print('K, I upgraded your mainhand!')
            else:
                offhand[0]+=3
                offhand[1]+=3
                inventory[6]+=' (upgraded)'
                print('K, I upgraded your offhand!')
        else:
            print('Sorry, you don\'t have enough.')
        sleep(1)
    if magesmith_location==1000000000:
        print('"I added my spot to the map... if you ever need to see me again, just stop by!"')
        magesmith_location=pp
    else:
        print('"See ya later!"')
    pass
def shop_encounter():
    global shop
    global items_collectable
    global adjective
    global inventory
    global souls
    global pp
    global shop_location
    global effect_names
    global inventory
    soul_constant=ceil(souls/2)
    costs=[randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3)),randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3)),
    randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3)),randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3)),
    randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3)),randint( (1* ceil(souls/2 * 1) ),3*ceil(souls/2*3))]
    print('"Yo!"')
    sleep(1)
    print('"My name\'s Aiden!"')
    sleep(1)
    print('"I have some stuff you might want to buy..."')
    sleep(1)
    for i in range(6):
        print('"Item number '+str(i+1)+'!"')
        current_item=items_collectable[shop[i]]
        sleep(1)
        if str(i+1) in purchasable_items:
            print('I have this '+adjective[randint(1,len(adjective)-1)]+' '+current_item[0]+'...')
            if current_item[len(current_item)-1]=='w':
                print('It\'s a weapon...')
                sleep(1)
                print('It has '+str(current_item[1]*soul_constant)+' damage and '+str(current_item[2]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[3]==0:
                    if current_item[3]==1:
                        print('It gives you level '+str(current_item[5])+' '+effect_names[current_item[4]]+'...')
                    else:
                        print('It gives your enemies level '+str(current_item[5])+' '+effect_names[current_item[4]]+'...')
                    sleep(0.3)
            elif current_item[len(current_item)-1]=='h':
                print('It\'s a headgear...')
                sleep(0.3)
                print('It gives you '+str(current_item[1]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[2]==0:
                   print('It gives you level '+str(current_item[3])+' '+effect_names[current_item[2]]+' every turn...')
                   sleep(0.3)
            elif current_item[len(current_item)-1]=='c':
                print('It\'s a chestpiece...')
                sleep(0.3)
                print('It gives you '+str(current_item[1]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[2]==0:
                    print('It gives you level '+str(current_item[3])+' '+effect_names[current_item[2]]+' every turn...')
                    sleep(0.3)
            elif current_item[len(current_item)-1]=='l':
                print('It\'s a leggear...')
                sleep(0.3)
                print('It gives you '+str(current_item[1]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[2]==0:
                    print('It gives you level '+str(current_item[3])+' '+effect_names[current_item[2]]+' every turn...')
                    sleep(0.3)
            elif current_item[len(current_item)-1]=='f':
                print('It\'s a footgear...')
                sleep(0.3)
                print('It gives you '+str(current_item[1]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[2]==0:
                    print('It gives you level '+str(current_item[3])+' '+effect_names[current_item[2]]+' every turn...')
                    sleep(0.3)
            elif current_item[len(current_item)-1]=='ha':
                print('It\'s a handgear...')
                sleep(0.3)
                print('It gives you '+str(current_item[1]*soul_constant)+' block...')
                sleep(0.3)
                if not current_item[2]==0:
                    print('It gives you level '+str(current_item[3])+' '+effect_names[current_item[2]]+' every turn...')
                    sleep(0.3)
            print('It costs '+str(costs[i])+'.')
            print('---------------------------'.center(106,' '))
    answer=(input('"K, you wanna buy anything? (input the item number of the thing you want to purchase.)"'))
    while answer in purchasable_items:
        if inventory[7]>=costs[int(answer)-1]:
            current_item=items_collectable[shop[int(answer)-1]]
            sanswer=input('"Okay, you\'re getting the '+current_item[0]+'?" (y or n)')
            if sanswer=='y':
                if current_item[len(current_item)-1]=='w':
                    sanswer=str(input('Mainhand or offhand? (m or o)'))
                    if sanswer=='m':
                        inventory[5]=current_item[0]
                        mainhand[0]=current_item[1]*soul_constant
                        mainhand[1]=current_item[2]*soul_constant
                        mainhand[2]=current_item[3]
                        mainhand[3]=current_item[4]
                        mainhand[4]=current_item[5]
                        purchasable_items.pop(purchasable_items.index(answer))
                        print('"Okay, there you go!"')
                    else:
                        inventory[6]=current_item[0]
                        offhand[0]=current_item[1]*soul_constant
                        offhand[1]=current_item[2]*soul_constant
                        offhand[2]=current_item[3]
                        offhand[3]=current_item[4]
                        offhand[4]=current_item[5]
                        purchasable_items.pop(purchasable_items.index(answer))
                        print('"Okay, there you go!"')
                elif current_item[len(current_item)-1]=='h':
                    inventory[0]=current_item[0]
                    h_bonus[0]=current_item[1]*soul_constant
                    h_bonus[1]=current_item[2]
                    h_bonus[2]=current_item[3]
                    purchasable_items.pop(purchasable_items.index(answer))
                    print('"Okay, there you go!"')
                elif current_item[len(current_item)-1]=='c':
                    inventory[1]=current_item[0]
                    c_bonus[0]=current_item[1]*soul_constant
                    c_bonus[1]=current_item[2]
                    c_bonus[2]=current_item[3]
                    purchasable_items.pop(purchasable_items.index(answer))
                    print('"Okay, there you go!"')
                elif current_item[len(current_item)-1]=='l':
                    inventory[2]=current_item[0]
                    l_bonus[0]=current_item[1]*soul_constant
                    l_bonus[1]=current_item[2]
                    l_bonus[2]=current_item[3]
                    purchasable_items.pop(purchasable_items.index(answer))
                    print('"Okay, there you go!"')
                elif current_item[len(current_item)-1]=='f':
                    inventory[3]=current_item[0]
                    f_bonus[0]=current_item[1]*soul_constant
                    f_bonus[1]=current_item[2]
                    f_bonus[2]=current_item[3]
                    purchasable_items.pop(purchasable_items.index(answer))
                    print('"Okay, there you go!"')
                elif current_item[len(current_item)-1]=='ha':
                    inventory[4]=current_item[0]
                    ha_bonus[0]=current_item[1]*soul_constant
                    ha_bonus[1]=current_item[2]
                    ha_bonus[2]=current_item[3]
                    purchasable_items.pop(purchasable_items.index(answer))
                    print('"Okay, there you go!"')
            else:
                print('Okay then.')
                sleep(0.3)
        answer=(input('"You wanna buy anything else?" (input the item number of the thing you want to purchase.)'))
    if shop_location==1000000000:
        print('"See ya! Also, I put my location on the map if you need to find me again."')
        shop_location=pp
    else:
        print('"Bye!"')
    pass
def sage_encounter():
    global inventory
    global name
    global pp
    global sage_position
    print('"Hello, '+name+'."')
    sleep(1)
    print('"Do not be alarmed."')
    sleep(1)
    print('"I am William, the sage."')
    sleep(1)
    if True:
        answer=input('"Have you come here seeking knowledge?" (y or n)')
        if answer=='y':
            print('"Then I will give it to you."')
            sleep(2)
            print('"Of what subject do you wish to speak?"')
            answer=input('Enter p for this place, y for you, m for magesmith, s for shopkeeper, b for the Beast, n for nevermind.')
            if answer=='p':
                print('"This is the gremlin closet, a place full of dark energy and strange beasts."')
                sleep(2)
                print('"It is formed of pure darkness, and will corrupt you if you stay too long."')
                sleep(2)
                print('Will pulls back a sleeve of his robe, revealing a dark purple blotch on his forearm.')
                sleep(2)
                print('"That is what this cursed place gave to me. It will continue growing until..."')
                sleep(2)
                print('"Until it takes over my mind."')
                sleep(2)
                print('Will seems exhausted.')
                sleep(2)
                print('"Goodbye, '+name+ '."')
                sleep(2)
                print('You leave, unsettled.')
            if answer=='y':
                print('"You wish to know about me?"')
                sleep(2)
                print('"I fell in here some time ago..."')
                sleep(2)
                print('"I think I turned 13 around 3 weeks ago...?"')
                sleep(2)
                print('"I found this tower, and I have stayed here since, gathering knowledge and reading from the vast library."')
                sleep(2)
                print('"My only purpose is to guide travelers like you back home."')
                sleep(2)
                print('Will seems depressed.')
                sleep(2)
                print('"Goodbye, '+name+'."')
            if answer=='m':
                print('"Hunter is a member of an ancient order of mages."')
                sleep(2)
                print('"He knows even more magic than I do."')
                sleep(2)
                print('"If you have any questions about magic, you should probably ask him."')
                sleep(2)
                print('"He can make weapons even more powerful than they already are."')
                sleep(2)
                print('"He fell down here around 3 years ago, right after me."')
                sleep(2)
                print('"Goodbye, '+name+'."')
            if answer=='s':
                print('"Alas, I don\'t know the shopkeeper..."')
                sleep(2)
                print('"All I know is he runs around killing things to find more money and loot."')
                sleep(2)
                print('"Goodbye, '+name+'."')
            if answer=='b':
                print('Will visibly becomes uncomfortable.')
                sleep(2)
                print('"The Beast..."')
                sleep(2)
                print('"It is said that he is the first kid to fall down here."')
                sleep(2)
                print('"Eventually, the darkness took over his mind."')
                sleep(2)
                print('"Now, he waits, serving the darkness, biding his time before another becomes corrupt."')
                sleep(2)
                print('"You are not the first to come here to retreive something."')
                sleep(2)
                print('"It was most likely stolen by the Beast."')
                sleep(2)
                print('"He waits for you to come so that he can corrupt you."')
                sleep(2)
                print('"It has happened to so many others..."')
                sleep(2)
                print('Will whispers a barely audible name as he blinks away a single tear.')
                sleep(2)
                print('"I\'m afraid you cannot defeat him."')
                sleep(2)
                print('"Goodbye, '+name+'."')
        else:
            print('"Then goodbye, '+name+'."')
        sage_position=pp
def chest(ind):
    global inventory
    global inventorder
    global effect_names
    global actual_events
    global ip
    print('You found a chest!')
    sleep(0.5)
    for i in range(randint(3,6)):
        collect()
        print('---------------------------'.center(106,' '))
    extra=randint(1,20)
    print('You also found '+str(extra)+' coins.')
    inventory[7]+=extra
    ip.pop(ind)
    actual_events.pop(ind)
def healer():
    global phealth
    global inventory
    global heal_position
    global pp
    holder=[]
    print('"I am Brynn, a master of the healing arts."')
    sleep(2)
    print('"For a cost, I can heal your wounds."')
    sleep(2)
    answer=input('"Would you like to be healed?" (y or n)')
    if answer=='y':
        print('"Ah, lovely. I will heal 3 points of damage for every coin you pay me."')
        sleep(2)
        answer=input('Enter how many coins you will pay Brynn (a whole number from 0 to '+str(inventory[7])+')')
        for i in range(inventory[7]):
            holder.append(str(i))
        if answer in holder:
            answer=int(answer)
            if answer>0 and answer<=inventory[7]:
                phealth+=answer*3
                inventory[7]-=answer
                print('"I have healed you."')
            else:
                print('"You don\'t have enough money."')
        else:
            print('"That\'s not a number..."')
        if heal_position==1000000000:
            print('"I have put my location on the map, if you need me again."')
            heal_position=pp
        else:
            print('"Goodbye, traveler."')
def collect():
    global collected_item
    global collect_index
    global items_collectable
    global effect_names
    global inventory
    global mainhand
    global offhand
    global items_interpret
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global putdown
    collect_index=randint(0,len(items_collectable)-1)
    collected_item = items_collectable[collect_index]
    while collected_item[0]=='Ravens Jersey':
        collect_index=randint(0,len(items_collectable)-1)
        collected_item = items_collectable[collect_index]
    soul_constant=ceil(souls/2)
    print('You found a '+collected_item[0]+'!')
    sleep(0.3)
    if collected_item[len(collected_item)-1]=='w':
        print('It has '+str(collected_item[1]*soul_constant)+' damage and '+str(collected_item[2]*soul_constant)+' block.')
        sleep(0.3)
        if not collected_item[3]==0:
            if collected_item[3]==1:
                print('It gives level '+str(collected_item[5])+' '+effect_names[collected_item[4]])
            else:
                print('It inflicts level '+str(collected_item[5])+' '+effect_names[collected_item[4]]+' upon thy enemies!')
        sleep(0.3)
        print('Your current mainhand weapon is '+inventory[5]+'.')
        sleep(0.3)
        print('It has '+str(mainhand[0])+' damage and '+str(mainhand[1])+' block.')
        sleep(0.3)
        if not mainhand[2]==0:
            if mainhand[2]==1:
                print('It gives level '+str(mainhand[4])+' '+effect_names[mainhand[3]])
            else:
                print('It inflicts level '+str(mainhand[4])+' '+effect_names[mainhand[3]]+' upon thy enemies!')
            sleep(0.3)
        print('Your current offhand weapon is '+inventory[6]+'.')
        sleep(0.3)
        print('It has '+str(offhand[0])+' damage and '+str(offhand[1])+' block.')
        sleep(0.3)
        if not offhand[2]==0:
            sleep(0.3)
            if offhand[2]==1:
                print('It gives level '+str(offhand[4])+' '+effect_names[offhand[3]])
            else:
                
                print('It inflicts level '+str(offhand[4])+' '+effect_names[offhand[3]]+' upon thy enemies!')
            sleep(0.3)
        while True:
            action=str(input('Will you take it? (m to replace mainhand, o to replace offhand, or l to leave it.)'))
            sleep(0.3)
            if action == 'm':
                mainhand=collected_item[1:5]
                inventory[5]=collected_item[0]
                break
            if action in 'm o l'.split():
                break
            print('Try again.')
        if action=='m':
            mainhand=collected_item[1:6]
            inventory[5]=collected_item[0]
        if action=='o':
            offhand=collected_item[1:6]
            inventory[6]=collected_item[0]
        elif action == 'l':
            print(putdown[randint(0,len(putdown)-1)])
    elif collected_item[len(collected_item)-1]=='h':
        print('It gives you '+str(collected_item[1]*soul_constant)+' block every turn.')
        sleep(0.3)
        if not collected_item[2]==0:
            print('It gives you +'+str(collected_item[3])+' '+effect_names[collected_item[2]]+' every turn.')
            sleep(0.3)
        print('It is a headgear. Your current headgear is '+inventory[0]+'.') 
        sleep(0.3)
        print('It currently gives you '+str(h_bonus[0])+' block every turn.')
        sleep(0.3)
        if not h_bonus[1]==0:
            print('It gives you +'+str(h_bonus[2])+' '+effect_names[h_bonus[1]]+' every turn.')
            sleep(0.3)
        answer=str(input('Will you take it? (y or n)'))
        sleep(0.3)
        while not answer in 'y n'.split():
            answer=str(input('Will you take it? (y or n)'))
        if answer=='y':
            print('You equipped the '+collected_item[0]+'!')
            sleep(0.3)
            h_bonus[0]=collected_item[1]*soul_constant
            h_bonus[1]=collected_item[2]
            h_bonus[2]=collected_item[3]*soul_constant
            inventory[0]=collected_item[0]
        else:
            print(putdown[randint(0,len(putdown)-1)])
            sleep(0.3)
    elif collected_item[len(collected_item)-1]=='c':
        print('It gives you '+str(collected_item[1]*soul_constant)+' block every turn.')
        sleep(0.3)
        if not collected_item[2]==0:
            print('It gives you +'+str(collected_item[3])+' '+effect_names[collected_item[2]]+' every turn.')
            sleep(0.3)
        print('It is a chestpiece. Your current chestpiece is '+inventory[1]+'.') 
        sleep(0.3)
        print('It currently gives you '+str(c_bonus[0])+' block every turn.')
        sleep(0.3)
        if not c_bonus[1]==0:
            print('It gives you +'+str(c_bonus[2])+' '+effect_names[c_bonus[1]]+' every turn.')
            sleep(0.3)
        answer=str(input('Will you take it? (y or n)'))
        sleep(0.3)
        while not answer in 'y n'.split():
            answer=str(input('Will you take it? (y or n)'))
            sleep(0.3)
        if answer=='y':
            print('You equipped the '+collected_item[0]+'!')
            sleep(0.3)
            c_bonus[0]=collected_item[1]*soul_constant
            c_bonus[1]=collected_item[2]
            c_bonus[2]=collected_item[3]*soul_constant
            inventory[1]=collected_item[0]
        else:
            print(putdown[randint(0,len(putdown)-1)])
            sleep(0.3)
    elif collected_item[len(collected_item)-1]=='l':
        print('It gives you '+str(collected_item[1]*soul_constant)+' block every turn.')
        sleep(0.3)
        if not collected_item[2]==0:
            print('It gives you +'+str(collected_item[3])+' '+effect_names[collected_item[2]]+' every turn.')
            sleep(0.3)
        print('It is a legpiece. Your current legpiece is '+inventory[2]+'.') 
        sleep(0.3)
        print('It currently gives you '+str(l_bonus[0])+' block every turn.')
        sleep(0.3)
        if not l_bonus[1]==0:
            print('It gives you +'+str(l_bonus[2])+' '+effect_names[l_bonus[1]]+' every turn.')
            sleep(0.3)
        answer=str(input('Will you take it? (y or n)'))
        sleep(0.3)
        while not answer in 'y n'.split():
            answer=str(input('Will you take it? (y or n)'))
            sleep(0.3)
        if answer=='y':
            print('You equipped the '+collected_item[0]+'!')
            sleep(0.3)
            l_bonus[0]=collected_item[1]*soul_constant
            l_bonus[1]=collected_item[2]
            l_bonus[2]=collected_item[3]*soul_constant
            inventory[2]=collected_item[0]
        else:
            print(putdown[randint(0,len(putdown)-1)])
            sleep(0.3)
    elif collected_item[len(collected_item)-1]=='f': #footgear
        print('It gives you '+str(collected_item[1]*soul_constant)+' block every turn.')
        sleep(0.3)
        if not collected_item[2]==0:
            print('It gives you +'+str(collected_item[3])+' '+effect_names[collected_item[2]]+' every turn.')
            sleep(0.3)
        print('It is a footgear. Your current footgear is '+inventory[3]+'.') 
        sleep(0.3)
        print('It currently gives you '+str(f_bonus[0])+' block every turn.')
        sleep(0.3)
        if ha_bonus != 0:
            print('It gives you +'+str(f_bonus[2])+' '+effect_names[f_bonus[1]]+' every turn.')
            sleep(0.3)
        answer=str(input('Will you take it? (y or n)'))
        sleep(0.3)
        while not answer in 'y n'.split():
            answer=str(input('Will you take it? (y or n)'))
            sleep(0.3)
        if answer=='y':
            print('You equipped the '+collected_item[0]+'!')
            sleep(0.3)
            f_bonus[0]=collected_item[1]*soul_constant
            f_bonus[1]=collected_item[2]
            f_bonus[2]=collected_item[3]*soul_constant
            inventory[3]=collected_item[0]
        else:
            print(putdown[randint(0,len(putdown)-1)])
            sleep(0.3)
    elif collected_item[len(collected_item)-1]=='ha': #handgear
        print('It gives you '+str(collected_item[1]*soul_constant)+' block every turn.')
        sleep(0.3)
        if not collected_item[2]==0:
            print('It gives you +'+str(collected_item[3])+' '+effect_names[collected_item[2]]+' every turn.')
            sleep(0.3)
        print('It is a handpiece. Your current handpiece is '+inventory[4]+'.') 
        sleep(0.3)
        print('It currently gives you '+str(ha_bonus[0])+' block every turn.')
        sleep(0.3)
        if not c_bonus[1]==0:
            print('It gives you +'+str(ha_bonus[2])+' '+effect_names[ha_bonus[1]]+' every turn.')
            sleep(0.3)
        answer=str(input('Will you take it? (y or n)'))
        sleep(0.3)
        while not answer in 'y n'.split():
            answer=str(input('Will you take it? (y or n)'))
            sleep(0.3)
        if answer=='y':
            print('You equipped the '+collected_item[0]+'!')
            sleep(0.3)
            ha_bonus[0]=collected_item[1]*soul_constant
            ha_bonus[1]=collected_item[2]
            ha_bonus[2]=collected_item[3]*soul_constant
            inventory[4]=collected_item[0]
        else:
            print(putdown[randint(0,len(putdown)-1)])
            sleep(0.3)
    pass
def encounter():
    global enemy_names
    global phealth
    global pdefense
    global pdamage
    global souls
    global enemy_damage
    global enemy_defense
    global enemy_health
    global player_effects
    global enemy_effects
    player_effects=[0,0,0,0,0,0]
    enemy_effects=[0,0,0,0,0,0]
    enemy_seed=randint(0,len(enemy_names)-1)
    enemy_health=souls+1*randint(1,3)+5
    enemy_defense=souls+1*randint(0,2)
    enemy_damage=souls+1*randint(1,3)
    enemy_data=[enemy_health,enemy_defense,enemy_damage]
    print('You have encountered '+enemy_names[enemy_seed]+'!')
    for i in range(3):
        print(enemy_print[i]+str(enemy_data[i]))
    while enemy_health>0:
        enemyturn()
        playerturn()
        aftermath()
    sleep(0.3)
    print('You have defeated '+enemy_names[enemy_seed]+'!')
    sleep(0.3)
    extra=randint(1,3)*souls
    souls+=1
    inventory[7]+=extra
    print('You have gained '+str(extra)+' coins!')
    sleep(0.3)
    collect()
    pass
def enemyturn():
    global enemy_damage
    global enemy_defense
    global enemy_current_damage
    global enemy_current_block
    global souls
    global player_effects
    global enemy_effects
    global enemy_buff
    global enemy_debuff
    global effect_names
    global effect_print
    enemy_debuff=[0,0]
    enemy_buff=[0,0]
    if randint(1,2)==2:
        enemy_current_damage=enemy_damage+(randint(0,3)*souls)+enemy_effects[3] - enemy_effects[2]
        enemy_current_block=0
        print('Enemy will attack for '+str(enemy_current_damage)+'!')
    else:
        enemy_current_damage=0
        enemy_current_block=enemy_defense+(randint(0,3)*souls) + enemy_effects[5] - enemy_effects[4]
        print('Enemy will block for '+str(enemy_current_block)+'!')
    if randint(1,10)==1 and souls>5:
        if randint(1,2)==2:
            enemy_buff[0]=(2*randint(1,3))-1
            enemy_buff[1]=randint(1,souls)
            print('Enemy will gain '+effect_names[enemy_buff[0]]+' at level '+str(enemy_buff[1])+'!')
        else:
            enemy_debuff[0]=(2*randint(1,3))-2
            enemy_debuff[1]=randint(1,souls)
            print('Enemy will inflict '+effect_names[enemy_debuff[0]]+' at level '+str(enemy_debuff[1])+'!')
def playerturn():
    global effect_print
    global mainhand
    global offhand
    global player_effects
    global player_current_damage
    global player_current_block
    global effect_names
    global inventory
    global inventorder
    global player_debuff
    global player_buff
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global enemy_effects
    player_buff=[0,0]
    player_debuff=[0,0]
    player_current_block=0
    player_current_damage=0
    if True:
        if not h_bonus[1]==0:
            player_effects[h_bonus[1]]+=h_bonus[2]
        if not c_bonus[1]==0:
            player_effects[c_bonus[1]]+=c_bonus[2]
        if not l_bonus[1]==0:
            player_effects[l_bonus[1]]+=l_bonus[2]
        if not f_bonus[1]==0:
            player_effects[f_bonus[1]]+=f_bonus[2]
        if not ha_bonus[1]==0:
            player_effects[ha_bonus[1]]+=ha_bonus[2]
    player_current_block+=h_bonus[0]+player_effects[5]
    player_current_block+=c_bonus[0]+player_effects[5]
    player_current_block+=l_bonus[0]+player_effects[5]
    player_current_block+=f_bonus[0]+player_effects[5]
    player_current_block+=ha_bonus[0]+player_effects[5]
    player_debuff=[0,0]
    player_buff=[0,0]
    while True:
        action=input('What will you do? (m for mainhand, o for offhand, s to skip, i for info)').lower()
        if action=='i':
            print('Player:')
            for c in range(8):
                print(inventorder[c]+str(inventory[c]))
                sleep(0.1)
            for c in range(6):
                print(effect_print[c]+str(player_effects[c]))
                sleep(0.1)
            print('Enemy:')
            for c in range(6):
                print(effect_print[c]+str(enemy_effects[c]))
                sleep(0.1)
        elif action in 'm o s'.split():
            break
        else:
            print('Invalid action.')
    if action == 'm':
        player_current_damage+=(mainhand[0]- player_effects[2]) + player_effects[3]
        player_current_block+=(mainhand[1] - player_effects[4]) + player_effects[5]
        print(name+' will attack for '+str(player_current_damage)+' and block for '+str(player_current_block)+'!')
        if not mainhand[2] == 0:
            if mainhand[2]==1:
                player_buff[0]=mainhand[3]
                player_buff[1]=mainhand[4]
                print(name+' will gain level '+str(player_buff[1])+' '+effect_names[player_buff[0]]+'!')
            else:
                player_debuff[0]=mainhand[3]
                player_debuff[1]=mainhand[4]
                print(name+' will inflict level '+str(player_debuff[1])+' '+effect_names[player_debuff[0]]+'!')
    if action == 'o':
        player_current_damage+=(offhand[0]- player_effects[2]) + player_effects[3]
        player_current_block+=(offhand[1] - player_effects[4]) + player_effects[5]
        print(name+' will attack for '+str(player_current_damage)+' and block for '+str(player_current_block)+'!')
        if not offhand[2] == 0:
            if offhand[2]==1:
                player_buff[0]=offhand[3]
                player_buff[1]=offhand[4]
                print(name+' will gain level '+str(player_buff[1])+' '+effect_names[player_buff[0]]+'!')
            else:
                player_debuff[0]=offhand[3]
                player_debuff[1]=offhand[4]
                print(name+' will inflict level '+str(player_debuff[1])+' '+effect_names[player_debuff[0]]+'!')
    player_current_block+=h_bonus[0]
    player_current_block+=c_bonus[0]
    player_current_block+=l_bonus[0]
    player_current_block+=f_bonus[0]
    player_current_block+=ha_bonus[0]
    pass
def aftermath():
    global effect_names
    global effect_print
    global enemy_health
    global enemy_current_block
    global enemy_current_damage
    global enemy_debuff
    global enemy_buff
    global enemy_effects
    global phealth
    global player_current_block
    global player_current_damage
    global player_debuff
    global player_buff
    global player_effects
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global name
    global souls
    for c in range(6):
        if player_effects[c] > 0:
            player_effects[c]-=1
        if enemy_effects[c] > 0:
            enemy_effects[c]-=1
    if phealth<1: print('You died.'),quit()
    taken_damage=player_current_damage - enemy_current_block
    if taken_damage<1: taken_damage=0
    enemy_health-=taken_damage
    print('Enemy took '+str(taken_damage)+' damage! They have '+str(enemy_health)+' remaining!')
    sleep(1)
    if not player_debuff == [0,0]:
        print('Enemy became debufffed with '+effect_names[player_debuff[0]]+' at level '+str(player_debuff[1])+'!')
        enemy_effects[player_debuff[0]]+=player_debuff[1]
    if not enemy_buff == [0,0]:
        print('Enemy gained '+effect_names[enemy_buff[0]]+'!')
        enemy_effects[enemy_buff[0]]+=enemy_buff[1]
    taken_damage= enemy_current_damage - player_current_block
    if taken_damage<1: taken_damage=0
    phealth-=taken_damage
    sleep(1)
    print(name+' took '+str(taken_damage)+' damage! They have '+str(phealth)+' remaining!')
    sleep(1)
    if not enemy_debuff == [0,0]:
        print(name+' became debufffed with '+effect_names[enemy_debuff[0]]+' at level '+str(enemy_debuff[1])+'!')
        player_effects[enemy_debuff[0]]+=enemy_debuff[1]
    if not player_buff == [0,0]:
        print(name+' gained '+effect_names[player_buff[0]]+'!')
        player_effects[player_buff[0]]+=player_buff[1]
    if enemy_effects[0]>0: 
        enemy_health -= int(enemy_effects[0])
        print('Enemy took '+str(enemy_effects[0])+' poison damage!')
    if player_effects[0]>0: 
        phealth -= int(player_effects[0])
        print(name+' took '+str(player_effects[0])+' poison damage!')
    if enemy_effects[1]>0: 
        enemy_health += int(enemy_effects[1])
        print('Enemy gained '+str(enemy_effects[1])+' health from regen!')
    if player_effects[1]>0: 
        phealth += int(player_effects[1])
        print(name+' gained '+str(player_effects[1])+' health from regen!')
    pass
def final_battle():
    global enemy_health
    global enemy_damage
    global enemy_defense
    global turns
    print('You see your engineering project, and quickly run towards it, happy to finally find it.')
    sleep(2)
    print('"Hello there~" A voice behind you says. Startled, you turn around.')
    sleep(2)
    print('Before you, there is a boy. He has dark purple skin, and his hair is jet black. He watches you with cold eyes, smirking.')
    sleep(2)
    print('"Took you long enough to arrive." He says, beginning to circle around you.')
    sleep(2)
    print('"Now, I can finally get a new servant."')
    sleep(2)
    print('He laughs, and then lunges towards you.')
    sleep(2)
    print('This is it.')
    sleep(2)
    print('You have encountered the Beast!')
    sleep(1)
    enemy_health=666
    enemy_defense=20
    enemy_damage=30
    turns=5
    while enemy_health>0:
        bossturn()
        playerbossturn()
        aftermathboss()
    finish()
    pass
def bossturn():
    global enemy_effects
    global enemy_health
    global turns
    global boss_block
    global boss_damage
    global boss_effect
    boss_effect=[0,0,0]
    boss_block=0
    boss_damage=0
    turns+=1
    if randint(1,3)==1:
        boss_block += randint(1*turns , 5 *turns) +enemy_effects[5] - enemy_effects[4]
        boss_damage+=randint(round((1*turns)/2),round((5*turns)/2))+enemy_effects[3] - enemy_effects[2]
    elif randint(1,2)==1:
        boss_damage += randint(round( 1 * turns) , round(5 * turns)) + enemy_effects[5] - enemy_effects[4]
        boss_block+=randint(round((1*turns)/2),round((5*turns)/2))+enemy_effects[3] - enemy_effects[2]
    else:
        pick=randint(0,1)
        if pick==1:
            boss_effect[0]=1
            boss_effect[1]=(randint(1,4)*2)-2
            boss_effect[2]=randint(round(turns/2),turns)
        else:
            boss_effect[0]=2
            boss_effect[1]=(randint(1,3)*2)-1
            boss_effect[2]=randint(round(turns/2),turns)
    if boss_damage>0:
        print('The Beast will block for '+str(boss_block)+' and will attack for '+str(boss_damage)+'.')
    else:
        if boss_effect[0]==1:
            print('The Beast will inflict '+effect_names[boss_effect[1]]+' at level '+str(boss_effect[2])+'.')
def playerbossturn():
    global effect_print
    global mainhand
    global offhand
    global player_effects
    global player_current_damage
    global player_current_block
    global effect_names
    global inventory
    global inventorder
    global player_debuff
    global player_buff
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    if True:
        if not h_bonus[1]==0:
            player_effects[h_bonus[1]]+=h_bonus[2]
        if not c_bonus[1]==0:
            player_effects[c_bonus[1]]+=c_bonus[2]
        if not l_bonus[1]==0:
            player_effects[l_bonus[1]]+=l_bonus[2]
        if not f_bonus[1]==0:
            player_effects[f_bonus[1]]+=f_bonus[2]
        if not ha_bonus[1]==0:
            player_effects[ha_bonus[1]]+=ha_bonus[2]
    player_current_block+=h_bonus[0]+player_effects[5]
    player_current_block+=c_bonus[0]+player_effects[5]
    player_current_block+=l_bonus[0]+player_effects[5]
    player_current_block+=f_bonus[0]+player_effects[5]
    player_current_block+=ha_bonus[0]+player_effects[5]
    player_debuff=[0,0]
    player_buff=[0,0]
    player_effects=[0,0,0,0,0,0,0]
    while True:
        action=input('What will you do? (m for mainhand, o for offhand, s to skip, g to give up, i for info)').lower()
        if action=='i':
            print('Player:')
            for c in range(8):
                print(inventorder[c]+str(inventory[c]))
                sleep(0.1)
            for c in range(6):
                print(effect_print[c]+str(player_effects[c]))
                sleep(0.1)
            print('Enemy:')
            for c in range(6):
                print(effect_print[c]+str(enemy_effects[c]))
                sleep(0.1)
        elif action in 'm o s g'.split():
            break
        else:
            print('Invalid action.')
    if action == 'm':
        player_current_damage+=(mainhand[0]- player_effects[2]) + player_effects[3]
        player_current_block+=(mainhand[1] - player_effects[4]) + player_effects[5]
        print(name+' will attack for '+str(player_current_damage)+' and block for '+str(player_current_block)+'!')
        if not mainhand[2] == 0:
            if mainhand[2]==1:
                player_buff[0]=mainhand[3]
                player_buff[1]=mainhand[4]
                print(name+' will gain level '+str(player_buff[1])+' '+effect_names[player_buff[0]]+'!')
            else:
                player_debuff[0]=mainhand[3]
                player_debuff[1]=mainhand[4]
                print(name+' will inflict level '+str(player_debuff[1])+' '+effect_names[player_debuff[0]]+'!')
    elif action == 'o':
        player_current_damage+=(offhand[0]- player_effects[2]) + player_effects[3]
        player_current_block+=(offhand[1] - player_effects[4]) + player_effects[5]
        print(name+' will attack for '+str(player_current_damage)+' and block for '+str(player_current_block)+'!')
        if not offhand[2] == 0:
            if offhand[2]==1:
                player_buff[0]=offhand[3]
                player_buff[1]=offhand[4]
                print(name+' will gain level '+str(player_buff[1])+' '+effect_names[player_buff[0]]+'!')
            else:
                player_debuff[0]=offhand[3]
                player_debuff[1]=offhand[4]
                print(name+' will inflict level '+str(player_debuff[1])+' '+effect_names[player_debuff[0]]+'!')
    elif action=='g':
        give_up()
    else:
        print(name+' will skip!')
    player_current_block+=h_bonus[0]
    player_current_block+=c_bonus[0]
    player_current_block+=l_bonus[0]
    player_current_block+=f_bonus[0]
    player_current_block+=ha_bonus[0]
def aftermathboss():
    global effect_names
    global effect_print
    global enemy_health
    global boss_block
    global boss_damage
    global boss_effect
    global enemy_effects
    global phealth
    global player_current_block
    global player_current_damage
    global player_debuff
    global player_buff
    global player_effects
    global h_bonus
    global c_bonus
    global l_bonus
    global f_bonus
    global ha_bonus
    global name
    for c in range(6):
        if player_effects[c] > 0:
            player_effects[c]-=1
        if enemy_effects[c] > 0:
            enemy_effects[c]-=1
    if phealth<1: print('You died.'),quit()
    taken_damage=player_current_damage - boss_block
    if taken_damage<1: taken_damage=0
    enemy_health-=taken_damage
    print('The Beast took '+str(taken_damage)+' damage! They have '+str(enemy_health)+' remaining!')
    sleep(1)
    if not player_debuff == [0,0]:
        print('The Beast became debufffed with '+effect_names[player_debuff[0]]+' at level '+str(player_debuff[1])+'!')
        enemy_effects[player_debuff[0]]+=player_debuff[1]
    if boss_effect[0] == 1:
        print('The Beast gained '+effect_names[boss_effect[1]]+'!')
        enemy_effects[boss_effect[1]]+=boss_effect[2]
    taken_damage= boss_damage - player_current_block
    if taken_damage<1: taken_damage=0
    phealth-=taken_damage
    sleep(1)
    print(name+' took '+str(taken_damage)+' damage! They have '+str(phealth)+' remaining!')
    sleep(1)
    if boss_effect[0] == 2:
        print(name+' became debufffed with '+effect_names[boss_effect[0]]+' at level '+str(boss_effect[1])+'!')
        player_effects[boss_effect[0]]+=boss_effect[1]
    if not player_buff == [0,0]:
        print(name+' gained '+effect_names[player_buff[0]]+'!')
        player_effects[player_buff[0]]+=player_buff[1]
    if enemy_effects[0]>0: 
        enemy_health -= int(enemy_effects[0])
        print('Enemy took '+str(enemy_effects[0])+' poison damage! They have '+str(enemy_health)+' remaining!')
    if player_effects[0]>0: 
        phealth -= int(player_effects[0])
        print(name+' took '+str(player_effects[0])+' poison damage! They have '+str(phealth)+' remaining!')
    if enemy_effects[1]>0: 
        enemy_health += int(enemy_effects[1])
        print('The Beast gained '+str(enemy_effects[1])+' health from regen! He has '+str(enemy_health)+' remaining!')
    if player_effects[1]>0: 
        phealth += int(player_effects[1])
        print(name+' gained '+str(player_effects[1])+' health from regen! They have '+str(phealth)+' remaining!')
    if player_effects[6]>0:
        player_effects[0]+=2*player_effects[6]
        player_effects[2]+=2*player_effects[6]
        player_effects[4]+=2*player_effects[6]
        player_effects[6]-=1
    pass
def give_up():
    print('You tell the Beast that you give up.')
    sleep(2)
    print('"Perfect. I knew you would submit eventually." He says.')
    sleep(2)
    print('Everything goes dark around you.')
    quit()
def finish():
    alive=0
    global title
    print('"Ha... ha..."')
    sleep(2)
    print('"So this is how it ends..."')
    sleep(2)
    answer=input('"Can I tell you something?" (y or n)')
    if answer=='y':
        print('"My name..."')
        sleep(2)
        print('"My name is Andrew."')
        sleep(2)
        print('"I wanted to be the most powerful."')
        sleep(2)
        print('"I jumped in the closet, and look at me now."')
        sleep(2)
        print('Andrew laugs bitterly.')
        sleep(2)
        print('"I sacrificed my soul, and I\'m still not powerful enough to beat you."')
        sleep(2)
        print('"Well, this is it."')
        sleep(2)
        print('"Kill me."')
        answer=input('Will you kill him? (y or n)')
        if answer=='y':
            print('You deal the final blow. His body melts into a dark puddle on the ground.')
            sleep(2)
        else:
            print('"huh?"')
            sleep(2)
            print('Andrew looks up at you. The darkness slowly fades from his eyes.')
            sleep(2)
            print('"Why?"')
            sleep(2)
            print('"I don\'t understand..."')
            sleep(2)
            print('Andrew looks confused, and his hair changes to a blonde color.')
            sleep(2)
            print('"W-why?"')
            sleep(2)
            print('Andrew\'s skin slowly turns from purple.')
            sleep(2)
            print('"I don\'t get it..."')
            sleep(2)
            print('Andrew ran away.')
            sleep(2)
            alive=1
    else:
        print('You deal the final blow. His body melts into a dark puddle on the ground.')
        sleep(2)
    end=['                  _______   _    _   ______     ______   _   _   _____  ',
    '                 |__   __| | |  | | |  ____|   |  ____| | \ | | |  __ \ ',
    '                    | |    | |__| | | |__      | |__    |  \| | | |  | |',
    '                    | |    |  __  | |  __|     |  __|   | . ` | | |  | |',
    '                    | |    | |  | | | |____    | |____  | |\  | | |__| |',
    '                    |_|    |_|  |_| |______|   |______| |_| \_| |_____/ ']
    for i in end:
        print(i)
        sleep(1)
    sleep(3)
    for i in title:
        print(i)
        sleep(1)
    print()
    print()
    print()
    print('''   
                       _____   _____    ______   _____    _____   _______    _____ 
                      / ____| |  __ \  |  ____| |  __ \  |_   _| |__   __|  / ____|
                     | |      | |__) | | |__    | |  | |   | |      | |    | (___  
                     | |      |  _  /  |  __|   | |  | |   | |      | |     \___ \ 
                     | |____  | | \ \  | |____  | |__| |  _| |_     | |     ____) |
                      \_____| |_|  \_\ |______| |_____/  |_____|    |_|    |_____/ 
'''.center(106))
    print('Development: ActonWoods'.center(106))
    sleep(2)
    print('')
    print('Code: ActonWoods'.center(106))
    sleep(2)
    print('')
    print('Playetesters:'.center(106))
    print(''.center(106))
    sleep(2)
    print('')
    print('Assorted Help:'.center(106))
    sleep(2)
    print('')
    print('Hen Mihalak'.center(106))
    sleep(2)
    print('')
    print('Uncle David'.center(106))
    sleep(2)
    print('')
    print('The Internet'.center(106))
    sleep(2)
    print('')
    print('The people who let me use their names'.center(106))
    sleep(2)
    print('')
    print('. . .')
    sleep(2)
    print('"ha... ha..."')
    sleep(2)
    print('"I\'ll see you around."')
    sleep(2)
    quiet='''   
   _____                 _   _   _ _       _     _          __  
  / ____|               | | | \ | (_)     | |   | |    _____\ \ 
 | |  __  ___   ___   __| | |  \| |_  __ _| |__ | |_  |______| |
 | | |_ |/ _ \ / _ \ / _` | | . ` | |/ _` | '_ \| __|  ______| |
 | |__| | (_) | (_) | (_| | | |\  | | (_| | | | | |_  |______| |
  \_____|\___/ \___/ \__,_| |_| \_|_|\__, |_| |_|\__|        | |
          /\             | |          __/ |                 /_/ 
  ______ /  \   _ __   __| |_ __ ____|___/  __                  
 |______/ /\ \ | '_ \ / _` | '__/ _ \ \ /\ / /                  
       / ____ \| | | | (_| | | |  __/\ V  V /                   
      /_/    \_|_| |_|\__,_|_|  \___| \_/\_/         '''.splitlines()
    for i in quiet:
        print(i)
        sleep(1)
    quit()
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################










render()
while True:
    asktick()
    detect()
    render()







