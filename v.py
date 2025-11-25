import re 
group_str = "my name is rajat"
pat = r"[a-z]{3}"#match only look at the starting chracter only 
print(re.match(pat,group_str))

phone = "croral: 0987654321, nagaarjun: 0983123234,"
pat_1 = r"[0-9]{10}""""now findall built in module in re fxn find all the number repeted in 0-9 in the string 
but search can't do that"""
print(re.findall(pat_1,phone))
# other uses of findall fxn a



