

def update_inventory(inventoryDict, inventoryUpdate = []):  # Figure out the parameters and add to the function signature
    # inventoryDict format: {nameOfProduct : [[list of product Information],[stock information]]}

    for row in inventoryUpdate:
        # For each list containing everything to update on a product

        # Define everything in the row and create shallow copies of the lists to make things easier
        productName = row[0]
        descriptionsList = row[1]
        restockAndLocationList = row[2]

        if productName in inventoryDict.keys(): # If product exists already in our Dictionary

            # Create shallow copies of list values correspondent to the product name in the dictionary
            dictDescriptionsList = inventoryDict[productName][0]
            dictStockAndLocationList = inventoryDict[productName][1]
        
            if str(dictDescriptionsList[-1]) != dictDescriptionsList[-1]:
                # Check if weight exists in original dictionary and if it does make sure to remove and add it
                # back in after appending descriptions we want to add
                weight = dictDescriptionsList.pop(-1)
                for description in descriptionsList:
                    if description != '':
                        dictDescriptionsList.append(description)
                dictDescriptionsList.append(weight)

            else:
                for description in descriptionsList:
                    if description != '':
                        dictDescriptionsList.append(description)

            # Add what we're restocking to original stock
            dictStockAndLocationList[0] += restockAndLocationList[0]

            if restockAndLocationList[1] > " ": # if it's whitespace then we don't add it to Aisles (no way I actually made use of ASCII comparison values haha)
                dictStockAndLocationList[1] += " " + restockAndLocationList[1]

        # If product isn't in the existing stock
        else:
            inventoryDict[row[0]]=[row[1],row[2]]

    return inventoryDict
# Test Case:
"""
inventory = {
    'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']], 
    'Milk':[['dairy','sugar-free', 1.0], [2500, '11A']],
    'Bread': [['bakery','organic','whole wheat',0.5], [ 120, '21C']], 
    'Ice cream': [['dairy', 0.75],[3120, '9D']], 
    'salmon': [['frozen foods', 'wild cut', 3.0], [456, '6E']]
    }

restock = [
    ['Apple',['sweet'], [100,'']], 
    ['Bread',['gluten-free'], [520,'21D']],
    ['Chicken', ['butchery', 'farm-raised', 4.5], [974, '50A']]
    ]
    
print(update_inventory (inventory, restock))

"""
def merge_inventory (inventoryTuple, new_inventory = {}):  # Figure out the parameters and add to the function signature
    
    inventoryDict = {}  # initialize dictionary we will return after appending the stuff in inventoryTuple

    for list2D in inventoryTuple:
        productName = list2D[0]
        productDescriptions = list2D[1]
        productNumAndLocation = list2D[2]
        
        inventoryDict[productName] = [productDescriptions, productNumAndLocation]
    
    new_inventory = new_inventory.items()
    newInventoryList = []

    for tuple in new_inventory:
        productName = tuple[0]
        productDescriptions = tuple[1][0]
        productNumAndLocation = tuple[1][1]
        newInventoryList.append([productName, productDescriptions, productNumAndLocation])

    return update_inventory(inventoryDict, newInventoryList)
"""
inventory =(['Potato',['sweet', 9.0], [230,'26D']], 
            ['Bread',['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
            ['Shrimp', ['frozen foods','large', 3.0], [75, '51A']], 
            ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']],
            ['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']])

new_inventory = {'Apple':[['sweet'], [100,'']], 
                 'Bread': [['gluten-free'], [520,'21D']], 
                 'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]}
                 """
#Test:
#print(merge_inventory(inventory, new_inventory))
#for tuple in list(new_inventory.items()):

#print(new_inventory.items())


def products_info (products, products_detail, new_products_detail = ()):  # Figure out the parameters and add to the function signature
    inventory = []
    newInventory = {}
    
    for i in range(len(products)):
        # Loop based on how many products will be entered into the inventory & newInventory

        # Add product details to inventory list
        if products_detail[i][0] != [] and products_detail[i][1] != []:

            inventory.append([products[i], products_detail[i][0], products_detail[i][1]])

        if new_products_detail != ():
            if new_products_detail[i] != []:
                newInventory[products[i]] = new_products_detail[i]
    return merge_inventory(tuple(inventory), newInventory)
        



# TEST:
"""
products = ('Apple', 'Milk', 'Bread', 'Salmon')
products_detail =([['fruits', 'non-GMO', 5.0], [1540, '37B']], [['dairy','sugar-free', 1.0], [2500, '11A']], [['bakery','organic','whole wheat',0.5], [ 120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
new_products_detail = ([['sweet'], [100,'']], [], [['gluten-free'], [520, '21D']], [])

print(products_info(products, products_detail, new_products_detail))
"""
def digits_summation (n):
    sum = 0
    if n < 10:
        sum += n
        return sum
    else:
        sum = n%10
        digits = n//10
        sum += digits_summation(digits)
    return sum

# TEST:
#print(digits_summation(12345))
    

def vowel_counts (some_str, results={}):
    vowels = "aeiouAEIOU" 


    # Reset After each test case
    if len(results) == 0:
        results = {}

    # Base Case
    if len(some_str) == 1:
        if some_str[0] in vowels:
            if some_str not in results.keys():
                results[some_str[0]] = 1
            else:
                results[some_str[0]] += 1
        return results
    
    else:
        ltr = some_str[-1] 
        some_str = some_str[:-1]

        if ltr in vowels:

            if ltr not in results.keys():
                results[ltr] = 1
                
            else:
                results[ltr] += 1

        return vowel_counts(some_str,results)

"""    
print(vowel_counts('something'))
print(vowel_counts("This is a test string!")) # {'i': 3, 'a': 1, 'e': 1}
print(vowel_counts("****")) # {}
print(vowel_counts("thjdgfrwmli")) # {'i': 1}
print(vowel_counts("Hello Everyone, welcomE to coursE cs 112")) # {'e': 4, 'o': 5, 'E': 3,'u': 1}
"""
#print(vowel_counts('i'))