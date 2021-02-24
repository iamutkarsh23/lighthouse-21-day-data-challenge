item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]

buy_wholesale_list = []
for i in range(0, 4):
    if(retail_price[i] * amount_list[i] > wholesale_price_list[i]):
        buy_wholesale_list.append("Yes")
    else: 
        buy_wholesale_list.append("No")
print(buy_wholesale_list)

# Answer - ['Yes', 'Yes', 'No', 'No']