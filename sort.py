def mylist(sorted_list):

    

    odds = []
    evens = []
    characters = []

    new_dict = dict()
    
    new_dict['odds'] = odds
    new_dict['evens'] = evens
    new_dict['chars'] = characters

   

    for x in sorted_list:
        if isinstance(x,int):
            if x %  2 == 0:
               evens.append(x)
            else:
              odds.append(x)    
        elif isinstance(x, str):
            characters.append(x)
    
    new_dict['odds'] = sorted(odds)
    new_dict['evens'] = sorted(evens)
    new_dict['chars'] = sorted(characters)
    return new_dict

if __name__=='__main__':
   print (mylist([2,0,3,6,5,9,4,7,'s','n']))



