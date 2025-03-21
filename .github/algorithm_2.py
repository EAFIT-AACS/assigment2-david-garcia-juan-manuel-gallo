from unittest import result
import algorithm_1
import string

def pda_accepts(string):
    """Simulates a PDA for the grammar S -> aSb | ε."""
    stack = []
    for char in string:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if not stack or stack[-1] != 'a':
                return False
            stack.pop()
    return len(stack) == 0

def algorithm_2():
    accepted, rejected = algorithm_1.algorithm_1()
    print("PDA Validation:")
    for s in accepted + rejected:
        result = "accepted" if pda_accepts(s) else "rejected"
        print(f"The string '{s}' is {result} by the PDA.")
    
    return [s for s in accepted if pda_accepts(s)]

if __name__ == "__main__":
    algorithm_2()
    print(f"La cadena '{string}' es {'aceptada' if result else 'rechazada'} por el PDA.")