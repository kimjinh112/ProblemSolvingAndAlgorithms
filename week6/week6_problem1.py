list1 = ['risk', 'issue', 'test', 'maintenance', 'maturity']
list2 = ['security', 'plan', 'design', 'systematic', 'safety']
list3 = ['maintenance', 'verification', 'validation']

list4 = [list1, list2, list3]

selection = 0

for i in range(len(list4)):
    if 'maintenance' in list4[i]:
        if len(list4[i]) >= 5:
            selection = i+1

#print('list',selection,'will be tested.')          #둘 다 사용 가능
print('list%d will be tested.' % (selection))       #
            
    
