def Calculate_cost(Maintainace_cost,Wear_Tear_cost,Include_maintainance):
    if Include_maintainance:
        return(sum([Maintainace_cost,Wear_Tear_cost]))
    else: 
        return(Wear_Tear_cost)
