import algorithm_2

def build_derivation_tree(string, depth=0):
    """Constructs a leftmost derivation tree for a given accepted string."""
    if string == "":
        return "ε"
    
    left = "a" + " " * depth
    middle = build_derivation_tree(string[1:-1], depth + 2)
    right = "b"
    
    return f"({left}{middle}{right})"

def algorithm_3():
    accepted_strings = algorithm_2.algorithm_2()
    print("Derivation Trees:")
    for s in accepted_strings:
        print(f"String: '{s}'\nTree: {build_derivation_tree(s)}\n")

if __name__ == "__main__":
    algorithm_3()
