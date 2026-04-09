class Product:
    def __init__(self, sku, name, price):
        if price < 0:
            raise ValueError("Price must be >= 0")
        self.sku = sku
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(sku={self.sku!r}, price={self.price})"

    def __eq__(self, other):
        return isinstance(other, Product) and self.sku == other.sku


class Inventory:
    def __init__(self):
        self._stock = {}

    def add_stock(self, sku, qty):
        if qty <= 0:
            raise ValueError("qty must be > 0")
        self._stock[sku] = self._stock.get(sku, 0) + qty

    def remove_stock(self, sku, qty):
        if qty <= 0:
            raise ValueError("qty must be > 0")
        available = self._stock.get(sku, 0)
        if qty > available:
            raise ValueError("not enough stock")
        self._stock[sku] = available - qty

    def available(self, sku):
        return self._stock.get(sku, 0)


class CartItem:
    def __init__(self, product, qty):
        if qty < 1:
            raise ValueError("qty must be >= 1")
        self.product = product
        self.qty = qty


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, qty):
        self.items.append(CartItem(product, qty))

    def remove(self, sku):
        self.items = [item for item in self.items if item.product.sku != sku]

    def total(self):
        return sum(item.product.price * item.qty for item in self.items)


class Checkout:
    def __init__(self, inventory, cart):
        self.inventory = inventory
        self.cart = cart

    def place_order(self):
        for item in self.cart.items:
            if self.inventory.available(item.product.sku) < item.qty:
                raise ValueError("insufficient stock")
        for item in self.cart.items:
            self.inventory.remove_stock(item.product.sku, item.qty)
        receipt = {
            "items": [
                {"sku": i.product.sku, "qty": i.qty, "price": i.product.price}
                for i in self.cart.items
            ],
            "total": self.cart.total(),
        }
        return receipt


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_stock("SKU1", 10)

    cart = Cart()
    cart.add(Product("SKU1", "Keyboard", 25.0), 2)

    checkout = Checkout(inventory, cart)
    print(checkout.place_order())
