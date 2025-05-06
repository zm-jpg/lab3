import lab2.lab2 as lab2
def test_find_min_max():
    number_list=[4,3,5,6,3,7,9,10,20]
    max_num,min_num=lab2.calc_max(number_list)
    assert(max_num==20)
    assert(min_num==3)

def test_calc_average():
    number_list=[1,2,3,4,5,6,7]
    average=lab2.calc_average(number_list)
    assert (average==4)

def test_calc_median_temperature():
    number_list=[3,4,4,3,5,7,8,9]
    median=lab2.calc_median(number_list)
    assert (median==4.5)

