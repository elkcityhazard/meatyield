#These are the prompts for meat yield program

sub_primal_prompt = input("\nWhat is the sub primal you are testing? ")
sub_primal_cost_prompt = input("\nWhat is the sub primal cost in USD? ")
bagged_weight_prompt = input("\nWhat is the bagged weight of the sub primal? ")
naked_weight_prompt = input("\nWhat is the naked weight of the sub primal?")

yield_values = {}

# Set a flag to indicate active testing

yield_active = True

while yield_active:
    # prompt for information
    name = input(sub_primal_prompt)
    cost = float(input(sub_primal_cost_prompt))
    bagged = float(input(bagged_weight_prompt))
    naked = float(input(naked_weight_prompt))
    true_cost = cost / (bagged/naked)

    yield_values[name] = true_cost

    repeat = input("Would you like to add another cut (yes/no)?")
    if repeat == 'no':
        yield_test = False

# Yield Test Done. Show Results

print("\n--- Yield Test Results ---")
for name, yield_value in yield_values.items():
    print(name + "'s true cost is: " + yield_value + ".")
