from abc import ABC, abstractmethod

# Interfaz para Facturas
class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self):
        pass

    @abstractmethod
    def get_invoice_details(self):
        pass

# Implementación de Factura Local
class LocalInvoice(Invoice):
    def __init__(self, invoice_number, date, amount):
        self.invoice_number = invoice_number
        self.date = date
        self.amount = amount

    def generate_invoice(self):
        return f"Factura Local: #{self.invoice_number} - Fecha: {self.date} - Monto: {self.amount}"

    def get_invoice_details(self):
        return f"Factura Local Detalles: {self.generate_invoice()}"

# Implementación de Factura Internacional
class InternationalInvoice(Invoice):
    def __init__(self, invoice_number, date, amount, exchange_rate):
        self.invoice_number = invoice_number
        self.date = date
        self.amount = amount
        self.exchange_rate = exchange_rate

    def generate_invoice(self):
        amount_in_local_currency = self.amount * self.exchange_rate
        return f"Factura Internacional: #{self.invoice_number} - Fecha: {self.date} - Monto: {self.amount} - Tipo de Cambio: {self.exchange_rate} - Monto en Moneda Local: {amount_in_local_currency}"

    def get_invoice_details(self):
        return f"Factura Internacional Detalles: {self.generate_invoice()}"

# Fábrica Abstracta
class InvoiceFactory(ABC):
    @abstractmethod
    def create_invoice(self, invoice_number, date, amount, exchange_rate=None):
        pass

# Implementación de la Fábrica para Facturas Locales
class LocalInvoiceFactory(InvoiceFactory):
    def create_invoice(self, invoice_number, date, amount, exchange_rate=None):
        return LocalInvoice(invoice_number, date, amount)

# Implementación de la Fábrica para Facturas Internacionales
class InternationalInvoiceFactory(InvoiceFactory):
    def create_invoice(self, invoice_number, date, amount, exchange_rate):
        return InternationalInvoice(invoice_number, date, amount, exchange_rate)

# Creación y uso de la fábrica de facturas locales
local_invoice_factory = LocalInvoiceFactory()
local_invoice = local_invoice_factory.create_invoice(1, "2023-01-01", 100)
print(local_invoice.get_invoice_details())

# Creación y uso de la fábrica de facturas internacionales
international_invoice_factory = InternationalInvoiceFactory()
international_invoice = international_invoice_factory.create_invoice(2, "2023-01-01", 1000, 1.5)
print(international_invoice.get_invoice_details())
