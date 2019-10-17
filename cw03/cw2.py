



def unique(list1):
    list1 = [ char for char in list1 ]
    unique_list = [];

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return  unique_list;

def info(data_text):
    dict = {'length': len(data_text), 'letters': unique(data_text) , 'big_letters': data_text.upper(), 'small_letters': data_text.lower() };
    return dict;

zmienna = "Napiss gcghghfghfghf jghfgfh ghfjhg";
print(info(zmienna));