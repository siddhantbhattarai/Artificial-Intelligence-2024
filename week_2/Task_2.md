### **Task 2: Semantics – Semantic Net for Wildlife Image Sorting**  

---

### **Scenario**  
In this task, you are contributing to a machine vision project designed to automate the sorting of wildlife images. Your goal is to create a **semantic net** that clarifies the differences between **animals** and **birds** to improve classification accuracy.

---

### **1. Overview of Semantic Net**  
A semantic net is a graphical representation that uses **nodes** (representing entities) and **edges** (representing relationships) to illustrate the connections between concepts. In this case, the semantic net will distinguish between "animals" and "birds" by highlighting key properties such as physical characteristics, behaviors, and habitats.

---

### **2. Semantic Net Structure**  

#### **Top-Level Categories:**  
- **Animal (Superclass)**: General category for all wildlife.  
- **Bird (Subclass of Animal)**: A subset of animals with defining characteristics.

---

### **3. Key Nodes and Relationships**  

#### **Animal (Superclass)**  
- **Characteristics:**  
  - Has vertebrae  
  - Can have fur, feathers, or scales  
  - Breathes oxygen  

#### **Subcategories of Animals:**  
- **Mammals:**  
  - Has fur or hair  
  - Gives live birth (in most cases)  
  - Feeds young with milk  
- **Reptiles:**  
  - Has scales  
  - Lays eggs  
  - Cold-blooded  

#### **Bird (Subclass of Animal)**  
- **Characteristics:**  
  - Has feathers  
  - Lays eggs  
  - Has wings (but not all can fly)  
  - Has beaks (no teeth)  
- **Examples:**  
  - **Flight Capable:** Eagle, Sparrow  
  - **Flightless:** Penguin, Ostrich  

---

### **4. Sample Semantic Net Nodes and Edges:**  

```text
[Animal]  
  ├── [Mammal] → "Has fur"  
  ├── [Reptile] → "Has scales"  
  └── [Bird] → "Has feathers" → "Lays eggs" → "Has wings"  
          ├── [Eagle] → "Can fly"  
          └── [Penguin] → "Cannot fly"  
```

---

### **5. Group Discussion and Consensus**  

#### **Step 1: Collaborative Creation of Semantic Net**  
- **Member 1:** Focused on birds (flight vs flightless) and specific bird examples.  
- **Member 2:** Focused on mammals and their distinctive traits (fur, milk production).  
- **Member 3:** Covered reptiles to distinguish between non-avian animals with scales.  
- **You (Group Leader):** Compiled all relationships into the final semantic net structure.  

#### **Step 2: Feedback and Refinements:**  
- Collected feedback from members to ensure no key animal group was overlooked (e.g., amphibians were excluded from this net as they were not relevant).  
- Adjusted terminology consistency (e.g., "beak" vs. "bill") for precision.

---

### **6. Finalized Semantic Net:**  

```text
[Animal]  
  ├── [Mammal] → {Has fur, Live birth, Feeds young milk}  
  ├── [Reptile] → {Has scales, Cold-blooded, Lays eggs}  
  └── [Bird] → {Has feathers, Lays eggs, Has wings, Has beak}  
          ├── [Flight Capable] → Examples: Eagle, Sparrow  
          └── [Flightless] → Examples: Penguin, Ostrich  
```

---

### **7. Final Presentation**  
The finalized semantic net was shared with the group, ensuring that all relationships were represented visually in the diagram and logically connected. The consensus was reached that the semantic net effectively distinguishes between key wildlife categories and meets the project's requirements.

---

### **Conclusion**  
This semantic net provides a robust framework for the machine vision project to accurately differentiate between animals and birds. By organizing key attributes and examples hierarchically, the system can improve wildlife image sorting and classification with greater accuracy and clarity.