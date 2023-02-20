# Write a function called stringifyNumbers which takes in an object and finds all the values which are numbers and
# converts them to strings. Recursion would be a great way to solve this!

def stringifyNumbers(obj):
    for item in obj:
        if type(obj[item]) is dict:
            stringifyNumbers(obj[item])
        elif type(obj[item]) is int:
            obj[item] = str(obj[item])
    return obj


obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

print(stringifyNumbers(obj))
