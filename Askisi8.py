import random
winsw=0
winsb=0
#Dokimi stin skakiera 8*8
for i in range (100):
  
        
        #position of tower
        pos_white_i=random.randint(0,7)
        pos_white_j=random.randint(0,7)

        #position of bishop
        pos_black_i=random.randint(0,7)
        pos_black_j=random.randint(0,7)
        #elegxoume tin thesi tou pirgou orizontia kai katheta
        if(pos_white_i==pos_black_i)or (pos_black_j==pos_white_j):
            winsw=winsw+1
        a=pos_black_i
        b=pos_black_j
        #elegxoume tin thesi tou aksiwmatikou pros tis daigwnia
        
        while(a>=0 and b>=0):
            if(a==pos_white_i) and (b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b-1
        a=pos_black_i
        b=pos_black_j
        while(a<=7 and b>=0):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b-1
        
        a=pos_black_i
        b=pos_black_j
        
        while(a>=0 and b<=7):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b+1

        a=pos_black_i
        b=pos_black_j
        
        while(a<=7 and b<=7):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b+1

print("For a board8*8:\nWhite won ",winsw,"times\n black won",winsb,"times")
#Dokimi stin skakiera 7*7

winsw=0
winsb=0
for i in range (100):
  
        
        #position of tower
        pos_white_i=random.randint(0,6)
        pos_white_j=random.randint(0,6)

        #position of bishop
        pos_black_i=random.randint(0,6)
        pos_black_j=random.randint(0,6)
        #elegxoume tin thesi tou pirgou orizontia kai katheta
        
        if(pos_white_i==pos_black_i)or (pos_black_j==pos_white_j):
            winsw=winsw+1
        a=pos_black_i
        b=pos_black_j
        #elegxoume tin thesi tou pirgou orizontia kai katheta
        while(a>=0 and b>=0):
            if(a==pos_white_i) and (b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b-1
        a=pos_black_i
        b=pos_black_j

        while(a<=6 and b>=0):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b-1
        
        a=pos_black_i
        b=pos_black_j

        while(a>=0 and b<=6):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b+1

        a=pos_black_i
        b=pos_black_j

        while(a<=6 and b<=6):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b+1

print("For a board7*7: \nWhite won ",winsw,"times\n black won",winsb,"times")

#Dokimi stin skakiera 7*8
winsw=0
winsb=0
for i in range (100):
  
        
        #position of tower
        pos_white_i=random.randint(0,6)
        pos_white_j=random.randint(0,7)

        #position of bishop
        pos_black_i=random.randint(0,6)
        pos_black_j=random.randint(0,7)
        #elegxoume tin thesi tou pirgou orizontia kai katheta 
        
        if(pos_white_i==pos_black_i)or (pos_black_j==pos_white_j):
            winsw=winsw+1
        a=pos_black_i
        b=pos_black_j
        #elegxoume tin thesi tou pirgou orizontia kai katheta
        while(a>=0 and b>=0):
            if(a==pos_white_i) and (b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b-1
        a=pos_black_i
        b=pos_black_j

        while(a<=6 and b>=0):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b-1
        
        a=pos_black_i
        b=pos_black_j

        while(a>=0 and b<=7):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b+1

        a=pos_black_i
        b=pos_black_j

        while(a<=6 and b<=7):
            if(a==pos_white_i and b==pos_white_j):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b+1

print("For a board7*8:\n White won ",winsw,"times\n black won",winsb,"times")




