class My_assignment:
    #question no 1
    def sort_list_int(self):
        a = eval(input('enter a unordered int list'))
        l = len(a)
        for i in range(0, l):
            for j in range(0 , l - i -1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a
                    
    #question number 2
    def two_list_in_dict(self):
        a = eval(input('enter int list to make dict : '))
        b = eval(input('enter str dict to make dict : '))
        dict1 = {a[i] : b [i] for i in range(len(b))}
        return dict1

    #question no 3
    def common_num(self):
        a = eval(input('enter the first list to print common num : '))
        b = eval(input('enter the second list to print common num : '))

        result = [ ]
        for x in a:
            for y in b:
                if x == y:
                    result.append(x)
        return result
    
    #question no 4
    def add_occupation_in_dict(self):
        nested_dict = eval(input("enter a nested dictionary : "))

        for k , v in nested_dict.items():
            v['occupation'] = 'engineer'
        return nested_dict
        
    #question no 5
    def change_same_values_int(self): 
        a =eval(input('enter the dict with str key and int value : '))
        x =eval(input('enter the old value : '))
        y =eval(input('enter the new value : ')) 
        for k , v in a.items():
            if v == x: 
                a[k] = y
        return a
                
    #question no 6
    def change_same_values_str(self): 
        a =eval(input('enter the dict with int key and str value : '))
        x =eval(input('enter the old value : '))
        y =eval(input('enter the new value : ')) 
        for k , v in a.items():
            if v == x: 
                a[k] = y
        return a
                
    #question no 7
    def sort_list_str(self):
        a = eval(input('enter a unordered str list : '))
        l = len(a)
        for i in range(0, l):
            for j in range(0 , l - i -1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a
        
    #question no 8
    def sort_list_tuple(self):
        a = eval(input('enter a unordered list with tuple : '))
        l = len(a)
        for i in range(0, l):
            for j in range(0 , l - i -1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        
        return a
        
x = My_assignment()
result = x.sort_list_int()
print(result)

result = x.two_list_in_dict()
print(result)

result = x.common_num()
print(result)

result = x.add_occupation_in_dict()
print(result)

result = x.change_same_values_int()
print(result)

result = x.change_same_values_str()
print(result)

result = x.sort_list_str()
print(result)

result = x.sort_list_tuple()
print(result)