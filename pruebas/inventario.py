#estructura basica
#lista para guardar los productos
inventory = []


#2.funcion para mostrar el menu
def show_menu():
    print("\n---menu the inventary---")
    print("1. Add product")
    print("2. Show products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6.calculate total value")
    print("7. Exit")


#3.funcion para agregar productos
def add_product():
    #añade un nuevo producto a la lista
    print("\n---add product---")
    name = input("Enter the product name: ")
    #verificar si ya existe el producto
    for p in inventory:
        if p["name"].lower() == name.lower():
            print("the product already exists")
            return
        #validacion
        try: 
            price = float(input("price: "))
            quantity = int(input("quantity: "))
        except:
            print("error: price and quantity must be numbers")
            return
        inventory.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print("added product successfully!")
        print(inventory)
        #crea un diccionario con los datos y lo agrega alinventario
        #4.funcion para mostrar los productos
def show_products():
    #muestra todos los productos en el inventario
    print("\n---show products---")
    if not inventory:
        print("no products in the inventory")
        return
    for p in inventory:
        print(f"{p['name']} - price: ${p['price']} - quantity: {p['quantity']}")
#5.funcion para buscar un producto
def search_product():
    #busca un producto por nombre
    print("\n---search product---")
    name = input("Enter the product name: ").lower()
    for p in inventory:
        if p["name"].lower() == name:
            print(f"name: {p["name"]}")
            print(f"price: ${p["price"]}")  
            print(f"quantity: {p["quantity"]}")
            return
    print("product not found")
#6.funcion para actualizar un producto
def update_product():
    #actualiza el precio de un producto
    print("\n---update product---")
    name = input("Enter the product name: ").lower()
    for p in inventory:
        if p["name"].lower() == name:
            try:
                new_price = float(input("new price: "))
                p["price"] = new_price
                print("product updated successfully!")
            except:
                print("error: price and quantity must be numbers")
                return
    print("product not found")
#7.funcion para eliminar un producto
def delete_product():
    #elimina un producto por nombre
    print("\n---delete product---")
    name = input("Enter the product name: ").lower()

    for i,p in enumerate (inventory):
        if p["name"].lower() == name:
            inventory.pop(i)
            #elimina el producto de la lista
            print("product deleted successfully!")
            return
    print("product not found")
#8.funcion para calcular el valor total del inventario
def calculate_total_value():
    #calcula el valor total del inventario
    print("\n---calculate total value---")
    if not inventory:
        print("no products in the inventory")
        return
    total_value = 0
    for p in inventory:
        total_value += p["price"] * p["quantity"]

    print(f"total value of the inventory: ${total_value:.2f}")
#9.funcion principal
#se crea un menu para el usuario
def main():
    print("welcome to the inventory management system")
    #menu principal
    while True:
        show_menu()
        option = input("choose an option (1-7): ")

        if option == "1":
            add_product()
        elif option == "2":
            show_products()
        elif option == "3":
            search_product()
        elif option == "4":
            update_product()
        elif option == "5":
            delete_product()
        elif option == "6":
            calculate_total_value()
        elif option == "7":
            print("goodbye!")
            break
        else:
            print("invalid option")
#10.ejecucion del programa
if __name__ == "__main__":
    main()
#esta linea asegura que el programa solose ejecute cuando se llama directamente(no al importarlo como modulo)    
    