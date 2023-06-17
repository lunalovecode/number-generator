import random
max_sets, max_range = [int(x) for x in input("What type of lotto is it? (For example, 6/45) ").split("/")]
num_sets = int(input("How many sets do you want to fill in? "))
if num_sets > max_sets:
    print("You can't have that many sets!")
else:
    for i in range(num_sets):
        print(f"Set {i + 1}:")
        cur_set = []
        j = 0
        while len(cur_set) < 6:
            num = random.randint(1, max_range)
            if num not in cur_set:
                cur_set.append(num)
        cur_set.sort()
        print(cur_set)