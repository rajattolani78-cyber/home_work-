import re 
group_str = "my name is rajat"
pat = r"[a-z]{3}"#match only look at the starting chracter only 
print(re.match(pat,group_str))

phone = "croral: 0987654321, nagaarjun: 0983123234,"
pat_1 = r"[0-9]{10}""""now findall built in module in re fxn find all the number repeted in 0-9 in the string 
but search can't do that"""
print(re.findall(pat_1,phone))
# other uses of findall fxn 
phone = "croral: 0987654321, nagaarjun: 0983123234,anshu: 234312312312312312"
pat_2 = r"[0-9]{10,15}"# now it will print all the numbers who's value is min = 10  and max = 15 values
print(re.findall(pat_2,phone))




