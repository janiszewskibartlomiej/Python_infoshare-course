from homework1.shop.products import products


def order(product_name, value):
    list_of_order = []
    price = products[product_name]
    total_price = int(price['cena']) * value
    order_dict = {
        'product_name': product_name,
        'value': value,
        'total price': total_price
    }
    list_of_order.append(order_dict)
    return list_of_order
