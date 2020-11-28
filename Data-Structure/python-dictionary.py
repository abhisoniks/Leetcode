# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

if __name__ == '__main__':
    pb = {"Mike": 55555555}
    pb["Mike"] = 1234
    print(pb)
    del pb["Mike"]
    print(pb)
    pb["pi"]=456
    pb["ab"]=890
    print(pb)
    print(pb.get("pi"))
    print(pb)

    ## Loop through dictionary
    print("Only keys")
    for x in pb:
        print(x)

    print("Only Values")
    for y in pb.values():
        print(y)

    print("Keys and Values both")
    for key,val in pb.items():
        print(key,val)

    ## Adding element
    pb["new"]=89000
    print(pb)

    ## REmove element
    del pb["new"]
    print(pb)
    pb.pop("ab") # REmove element with given key
    pb.popitem() # Remove last inserted item


    # Convert lists to dictionary
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    sampleDict = dict(zip(keys, values))
    print(sampleDict)

    # Merge  two dictionary
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict3 = dict1.copy()
    dict3.update(dict2)
    print(dict3)
