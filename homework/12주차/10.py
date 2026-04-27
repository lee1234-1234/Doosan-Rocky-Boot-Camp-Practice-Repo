
account_list = []

with open("./pizza_file1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    
    for line in lines:
        pizza, price = line.strip().split()
        account_list.append(pizza)
    
print(account_list)