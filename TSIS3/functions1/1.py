def conversion(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("Enter in grams: "))
print(grams,"grams in ounces is",conversion(grams))