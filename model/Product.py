class Product:
    name = str
    price = int  # in cents
    stock = int
    img = str

    def __init__(self, name, price, stock, img = "/Users/appsazubi/PycharmProjects/ottoshop/img/ice.png"):
        self.name = name
        self.price = price
        self.stock = stock
        self.img = img

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.stock

    def reduceStock(self, reduction=1):
        self.stock -= reduction

