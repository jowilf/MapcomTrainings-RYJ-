filename = 'sticker.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        stick = f.readline().strip()
        precedent_letter, comp, result= None, 0, 1
        for letter in stick:
            if precedent_letter is None:
                if letter == "?":
                    continue
                else:
                    precedent_letter = letter
            else:
                if letter == "?":
                    comp+=1
                else:
                    if comp==0:
                        precedent_letter = letter
                    else:
                        if letter != precedent_letter:
                            result*=(1+comp)
                            precedent_letter = letter
                        comp = 0
        print(result%1000000007)