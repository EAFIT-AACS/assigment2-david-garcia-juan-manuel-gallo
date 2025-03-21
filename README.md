# 📌 Context-Free Grammar and Pushdown Automata Implementation

## 📖 Project Overview

This project implements a Context-Free Grammar (CFG) and a Pushdown Automaton (PDA) to recognize strings based on the grammar:

<pre>
S → aSb | ε
</pre>

It consists of three Python scripts:

🔹**Algorithm 1:** Generates strings that belong or do not belong to the language.

🔹**Algorithm 2:** Implements a PDA that validates the strings.

🔹**Algorithm 3:** Builds a derivation tree for accepted strings.

## 📜 **Team** 

🔹Juan Manuel Gallo López

🔹David Garcia 

🔹**Class code:** 7309


## 🚀 **How to Run the Project** 

1️⃣ Clone the Repository

Ensure you have Python installed and then clone this repository:

 git clone [repository-link](https://github.com/EAFIT-AACS/assigment2-david-garcia-juan-manuel-gallo/edit/main/README.md)
 
 cd <repository-folder>

2️⃣ Run the Algorithms in Order

Execute the scripts in sequence:
<pre>
python algorithm_1.py
python algorithm_2.py
python algorithm_3.py
</pre>

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
🔹 aaabbb
🔹 aaab
🔹 bb
 
</pre>

### 🎯 Algorithm 2 (PDA Validation)
<pre>
The string 'aabb' ✅ is accepted by the PDA.
The string 'aaabbb' ✅ is accepted by the PDA.
The string 'ab' ❌ is rejected by the PDA.
The string 'aabbbb' ❌ is rejected by the PDA.
</pre>

### 🎯 Algorithm 3 (Derivation Tree)
<pre>

</pre>



