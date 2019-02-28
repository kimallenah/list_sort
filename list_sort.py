

def list_sort(lst):
    even = []
    odd = []
    char = []
    for element in lst:
        if str(element) >= '0' and str(element) <= '9':
            if element % 2 == 0:
                even.append(element)
            else:
                odd.append(element)
        else:
            char.append(element)
            
    
    even.sort()
    odd.sort()
    char.sort()

    final_answer = {
        'evens': even,
        'odd': odd,
        'char': char
    }

    return print(final_answer)

lst1 = ['a', 2, 0, 'z', 6, 5, 1, 7]
list_sort(lst1)