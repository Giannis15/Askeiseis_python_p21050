import random
winsw=0
winsb=0

for i in range (100):
  
        #position of bishop
        pos_white_i1=random.randint(0,7)
        pos_white_j1=random.randint(0,7)
        #position of tower
        pos_white_i2=random.randint(0,7)
        pos_white_j2=random.randint(0,7)

        #position of queen
        pos_black_i=random.randint(0,7)
        pos_black_j=random.randint(0,7)
        
        #elegxoume tin thesi tou pirgou kai tis vasilisas orizontia kai katheta gia to ean kerdizei 
        if(pos_white_i2==pos_black_i)or(pos_white_j2==pos_black_j):
            winsw=winsw+1
        
        if (pos_white_i1==pos_black_i) or (pos_white_j1==pos_black_j):
            winsb=winsb+1
        if(pos_white_i2==pos_black_i) or (pos_white_j2==pos_black_j):
             winsb=winsb+1
        a=pos_black_i
        b=pos_black_j
        #elegxoume tin thesi tou aksiwmatikou kai tis vasilisas diagwnia gia to ean kerdizei 
        while(a>=0 and b>=0):
            if(a==pos_white_i1 and b==pos_white_j1):
                winsb=winsb+1
                winsw=winsw+1
                
            if (a==pos_white_i2 and b==pos_white_j2):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b-1
        a=pos_black_i
        b=pos_black_j

        while(a<=7 and b>=0):
            if(a==pos_white_i1 and b==pos_white_j1):
                winsb=winsb+1
                winsw=winsw+1
            if (a==pos_white_i2 and b==pos_white_j2):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b-1
        
        a=pos_black_i
        b=pos_black_j

        while(a>=0 and b<=7):
            if(a==pos_white_i1 and b==pos_white_j1):
                winsb=winsb+1
                winsw=winsw+1
            if (a==pos_white_i2 and b==pos_white_j2):
                winsb=winsb+1
                break
            else:
                a=a-1
                b=b+1

        a=pos_black_i
        b=pos_black_j

        while(a<=7 and b<=7):
            if(a==pos_white_i1 and b==pos_white_j1):
                winsb=winsb+1
                winsw=winsw+1
            if (a==pos_white_i2 and b==pos_white_j2):
                winsb=winsb+1
                break
            else:
                a=a+1
                b=b+1
        
print("For a board White won ",winsw,"times\n black won",winsb,"times")


