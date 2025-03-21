import random

def generate_accepted_strings(n=4):
    """Generates strings that belong to the grammar S -> aSb | ε"""
    def build_string(depth=0):
        return "a" + build_string(depth + 1) + "b" if random.choice([True, False]) or depth == 0 else ""
    
    return [build_string() for _ in range(n // 2)]

def generate_rejected_strings(n=4):
    """Generates strings with the same alphabet but that do not belong to the grammar."""
    accepted = set(generate_accepted_strings(n))
    rejected = set()
    
    while len(rejected) < n // 2:
        length = random.randint(1, 6)
        candidate = "".join(random.choice("ab") for _ in range(length))
        if candidate not in accepted and candidate.count("a") != candidate.count("b"):
            rejected.add(candidate)
    
    return list(rejected)

def algorithm_1():
    accepted = generate_accepted_strings()
    rejected = generate_rejected_strings()
    print("Generated Strings:")
    for s in accepted + rejected:
        print(f"{'✔' if s in accepted else '✘'} String: '{s}'")
    
    return accepted, rejected

if __name__ == "__main__":
    algorithm_1()