"""Consumer's parameters"""
alphas_factors={"kapital":-0.5,"labor":-0.5}
alphas_goods={"banana":0.5,"apple":0.8}
goods={"banana": 8,"apple": 6}
factors={"kapital":6,"labor":7}
constance=1

"""Define a CobbDouglas function"""
def CobbDouglas(constance,factors,alphas_factors,goods,alphas_goods):
    """In this functions, we're going to use two loops to compute the result. The first one is to iterate through goods and the second one to iterate through factors"""

    """Constance c is the first component of the CobbDouglass function. So we start with a result equal to c and next we multiply the other components"""
    result=constance
    
    """Iterates through goods to compute the X**alpha for each good and multiply to the result"""
    for good in goods:
         result*=goods[good]**alphas_goods[good]

    """Iterate through factors to compute the Y**alpha for each factor and multiply this to the result"""
    for factor in factors:
        result*=factors[factor]**alphas_factors[factor]
    return result

print CobbDouglas(constance,factors,alphas_factors,goods,alphas_goods)


