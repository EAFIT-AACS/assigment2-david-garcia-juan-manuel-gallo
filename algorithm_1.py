import random

def generate_accepted_strings(n=4):
    """Genera cadenas que pertenecen a la gramática S -> aSb | ε"""
    def build_string(depth=0):
        # Se decide recursivamente si agregar más "a" y "b"
        return "a" + build_string(depth + 1) + "b" if random.choice([True, False]) or depth == 0 else ""
    
    # Se generan n//2 cadenas
    return [build_string() for _ in range(n // 2)]

def generate_rejected_strings(n=4):
    """Genera cadenas con el mismo alfabeto pero que no pertenecen a la gramática."""
    accepted = set(generate_accepted_strings(n))
    rejected = set()
    
    while len(rejected) < n // 2:
        length = random.randint(1, 6)
        candidate = "".join(random.choice("ab") for _ in range(length))
        # Se verifica que la cadena no sea aceptada y que el número de 'a' y 'b' sean diferentes
        if candidate not in accepted and candidate.count("a") != candidate.count("b"):
            rejected.add(candidate)
    
    return list(rejected)

def algorithm_1():
    # Generamos las cadenas aceptadas y rechazadas
    cadenas_aceptadas = generate_accepted_strings()
    cadenas_rechazadas = generate_rejected_strings()
    
    # Combinamos ambas listas
    todas_cadenas = cadenas_aceptadas + cadenas_rechazadas

    print("Cadenas generadas:")
    # Enumeramos y mostramos cada cadena sin indicar su categoría
    for idx, cadena in enumerate(todas_cadenas, start=1):
        print(f"{idx}. {cadena}")
    
    return cadenas_aceptadas, cadenas_rechazadas

if __name__ == "__main__":
    algorithm_1()
