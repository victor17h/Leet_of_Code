candies = [2,3,5,1,3]
extraCandies = 3

def kids(candies, extraCandies):
    max_candies = max(candies)
    for i in range(len(candies)):
        candies[i] = candies[i] + extraCandies >= max_candies
    return candies


print(kids(candies,extraCandies))

