#https://fellowship.hackbrightacademy.com/materials/serft15/homework/underpaid-customers/
"""
Homework Task:
How can you create a function to tell us if a customer
underpaid or overpaid for their delivery. It's currently set up with an
if-statement for each customer... and as the amount of customers grow,
it needs to be made more efficient! 

Example output should say something like: Sean paid $9.50, expected $9.00.
"""

melon_cost = 1.00

def what_custumer_paid_vs_expected(filename):

    data = open(filename)

    for line in data:
        #This was my initial thinking for how to assign data to the variables,
        #...but it can be written more efficiently like the code below! 
        individual_customer_data = line.split("|")
        customer_name = individual_customer_data[1]
        first_name = customer_name.split(" ")[0]
        melon_quantity = float(individual_customer_data[2])
        amount_paid = float(individual_customer_data[3])

        # _, customer_name, melon_quantity, amount_paid = line.rstrip().split("|")

        customer_expected_price = melon_quantity * melon_cost
        print(f"{first_name} paid ${amount_paid:.2f},",
        f"expected ${customer_expected_price:.2f}")


print(what_custumer_paid_vs_expected("customer-orders.txt"))

##"Original code that needs updated to be more effificent!"
melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )
