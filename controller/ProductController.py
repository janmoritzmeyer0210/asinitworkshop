from model.Product import Product


class ProductController:
    products = [
        Product("Haar Shampoo", 499, 5, description="Dis ist toll weil Baum"),
        Product("Duschgel", 499, 8),
        ## Aufgabe 1
        Product("Rasierer", 499, 3),
        Product("Zahnbürste", 499, 2),
        Product("Telefon", 899, 1)
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
