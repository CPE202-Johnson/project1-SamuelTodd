# int -> boolean
# returns a boolean value representing the possibility of winning the game with n bears
def bears(n):
    # base case 1
    if n == 42:
        return True
    
    # base case 2
    if n < 42:
        return False
    
    # even
    if n%2 == 0:
        give = n/2
        if bears(n - give) == True:
            return True

    # divisible by 3 or 4
    if (n%3 == 0) or (n%4 == 0):
        lastd = n%10
        secondlastd = (n%100)/10
        give = lastd * secondlastd
        if give > 0:
            if bears(n - give) == True:
                return True
    
    # divisible by 5
    if n%5 == 0:
        give = 42
        if bears(n - give) == True:
            return True

    # not possible
    return False
