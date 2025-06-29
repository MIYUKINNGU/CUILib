class InitializeError(Exception):
    pass

class PropertyError(Exception):
    pass

def InstantiateValidError(T: type):
    return SyntaxError(f"It is not valid to instantiate {T.__name__} class.")