import unittest
import math
from kiemtratamgiac import KiemTraTamGiac

class TestSequenceFunctions(unittest.TestCase) :
    
    def test_a_is_invalidInputRange(self):
            self.assertEqual(KiemTraTamGiac(-1,1,1),"Input Range Error")
    
    def test_b_is_invalidInputRange(self):
            self.assertEqual(KiemTraTamGiac(1,-1,1),"Input Range Error")
    
    def test_c_is_invalidInputRange(self):
            self.assertEqual(KiemTraTamGiac(1,1,-1),"Input Range Error")
    
    def test_abc_is_invalidInputRange_LessThan_MIN(self):
            self.assertEqual(KiemTraTamGiac(-1,-1,-1),"Input Range Error")

    def test_abc_is_invalidInputRange_GreaterThan_MAX(self):
            self.assertEqual(KiemTraTamGiac(2**32,2**32,2**32),"Input Range Error")
    
    def test_a_is_invalidInputType(self):
            self.assertEqual(KiemTraTamGiac('s',1,1),"Input Type Error")
    
    def test_b_is_invalidInputType(self):
            self.assertEqual(KiemTraTamGiac(1,'s',1),"Input Type Error")
            
    def test_c_is_invalidInputType(self):
            self.assertEqual(KiemTraTamGiac(1,1,'s'),"Input Type Error")
            
    def test_abc_is_invalidInputType(self):
            self.assertEqual(KiemTraTamGiac('s','s','a'),"Input Type Error")
            
    def test_TamGiacThuong(self):
            self.assertEqual(KiemTraTamGiac(2,3,4),"Thuong")

    def test_TamGiacVuong_Tai_a(self):
            self.assertEqual(KiemTraTamGiac(5,4,3),"Vuong")

    def test_TamGiacVuong_Tai_b(self):
            self.assertEqual(KiemTraTamGiac(4,5,3),"Vuong")

    def test_TamGiacVuong_Tai_c(self):
            self.assertEqual(KiemTraTamGiac(3,4,5),"Vuong")

    def test_TamGiacDeu(self):
            self.assertEqual(KiemTraTamGiac(3,3,3),"Deu")

    def test_TamGiacCan(self):
            self.assertEqual(KiemTraTamGiac(3,3,4),"Can")

    def test_TamGiacVuongCan(self):
            self.assertEqual(KiemTraTamGiac(1,1,math.sqrt(2)),"Vuong Can")
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()
