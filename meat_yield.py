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
    #store the responses in meat_dict
    meat_dict[cut] = weight

    repeat = input("Would you like to add another cut? (yes/no)")
    if repeat == 'no':
        add_active = False

print("\n --- Here are the results ---")

for cut, weight in meat_dict.items():
    print(cut.title() + " " + str(weight))


#display the percentage yield
print("\n\tThe percent of each cut is: ")
for cut, weight in meat_dict.items():
    percent = float(weight) / float(naked)
    print(percent)
#display the true cost of each cut
print("\n\tThe cost of each cut is: ")
for cut, weight in meat_dict.items():
    cut_cost = float(weight) * float(naked_cost)
    print(cut.title() + " " + str(cut_cost))
