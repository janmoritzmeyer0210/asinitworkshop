import PySimpleGUI as sg

class Product:
    name = str
    price = int  # in cents
    stock = int
    img = str
    description = str

    def __init__(self, name, price, stock, img = "img/ice.png", description = ""):
        self.name = name
        self.price = price
        self.stock = stock
        self.img = img
        self.description = description

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getStock(self):
        return self.stock

    def reduceStock(self, reduction=1):
        self.stock -= reduction

class ProductController:
    products = [
        Product("Rasierer", 499, 5, description="Dis ist toll weil Baum", img="img/rasierer.png"),
        Product("Duschgel", 499, 8, img="img/shampoo.png"),
        Product("iPhone", 104999, 1, img="img/iphone.png")
    ]

    def getProduct(self, index):
        return self.products[index]

    def getProducts(self):
        return self.products

    def getProductByName(self, name):
        for product in self.products:
            if product.name == name:
                return product

    def buyProduct(self, index):
        self.getProduct(index).reduceStock()

sg.theme('Material 2')

## Aufgabe 4
def createCheckoutWindow(product = Product):
    layout = [[sg.Text("Produkt: {}".format(product.name))],[sg.Text("Zahlungsarten:")],[sg.Button("Paypal")]]
    sg.Window(title="Checkout", layout=layout).read()

if __name__ == '__main__':
    productController = ProductController()
    while True:
        layout = [[sg.Text("Mein toller Onlineshop"), sg.Image("img/otto.png")]]
        for product in productController.getProducts():
            ## Aufgabe 2
            if product.stock < 1:
                continue
            ## Aufgabe 3
            productText = sg.Text("{} noch {} mal verfügbar \r\n{}".format(product.name, product.stock, product.description))
            productButton = sg.Button("{}€".format(float(product.price) / 100), key=product.name)
            productImage = sg.Image(product.img, size=(100, 100))
            layout.append([productText, productButton, productImage])
        window = sg.Window(title="Toller Shop", layout=layout, margins=(100, 50))
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                quit()
            product = productController.getProductByName(event)
            product.reduceStock()
            createCheckoutWindow(product)
            window.close()
            break



