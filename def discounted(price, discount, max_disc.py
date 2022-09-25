def discounted(price, discount, max_discount=20):
    price=abs(price)
    discount=abs(discount)
    max_discount=abs(max_discount)
    if max_discount>=100:
        raise ValueError("Max discount cant be higher than 100")
    if discount>=max_discount:
        price_with_disc=price
    else:
        price_with_disc=price-price*discount/100
    return price_with_disc
    

print(discounted(100,40, max_discount=60))