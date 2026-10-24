def total_calc(total_cost,tip_percent):
    total=total_cost*(1+0.01*tip_percent)
    new_total=round(total,2)
    print("your total with tip is",new_total)

total_calc(150,20)