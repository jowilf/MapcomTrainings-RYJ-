"""
@author: yannick - RYJ
"""
filename = 'mobile.in'
facturations = [{"call_per_mn": 30, "data_per_mb": 40},
                {"call_per_mn": 35, "data_per_mb": 30},
                {"call_per_mn": 40, "data_per_mb": 20}]
with open(filename, 'r') as f:
    end = False
    while(not end):
        call_in_mn, data_in_mb = map(int,f.readline().strip().split(" "))
        if(call_in_mn==0 and data_in_mb==0):
            end = True
        else:
            min_facturation = min([f["call_per_mn"]*call_in_mn+f["data_per_mb"]*data_in_mb for f in facturations])
            print(min_facturation)
        