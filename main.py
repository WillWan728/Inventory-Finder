#   ========The beginning of the class==========

class Shoe:

    # initialising attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):  # prints out objects as string
        return f"{self.country},{self.code},{self.product}, {self.cost}, {self.quantity}"

    def __repr__(self):     # represents values in data structure
        return f"{self.country},{self.code},{self.product}, {self.cost}, {self.quantity}"

    def total_cost(self):
        print(self.cost)
        return int(self.cost) * int(self.quantity)

    def get_product(self):
        return self.product

    def get_code(self):
        return self.code

#   =============Shoe list===========

# The list will be used to store a list of objects of shoes.


shoe_list = []

#   ==========Functions outside the class==============


def read_shoes_data():
    """
    Opens inventory.txt file and appends data into list.
    """
    try:
        file_var = open("inventory.txt", "r")
        shoes = file_var.readlines()[1:]  # read lines in text file other than first line. Slicing through txt

    # Loops through the txt file and append into shoe list.
        for line_text in shoes:
            new_shoes = line_text.strip().split(",")
            shoe_list.append(Shoe(new_shoes[0], new_shoes[1], new_shoes[2], new_shoes[3], new_shoes[4]))

    except FileNotFoundError:
        print("File inventory.txt not available")
    return shoe_list


def capture_shoes():
    """
    Function to capture new shoe information
    Append into list and also inventory.txt
    """

    # User inputs information regarding new shoe.
    country = input("Please enter the new shoes country location e.g Canada:")
    code = input("Please enter the shoes code:")
    shoe = input("Please enter the products name:")
    cost = input("Please enter the cost:")
    quantity = input("Quantity of new shoe:")

    # Append new data into shoe_list
    shoe_list.append(Shoe(country, code, shoe, cost, quantity))
    print("New shoe has been added! Thank you")

    # write to txt file.
    write_file = open("inventory.txt", "a")
    write_file.write(f"\n{country},{code},{shoe},{cost},{quantity}")
    write_file.close()


def view_all():
    #   View all shoes in inventory
    all_list = read_shoes_data()
    [print(f"{sneakers}\n") for sneakers in all_list]


def re_stock():
    """
    Function to find the lowest quantity shoe
    Ask user the quantity they want to restock.
    """
    min_value = shoe_list[0].quantity
    position = 0

    # looping through shoe list, finding the lowest quantity
    for i, shoe in enumerate(shoe_list):
        if shoe.quantity < min_value:
            min_value = shoe.quantity
            lowest_shoe = shoe
            position = i

    # Ask user quantity they would like to add
    restock = int(input("Please enter the quantity you would like to add:"))
    total = restock + min_value
    lowest_shoe.quantity = total
    print(shoe_list[position])

    # Writing shoe_list back to inventory.txt
    stock = open("inventory.txt", "w")
    stock.write("Country,Code,Product,Cost,Quantity")
    for shoe in shoe_list:
        stock.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")


def search_shoe():
    """
        This function will search for a shoe from the list
        using the shoe code and return this object so that it will be printed.g
    """
    search_input = input("Please enter the code for the shoe.").strip()
    for shoe in shoe_list:
        if shoe.code == search_input:
            search_shoe = shoe
    print(search_shoe)


def value_per_item():
    #   This function will calculate the total value for each item.
    for shoe in shoe_list:
        value = shoe.quantity * shoe.cost
        print(f" {shoe.product}:{value}")


def highest_qty():
    #   Prints the highest quantity shoe
    max_value = shoe_list[0].quantity
    position = 0
    for i, shoe in enumerate(shoe_list):
        if shoe.quantity > max_value:
            max_value = shoe.quantity
            position = i
    print(f"{shoe_list[position]}\nThis shoe should be brought out for sale.")


#   ==========Main Menu============="""
read_shoes_data()
while True:
    menu = input(""" Select on of the following options below:
    c  - Capture new shoes
    va - View all shoes
    rs - Restock lowest quantity shoe 
    ss - Search shoe
    vi - Value per item
    hi - highest quantity stock
    ex - exit 
    :""").lower()

    # Capture new shoes
    if menu == "c":
        capture_shoes()

    # View all shoes
    elif menu == "va":
        view_all()

    # Restock the lowest quantity shoe
    elif menu == "rs":
        re_stock()

    # Search shoe
    elif menu == "ss":
        search_shoe()

    # Value per item
    elif menu == "vi":
        value_per_item()

    # Highest quantity
    elif menu == "hi":
        highest_qty()

    # Exit program
    elif menu == "ex":
        print("Exiting program. Thank you.")
        exit()

    else:
        print("You have made a wrong choice, please try again.")
