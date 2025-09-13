# 📄 PDF Chatbot - Summarize & Query Your PDFs

<img width="1773" height="359" alt="Screenshot 2025-09-13 160838" src="https://github.com/user-attachments/assets/67bd3fa2-068a-4077-b0ad-41e9493af2c4" />

A **Streamlit-based AI Chatbot** that allows you to **upload PDFs** and interact with them using **natural language queries**. It also provides accurate summaries and handles large PDF files efficiently.

---

## 🔹 Features

- Upload PDFs (up to 200 MB)  
- Automatic PDF text extraction  
- Smart **text chunking** for better performance  
- **Summarization** of entire PDF content  
- **Question-Answering** on PDF content  
- Vector similarity search using **FAISS**  
- Interactive and responsive **Streamlit UI**  

---

## 🔹 Technologies Used

- **Python 3.10+**  
- **Streamlit** – UI framework  
- **pdfplumber** – PDF text extraction  
- **Transformers** – HuggingFace models for NLP  
- **Sentence-Transformers** – Embeddings  
- **FAISS** – Efficient vector search  

---

## 🔹 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot
```

2. Create a virtual environment:

```bash
python -m venv chatbot_env
chatbot_env\Scripts\activate   # Windows
# source chatbot_env/bin/activate  # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 🔹 Usage

1. Upload a PDF in the Streamlit interface.  
2. Wait for the text to be processed (chunking + embedding).  
3. Ask any question related to the PDF.  
4. Get summaries and answers instantly.  

---

## 🔹 Folder Structure

```
pdf-chatbot/
│
├─ app.py              # Main Streamlit app
├─ requirements.txt    # Python dependencies
├─ README.md           # Project documentation
├─ chatbot_env/        # Virtual environment
└─ data/               # Optional folder for PDFs
```

---

## 🔹 Screenshots

![Upload PDF](images/upload.png)  
*Upload your PDF file*

![Query PDF](images/query.png)  
*Ask questions & get answers*

---

## 🔹 Author

**Sachin Kumar**  
Delhi, India  
📧 sachin@example.com
