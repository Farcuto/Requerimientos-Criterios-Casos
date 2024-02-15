import pytest
import time
from firts_assigment import romans_converted


def test_roman_conversion(decimal=1):
    assert romans_converted(decimal) == "I"
    
def test_2(decimal=3999):
    assert  romans_converted(decimal) == "MMMCMXCIX"
def test_3(decimal=1892):
    assert romans_converted(decimal) == "MDCCCXCII"

def test_5(decimal=0):
    assert  romans_converted(decimal=0) == None
def  test_6(decimal=4000):
    assert romans_converted(decimal=4000)== None
def test_7():
    tI =  time.time() * 1000
    romans_converted(decimal=1940)
    tF = time.time() * 1000
    tR = tF - tI
    print(f"The execution of the function took {tR} seconds")
    assert tR <= 0.5
    
test_roman_conversion()
test_2()
test_3()
test_7()
test_5()
test_6()

