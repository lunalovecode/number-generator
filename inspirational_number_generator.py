import random
num_nums, max_range = [int(x) for x in input("What type of lotto is it? (For example, 6/45) ").split("/")]
num_sets = int(input("How many sets do you want to fill in? "))
quotes = ["With great power comes great responsibility. - Uncle Ben, Spiderman",
          "Dollar, dollars, dropping on my a$$ tonight! - Lisa Manoban",
          "Money is the opposite of the weather. Nobody talks about it, but everybody does something about it. - Rebecca Johnson",
          "The trick is to stop thinking of it as 'your' money. - an IRS auditor",
          "Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like. - Will Smith",
          "Money's only something you need in case you don't die tomorrow. - Carl Fox (played by Martin Sheen), Wall Street",
          "It's amazing how fast later comes when you buy now! - Milton Berle",
          "You can be young without money but you can't be old without it. - Tennessee Williams",
          "Money is like manure; it's not worth a thing unless it's spread around. - Brooke Astor",
          "Don't stay in bed, unless you can make money in bed. - George Burns"]
for i in range(num_sets):
    cur_set = []
    j = 0
    while len(cur_set) < num_nums:
        num = random.randint(1, max_range)
        if num not in cur_set:
            cur_set.append(num)
    cur_set.sort()
    print(f"Set {i + 1}: {cur_set}")
    print(quotes[sum(cur_set) % 10])