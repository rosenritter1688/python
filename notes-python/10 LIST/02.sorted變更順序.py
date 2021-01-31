

#? works in string or list or set
#? not works in set

org_str = 'cebad'
new_str_list = sorted(org_str)
print(f'org_str = \"{org_str}\"')
##org_str = "cebad"
print(f'new_str_list = \"{new_str_list}\"')
##new_str_list = "['a', 'b', 'c', 'd', 'e']"


#* below will use poker as example

import random
typeList=["D","S","C","H"]
num= random.randint(1,13)
cards = set()
def shuffle():
    global cards
    while len(cards) != 52:
        cardtype= random.choice(typeList)
        num = random.randint(1,13)
        str_num = str(num).strip()
        cards.add(cardtype.strip()+str_num)
shuffle()
print("type of cards is ",type(cards))
## type of cards is  <class 'set'>
#! sorted(cards)  #CAUTION!!! cards is a set  
'''
Use sorted on set
'''

print(sorted(cards))
## ['C1', 'C10', 'C11', 'C12', 'C13', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D10', 'D11', 'D12', 'D13', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'H1', 'H10', 'H11', 'H12', 'H13', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'S1', 'S10', 'S11', 'S12', 'S13', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']
print("-----------")


#! turn  set to list
turn_cards_from_set_to_list = list(cards)
print(type(turn_cards_from_set_to_list))
##<class 'list'>


#! cant do in this way
print(turn_cards_from_set_to_list.sort())
## None

#! 正確用法
turn_cards_from_set_to_list.sort()
print(turn_cards_from_set_to_list)
## ['C1', 'C10', 'C11', 'C12', 'C13', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D10', 'D11', 'D12', 'D13', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'H1', 'H10', 'H11', 'H12', 'H13', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'S1', 'S10', 'S11', 'S12', 'S13', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']

