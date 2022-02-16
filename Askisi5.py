from collections import Counter
from typing import Counter 
f = open("two_cities_ascii.txt", "r")
#Pername to keimeno stin metavliti string
string = f.read()
#allazoume ton typo tis f ,dioti oso einai typoy _io.TextIOWrapper den epitrepe na leitourgisei i .lower

#edw kanoume tin string me pezous xaraktires
string=string.lower()

#Eisagoume stin lista f1 tis lekseis tou string xwris ta space
f1 = string.split()

first2=[]
first3=[]
words10=[]
c=10

for i in range (len(f1)) :
    
    first2.append(f1[i][:2])
    #Elegxoume wste to mikos kathe lekseis na einai megalitero tou 3 ,dioti tha metrithoun kai kapoioi sindiasmoi grammatwn ,pou einai mono me 2grammata .Example , o sindiasmos "of"
    if len(f1[i])>= 3:
        first3.append(f1[i][:3])
count1=Counter(f1)
count2=Counter(first2)
count3=Counter(first3)
#Me to Counter kai to tin most_common briskoume tous most dimofilesterous syndyasmous pou exoun emfanistei tis perissoteres fores
print("Oi deka dimofilesteres lekseis einai oi:")
print(count1.most_common(10),"\n")
print("Oi 3 prwtoi sindiasmoi 2 grammatwn einai oi :")
print(count2.most_common(3),"\n")
print("Oi 3 prwtoi sindiasmoi 3 grammatwn einai oi :")
print(count3.most_common(3),"\n")
