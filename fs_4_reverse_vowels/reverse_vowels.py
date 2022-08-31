import copy
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    temp_list = []
    temp_s_list =list(s)
    for i in range (len(s)-1):
        if s[i] in vowels:
            temp_list.append([s[i],i])
    #print (temp_list)

    temp_list_reversed = copy.deepcopy(temp_list)
    temp_list_reversed.reverse()
   # print(temp_list_reversed)
    for i in range (len(temp_list_reversed)):
    
       
        temp_list[i][0] = temp_list_reversed[i][0]
    
   # print(temp_list_reversed)
    #print(temp_s_list)

    for char in temp_list:
        
        temp_s_list[char[1]] = char[0]

    return f"{''.join(temp_s_list)}"



print(reverse_vowels("Reverse Vowels In A String"))