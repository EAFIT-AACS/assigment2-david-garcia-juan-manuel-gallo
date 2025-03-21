import algorithm_2
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []
    
    def add_child(self, child):
        self.children.append(child)
    
    def __str__(self):
        if not self.children:
            return str(self.label)
        return f"({self.label} {' '.join(str(child) for child in self.children)})"

def build_tree_from_string(string):
    """Construye un árbol para la cadena dada según la gramática."""
    if string == "":
        return Tree("ε")
    
    # Crear el nodo raíz con etiqueta S
    root = Tree("S")
    
    # Agregar el nodo 'a' a la izquierda
    a_node = Tree("a")
    root.add_child(a_node)
    
    # Agregar el subárbol del medio (si hay contenido entre a y b)
    if len(string) > 2:
        middle = build_tree_from_string(string[1:-1])
        root.add_child(middle)
    
    # Agregar el nodo 'b' a la derecha
    b_node = Tree("b")
    root.add_child(b_node)
    
    return root

def build_derivation_tree(string, depth=0):
    """Constructs a leftmost derivation tree for a given accepted string."""
    if string == "":
        return "ε"
    
    left = "a" + " " * depth
    middle = build_derivation_tree(string[1:-1], depth + 2)
    right = "b"
    
    return f"({left}{middle}{right})"

class TreeDrawer:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.unit = 20  # Unidad básica para el espaciado
        self.level_height = 60  # Altura entre niveles
        self.font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        
    def draw(self, tree):
        # Limpiar el canvas
        self.canvas.delete("all")
        
        # Calcular la posición de cada nodo
        self.positions = {}
        self.calculate_positions(tree, 0)
        
        # Ajustar las coordenadas para que el árbol esté centrado
        min_x = min(pos[0] for pos in self.positions.values())
        max_x = max(pos[0] for pos in self.positions.values())
        offset_x = (self.width - (max_x - min_x)) / 2 - min_x
        
        # Dibujar las líneas primero
        for node, (x, y) in self.positions.items():
            x += offset_x
            for child in node.children:
                child_x, child_y = self.positions[child]
                child_x += offset_x
                self.canvas.create_line(x, y, child_x, child_y, fill="black", width=1)
        
        # Luego dibujar los nodos sobre las líneas
        for node, (x, y) in self.positions.items():
            x += offset_x
            # Calcular el tamaño del texto para el nodo
            text_width = self.font.measure(node.label)
            text_height = self.font.metrics("linespace")
            
            # Dibujar un rectángulo blanco detrás del texto
            padding = 5
            self.canvas.create_rectangle(
                x - text_width/2 - padding,
                y - text_height/2 - padding,
                x + text_width/2 + padding,
                y + text_height/2 + padding,
                fill="white", outline="white"
            )
            
            # Dibujar el texto del nodo
            self.canvas.create_text(x, y, text=node.label, font=self.font)
    
    def calculate_positions(self, node, level):
        """Calcula la posición de cada nodo en el árbol."""
        if not node.children:
            # Para nodos hoja
            x = len(self.positions) * self.unit * 3
            y = level * self.level_height + 50
            self.positions[node] = (x, y)
            return 1, x
        
        # Para nodos internos
        width = 0
        mid_x = 0
        
        # Primero posicionar todos los hijos
        for child in node.children:
            child_width, child_x = self.calculate_positions(child, level + 1)
            width += child_width
            mid_x += child_x
        
        # La posición x del nodo es el promedio de las posiciones x de sus hijos
        mid_x /= len(node.children)
        y = level * self.level_height + 50
        
        self.positions[node] = (mid_x, y)
        return width, mid_x

def visualize_tree(string):
    """Visualiza el árbol de derivación al estilo NLTK."""
    # Crear la ventana
    root = tk.Tk()
    root.title(f"Árbol de Derivación para '{string}'")
    
    # Configurar tamaño y posición
    width, height = 800, 600
    root.geometry(f"{width}x{height}")
    
    # Crear el canvas para dibujar
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # Construir el árbol
    tree = build_tree_from_string(string)
    
    # Dibujar el árbol
    drawer = TreeDrawer(canvas, width, height)
    drawer.draw(tree)
    
    # Etiqueta con la representación textual
    text_label = tk.Label(root, text=f"Representación textual: {build_derivation_tree(string)}", 
                          font=("Helvetica", 10))
    text_label.pack(pady=5)
    
    # Botón para cerrar
    close_button = tk.Button(root, text="Cerrar", command=root.destroy)
    close_button.pack(pady=10)
    
    # Iniciar el bucle de eventos
    root.mainloop()

def algorithm_3():
    accepted_strings = algorithm_2.algorithm_2()
    print("Derivation Trees:")
    
    for s in accepted_strings:
        print(f"String: '{s}'\nTree: {build_derivation_tree(s)}\n")
        visualize_tree(s)

if __name__ == "__main__":
    algorithm_3()
