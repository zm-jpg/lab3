import lab2.bmi as bmi



def test_bmi_normal_weight(): 
    bmi_1,category= bmi.calculate_bmi(1.8,80)
    result=80/(1.8*1.8)
    assert (result==bmi_1)
    assert (category==0)

def test_bmi_over_weight(): 
    bmi_1,category=bmi.calculate_bmi(1.8,90)
    result=90/(1.8*1.8)
    assert (result==bmi_1)
    assert (category==1)

def test_bmi_under_weight():
    bmi_1,category=bmi.calculate_bmi(1.8,59)
    result=59/(1.8*1.8)
    assert (result==bmi_1)
    assert (category==-1)