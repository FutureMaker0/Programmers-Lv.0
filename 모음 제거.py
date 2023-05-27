def solution(my_string):
    
    for i in "aeiou":
        if i in my_string:
            my_string = my_string.replace(i, "")

    return my_string
