import PySimpleGUI as sg

from controller.ProductController import ProductController

sg.theme('Dark Blue 3')

if __name__ == '__main__':
    productController = ProductController()
    while True:
        layout = [[sg.Text("Mein toller Onlineshop")]]
        for product in productController.getProducts():
            layout.append([sg.Text("{} noch {} mal verfügbar".format(product.name, product.stock)), sg.Button(product.name), sg.Image(product.img, size=(100,100))])
        window = sg.Window(title="Toller Shop", layout=layout, margins=(100, 50))
        while True:
            event, _ = window.read()
            product = productController.getProductByName(event)
            product.reduceStock()
            window.close()
            break


