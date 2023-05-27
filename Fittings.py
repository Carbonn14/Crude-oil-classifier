#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys


# In[ ]:


print('A- Pipe fittings like couplings, tees, elbows, wyes, plugs, unions, pipe caps, and reducers')
print('B- All flanges')
print('C- All line valves')
print('D- All types of expansion joints, flexible connections, and hose assemblies')
print('E- Strainers, filters, separators, and steam traps')
print('F- measuring devices, including pressure gauges, level gauges, sight glasses, levels, and pressure transmitters')
print('G- certified capacity-related pressure relief devices acceptable as primary overpressure protection on boilers, pressure vessels and pressure piping, and fusible plugs')
print('H- pressure-retaining components that do not fall into Categories A to G')
x=input('\nEnter the code from the above list that applies to your equipment: ')


# In[3]:


if x=='A' or x=='a' or x=='B' or x=='b' or x=='C' or x=='c' or x=='D' or x=='d' or x=='E' or x=='e' or x=='F' or x=='f' or x=='G' or x=='g':
    print('Can be registered as fitting')
    input('Press enter to exit...')
    raise Exception('Code finished')
elif x=='H' or x=='h':
    print('\n\na- Liquids not more hazardous than water')
    print('b- Non-lethal gas or vapour or a non lethal liquid')
    print('c- Lethal substances')
    print('\nNote: The jurisdiction is not responsible for determing if a liquid is more hazardous than water. It is the responsibility of owner to decide that. \nOne can look at the toxicity,  health effects and first aid section of MSDS to decide if the liquid is hazardous than water. \nLethal substances are poisonous gases or liquids of such a nature that a very small amount of the gas or of the liquid’s vapor mixed or unmixed with air is dangerous to life when inhaled. ')
    y=input('\nEnter the code from above that applies to your service fluid: ')
else:
    print('Incorrect code entered')
    input('Press enter to exit....')
    raise Exception("Incorrect code")


# In[ ]:


p=input('\nEnter the MAWP (max. allowable working pressure) of your equipment in kPa: ')
p=int(p)


# In[ ]:


v=input('\nEnter the volume of your equipment in litres: ')
v=int(v)


# In[ ]:


d=input('\nEnter the diameter of the vessel in mm: ')
d=int(d)


# In[ ]:


t=input('\nEnter the fluid temperature in deg. C: ')
t=int(t)


# In[ ]:


if y=='B' or y=='b':
    if p>103:
        if p>4140 and v>42.5:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif p>4140 and v<=42.5 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif p>4140 and v<=42.5 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif p<=4140 and v>42.5 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif p<=4140 and v>42.5 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif p<=4140 and v<=42.5:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
    else:
        print('B51 requirement not applicable')
        input('Press enter to exit...')
elif y=='A' or y=='a':
    if p>103:
        if t>65 and p>4140 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif t>65 and p>4140 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif t>65 and p<=4140 and v>42.5 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
        elif t>65 and p<=4140 and v>42.5 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif t>65 and p<=4140 and v<=42.5:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif t<=65 and p>1720 and v>42.5 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif t<=65 and p>1720 and v>42.5 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif t<=65 and p>1720 and v<=42.5:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
        elif t<=65 and p<=1720:
            print('B51 requirement not applicable')
            input('Press enter to exit...')
    else:
        print('B51 requirement not applicable')
        input('Press enter to exit...')
elif y=='C' or y=='c':
    if p>103:
        if v>42.5:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif v<=42.5 and d>152:
            print('Registered as pressure vessel and inspected by authorized inspector')
            input('Press enter to exit...')
        elif v<=42.5 and d<=152:
            print('Registered as H fitting and inspected by the manufacturer')
            input('Press enter to exit...')
    else:
        print('B51 requirement not applicable')
        input('Press enter to exit...')
else:
    input('Incorrect code entered. Press enter to exit...')
    
        

