# 📌 Context-Free Grammar and Pushdown Automata Implementation

## 📖 Project Overview

This project implements a Context-Free Grammar (CFG) and a Pushdown Automaton (PDA) to recognize strings based on the grammar:

<pre>
S → aSb | ε
</pre>

It consists of three Python scripts:

🔹 **Algorithm 1:** Generates strings that either belong or do not belong to the language.  
🔹 **Algorithm 2:** Implements a PDA that validates the strings.  
🔹 **Algorithm 3:** **Main Algorithm** – This script imports and executes both Algorithm 1 and Algorithm 2, and in addition, builds a derivation tree for accepted strings.

**Note:** Although Algorithms 1 and 2 can be run individually to observe their respective functionalities, executing Algorithm 3 is sufficient to see the complete process in action.

## 📜 **Team** 

🔹Juan Manuel Gallo López

🔹David Garcia Zapata

🔹**Class code:** 7309


## 🚀 **How to Run the Project** 

1️⃣ Clone the Repository

Ensure you have Python installed and then clone this repository:

 git clone [repository-link](https://github.com/EAFIT-AACS/assigment2-david-garcia-juan-manuel-gallo/edit/main/README.md)
 
 cd <repository-folder>

2️⃣ Run the Algorithms

To run individual algorithms:
If you want to test Algorithm 1 and Algorithm 2 separately, you can execute them individually:
<pre>
python algorithm_1.py
python algorithm_2.py
</pre>

To run the complete integrated process:
Execute Algorithm 3, which imports and runs Algorithms 1 and 2, and also displays the derivation tree:
<pre>
python algorithm_3.py
</pre>
⚠️**Important:** When running Algorithm 3, a pop-up window displaying the derivation tree will appear. To view the different trees, close the current window and the next tree window will automatically open.

## 📂 **File Structure**
<pre>
📂 project-folder/
 ├── algorithm_1.py  # String Generator
 ├── algorithm_2.py  # PDA Implementation
 ├── algorithm_3.py  # Derivation Tree Builder
 ├── README.md       # Project documentation
</pre>

## 🛠️**Development environment**

   ✦**Operative system:** Windows 11 
   
   ✦**Programming language:** Python 
   
   ✦**Tools:** Visual Studio Code
   
## 📌 **Example Outputs**

### 🎯 **Algorithm 1 (String Generation)**
<pre>
Generated Strings:
🔹 ab
🔹 aabb
🔹 babb
🔹 aab
 
</pre>

### 🎯 Algorithm 2 (PDA Validation)
<pre>
La cadena 'ab' ✅ is accepted by the PDA.
La cadena 'aabb' ✅ is accepted by the PDA.
La cadena 'babb' ❌ is rejected by the PDA.
La cadena 'aab' ❌ is rejected by the PDA.
</pre>

### 🎯 Algorithm 3 (Derivation Tree)
<pre>
 Derivation tree for 'ab':

            S
           / \
          a   b
</pre>
<pre>
  Derivation tree for 'aabbb':

             S
           / | \
          a  S  b
            / \
           a   b

</pre>






