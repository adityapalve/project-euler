'''
Problem 31:
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can £2 be made using any number of coins?
'''
def count_ways_to_make_200():
    # Coin denominations in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    # Target amount in pence
    target = 200

    # Initialize an array to store the number of ways to make each amount
    ways = [0] * (target + 1)
    ways[0] = 1  # There's one way to make 0p — using no coins

    # Loop through each coin and update the ways to make each amount
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    
    print(ways)
    return ways[target]

# Call the function and print the result
result = count_ways_to_make_200()
print(f"Number of ways to make £2: {result}")
