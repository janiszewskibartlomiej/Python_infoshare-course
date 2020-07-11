from homework1.shop.order import order


def list_of_order():
    product = input("Proszę podac nazwe produktu: ")
    value = input("Proszę podac ilość: ")
    order_list = order(product_name=product, value=int(value))
    return order_list


if __name__ == '__main__':
    ord = list_of_order()
    print(ord)
