import ast

class inClass:
    def __init__(self) -> None:
        safe_expression = "{'key': 'value'}"
        result = ast.literal_eval(safe_expression)
        print(result)

def inFunction():
    safe_expression = "{'key': 'value'}"
    result = ast.literal_eval(safe_expression)
    print(result)


safe_expression = "{'key': 'value'}"
result = ast.literal_eval(safe_expression)
print(result)



def alt_eval():
    print("An method with another Name")

alt_eval()

def altEval():
    print("An method with another Name")
altEval()

def alt1Eval():
    print("An method with another Name")
alt1Eval()