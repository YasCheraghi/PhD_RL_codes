# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:15:11 2022

@author: 2925376
"""

# RL Codes
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:15:11 2022

@author: 2925376
"""

# RL Codes

# creating a function to generate the transition function

# We know that moving up is equivalent of -4,moving down is equivalent of +4, moving right is equivalent of +1 and moving left is equivalent of -1

def transition_probability(next_state,s,a):
    
    if a=='u': a_eq= -4
    if a=='d': a_eq=  4
    if a=='r': a_eq=  1
    if a=='l': a_eq= -1
    
    location=s+a_eq
    
    
    if next_state==location:
        
        if 0<=location<=15:
        
            p=1
        
    else:
        
        p=0
        
        
# Correction for right hand side margin        
        
    if s==3 and next_state==3:
        
        if a=='r':
            
            p=1
            
    if s==3 and next_state==4:
        
        if a=='r':
            
            p=0     
            
    if s==7 and next_state==7:
        
        if a=='r':
            
            p=1
            
    if s==7 and next_state==8:
        
        if a=='r':
            
            p=0         
        
    if s==11 and next_state==11:
        
        if a=='r':
            
            p=1
            
    if s==11 and next_state==12:
        
        if a=='r':
            
            p=0     

# Correction for left hand side margin                         
            
    if s==4 and next_state==4:
        
        if a=='l':
            
            p=1
            
    if s==4 and next_state==3:
        
        if a=='l':
            
            p=0     
            
    if s==8 and next_state==8:
        
        if a=='l':
            
            p=1
            
    if s==8 and next_state==7:
        
        if a=='l':
            
            p=0         
        
    if s==12 and next_state==12:
        
        if a=='l':
            
            p=1
            
    if s==12 and next_state==11:
        
        if a=='l':
            
            p=0     
    
    if s==13 and next_state==13:
        
        if a=='d':
            
            p=1
    
    if s==14 and next_state==14:
        
        if a=='d':
            
            p=1
    
    if s==1 and next_state==1:
        
        if a=='u':
            
            p=1
    
    if s==2 and next_state==2:
        
        if a=='u':
            
            p=1

    return p


teta=0.1
delta=10
current_state_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
next_state_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


value_list=[0]*14
action_list=['u','d','r','l']
r=-1
#equiprobable random policy for all states

policy={'u':1/4,'d':1/4,'r':1/4,'l':1/4}

for it in range(2):
    
    delta=0

    for i in range(len(current_state_list)):
        current_state=current_state_list[i]
        previous_value=value_list[i]
        c=0
        for a in range(len(action_list)):
            pi=policy.get(action_list[a])
            current_action=action_list[a]
            for j in range(len(next_state_list)):
                
                next_state=next_state_list[j]
                
                p_func=transition_probability(next_state,current_state,action_list[a])
                

                if j!=0 and j!=15:
                    
                    next_state_value=value_list[i]
                
                if j==0 or j==15:
                    
                    next_state_value=0
                    
#                if current_state==1  and next_state==0  and current_action=='l': new_value+=pi*p_func*(-1+next_state_value)
#                if current_state==4  and next_state==0  and current_action=='u': new_value+=pi*p_func*(-1+next_state_value)
#                if current_state==11 and next_state==15 and current_action=='d': new_value+=pi*p_func*(-1+next_state_value)
#                if current_state==14 and next_state==15 and current_action=='r': new_value+=pi*p_func*(-1+next_state_value)

                c=c+ pi*p_func*(r+next_state_value)
    
        
                  
        new_value=c
        delta=max(delta, abs(new_value-previous_value))          
        value_list[i]=new_value
       
    
                      
print(value_list)
  