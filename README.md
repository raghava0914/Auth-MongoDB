# **MongoDB Blog Dashboard** 🚀  
A **modern user authentication system** with **MongoDB, Flask, and Tailwind CSS**, featuring a **secure signup/login system** and a **beautiful dashboard** with a MongoDB tutorial.  

![Dashboard Preview](static/images/dashboard_preview.png)  

## **📌 Features**  
✅ **User Authentication** – Secure signup & login using MongoDB  
✅ **Modern UI** – Styled with **Tailwind CSS** for a sleek look  
✅ **Logout Button** – Unique design with hover effects  
✅ **MongoDB Blog Section** – Displays a guide for users  
✅ **Fully Responsive** – Works on mobile, tablet, and desktop  

---

## **📁 Project Structure**  

```
/Auth-MongoDB-Blog-Dashboard
│── /templates
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│── app.py
│── config.py
│── models.py
│── auth.py
│── README.md
│── requirements.txt
```

---

## **⚡ Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/raghava0914/Auth-MongoDB.git
cd Auth-MongoDB
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Start MongoDB Server**  
Make sure **MongoDB** is installed and running.  
For local MongoDB, start it with:  
```bash
mongod
```
For **MongoDB Atlas**, update the `MONGO_URI` in `config.py` with your connection string.

### **5️⃣ Run the Flask App**  
```bash
python app.py
```
Your app will be live at: **`http://127.0.0.1:5000`** 🚀  

---

## **🛠 Tech Stack**  
🔹 **Python Flask** – Backend framework  
🔹 **MongoDB** – NoSQL database for user data  
🔹 **Tailwind CSS** – Modern styling framework  
🔹 **HTML5 + Jinja2** – Templating engine for Flask  
🔹 **Flask-Login** – User session management  

---

## **📸 Screenshots**  

### 🔹 **Signup & Login Page**  
![Signup Page](static/images/signup_preview.png)  

### 🔹 **Dashboard with User Info**  
![Dashboard](static/images/dashboard_preview.png)  

---


## **📜 Environment Variables (config.py)**  
```python
MONGO_URI = "mongodb://localhost:27017/auth_system"
SECRET_KEY = "your_secret_key_here"
SESSION_TYPE = "filesystem"
```

---

## **🛡 Security Features**  
✅ **Hashed Passwords** using `Werkzeug Security`  
✅ **Session Management** for user authentication  
✅ **Regular Expressions for Input Validation**  

---

## **🤝 Contributing**  
Contributions are welcome! Please follow these steps:  
1. **Fork the repository**  
2. **Create a new branch** (`feature-new`)  
3. **Commit your changes**  
4. **Push to your fork & submit a PR**  

---

## **📃 License**  
This project is **open-source** under the **MIT License**.  

---

## **📩 Contact**  
💡 **Author:** K Ranga Raghava Varma  
📧 Email: brahmajibrahma025@gmail.com  
📍 Location: Medchal, Hyderabad  
