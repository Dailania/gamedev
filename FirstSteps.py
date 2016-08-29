import random

races=['Hylian','Kokiri','Deku','Goron','Zora','Gerudo']

def newgame():
    players=[]
    num=int(input('\nhow many players? 1-4: '))
    while type(num)!= int or num>4:
        print('\nerror, whole number only, 1-4')
        num=int(input('\nplease re-enter: '))
    count=0
    while num>count:
        name=input('\nplayer name?: ')
        print(races)
        race=input('\nplayer race?: ')
        while race not in races:
            print('\ninvalid race')
            print(races)
            race=input('\nplease re-enter: ')
        print('\n10 stat points available for POWER, DEXTERITY, COURAGE, VITALITY, and WISDOM')
        sth=0
        spd=0
        acc=0
        vit=0
        mag=0
        yesno=input('\nrandom characteristics? yes or no: ')
        if yesno=='yes':
            while sth+spd+acc+vit+mag!=10:
                sth=random.randint(0,5)
                spd=random.randint(0,5)
                acc=random.randint(0,5)
                vit=random.randint(1,5)
                mag=random.randint(0,5)
        else:
            while sth+spd+acc+vit+mag!=10:
                sth=int(input('\nstrength? 5 max: '))
                while type(sth) != int or sth>5:
                    print('\nerror, whole number only, max 5')
                    power=int(input('\nplease re-enter: '))
                spd=int(input('\ndexterity? 5 max: '))
                while type(dex) != int or dex>5:
                    print('\nerror, whole number only, max 5')
                    dex=int(input('\nplease re-enter'))
                acc=int(input('\ncourage? 5 max: '))
                while type(cor) != int or cor>5:
                    print('\nerror, whole number only, max 5')
                    cor=int(input('\nplease re-enter'))
                vit=int(input('\nvitality? 1 min, 5 max: '))
                while type(vit) != int or vit<1 or vit>5:
                    print('\nerror, whole number only, min 1, max 5')
                    vit=int(input('\nplease re-enter'))
                mag=int(input('\nwisdom? 5 max: '))
                while type(wis) != int or vit>5:
                    print('\nerror, whole number only, max 5')
                    wis=int(input('\nplease re-enter'))
                if power+dex+cor+vit+wis>10:
                    print('\nerror, only 10 points available')
        atk=power*0.025
        dodge=dex*0.025
        health=vit*4
        list=[name,'race',race,'level',0,'stats','power',power,'dexterity',dex,'courage',cor,'vitality',vit,'wisdom',wis,'attack bonus',atk,'dodge',dodge,'health',health,'magic',wis,['equip','head','none','body','clothes','acc','none']]
        players += [list]
        count=count+1
    file=open('save.txt','w')
    file.write(str(players))
    file.close()
    return 

def loadgame():
    save=open('save.txt','r')
    game=save.read()
    save.close()
    return game

def m():
    '''attack=a, magic=m, run=r'''
    move=input('\nattack, magic, run: ')
    if move=='a':
        num=random.random()
        if num+attkbns>0.5 and num<=0.95:
            print(num,'\n+',attkbns,'HIT!')
            dam=random.randint(1,10)
            print(dam, '\nDAMAGE!')
        elif num>0.95:
                print(num,'\nCRITICAL!')
                dam=random.randint(1,10)
                dam=dam*2
                print(dam, '\nDAMAGE!')
        else: print(num,'\n+',attkbns,'MISS!')
    elif move=='m':
        print(spells)
        spell=input('\nwhich spell?: ')
        if spell=='\nspell1':
            print('\nFireball! 5 DAMAGE!')
        elif spell=='spell2':
            print('\nIce Rod! Enemy is frozen!!')
    return

def e(level):
    '''enter the desired level of npc'''
    party=[]
    num=int(input('\nhow many combatants?: '))
    while type(num)!=int and num>10:
        print('\nerror, whole numbers only, max 10')
        num=int(input('\nplease re-enter: '))
    count=0
    while num>count:
        name=input('\nnpc name?: ')
        race=input('\nnpc race?: ')
        power=0
        dex=0
        cor=0
        vit=0
        wis=0
        pnts=10+level
        while (power+dex+cor+vit+wis)!=(pnts):
            power=random.randint(0,pnts/2)
            dex=random.randint(0,pnts/2)
            cor=random.randint(0,pnts/2)
            vit=random.randint(1,pnts/2)
            wis=random.randint(0,pnts/2)
        atk=power*0.025
        dodge=dex*0.025
        health=vit*4
        list=[name,'race',race,'level',level,'stats','power',power,'dexterity',dex,'courage',cor,'vitality',vit,'wisdom',wis,'attack bonus',atk,'dodge',dodge,'health',health,'magic',wis]
        party += [list]
        count=count+1
    print(party)
        
    

def f():
    num=random.random()
    if num<=0.5:
        print(num,'\nfound nothing')
    if num>0.5 and num<=0.53636:
        print(num,'\nfound 1 green rupee')
    if num>0.53636 and num<=0.56908:
        print(num,'\nfound 2 green rupees')
    if num>0.56908 and num<=0.59818:
        print(num,'\nfound 3 green rupees')
    if num>0.59818 and num<=0.62364:
        print(num,'\nfound 1 blue rupee')
    if num>0.62364 and num<=0.64546:
        print(num,'\nfound 2 blue rupees')
    if num>0.64546 and num<=0.66364:
        print(num,'\nfound 3 blue rupees')
    if num>0.66364 and num<=0.67818:
        print(num,'\nfound 1 red rupee')
    if num>0.67818 and num<=0.68908:
        print(num,'\nfound 2 red rupees')
    if num>0.68908 and num<=0.69636:
        print(num,'\nfound 3 red rupees')
    if num>0.69636 and num<=0.7:
        print(num,'\nfound 1 purple rupee')
    if num>0.7 and num<=0.725:
        print(num,'\nfound 5 arrows/bullets')
    if num>0.725 and num<=0.7416667:
        print(num,'\nfound 10 arrows/bullets')
    if num>0.7416667 and num<=0.75:
        print(num,'\nfound 20 arrows/bullets')
    if num>0.75 and num<=0.8:
        print(num,'\nfound 5 bombs')
    if num>0.8 and num<=0.84:
        print(num,'\nfound small magic jar')
    if num>0.84 and num<=0.85:
        print(num,'\nfound big magic jar')
    if num>0.85 and num<=0.8508333:
        print(num,'\nfound Knife')
    if num>0.8508333 and num<=0.8516667:
        print(num,'\nfound Dagger')
    if num>0.8516667 and num<=0.8525:
        print(num,'\nfound Gladius')
    if num > 0.8525000 and num <= 0.8533333 :
        print(num,'\nfound Shortsword')
    if num > 0.8533333 and num <= 0.8541667 :
        print(num,'\nfound Sabre')
    if num > 0.8541667 and num <= 0.8550000 :
        print(num,'\nfound Falchion')
    if num > 0.8550000 and num <= 0.8558333 :
        print(num,'\nfound Scimitar')
    if num > 0.8558333 and num <= 0.8566667 :
        print(num,'\nfound Broadsword')
    if num > 0.8566667 and num <= 0.8575000 :
        print(num,'\nfound Longsword')
    if num > 0.8575000 and num <= 0.8583333 :
        print(num,'\nfound Spatha')
    if num > 0.8583333 and num <= 0.8591667 :
        print(num,'\nfound Estoc')
    if num > 0.8591667 and num <= 0.8600000 :
        print(num,'\nfound Schiavona')
    if num > 0.8600000 and num <= 0.8608333 :
        print(num,'\nfound Spada da Lato')
    if num > 0.8608333 and num <= 0.8616667 :
        print(num,'\nfound Flammard')
    if num > 0.8616667 and num <= 0.8625000 :
        print(num,'\nfound Claymore')
    if num > 0.8625000 and num <= 0.8637500 :
        print(num,'\nfound Hatchet ')
    if num > 0.8637500 and num <= 0.8650000 :
        print(num,'\nfound Small Axe')
    if num > 0.8650000 and num <= 0.8662500 :
        print(num,'\nfound Francisca')
    if num > 0.8662500 and num <= 0.8675000 :
        print(num,'\nfound Hammer')
    if num > 0.8675000 and num <= 0.8687500 :
        print(num,'\nfound Mace')
    if num > 0.8687500 and num <= 0.8700000 :
        print(num,'\nfound Morning Star')
    if num > 0.8700000 and num <= 0.8712500 :
        print(num,'\nfound Bearded Axe')
    if num > 0.8712500 and num <= 0.8725000 :
        print(num,'\nfound Warhammer')
    if num > 0.8725000 and num <= 0.8737500 :
        print(num,'\nfound Hafted Axe')
    if num > 0.8737500 and num <= 0.8750000 :
        print(num,'\nfound Greataxe')
    if num > 0.8750000 and num <= 0.8762500 :
        print(num,'\nfound Stake')
    if num > 0.8762500 and num <= 0.8775000 :
        print(num,'\nfound Javelin')
    if num > 0.8775000 and num <= 0.8787500 :
        print(num,'\nfound Short Spear')
    if num > 0.8787500 and num <= 0.8800000 :
        print(num,'\nfound Spear ')
    if num > 0.8800000 and num <= 0.8812500 :
        print(num,'\nfound Long Spear ')
    if num > 0.8812500 and num <= 0.8825000 :
        print(num,'\nfound Pike')
    if num > 0.8825000 and num <= 0.8837500 :
        print(num,'\nfound Trident')
    if num > 0.8837500 and num <= 0.8850000 :
        print(num,'\nfound Glaive')
    if num > 0.8850000 and num <= 0.8862500 :
        print(num,'\nfound Guisarme')
    if num > 0.8862500 and num <= 0.8875000 :
        print(num,'\nfound Halberd')
    if num > 0.8875000 and num <= 0.8887500 :
        print(num,'\nfound Sling')
    if num > 0.8887500 and num <= 0.8900000 :
        print(num,'\nfound Slingshot')
    if num > 0.8900000 and num <= 0.8912500 :
        print(num,'\nfound Hunting Bow')
    if num > 0.8912500 and num <= 0.8925000 :
        print(num,'\nfound Shortbow')
    if num > 0.8925000 and num <= 0.8937500 :
        print(num,'\nfound Bow')
    if num > 0.8937500 and num <= 0.8950000 :
        print(num,'\nfound Longbow')
    if num > 0.8950000 and num <= 0.8962500 :
        print(num,'\nfound Composite Bow')
    if num > 0.8962500 and num <= 0.8975000 :
        print(num,'\nfound Recurve Bow')
    if num > 0.8975000 and num <= 0.8987500 :
        print(num,'\nfound Crossbow')
    if num > 0.8987500 and num <= 0.9000000 :
        print(num,'\nfound Arbalest')
    if num > 0.9000000 and num <= 0.9012500 :
        print(num,'\nfound Rotella')
    if num > 0.9012500 and num <= 0.9025000 :
        print(num,'\nfound Small Shield')
    if num > 0.9025000 and num <= 0.9037500 :
        print(num,'\nfound Targa')
    if num > 0.9037500 and num <= 0.9050000 :
        print(num,'\nfound Kite Shield')
    if num > 0.9050000 and num <= 0.9062500 :
        print(num,'\nfound Parma')
    if num > 0.9062500 and num <= 0.9075000 :
        print(num,'\nfound Large Shield')
    if num > 0.9075000 and num <= 0.9087500 :
        print(num,'\nfound Knight Shield ')
    if num > 0.9087500 and num <= 0.9100000 :
        print(num,'\nfound Great Shield')
    if num > 0.9100000 and num <= 0.9112500 :
        print(num,'\nfound Phalanx')
    if num > 0.9112500 and num <= 0.9125000 :
        print(num,'\nfound Testudo')
    if num > 0.9125000 and num <= 0.9137500 :
        print(num,'\nfound Clothing')
    if num > 0.9137500 and num <= 0.9150000 :
        print(num,'\nfound Padded')
    if num > 0.9150000 and num <= 0.9162500 :
        print(num,'\nfound Leather')
    if num > 0.9162500 and num <= 0.9175000 :
        print(num,'\nfound Brigandine')
    if num > 0.9175000 and num <= 0.9187500 :
        print(num,'\nfound Lamellar')
    if num > 0.9187500 and num <= 0.9200000 :
        print(num,'\nfound Ringmail')
    if num > 0.9200000 and num <= 0.9212500 :
        print(num,'\nfound Lorica Hamata')
    if num > 0.9212500 and num <= 0.9225000 :
        print(num,'\nfound Lorica Squamata')
    if num > 0.9225000 and num <= 0.9237500 :
        print(num,'\nfound Lorica Segmentata')
    if num > 0.9237500 and num <= 0.9250000 :
        print(num,'\nfound Breastplate')
    if num > 0.9250000 and num <= 0.9262500 :
        print(num,'\nfound Hood')
    if num > 0.9262500 and num <= 0.9275000 :
        print(num,'\nfound Cap')
    if num > 0.9275000 and num <= 0.9287500 :
        print(num,'\nfound Coif')
    if num > 0.9287500 and num <= 0.9300000 :
        print(num,'\nfound Cervelliere')
    if num > 0.9300000 and num <= 0.9312500 :
        print(num,'\nfound Spangenhelm')
    if num > 0.9312500 and num <= 0.9325000 :
        print(num,'\nfound Aventail')
    if num > 0.9325000 and num <= 0.9337500 :
        print(num,'\nfound Sallet')
    if num > 0.9337500 and num <= 0.9350000 :
        print(num,'\nfound Corinthian')
    if num > 0.9350000 and num <= 0.9362500 :
        print(num,'\nfound Armet')
    if num > 0.9362500 and num <= 0.9375000 :
        print(num,'\nfound Great Helm')
    if num > 0.9375000 and num <= 0.9387500 :
        print(num,'\nfound Scarf')
    if num > 0.9387500 and num <= 0.9400000 :
        print(num,'\nfound Cape')
    if num > 0.9400000 and num <= 0.9412500 :
        print(num,'\nfound Vest')
    if num > 0.9412500 and num <= 0.9425000 :
        print(num,'\nfound Mantle')
    if num > 0.9425000 and num <= 0.9437500 :
        print(num,'\nfound Cloak')
    if num > 0.9437500 and num <= 0.9450000 :
        print(num,'\nfound Heavy Cloak')
    if num > 0.9450000 and num <= 0.9462500 :
        print(num,'\nfound Coat')
    if num > 0.9462500 and num <= 0.9475000 :
        print(num,'\nfound Cassock')
    if num > 0.9475000 and num <= 0.9487500 :
        print(num,'\nfound Robes')
    if num > 0.9487500 and num <= 0.9500000 :
        print(num,'\nfound Regalia')
    if num > 0.9500000 and num <= 1.0000000 :
        print(num,'\nfound RARE ITEM')
