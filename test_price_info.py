
import price_info

def test_total_cost_shopping():
    price_info.price_list= {'apple':1.5,'orange':1.2 ,'banana':1.1,'pear':1.5}
    price_info.quantity_list= {'apple':100,'orange':50,'banana':68,'pear':42}
    totalcosts=price_info.total_cost_shopping()
    
    assert (totalcosts==347.8)

def test_cost_of_fruit():
    price_info.price_list= {'apple':1.5,'orange':1.2 ,'banana':1.1,'pear':1.5}
    price_info.quantity_list= {'apple':100,'orange':50,'banana':68,'pear':42}
    fruit='pear'
    quantity=50
    costs=price_info.cost_of_fruits(fruit,quantity)

    assert (costs==75)