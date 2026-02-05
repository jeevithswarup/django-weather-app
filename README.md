# 🌦️ Django Weather Application

A Django-based web application that provides real-time weather information for any city by integrating a third-party weather API.

This project focuses on demonstrating how backend applications fetch, process, and present live external data in a clean and user-friendly web interface.

---

## 🚀 What You’ll Find Here

This repository demonstrates practical usage of Django for building real-world applications, including:

- 🌍 Fetching real-time weather data using an external API  
- 🧠 Backend processing and business logic using Django views  
- 🔄 Handling and parsing JSON responses  
- 📄 Rendering dynamic data using Django templates  
- 🧾 User input handling through forms  
- 🌐 URL routing and request handling  
- 💻 Basic frontend integration using HTML and CSS  

---

## 💡 Why This Repository Exists

This project was created to gain hands-on experience with **API-driven web applications** using Django.

Instead of working with static data, this application communicates with a live weather service to retrieve current atmospheric conditions such as temperature, humidity, and weather description based on user input.

The goal of this project is to understand:

- How real-world APIs are consumed in backend systems  
- How Django manages HTTP requests and responses  
- How dynamic content is generated and displayed on web pages  
- How backend logic connects seamlessly with frontend templates  

This project is especially useful for beginners who want to move beyond basic Django concepts and build applications that interact with real external services.

---

## 🛠️ How It Works

1. The user enters a city name in the search form  
2. Django sends a request to the external weather API  
3. The API responds with structured weather data in JSON format  
4. The backend processes the response and extracts required values  
5. The weather information is displayed dynamically on the web page  

This entire process happens in real time for every user request.

---

## 🛠️ How to Run the Project

Follow these steps to run the project locally:

```bash
git clone https://github.com/jeevithswarup/django-weather-app.git
cd django-weather-app
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

git clone https://github.com/jeevithswarup/django-weather-app.git
cd django-weather-app
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
*open web browser*
http://127.0.0.1:8000/
