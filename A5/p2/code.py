def twotoone(x,y):
    return 3*x + y

def onetotwo(s):
    x=(int)(s/3)
    y=s%3
    return x,y

def statetocomps(val):
    c=val%2
    t=((int)(val/2))%9
    a=((int)(val/18))%9
    return a,t,c

def compstostate(a,t,c):
    #a,t is 0 to 9
    #c is 0 or 1
    return a*18 + t*2 + c

def nextstatesuccess(p,ac):
    x,y=onetotwo(p)
    x2=x
    y2=y

    if(ac==1 and y!=2): #up
        y2+=1
    
    elif(ac==2 and y!=0): #down
        y2-=1

    elif(ac==3 and x!=0): #left
        x2-=1
    
    elif(ac==4 and x!=2): #right
        x2+=1

    return twotoone(x2,y2)

def nextstatefail(p,ac):
    x,y=onetotwo(p)
    x2=x
    y2=y

    if(ac==2 and y!=2): #up
        y2+=1
    
    elif(ac==1 and y!=0): #down
        y2-=1

    elif(ac==4 and x!=0): #left
        x2-=1
    
    elif(ac==3 and x!=2): #right
        x2+=1

    return twotoone(x2,y2)


def probagent(p1,p2,ac):

    if(ac==0):
        if(p1==p2):
            return 1
        else:
            return 0
    
    if(nextstatesuccess(p1,ac)==p2):
        return x_roll
    
    if(nextstatefail(p1,ac)==p2):
        return 1-x_roll

    return 0

def probtarget(p1,p2):

    ret=0

    if(p1==p2):
        ret+=0.4
        
    for ac in range(1,5):
        if(nextstatesuccess(p1,ac)==p2):
            ret+=0.15

    return ret

def probcall(c1,c2,a,t):

    if(a==t): #if agent and target are in the same place, treat c1 as if it is 0 even if it is 1
        if(c2==0):
            return 0.6
        else:
            return 0.4

    if(c1==c2):
        if(c1==0): #remain off
            return 0.6
        else: #remain on
            return 0.8
    
    else:
        if(c1==0): # turn on
            return 0.4
        else: #turn off
            return 0.2


def prob(s1,s2,ac):
    a1,t1,c1=statetocomps(s1)
    a2,t2,c2=statetocomps(s2)

    return probagent(a1,a2,ac)*probtarget(t1,t2)*probcall(c1,c2,a1,t1)

def reward(s,ac):
    a,t,c=statetocomps(s)

    if(a==t and c==1): #gets the reward only if call is on 
        if(ac==0): #came via a stay 
            return roll_rew
        else: #came via an action
            return roll_rew-1
    elif(ac==0):
        return 0
    else:
        return -1

def getobs(s):
    a,t,c=statetocomps(s)
    
    xa,ya=onetotwo(a)
    xt,yt=onetotwo(t)

    if(a==t):
        return 0
    elif(xt==xa+1 and yt==ya):#target to the right
        return 1
    elif(xt==xa and yt==ya-1): #target below
        return 2
    elif(xt==xa-1 and yt==ya):#target to the left
        return 3
    elif(xt==xa and yt==ya+1):
        return 4
    else:
        return 5


def q1():
    print("start include:",compstostate(0,4,0),compstostate(0,4,1),compstostate(2,4,0),compstostate(2,4,1),compstostate(6,4,0),compstostate(6,4,1),compstostate(8,4,0),compstostate(8,4,1))

def q2():
    print("start include:",compstostate(1,2,0),compstostate(1,4,0),compstostate(1,0,0),compstostate(1,1,0))

def q4():

    six=twotoone(0,1)
    four=twotoone(2,1)

    print("start: ",end="")

    for a in range(9):
        for t in range(9):
            for c in range(2):
                ans=1
                if a==six:
                    ans*=0.6
                elif a==four:
                    ans*=0.4
                else:
                    ans*=0
                
                if t==0 or t==2 or t==8 or t==6:
                    ans*=0.25
                else:
                    ans*=0
                
                ans*=0.5

                print(ans,end=" ")
    
    print()

x_roll=0.87
roll_rew=22
#actions 0 to 4 Stay, Up, Down, Left, Right.
#call on means 1


#initial probs
print("discount: 0.5")
print("values: reward")
print("states: 162")
print("actions: 5")
print("observations: 6")
q1()
#transition probabilities
for s1 in range(162):
    for ac in range(5):
        for s2 in range(162):
            p=prob(s1,s2,ac)
            if(p!=0):
                print("T: "+str(ac)+" : "+str(s1)+" : "+str(s2)+" "+str(p))

#observation
for s in range(162):
    print("O : * : "+str(s)+" : "+str(getobs(s))+" 1")


#rewards
for s in range(162):
    for ac in range(5):
            print("R: "+str(ac)+" : * : "+str(s)+" : "+str(getobs(s))+" "+str(reward(s,ac)))
