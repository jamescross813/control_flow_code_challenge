# Write your twice_as_large function here:
def twice_as_large(a,b):
    result = b*2
    if(a>result):
        return True
    else:
        return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True