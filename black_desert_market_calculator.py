sale_price = int(input(print("Sale price:")))
quantity = int(input(print("Quantity:")))

profit = sale_price * quantity

profit_no_value_pack = profit * 0.65
print("profit without value pack: {}".format(profit_no_value_pack))

profit_value_pack = profit_no_value_pack + profit_no_value_pack * 0.3
print("profit with value pack: {}".format (profit_value_pack))

difference = profit_value_pack - profit_no_value_pack
print("Value Pack Profit: {}".format(difference))