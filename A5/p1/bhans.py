obs = {}
obs['rr'] = 0.85
obs['gg'] = 0.9
obs['gr'] = 0.15
obs['rg'] = 0.1

o = ['r','r','g','g','r']
actions = ['r','l','l']
observations = ['r','g','g']
b = [0.333333,0.333333,0,0,0.333333]

ps = 0.8
pf = 0.2
right = [
    [0.20,0.80,0,0,0],
    [0.20,0,0.80,0,0],
    [0,0.20,0,0.80,0],
    [0,0,0.20,0,0.80],
    [0,0,0,0.20,0.80]]
left = [
    [0.80,0.20,0,0,0],
    [0.80,0,0.20,0,0],
    [0,0.80,0,0.20,0],
    [0,0,0.80,0,0.20],
    [0,0,0,0.80,0.20]]
# right = [
#     [0.29,0.71,0,0,0],
#     [0.29,0,0.71,0,0],
#     [0,0.29,0,0.71,0],
#     [0,0,0.29,0,0.71],
#     [0,0,0,0.29,0.71]]
# left = [
#     [0.71,0.29,0,0,0],
#     [0.71,0,0.29,0,0],
#     [0,0.71,0,0.29,0],
#     [0,0,0.71,0,0.29],
#     [0,0,0,0.71,0.29]]


observed  = 'g'
sum=0
B = []
for idx in range(3):
    observed = observations[idx]
    sum=0
    if(actions[idx]=='r'):
        for i in range(5):
            qw = observed+o[i]
            print('Ub\'[S'+str(i+1)+']='+str(obs[qw])+'[ ',end='')
            k=0
            for j in range(5):
                k+=right[j][i]*b[j]
                print("("+str(right[j][i])+' * '+str(b[j])+")" + ' + ',end='')
            print(' ]='+str(k*obs[qw]))
            B.append(k*obs[qw])
            sum+=k*obs[qw]
        
    else:
        for i in range(5):
            qw = observed+o[i]
            print('Ub\'[S'+str(i+1)+']='+str(obs[qw])+'[ ',end='')
            k=0
            for j in range(5):
                k+=left[j][i]*b[j]
                print("("+str(left[j][i])+' * '+str(b[j])+")" + ' + ',end='')
            print(' ]='+str(k*obs[qw]))
            B.append(k*obs[qw])
            sum+=k*obs[qw]
    print('sum',sum)
    B = [x/sum for x in B]
    print(B)
    b = B
    B=[]
