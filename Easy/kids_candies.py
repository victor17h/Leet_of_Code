candies = [2,3,5,1,3]
extraCandies = 3


def sweetest(candies, extraCandies):
    maxi = max(candies)
    for i in range(len(candies)):
        candies[i] = True if (candies[i]+extraCandies >= maxi) else False
    return candies


print(sweetest(candies,extraCandies))