def solution(price):
    if price < 100000:
        return int(price)
    elif 100000 <= price and price < 300000:
        return int(price*0.95)
    elif 300000 <= price and price < 500000:
        return int(price*0.90)
    elif 500000 <= price:
        return int(price*0.80)