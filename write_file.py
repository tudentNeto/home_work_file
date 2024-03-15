list_files=['1.txt', '2.txt', '3.txt']
dict_txt={}
list_str=[]
for el in list_files:
    with open(el, encoding='utf-8') as f:
        for i in f:
            list_str.append(i.strip())
    dict_txt[el]=list_str
    list_str=[]
dict_sort = dict(sorted(dict_txt.items(), key=lambda value: len(value[1])))
for k,v in dict_sort.items():
    with open('result.txt', 'a') as f:
        f.write(k+ '\n')
        f.write(str(len(v))+ '\n')
        for i in v:
            f.write(i+'\n')
