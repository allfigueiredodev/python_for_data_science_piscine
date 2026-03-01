import math

def NULL_not_found(object: any) -> int:
    match  object:
        case None:
            print(f"Nothing: {object} {type(object)}")
            return 0
        case False:
            print(f"Fake: {object} {type(object)}")
            return 0
        case 0:
            print(f"Zero: {object} {type(object)}")
            return 0
        case "":
            print(f"Empty: {object} {type(object)}")
            return 0
        case float() if math.isnan(object):
            print(f"Chesse: {object} {type(object)}")
            return 0
        case _:
            print(f"Type not Found")
            return 1