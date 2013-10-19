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

    #kiem tra cac khoang co hop le hay khong
    i = 0
    while (i < len(array)):
        if (array[i][1] < array[i][0]):
            raise Exception("wrong input")
        i = i+1
    
    #kiem tra overlap
    i = 0
    while (i < len(array)-1):
        if (array[i][1] >= array[i+1][0]):
            raise Exception("wrong input")
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
import unittest
import itertools

class Tests(unittest.TestCase):
        pass

def test_generator(*args):
    def test(self):
        self.assertEqual(main(*args),1)
    return test

if __name__=="__main__":
    for arr in itertools.product(*listdata):
        test_name='test{0}'.format(arr)
        test = test_generator(*arr)
        setattr(Tests,test_name,test)
    unittest.main()
