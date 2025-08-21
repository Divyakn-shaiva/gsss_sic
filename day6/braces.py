import sys
def my_string(chr):
    open_count = 0
    close_count = 0
    my_str = my_str.count
    for i in range(my_str):
        if open_count > close_count:
            print(my_str)
            i += 1
        else:
            print("not properly arranged")
my_str =  sys.argv[1]
my_string(chr)
#argv -->we need to give input along with run command
#python -m pdb filename .py
#help
#n -->next
# q--->quit
#s -->step when function calls
'''import pdb
pdb.set_trace()'''
#codechef.com     codeforces.com
#bengaluru.find("ooru") --> returns -1
#bengaluru.index("ooru") --> ValueError      find and index  both acts as same 

