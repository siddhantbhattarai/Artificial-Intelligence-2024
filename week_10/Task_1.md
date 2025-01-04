### **e-Portfolio: Neural Networks Application Info Sheet**

---

### **Application of Artificial Neural Network: Facial Recognition System**

---

#### **a. What is it being used for?**  
A facial recognition system is used for:  
- **Security and Authentication:** Unlocking smartphones, surveillance, airport security, and secure building access.  
- **Social Media:** Auto-tagging in photos (e.g., Facebook’s face detection feature).  
- **Healthcare:** Monitoring patients' emotions during virtual therapy.  
- **Retail:** Personalized customer experiences (e.g., tracking frequent customers' preferences).

---

#### **b. Any Success/Failure Stats**  

- **Success Rates:**  
  - Apple's Face ID has a success rate of **98-99%** for correctly identifying authorized users.  
  - The accuracy of deep learning-based face recognition models such as **FaceNet** exceeds **99.6%** on the benchmark LFW (Labelled Faces in the Wild) dataset.  
- **Failures:**  
  - **Bias and Errors:** Studies have shown that some systems have biases based on skin color, gender, and age. For instance, early versions of facial recognition systems had an error rate of **30-35%** for darker skin tones compared to **1%** for lighter skin tones.

---

#### **c. What type of ANN it is and any methods it employs?**

- **Type of ANN:** Convolutional Neural Network (CNN)  
  - CNNs are widely used for image-related tasks due to their ability to detect spatial features like edges and textures.  
- **Methods Used:**  
  - **FaceNet (Embedding-based Approach):**  
    Converts facial images into embeddings (numerical vectors) and compares them using cosine similarity for classification.  
  - **ResNet (Residual Neural Network):**  
    Utilizes skip connections to improve training and avoid the vanishing gradient problem.  

---

#### **d. Why do you think it is interesting?**  

- **Real-World Impact:** Facial recognition is transforming security, healthcare, and entertainment industries.  
- **Complexity:** Despite the technical complexity (e.g., handling lighting, pose variations, and occlusions), the system performs remarkably well in real-time applications.  
- **Ethical Implications:** This technology raises interesting questions about privacy and fairness, making it a topic of discussion not just for technologists but for policymakers and society as a whole.
