def pura_hex(i,newbase):
    if(i=="A" and newbase>10):
        return 10;
    elif(i=="B" and newbase>11):
        return 11;
    elif(i=="C" and newbase>12):
        return 12;
    elif(i=="D" and newbase>13):
        return 13;
    elif(i=="E" and newbase>14):
        return 14;
    elif(i=="F" and newbase>15):
        return 15;
    elif(i=="G" and newbase>16):
        return 16;
    elif(i=="H" and newbase>17):
        return 17;
    elif(i=="I" and newbase>18):
        return 18;
    elif(i=="J" and newbase>19):
        return 19;
    elif(i=="K" and newbase>20):
        return 20;
    elif(i=="L" and newbase>21):
        return 21;
    elif(i=="M" and newbase>22):
        return 22;
    elif(i=="N" and newbase>23):
        return 23;
    elif(i=="O" and newbase>24):
        return 24;
    elif(i=="P" and newbase>25):
        return 25;
    elif(i=="Q" and newbase>26):
        return 26;
    elif(i=="R" and newbase>27):
        return 27;
    elif(i=="S" and newbase>28):
        return 28;
    elif(i=="T" and newbase>29):
        return 29;
    elif(i=="U" and newbase>30):
        return 30;
    elif(i=="V" and newbase>31):
        return 31;
    elif(i=="W" and newbase>32):
        return 32;
    elif(i=="X" and newbase>33):
        return 33;
    elif(i=="Y" and newbase>34):
        return 34;
    elif(i=="Z" and newbase>35):
        return 35;
    else:
        return int(i);
        #palautetaan tuntematon arvo

def muunna_base10(muunnettava,oldbase):
    pilkottu = [];
    i = 0;
    while(i<len(str(muunnettava))):
        lisattava = str(muunnettava)[i];
        pilkottu.append(pura_hex(lisattava,oldbase));
        i+=1;
    total=0;
    for i in range(len(pilkottu)):
        #lasketaan joka solu
        lasku = pilkottu[i]*(oldbase**((len(pilkottu)-1)-i));
        total+= lasku;
        print("("+str(pilkottu[i])+" * "+str(oldbase)+"**"+str((len(pilkottu)-1))+") = "+str(lasku))
        #= (1 × 3**3) + (0 × 3**2) + (1 × 3**1) + (0 × 3**0) = (30)10
        i+=1;
    print(total);
    return total;



print("""
Muunnetaan Base numerojärjestelmä toiseen numerojärjestelmään.
""");
def hankinumero(k):
    i=input(k);
    #try:
    #    i=float(i);
    #    return i;
    #except:
    #    #kysytään uudelleen
    #    print("Virheellinen numero!");
    #KIRJAIMIAKIN TARVITAAN KUN MENNÄÄN BIN10 YLI
    return i; #hankinumero(k);

def sallittu(mi,ma,k):
    i=float(hankinumero(k));
    if(i>=mi and i<=ma):
        return i;
    else:
        print("Anna arvo oikealta alueelta!");
        return sallittu(mi,ma,k);

def hanki_hex(i,newbase):
    if(i==10 and newbase>10):
        return "A";
    elif(i==11 and newbase>11):
        return "B";
    elif(i==12 and newbase>12):
        return "C";
    elif(i==13 and newbase>13):
        return "D";
    elif(i==14 and newbase>14):
        return "E";
    elif(i==15 and newbase>15):
        return "F";
    elif(i==16 and newbase>16):
        return "G";
    elif(i==17 and newbase>17):
        return "H";
    elif(i==18 and newbase>18):
        return "I";
    elif(i==19 and newbase>19):
        return "J";
    elif(i==20 and newbase>20):
        return "K";
    elif(i==21 and newbase>21):
        return "L";
    elif(i==22 and newbase>22):
        return "M";
    elif(i==23 and newbase>23):
        return "N";
    elif(i==24 and newbase>24):
        return "O";
    elif(i==25 and newbase>25):
        return "P";
    elif(i==26 and newbase>26):
        return "Q";
    elif(i==27 and newbase>27):
        return "R";
    elif(i==28 and newbase>28):
        return "S";
    elif(i==29 and newbase>29):
        return "T";
    elif(i==30 and newbase>30):
        return "U";
    elif(i==31 and newbase>31):
        return "V";
    elif(i==32 and newbase>32):
        return "W";
    elif(i==33 and newbase>33):
        return "X";
    elif(i==34 and newbase>34):
        return "Y";
    elif(i==35 and newbase>35):
        return "Z";
    else:
        return str(i);
        #palautetaan tuntematon arvo
    
while(True):
    numero=hankinumero("Anna ensiksi muunnettava numero muodossa base 2-36: ");
    mista=sallittu(2,36,"Missä numerojärjestelmässä annoit numeron base 2-36: ");
    if(mista!=10):
        print("Koska numerojärjestelmäsi oli muu kuin base10 muunnetaan se eka base10 ja jatketaan sitten.");
        lasketaan=muunna_base10(numero,mista);
    else:
        #ei tarvitse muuntaa base10 to base10
        print("Koska annoit base10 muodossa ei tarvitse muuntaa sitä ekaksi base10 muotoon.");
        lasketaan=int(numero);
    muunnetaan=sallittu(2,36,"Mihin base 2-36 numerojärjestelmään haluat muuntaa?: ");
    lista=[];
    print("\n========================================================================\n");
    while(lasketaan>0):
        og = lasketaan; #tallenetaan piirtämistä varten

        #otetaan jakojäännös
        jakojaannos=lasketaan % muunnetaan
    
        #jaetaan ja otetaan pelkkä kokonaisluku
        lasketaan=lasketaan//muunnetaan;

        print(str(round(og))+"/"+str(round(muunnetaan))+"  "+str(og/muunnetaan)+" = "+str((jakojaannos)));
    
        #lisätään listalle
        lista.append(hanki_hex(round(jakojaannos),muunnetaan));

        #lista joka on vielä väärin päin
        #print(lista);
    
    kaannetty_lista=[];
    #käännetään lista
    print("\n========================================================================\n");
    for i in range(len(lista)):
        kaannetty_lista.append(lista[len(lista)-(i+1)]);
        txt = "";
    
        for i in range(len(kaannetty_lista)):
            if(txt!=""):
                txt=txt+" "+str(kaannetty_lista[i]);
            else:
                txt=str(kaannetty_lista[i]);
    print("\nNumero arvosi muunnettuna BASE"+str(round(muunnetaan))+" numero järjestelmään: \n"+str(txt));
    x=input("\nPaina Enter jos haluat muuntaa lisää... \njos et palauta mitä tahansa muuta niin ohjelma sammuu.");
    if(x!=""):
        break;
#Amazing code by: jaakko talvitie 
#project finished 7.10.2022 15:54