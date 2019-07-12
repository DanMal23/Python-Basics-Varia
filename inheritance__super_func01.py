# inheritance and super() function

class Sales_DataMart:    
    
    def __init__ (self, sale_id ):
        self.id = sale_id
        
    def get_id(self):
        return self.id
    
class Product(Sales_DataMart):
    
    def  __init__ (self, product_id, product_name, product_category, price, currency):
        super().__init__(product_id)
        self.name = product_name
        self.category = product_category
        self.price = price
        self.currency = currency
        
    def  product_info(self):
        print("Product name: ", self.name, ", category: ", self.category)
        
    def price_info(self):
        print("Product id: ", self.get_id(), ", at price: ", self.price, self.currency)
        
class Supplier(Sales_DataMart):
    
    def __init__(self, supplier_id, supplier_name, supplier_contact):
        super().__init__(supplier_id)
        self.name = supplier_name
        self.contact = supplier_contact
        
    def supplier_info(self):
        print("Product delivered by", self.name, ", contact number:", self.contact)

class Office(Sales_DataMart):
    
    def __init__(self, office_code, office_address):
        super().__init__(office_code)
        self.office_address = office_address
        
    def office_info(self):
        print("Office address:", self.office_address)
        
class Delivery(Sales_DataMart):
   
    def __init__(self, product_id, delivery_date, delivery_address):
        super().__init__(product_id)
        self.date = delivery_date
        self.address = delivery_address
    def delivery_info(self):
        print("Delivery  on: ", self.date, "at address: ", self.address)
        
s1 = Sales_DataMart("011")
print("Sales id:", s1.get_id())
product1 = Product("011", "iPod Touch", "portable media player", "400", "AUD")
product1.product_info()
product1.price_info()
sup1 = Supplier("xyz", "ABC","+61909090")
print("Supplier id: ", sup1.get_id())
sup1.supplier_info()
o = Office("5050", "Perth Street 8")
o.office_info()
d = Delivery("011", "7/7/2019","Green Street 10")
print("Product id: ",d.get_id())
d.delivery_info()



