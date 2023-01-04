class Monkey:
    
    def __init__(self, monkeys_dict, monkey_num, starting_items, inspect_operation, inspect_value, test_value, true_monkey, false_monkey):
        self.monkeys_dict = monkeys_dict
        self.monkey_num = monkey_num
        self.items = starting_items
        self.inspection_count = 0
        self.inspect_operation = inspect_operation
        self.inspect_value = inspect_value
        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        
    def __repr__(self):
        return f"""
    Monkey {self.monkey_num}:
        Inspection_count = {self.inspection_count}
        Items: {self.items}
        Operation: new = old {self.inspect_operation} {self.inspect_value}
        Test: divisible by {self.test_value}
            If true: throw to monkey {self.true_monkey}
            If false: throw to monkey {self.false_monkey}"""
        
    def __lt__(self, monkey):
        return self.inspection_count < monkey.inspection_count
        
    def inspect_items(self, worry_reduction_factor = 1):
        
        # "modulo trick" where 9699690 is the product (and LCM) of all the monkeys' test_values
        # keep the numbers small by keeping the worry level modulo of that value over all iterations
        # tbh -- i still don't fully understand this. 😢
        self.items = list(map(lambda x: x % 9699690, self.items))
        
        for i in range(0, len(self.items)):
            
            item = self.items.pop(0)
            self.inspection_count += 1
            
            match self.inspect_operation:
                case "*":
                    if isinstance(self.inspect_value, int):
                        item = item * self.inspect_value
                    else:
                        item = item * item
                case "+":
                    if isinstance(self.inspect_value, int):
                        item = item + self.inspect_value
                    else:
                        item = item + item
                        
            item = item // worry_reduction_factor
            
            if item % self.test_value == 0:
                throw_item(self.monkeys_dict, self.true_monkey, item)
            else:
                throw_item(self.monkeys_dict, self.false_monkey, item)
    
    # not necessary, but while trying to figure out my inefficiencies, I simplified the function above using lambdas            
    def inspect_items_efficient(self):
        self.inspection_count += len(self.items)
        
        self.items = list(map(lambda x: x % 9699690, self.items))
        
        if isinstance(self.inspect_value, int):
            if self.inspect_operation == "*":
                self.items = list(map(lambda x: x * self.inspect_value, self.items))
            else:
                self.items = list(map(lambda x: x + self.inspect_value, self.items))
        else:
            self.items = list(map(lambda x: x * x, self.items))
            
        [throw_item(self.monkeys_dict, self.true_monkey, x) if x % self.test_value == 0 else throw_item(self.monkeys_dict, self.false_monkey, x) for x in self.items]
        
        self.items = []

    
def throw_item(monkeys_dict, monkey_value, item):
    monkeys_dict[monkey_value].items.append(item)

monkeys = {}

# Part 1 (modified from original by adding worry factor arguement)

monkeys[0] = Monkey(monkeys, 0, [83,88,96,79,86,88,70], "*", 5, 11, 2, 3)
monkeys[1] = Monkey(monkeys, 1, [59,63,98,85,68,72], "*", 11, 5, 4, 0)
monkeys[2] = Monkey(monkeys, 2, [90,79,97,52,90,94,71,70], "+", 2, 19, 5, 6)
monkeys[3] = Monkey(monkeys, 3, [97, 55, 62], "+", 5, 13, 2, 6)
monkeys[4] = Monkey(monkeys, 4, [74, 54, 94, 76], "*", "old", 7, 0, 3)
monkeys[5] = Monkey(monkeys, 5, [58], "+", 4, 17, 7, 1)
monkeys[6] = Monkey(monkeys, 6, [66, 63], "+", 6, 2, 7, 5)
monkeys[7] = Monkey(monkeys, 7, [56, 56, 90, 96, 68], "+", 7, 3, 4, 1)

for i in range (0, 20):
    for monkey in monkeys:
        monkeys[monkey].inspect_items(3)
        
two_most_active_monkeys = sorted(monkeys.values(), reverse = True)[:2]

monkey_business_part_1 = two_most_active_monkeys[0].inspection_count * two_most_active_monkeys[1].inspection_count

# Part 2

# reset monkeys
monkeys[0] = Monkey(monkeys, 0, [83,88,96,79,86,88,70], "*", 5, 11, 2, 3)
monkeys[1] = Monkey(monkeys, 1, [59,63,98,85,68,72], "*", 11, 5, 4, 0)
monkeys[2] = Monkey(monkeys, 2, [90,79,97,52,90,94,71,70], "+", 2, 19, 5, 6)
monkeys[3] = Monkey(monkeys, 3, [97, 55, 62], "+", 5, 13, 2, 6)
monkeys[4] = Monkey(monkeys, 4, [74, 54, 94, 76], "*", "old", 7, 0, 3)
monkeys[5] = Monkey(monkeys, 5, [58], "+", 4, 17, 7, 1)
monkeys[6] = Monkey(monkeys, 6, [66, 63], "+", 6, 2, 7, 5)
monkeys[7] = Monkey(monkeys, 7, [56, 56, 90, 96, 68], "+", 7, 3, 4, 1)

for i in range (0, 10000):
    for monkey in monkeys:
        monkeys[monkey].inspect_items()
        
two_most_active_monkeys = sorted(monkeys.values(), reverse = True)[:2]

monkey_business_part_2 = two_most_active_monkeys[0].inspection_count * two_most_active_monkeys[1].inspection_count

print(monkey_business_part_1)
print(monkey_business_part_2)