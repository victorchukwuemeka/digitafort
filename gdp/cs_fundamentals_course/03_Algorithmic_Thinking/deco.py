## food ingredent
##  washing the vegetables 
## chooping the vegs 
##  stir- frying 



def get_in():
    ##getting what the  list of the materials needed 
    ing = ["tufu","p","o", "ge","s"]
    return ing 

def washing(ing):
    ## water and salt 
    print(" washing with water and salt ")
    washed_ing = ing.append("washed")  
    return washed_ing


def  chopping_v(ing):
     chopping = {
        "pro" : ['tofu'],
        "veg" : ['sliced p','diced o','ge']
         }
     return chopping 

def stir_fry(ing):
    return "stir-fry "




ing  = get_in()


print(washing(ing))
