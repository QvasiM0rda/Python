name = input()
amount = float(input())
price = float(input())
summary = amount * price

print("| %-30s | %-6d | %-10.2f | %12.2f |" % (name, amount, price, summary))
