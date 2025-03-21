import algorithm_1

def pda_accepts(cadena):
    """Simula un PDA para la gramática S -> aSb | ε."""
    stack = []
    for char in cadena:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if not stack or stack[-1] != 'a':
                return False
            stack.pop()
    return len(stack) == 0

def algorithm_2():
    # Se obtienen las cadenas generadas por el primer código
    accepted, rejected = algorithm_1.algorithm_1()
    print("\nValidación del PDA:")
    for s in accepted + rejected:
        result = "aceptada" if pda_accepts(s) else "rechazada"
        print(f"La cadena '{s}' es {result} por el PDA.")
    
    return [s for s in accepted if pda_accepts(s)]

if __name__== "__main__":
    algorithm_2()
