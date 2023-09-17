#################################################
# purchases.py
# Due Date: 9/22/2023
# name: Sichao(Tommy) Bi
# https://bostoncollege.instructure.com/courses/1647097/assignments/7293403
##################################################

# returns a new list with that sales tax applied to each value in the list.
def add_tax(costs, tax):
    for i in range(len(costs)):
        costs[i] *= (1 + tax)

    return costs


# Get user inputs
purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

customers = []
costs_pre_tax = []

for i in range(purchases):
    customers.append(input("Customer: "))
    costs_pre_tax.append(float(input("Cost: ")))

final_cost = add_tax(costs_pre_tax, sales_tax)

# Dictionary with {Customer, Sales after tax} pairs
res = {}

for i in range(len(final_cost)):
    if customers[i] in res:
        res[customers[i]] += final_cost[i]
    else:
        res[customers[i]] = final_cost[i]

print(res)
