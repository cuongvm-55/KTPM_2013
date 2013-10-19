from input import main

#doc chuoi docstring tu file input.py
string = main.__doc__.split()

listdata = []
#thao tac voi moi bien
for x in string:
    #lay cac khoang cua tung bien tu xau docstring
    data = []
    x = x.replace("][",";");
    for char in x:
        if (char.isdigit() == False) and (char != '-') and (char != ';'):
            x = x.replace(char,"")
            tmplist = x.split(';');

    data = []
    for item in tmplist:
        data.append(int(item))

    #cat cac khoang cua bien ra 1 mang de kiem tra overlap
    i = 0
    array = []
    while (i < len(data)/2):
        array.append(data[(i*2):i*2+2:1])
        i = i+1
    array = sorted(array) #sap xep mang

    #kiem tra overlap
    i = 0
    while (i < len(array)-1):
        if (array[i][1] >= array[i+1][0]):
            raise Exception("Overlap")
        i = i+1

    #tao cac gia tri cho test
    i = 0
    templist = []
    while (i < len(array)):
        test_value = (array[i][0] + array[i][1]) / 2
        templist.append(test_value)
        i = i+1
    listdata.append(templist)

#Unittest
import itertools
import unittest
from input import main

class Tests(unittest.TestCase): 
    def check(self, *arg):
        self.assertEquals(main(*arg), -1) #goi ham main tu file input.py

for each_variable_data in itertools.product(*listdata):   
    def ch(*arg):
        return lambda self: self.check(*arg)
    setattr(Tests, "test{0}".format(each_variable_data), ch(each_variable_data))

#print element
if __name__=="__main__":
    unittest.main()