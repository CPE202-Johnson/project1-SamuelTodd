# string -> list
# returns a list of permutations of the strings in lexiographic order
def perm_gen_lex(a): 
    # base case
    if len(a) == 0:
        return []

    # base case 2
    if len(a) == 1:
        return [a]

    # create list
    permutations = []

    # for each character in the input string
    for c in a:
        # forming simpler string by removing the character
        char = c
        simp = a.replace(c,'')

        # generating permutations of the simpler string recursively
        perms = perm_gen_lex(simp)

        # adding the removed character to the permutation and adding it to the list
        for p in perms:
            permutations.append(char + p) 

    return permutations
