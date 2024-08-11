from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Jacket(models.Model):
    code = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField()
    total_pice_quantity = models.IntegerField(default=0)
    manafacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.sale_price

    def __str__(self):
        return f"{self.fabric_type.name} - {self.size}"


class Pant(models.Model):
    brand_name = models.CharField(max_length=50)
    cutt_no = models.CharField(max_length=50)  # Allows storing a list of numbers
    wash = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    piece_style = models.CharField(max_length=50)
    wash_type = models.CharField(max_length=50) 
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    set_quantity = models.IntegerField()
    quantity = models.IntegerField()
    total_pcs_quantity = models.IntegerField(default=0)
    manufacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    # brand_name = models.CharField(max_length=100)
    
    def total_price(self):
        return self.quantity * self.sale_price
    def __str__(self):
        return f'{self.fabric_type} - {self.size}'



class Shirt(models.Model):
    code = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField()
    total_pice_quantity = models.IntegerField(default=0)
    manafacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.sale_price

    def __str__(self):
        return f"{self.fabric_type.name} - {self.size}"



class Shorts(models.Model):
    
    brand_name = models.CharField(max_length=50)
    cutt_no = models.CharField(max_length=50)  # Allows storing a list of numbers
    wash = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    piece_style = models.CharField(max_length=50)
    wash_type = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    set_quantity = models.IntegerField()
    quantity = models.IntegerField()
    total_pcs_quantity = models.IntegerField(default=0)
    manufacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def total_price(self):
        return self.quantity * self.sale_price
    def __str__(self):
        return f'{self.fabric_type} - {self.size}'
    

class T_shirt(models.Model):
    code = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField()
    total_pice_quantity = models.IntegerField(default=0)
    manafacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.sale_price

    def __str__(self):
        return f"{self.fabric_type.name} - {self.size}"


class Trouser(models.Model):
    brand_name = models.CharField(max_length=50)
    cutt_no = models.CharField(max_length=50)  # Allows storing a list of numbers
    wash = models.CharField(max_length=50)
    fabric_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    piece_style = models.CharField(max_length=50)
    wash_type = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    set_quantity = models.IntegerField()
    quantity = models.IntegerField()
    total_pcs_quantity = models.IntegerField(default=0)
    manufacturing_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def total_price(self):
        return self.quantity * self.sale_price
    def __str__(self):
        return f'{self.fabric_type} - {self.size}'



