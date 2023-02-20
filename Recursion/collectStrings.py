# Write a function called collectStrings which accepts an object and returns an array of all the values in the object
# that have a type of string.

def collectStrings(obj):
    l1 = []
    for x in obj:
        if type(obj[x]) is dict:
            l1 += collectStrings(obj[x])
        elif type(obj[x]) is str:
            l1.append(obj[x])
    return l1


obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))
