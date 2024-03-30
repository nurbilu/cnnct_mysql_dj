from django.db import models

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.CategoryName

class Supplier(models.Model):
    SupplierID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255)
    ContactTitle = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Region = models.CharField(max_length=255, null=True, blank=True)
    PostalCode = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Fax = models.CharField(max_length=255, null=True, blank=True)
    HomePage = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.CompanyName

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    QuantityPerUnit = models.CharField(max_length=255)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    UnitsInStock = models.IntegerField()
    UnitsOnOrder = models.IntegerField(default=0)
    ReorderLevel = models.IntegerField(default=0)
    Discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.ProductName

class Customer(models.Model):
    CustomerID = models.CharField(max_length=5, primary_key=True)
    CompanyName = models.CharField(max_length=255)
    ContactName = models.CharField(max_length=255, null=True, blank=True)
    ContactTitle = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    City = models.CharField(max_length=255, null=True, blank=True)
    Region = models.CharField(max_length=255, null=True, blank=True)
    PostalCode = models.CharField(max_length=255, null=True, blank=True)
    Country = models.CharField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=255, null=True, blank=True)
    Fax = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ContactName

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderDate = models.DateTimeField()
    RequiredDate = models.DateTimeField()
    ShippedDate = models.DateTimeField(null=True, blank=True)
    ShipVia = models.IntegerField()
    Freight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ShipName = models.CharField(max_length=255, null=True, blank=True)
    ShipAddress = models.CharField(max_length=255, null=True, blank=True)
    ShipCity = models.CharField(max_length=255, null=True, blank=True)
    ShipRegion = models.CharField(max_length=255, null=True, blank=True)
    ShipPostalCode = models.CharField(max_length=255, null=True, blank=True)
    ShipCountry = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Order {self.OrderID}'

class OrderDetail(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.IntegerField()
    Discount = models.FloatField()

    def __str__(self):
        return f'Order {self.Order.OrderID} - Product {self.Product.ProductName}'

