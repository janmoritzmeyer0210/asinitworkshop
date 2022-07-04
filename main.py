import PySimpleGUI as sg

from controller.ProductController import ProductController

sg.theme('Material 2')

if __name__ == '__main__':
    productController = ProductController()
    while True:
        layout = [[sg.Text("Mein toller Onlineshop"), sg.Image("img/otto.png")]]
        for product in productController.getProducts():
            ## Aufgabe 2
            if product.stock < 1:
                continue
            ## Aufgabe 3
            layout.append([sg.Text("{} noch {} mal verfügbar \r\n{}".format(product.name, product.stock, product.description)), sg.Button("{}€".format(float(product.price)/100), key=product.name), sg.Image(product.img, size=(100,100))])
        window = sg.Window(title="Toller Shop", layout=layout, margins=(100, 50))
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                quit()
            product = productController.getProductByName(event)
            product.reduceStock()
            window.close()
            break


