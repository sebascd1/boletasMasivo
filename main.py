from estructuras import *
import math

##
# Var 1: SKU
# Var 2: Precio Unitario
# Var 3: Cantidad
# Var 4: Cantidad x SKU
# Var 5: RUC



def skugroup(docuInterno):

    mapita = {}

    #Mapea las cantidades necesarias por cada SKU
    for currItem in docuInterno.LineItems:

        #Suma al mapa la cantidad de items por cada SKU.
        if(currItem.sku in mapita):

            mapita[currItem.sku] += currItem.cantidad
        else:
            mapita[currItem.sku] = currItem.cantidad

    print("Las llaves son ", mapita)
    return mapita

        
def crearLineItems(skus):

    acumulado = 0
    items = []

    for currKey in skus.keys():
            
        newItem = LineItems("Boleta", "Documento", currKey, 0)
        
        if(acumulado < 699.99):

            items.append(newItem)

            for i in range(skus[currKey]):

                if(acumulado + currKey.precio < 699.99):

                    acumulado += currKey.precio
                    newItem.cantidad = i + 1
            
            newItem.setImporte()

            print("SKU", currKey.code, " tendrá ", newItem.cantidad, " elementos con importe de", newItem.importe)


    print("La boleta tendrá ", len(items), " ítems.")

restart = True
totalLineas = []

while restart == True:
    ruc = input("Ingrese RUC de la Boleta")
    codigoProd = input("Ingrese codigo de producto")
    precioProd = float(input("Ingrese precio unitario del producto"))
    cantidadProd = int(input("Ingrese cantidad de unidades"))
    
    crearLinea = input("Desea crear una nueva línea?")

    if(crearLinea == "no"):
        restart = False
    
    nuevoSku = sku(codigoProd, precioProd)
    nuevaLinea = LineItems("Boleta", "Docu", nuevoSku, cantidadProd)
    totalLineas.append(nuevaLinea)

docuInterno = DocumentoInterno(totalLineas, ruc)

mapa = skugroup(docuInterno)
crearLineItems(mapa)


###
# boleta = BoletaSalida("700000",  [linea1, linea2])
# print(linea1.importe)
# sku.verify(sku1)
# print("Total Boleta ",boleta.total)

