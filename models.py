from django.db import models
from django.utils import timezone


# Create your models here.

class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    year = models.IntegerField()
    for_sale = models.BooleanField()

    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state_province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    

class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=200, unique=True)
    date = models.DateField()

    # 1 car per invoice
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)



class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=200, decimal_places=2)
    
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=200)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    date_received = models.DateTimeField("date received")
    comments = models.CharField(max_length=20000)
    date_returned = models.DateField(null=True, blank=True)    

class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)

    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)

    hours = models.CharField(max_length=200)
    comment = models.CharField(max_length=20000)
    rate = models.DecimalField(max_digits=200, decimal_places=2)
    
class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    purchase_price = models.DecimalField(max_digits=200, decimal_places=2)
    retail_price = models.DecimalField(max_digits=200, decimal_places=2)


class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)

    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)

    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=200, decimal_places=2)

