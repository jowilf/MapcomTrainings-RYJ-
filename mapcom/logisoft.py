filename = 'logisoft.in'
with open(filename, 'r') as f:
    end = False
    while(not end):
        values = f.readline().strip().split(" ")
        if all([v == "0000" for v in values]):
            end = True
        else:
            card_number = "".join(values)
            even = card_number[0::2]
            odd = card_number[1::2]
            odd = list(map(int,odd))
            even = [2*int(val) for val in list(even)]
            even = [val - 9 if val>9 else val for val in even]
            result = sum(odd)+sum(even)
            response = "No"
            if result%10==0:
                response = "Yes"
            print(response)
            