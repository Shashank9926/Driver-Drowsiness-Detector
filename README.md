# 🚗 Driver Drowsiness Detection & SOS Alert System

A real-time **Driver Drowsiness Detection System** that monitors a driver’s eye state using Computer Vision and Deep Learning. When drowsiness is detected, the system triggers an **audio alarm** and automatically raises an **SOS alert** to a backend server for monitoring.

This project combines **AI + OpenCV + Flask API + MySQL**, making it a complete **AI-powered safety system**.

---

## 🧠 Project Overview

Driver fatigue is a major cause of road accidents. This system detects prolonged eye closure and:

• Sounds an alarm to wake the driver  
• Sends an SOS alert to a backend server  
• Stores SOS and session data in a MySQL database  

---

## ⚙️ Tech Stack

**Computer Vision & AI**
- Python  
- OpenCV  
- Keras / TensorFlow (CNN Model)  
- NumPy  

**Backend**
- Flask (REST API)  

**Database**
- MySQL  

**Other**
- Pyglet (Alarm sound)  
- Haarcascade Classifiers (Face & Eye detection)

---

## 🏗 System Architecture

Camera → Eye Detection → CNN Model Prediction → Drowsiness Check → Alarm Trigger → SOS API Call → Database Storage

---

## 📂 Project Structure

```
Driver-Drowsiness-System/
│
├── detect_drowsiness.py       # Main computer vision detection script
├── driver_drowsiness_train.py # CNN model training script
├── drowiness_new7.h5          # Trained deep learning model
├── alarm.wav                  # Alarm sound
│
├── service.py                 # Flask backend service
├── dao.py                     # Database access layer
│
└── data/
    ├── haarcascade_frontalface_default.xml
    ├── haarcascade_lefteye_2splits.xml
    └── haarcascade_righteye_2splits.xml
```

---

## 🎯 Features

✅ Real-time face and eye detection  
✅ CNN-based eye state classification (Open / Closed)  
✅ Drowsiness detection using consecutive frame monitoring  
✅ Alarm sound alert  
✅ Automatic SOS alert to backend server  
✅ MySQL database logging  

---

## 🖥 How Drowsiness Detection Works

1. Webcam captures live video frames  
2. Face detected using Haarcascade  
3. Eye regions extracted  
4. Each eye is passed into a trained CNN model  
5. If both eyes are detected **closed for 10+ frames**, the system:
   - Triggers alarm sound  
   - Calls `dao.raise_sos()` to raise an SOS alert  

---

## 🚨 SOS Backend System

When drowsiness is confirmed:

- A record is inserted into the **SOS table**
- Flask API allows monitoring of:
  - Driver sessions
  - Active SOS alerts

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/session` | GET | Fetch driver session details |
| `/sos` | GET | Fetch active SOS alerts |
| `/sos` | POST | Mark SOS as actioned |

Server runs on:

http://localhost:6068

---

## 🗄 Database

**Database Name:** `DRIVER_DROWSINESS`

Tables used:
- `user`
- `taxi`
- `session`
- `sos`

⚠ Update database username & password inside `dao.py`

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/driver-drowsiness-system.git
cd driver-drowsiness-system
```

### 2️⃣ Install Dependencies
```bash
pip install opencv-python numpy tensorflow keras pyglet flask mysql-connector-python
```

### 3️⃣ Setup Database
- Install MySQL
- Create database: `DRIVER_DROWSINESS`
- Create required tables (user, taxi, session, sos)

### 4️⃣ Run Backend Server
```bash
python service.py
```

### 5️⃣ Run Drowsiness Detector
```bash
python detect_drowsiness.py
```

---

## 🧪 Model Training

To retrain the eye state detection model:

```bash
python driver_drowsiness_train.py
```

Dataset structure should contain **Open** and **Closed** eye images.

---

## 🚧 Limitations

- Low-light conditions reduce accuracy  
- Glasses may affect eye detection  
- Requires front-facing camera angle  

---

## 🔮 Future Improvements

✨ Yawn detection  
✨ Head nodding detection  
✨ GPS location in SOS alert  
✨ Cloud-based monitoring dashboard  
✨ Night vision support  

---

## 👨‍💻 Author

**Shashank Shukla**  
B.Tech Mechanical Engineering | AI & Data Enthusiast  

If you found this project useful, consider giving it a ⭐ on GitHub!
