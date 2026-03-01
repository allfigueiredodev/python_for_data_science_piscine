def all_thing_is_obj(object: any) -> int:
    if (type(object) == str):
        print(f"{object} is in the kitchen : {type(object)}")
        return 42
    elif (type(object) == int):
        print("Type not found")
        return 42
    print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return 42