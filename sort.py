def mylist(sorted_list):
    sorted_list = [2,0,3,6,5,9,4,7,'s','n']
    list_of_odds = []
    list_of_evens = []
    list_of_chars = []
    list_of_others = []
    new_dict = {}
    for x in sorted_list:
        if isinstance(x,int):
            if(x%  2 == 0):
                list_of_evens.append(x)
            else:
                list_of_odds.append(x)    
        elif isinstance(x,str):
             list_of_chars.append(x)
        else:
             list_of_others.append(x)
    new_dict['odds'] = sorted(list_of_odds)
    new_dict['evens'] = sorted(list_of_evens)
    new_dict['chars'] = sorted(list_of_chars)
    new_dict ['others'] = sorted(list_of_others)

    print(sorted_list)



