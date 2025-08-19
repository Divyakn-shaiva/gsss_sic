def find(main_string, sub_string, start = 0, end = None):
    if end is None:
        end = len(main_string)
    for i in range(start, end - len(sub_string) + 1):
        if main_string[i : i + len(sub_string)] == sub_string:
            return i
    return -1
print(find("meghalaya" , "laya"))
print(find("meghalaya" , "laya" , 5 , 8))
print(find("meghalaya" , " "))