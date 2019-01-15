print('meat yield version 0.1.1')
print('\tby Andrew M McCall')


# gather some initial information about the cut - as purchased - edible product
cost = input("What is the sub primal at cost? $")
cost = float(cost)
bagged = input("what is the bagged weight of the sub primal? ")
bagged = float(bagged)
naked = input("what is the naked weight of the sub primal? ")
naked = float(naked)

#establish the true cost - bag weight and purge
naked_cost = (cost) / (naked/bagged)
naked_cost = str(naked_cost)

print("\nThe naked cost is: " + "\n\t" + naked_cost)

#enter the main cuts here

meat_dict = {}
# set a flag to indicate cuts are being added

add_active = True

while add_active:
    cut = input("\nname of cut? ")
    weight = input("\nweight of cut? ")
    weight = float(weight)
    retail_value = input("\nWhat is the retail amount?")
    retail_value = float(retail_value)
    #store the responses in meat_dict
    meat_dict_values = []
    meat_dict_values.append(weight)
    meat_dict_values.append(retail_value)
    meat_dict[cut] = meat_dict_values

    repeat = input("Would you like to add another cut? (yes/no)")
    if repeat == 'no':
        add_active = False

print("\n --- Here are the results ---")

for cut, weight in meat_dict.items():
    print(cut.title() + " " + str(weight))


#display the percentage yield
print("\n\tThe percent of each cut is: ")
for cut, meat_dict_values in meat_dict.items():
    percent = meat_dict_values[0] / (naked)
    print(cut.title() + " " + str(percent))
#display the true cost of each cut
print("\n\tThe cost of each cut is: ")
for cut, meat_dict_values in meat_dict.items():
    cut_cost = meat_dict_values[0] * float(naked_cost)
    print(cut.title() + " " + "$" + str(cut_cost))

#display the retail dollar amount of each cuts
print("\n\tThe retail dollar amount of each cut is: ")
for cut, meat_dict_values in meat_dict.items():
    retail_dollar_amount = ((meat_dict_values[0]) * (meat_dict_values[1]))
    print(cut.title() + " " + "$" + str(retail_dollar_amount))

#display margin of cut
print("\n\tThe margin of the cuts in an ideal environment are: ")
for cut, meat_dict_values in meat_dict.items():
    cut_cost = meat_dict_values[0] * float(naked_cost)
    retail_dollar_amount = meat_dict_values[0] * meat_dict_values[1]
    profit = float(retail_dollar_amount) - float(cut_cost)
    margin = profit / retail_dollar_amount
    print(str(margin) + " %")

# #display waste product
# print("\n\tThe amount of waste generated from the yield is: ")
# for cut, meat_dict_values in meat_dict.items():
#     weight_sum = naked - sum(meat_dict_values.pop(0))
#     print(str(weight_sum))
