
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):   
       self.country = country
       self.code = code
       self.product = product
       self.cost = cost
       self.quantity = quantity
            
    def get_cost(self):
        return(self.cost)
        
    def get_quantity(self):
        return(self.quantity)
    
    def __str__(self):
        return(f"\n{self.country}  {self.code}  {self.product}  {self.cost}  {self.quantity}")
        

#The list will be used to store a list of objects of shoes.
shoe_list = []

# This function will open the file inventory.txt and read the data from this file, then create a
# shoes object with this data and append this object into the shoes list.
def read_shoes_data():
    file = None
    try:    
        file = open("inventory.txt", "r")
        data_shoe_object = file.readlines()
        file.close()
    except FileNotFoundError:
        print("\nThe file that you are trying to open does not exist\n")
    finally:
        if file is not None:
            file.close()
    for shoe in data_shoe_object:
        shoe = shoe.strip("\n").split(",")
        shoe_object = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])
        shoe_list.append(shoe_object)       
    shoe_list.pop(0)
    
# capture_shoes - This function will allow a user to capture data about a shoe and 
#use this data to create a shoe object and append this object inside the shoe list.  
def capture_shoes():
    country = input("enter the country of the shoe: ")
    code = input("enter the code of the shoe: ")
    product = input("enter the product name of the shoe: ")
    while True:
        try:
            cost = float(input("enter the cost of the shoe: "))
            break
        except ValueError:
            print("Oops! That was not a valid cost. Try again...")
    while True:
        try:
            quantity = int(input("enter the quantity of the shoe: "))
            break
        except ValueError:
            print("Oops! That was not a valid quantity. Try again...")
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    file_inventory = open("inventory.txt", "w+")
    file_inventory.write("Country,Code,Product,Cost,Quantity")
    for count in range(len(shoe_list)):
        file_inventory.write(f"\n{shoe_list[count].country},{shoe_list[count].code},{shoe_list[count].product},{shoe_list[count].cost},{shoe_list[count].quantity}")
    file_inventory.close()
    print(f'\x1b[1;34;47m Shoe has been added to the list \x1b[0m')

#view_all- This function will iterate over the shoes list and print the details of the shoes returned from the __str__function.
def view_all():
    print('\x1b[1;34;47m')
    print("Country   " + "Code    " + "Product " + "Cost  " + "Quantity")   
    for count in range(len(shoe_list)):   
       print(shoe_list[count].__str__())
    print('\x1b[0m')

# This function will find the shoe object with the lowest quantity, which are the shoes that need to be re-stocked.
# Asks the user if they want to add this quantity of shoes and then update it. This quantity is  updated on the file for this shoe.  
def re_stock():
    shoe_quantity_list = []
    for count in range(len(shoe_list)):
        shoe_quantity_list.append(int(shoe_list[count].quantity))
    lowest_quantity = min(shoe_quantity_list)
    index_lowest_quantity = shoe_quantity_list.index(lowest_quantity)
    # shoe_list[index_lowest_quantity].__str__()
    print('\x1b[1;34;47m')
    print(f"Country:  {shoe_list[index_lowest_quantity].country}")
    print(f"Code:     {shoe_list[index_lowest_quantity].code}")
    print(f"Product:  {shoe_list[index_lowest_quantity].product}")
    print(f"Cost:     {shoe_list[index_lowest_quantity].cost}")
    print(f"Quantity: {shoe_list[index_lowest_quantity].quantity}")
    print('\x1b[0m')
    print(f"The shoe with above details needs to be restocked. ")
    restock_option = input("If you wish to restock this shoe enter 'y' for yes or 'n' for no: ").lower()
    if  restock_option == 'y':
        while True:
            try:
                restock_quantity = int(input("enter the quantity you want to add to the stock"))
                break
            except ValueError:
                print("Oops! That was not a valid quantity. Try again...")        
        new_quantity = int(shoe_list[index_lowest_quantity].quantity) + restock_quantity
        shoe_list[index_lowest_quantity].quantity = new_quantity
        file_inventory = open("inventory.txt", "w+")
        file_inventory.write("Country,Code,Product,Cost,Quantity")
        for count in range(len(shoe_list)):
            file_inventory.write(f"\n{shoe_list[count].country},{shoe_list[count].code},{shoe_list[count].product},{shoe_list[count].cost},{shoe_list[count].quantity}")
        file_inventory.close()
        print(f'\x1b[1;34;47m Quantity has been addded x1b[0m')

#search_shoe - This function will search for a shoe from the list using the shoe code and 
# return this object so that it will be printed.
def search_shoe():
    required_shoe_code = input("enter the code of the shoe you want to search: ")
    search_result = 0
    print('\x1b[1;34;47m')       
    for count in range(len(shoe_list)):
        if shoe_list[count].code == required_shoe_code:
            print("Below is the details of the shoe you are searching:")
            print(f"Country:  {shoe_list[count].country}")
            print(f"Code:     {shoe_list[count].code}")
            print(f"Product:  {shoe_list[count].product}")
            print(f"Cost:     {shoe_list[count].cost}")
            print(f"Quantity: {shoe_list[count].quantity}")
            search_result += 1 
    if search_result == 0:
        print("\nShoe with this code is not in the stock")
    print('\x1b[0m')


# value_per_item - This function will calculate the total value for each item . 
# Prints this information on the console for all the shoes.  
def value_per_item():
    for count in range(len(shoe_list)):
        cost_per_shoe = float(shoe_list[count].cost)
        quantity_shoe = int(shoe_list[count].quantity)
        value = cost_per_shoe * quantity_shoe
        print('\x1b[1;34;47m')
        print(f"Total Value of Shoe Code No.:{shoe_list[count].code} Name: {shoe_list[count].product} = {value}")
    print('\x1b[0m')

#highest_qty - This function determines the product with the highest quantity and print this shoe as being for sale.     
def highest_qty():
    print('\x1b[1;34;47m')
    shoe_quantity_list = []
    for count in range(len(shoe_list)):
        shoe_quantity_list.append(int(shoe_list[count].quantity))
    highest_quantity = max(shoe_quantity_list)
    index_highest_quantity = shoe_quantity_list.index(highest_quantity)
    print(f"\nShoe {shoe_list[index_highest_quantity].product} is for sale.")
    print('\x1b[0m')

#Calling function read_shoe_data 
read_shoes_data() 

#Presenting menu to the user#######################

usage_message = '''
Welcome to the Nike Warehouse stock overview. Please enter the letter for the desired task."

c - capture_shoes(to add new shoe in the stock)
v - view all the shoe in the stock
r - restock the shoe with the lowest quantity
s - search a shoe 
tv - to view the total value of each type of shoe
h - to view the shoe with the highest quantity and put it for sale
e - exit this program.
: '''
while True:
    print('\x1b[1;37;44m')      # prints menu on a white background in blue font.
    user_choice = input(usage_message).strip().lower()
    print('\x1b[0m')
    if user_choice == "c":
        capture_shoes()
     
       
    elif user_choice == "v":
        view_all()
        
            
    elif user_choice == "r":
        re_stock()
        
               
    elif user_choice == "s":
        search_shoe()
        

    elif user_choice == "tv":
        value_per_item()
      
      
    elif user_choice == "h":
        highest_qty()
        

    elif user_choice == "e":
        print("Goodbye")
        break

    else:
        print("Oops - incorrect input")
    

