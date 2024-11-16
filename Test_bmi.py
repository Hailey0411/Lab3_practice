import Lab2_practice.calculate_bmi as bmi

print ("test_bmi")

def test_bmi_overweight():
    assert bmi.calculate_bmi(weight=90,height=1.73)==1

def test_bmi_normal_weight():
    assert bmi.calculate_bmi(weight=70,height=1.73)==0

def test_bmi_underweight():  
    assert bmi.calculate_bmi(weight=50,height=1.73)==-1