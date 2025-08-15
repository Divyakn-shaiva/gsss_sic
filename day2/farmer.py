farmer_owns = 80
segments = 5
acres = farmer_owns / segments
tomato_yield = (0.3 * 16 * 10) + (0.7 * 16 * 12)
tomato_price = tomato_yield * 7 * 1000
potato_yield = 10 * 16
potato_price = (potato_yield) * 20 * 1000
cabbage_yield = 14 * 16
cabbage_price=(cabbage_yield) * 24 * 1000
sunflower_yield = 0.7*16
sunflower_price = (sunflower_yield) * 200 * 1000
total_yield = tomato_yield + potato_yield + cabbage_yield + sunflower_yield
total_price=tomato_price+potato_price+cabbage_price+sunflower_price
print("Total yield : ",total_yield)
print("Total Sales achived by Mahesh from the 80 acres of Land :",total_price)






























