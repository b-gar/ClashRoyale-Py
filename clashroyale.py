# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:26:47 2019

@author: Owner
"""

#def clash (rarity, current card level, current # cards for card, current total of gold)

commoncost = [5,20,50,150,400,1000,2000,4000,8000,20000,50000,100000]
rarecost = [50,150,400,1000,2000,4000,8000,20000,50000,100000]
epiccost = [400,2000,4000,8000,20000,50000,100000]
legendarycost = [5000,20000,50000,100000]

costdictionary = {"common":commoncost,"rare":rarecost,"epic":epiccost,"legendary":legendarycost}

commoncards = [2,4,10,20,50,100,200,400,800,1000,2000,5000]
rarecards = [2,4,10,20,50,100,200,400,800,1000]
epiccards = [2,4,10,20,50,100,200]
legendarycards = [2,4,10,20]

cardsdictionary = {"common":commoncards,"rare":rarecards,"epic":epiccards,"legendary":legendarycards}

def clash(rarity, currentlevel, currentcards, currentgold):
    # Turn Inputs Into Integers
    cl = int(currentlevel)
    cc = int(currentcards)
    cg = int(currentgold)
    
    # Common
    if rarity == str("common"):
        
        # Reference Common Dictionaries
        refcost = costdictionary["common"]
        refcards = cardsdictionary["common"]
        
        # Temp Variables
        cltemp = cl-2
        cgtemp = cg
        cctemp = cc
        
        # 1. cost
        for i in range(1,14-cl):
            tempcost = refcost[cltemp+i]
            newgold = cgtemp - tempcost
            finallevelcost = cl + i
            cgtemp = newgold
            try:   
                if cgtemp < refcost[cltemp+i+1]:
                        finallevelcost = cl + i
                        break
            except IndexError:
                if i == 1:
                    finallevelcost = cl
                else:
                    finallevelcost = cl + i
        print("Max Level Using Gold is:",finallevelcost)
        # 2. cards
        for i in range(1,14-cl):
            tempcards = refcards[cltemp+i]
            newcards = cctemp - tempcards
            finallevelcards = cl + i
            cctemp = newcards
            try:
                if cctemp < refcards[cltemp+i+1]:
                    finallevelcards = cl + i
                    break
            except IndexError:
                if i == 1:
                    finallevelcards = cl
                else:
                    finallevelcards = cl + i
        print("Max Level Using Cards is:",finallevelcards)
        
        finall = min(finallevelcost,finallevelcards)
        print("Your Max Card Level is: " + str(finall))
###############################################################         
     # Rare   
    elif rarity == str("rare"):
        
        # Reference Rare Dictionaries
        refcost = costdictionary["rare"]
        refcards = cardsdictionary["rare"]
        
        #Temp Variables
        cltemp = cl-4
        cgtemp = cg
        cctemp = cc
        
        # 1. cost
        for i in range(1,14-cl):
            tempcost = refcost[cltemp+i]
            newgold = cgtemp - tempcost
            finallevelcost = cl + i
            cgtemp = newgold
            try:   
                if cgtemp < refcost[cltemp+i+1]:
                        finallevelcost = cl + i
                        break
            except IndexError:
                if i == 1:
                    finallevelcost = cl
                else:
                    finallevelcost = cl + i
        print("Max Level Using Gold is:",finallevelcost)
        # 2. cards
        for i in range(1,14-cl):
            tempcards = refcards[cltemp+i]
            newcards = cctemp - tempcards
            finallevelcards = cl + i
            cctemp = newcards
            try:
                if cctemp < refcards[cltemp+i+1]:
                    finallevelcards = cl + i
                    break
            except IndexError:
                if i == 1:
                    finallevelcards = cl
                else:
                    finallevelcards = cl + i
        print("Max Level Using Cards is:",finallevelcards)
        
        finall = min(finallevelcost,finallevelcards)
        print("Your Max Card Level is: " + str(finall))
###############################################################        
    elif rarity == str("epic"):
        
        #Reference Epic Dictionaries
        refcost = costdictionary["epic"]
        refcards = cardsdictionary["epic"]
        
        #Temp Variables
        cltemp = cl-7
        cgtemp = cg
        cctemp = cc
        
        # 1. cost
        for i in range(1,14-cl):
            tempcost = refcost[cltemp+i]
            newgold = cgtemp - tempcost
            finallevelcost = cl + i
            cgtemp = newgold
            try:   
                if cgtemp < refcost[cltemp+i+1]:
                        finallevelcost = cl + i
                        break
            except IndexError:
                if i == 1:
                    finallevelcost = cl
                else:
                    finallevelcost = cl + i
        print("Max Level Using Gold is:",finallevelcost)
        # 2. cards
        for i in range(1,14-cl):
            tempcards = refcards[cltemp+i]
            newcards = cctemp - tempcards
            finallevelcards = cl + i
            cctemp = newcards
            try:
                if cctemp < refcards[cltemp+i+1]:
                    finallevelcards = cl + i
                    break
            except IndexError:
                if i == 1:
                    finallevelcards = cl
                else:
                    finallevelcards = cl + i
        print("Max Level Using Cards is:",finallevelcards)
    
        finall = min(finallevelcost,finallevelcards)
        print("Your Max Card Level is: " + str(finall))
 ###############################################################        
    elif rarity == str("legendary"):
        
        refcost = costdictionary["legendary"]
        refcards = cardsdictionary["legendary"]
    
        #Temp Variables
        cltemp = cl-10
        cgtemp = cg
        cctemp = cc
        
        # 1. cost
        for i in range(1,14-cl):
            tempcost = refcost[cltemp+i]
            newgold = cgtemp - tempcost
            finallevelcost = cl + i
            cgtemp = newgold
            try:   
                if cgtemp < refcost[cltemp+i+1]:
                        finallevelcost = cl + i
                        break
            except IndexError:
                if i == 1:
                    finallevelcost = cl
                else:
                    finallevelcost = cl + i
        print("Max Level Using Gold is:",finallevelcost)
        # 2. cards
        for i in range(1,14-cl):
            tempcards = refcards[cltemp+i]
            newcards = cctemp - tempcards
            finallevelcards = cl + i
            cctemp = newcards
            try:
                if cctemp < refcards[cltemp+i+1]:
                    finallevelcards = cl + i
                    break
            except IndexError:
                if i == 1:
                    finallevelcards = cl
                else:
                    finallevelcards = cl + i
        print("Max Level Using Cards is:",finallevelcards)
    
        finall = min(finallevelcost,finallevelcards)
        print("Your Max Card Level is: " + str(finall))
    else:
        print("Please Recheck Your Arguments")