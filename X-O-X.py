#yeni XoX
dizi1=[]
dizi2=[]
dizi3=[]
dizi4=[]
dizi5=[]
dizi6=[]
dizi7=[]
dizi8=[]
dizi9=[]
b_dizi=[dizi1,dizi2,dizi3,dizi4,dizi5,dizi6,dizi7,dizi8,dizi9]
kontrol_dizi={}
oyoncu={}
for i in range(1,4):
    dizi1.append("|     |")
    dizi2.append("     |")
    dizi3.append("     |")
    dizi4.append("|     |")
    dizi5.append("     |")
    dizi6.append("     |")
    dizi7.append("|     |")
    dizi8.append("     |")
    dizi9.append("     |")

for i in range(1,10):
    kontrol_dizi[i]=i
def kontrol(deger,degişken):
    kontrol_dizi[deger]=degişken
    if kontrol_dizi[1]==kontrol_dizi[2]==kontrol_dizi[3]:
        return True
    elif kontrol_dizi[4]==kontrol_dizi[5]==kontrol_dizi[6]:
        return True
    elif kontrol_dizi[7]==kontrol_dizi[8]==kontrol_dizi[9]:
        return True
    elif kontrol_dizi[1]==kontrol_dizi[4]==kontrol_dizi[7]:
        return True
    elif kontrol_dizi[2]==kontrol_dizi[5]==kontrol_dizi[8]:
        return True
    elif kontrol_dizi[3]==kontrol_dizi[6]==kontrol_dizi[9]:
        return True
    elif kontrol_dizi[1]==kontrol_dizi[5]==kontrol_dizi[9]:
        return True
    elif kontrol_dizi[3]==kontrol_dizi[5]==kontrol_dizi[7]:
        return True
    else:
        False
def oyun(deger,degişken):
    for i in range(1,10):
        if (deger==i and degişken=="x") and (deger==1 or deger==4 or deger==7) :
            b_dizi[deger-1][1]="|  x  |"
        elif (deger==i and degişken=="o") and (deger==1 or deger==4 or deger==7) :
            b_dizi[deger-1][1]="|  o  |"
        elif deger==i and degişken=="x":
            b_dizi[deger-1][1]="  x  |"
        elif deger==i and degişken=="o":
            b_dizi[deger-1][1]="  o  |"

    for k in range(1,4):
        print(f"{dizi1[k-1]}{dizi2[k-1]}{dizi3[k-1]}")
    print("-------------------")
    for k in range(1,4):
        print(f"{dizi4[k-1]}{dizi5[k-1]}{dizi6[k-1]}")
    print("-------------------")
    for k in range(1,4):
        print(f"{dizi7[k-1]}{dizi8[k-1]}{dizi9[k-1]}")
    return kontrol(deger,degişken)
sayac=1
tut={1:"x"}
a=0
def döndür():
    global sayac,a
    if(sayac==1):
        print(f"{sayac}.oyuncu:")
        deger=int(input("1,9 kadar aralaıkta bir deger girin:"))
        degişken=input("x veya o degerini girin:")
        sayac=2
        if(degişken=="a"):
            return True
        if tut[1]==degişken:
            a=1
            pass
        elif degişken=="o"and a==0:
            tut[1]="o"
        else:
            print("yanlış deger")
            sayac=1
            return
    elif(sayac==2):
        print(f"{sayac}.oyuncu:")
        deger=int(input("1,9 kadar aralaıkta bir deger girin:"))
        degişken=input("x veya o degerini girin:")
        if(tut[1]!=degişken):
            sayac=1
        else:
            print("yanlış deger")
            sayac=2
            return
    if(oyun(deger,degişken)):
        return True
while True:
    if(döndür()==True):
        print(f"{sayac}. oyuncu kaybetti")
        break
