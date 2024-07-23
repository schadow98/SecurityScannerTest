import ast

class inClass:
    def __init__(self) -> None:
        eval("1+1")
        ast.literal_eval("1+1")

def inFunction():
    eval("1+1")
    ast.literal_eval("1+1")

eval("1+1")
ast.literal_eval("1+1")