# Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można produkt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    shop_items = {'t-shirt': [100, 'M'], 'jeans': [200, 'S']}

    def show(self):
        print(self.shop_items)

    def try_item(self, id):
        print(self.shop_items[id])

    def buy_item(self, id):
        self.shop_items.pop(id)

    def return_item(self, item):
        self.shop_items.update(item)


if __name__ == '__main__':
    client = Shop()
    Shop.show(client)
    Shop.try_item(client, 't-shirt')
    Shop.buy_item(client, 'jeans')
    Shop.show(client)
    Shop.return_item(client, {'jeans': [200, 'S']})
    Shop.show(client)
