

class DocumentoInterno:
    def __init__(self,LineItems,ruc):
        self.LineItems = LineItems
        self.ruc = ruc

class LineItems:
    def __init__(self, tipoDocumento, documento, sku, cantidad):
        self.sku = sku
        self.cantidad = cantidad
        self.importe = 0
        self.documento = documento
        self.tipoDocumento = tipoDocumento

    def setImporte(self):
        self.importe = self.cantidad * self.sku.precio

class sku:
    def __init__(self, code, precio):
        self.code = code
        self.precio = precio

    def verify(sku):
        print("Tu SKU tiene el código ", sku.code)

class BoletaSalida:

    def __init__(self, ruc, LineItems):
        self.ruc = ruc
        self.LineItems = LineItems
        self.total = self.importeTotal()

    def importeTotal(self):

        total = 0
        
        for currItem in self.LineItems:
            total += currItem.importe
        return total
            
        

