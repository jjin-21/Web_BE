from django.shortcuts import render

# Create your views here.
def price(request, item, num):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if item in product_price:
        total = product_price.get(item) * num
    else:
        total = 0
    context = {
        'item' : item,
        'num' : num,
        'total' : total,
        'product_price' : product_price,
    }
    return render(request, 'prices/price.html', context)