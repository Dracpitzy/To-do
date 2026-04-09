#  To-Do API

A simple task management API built with Django and Django REST Framework.  
It helps users create, track, update, and organize their daily tasks efficiently.

---

##  Features

- Create tasks  
- Update tasks  
- Delete tasks  
- Mark tasks as completed  
- Organize tasks easily via API  

---

##  Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (default database)  

---

##  Installation & Setup

1. Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a virtual environment:
python -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the server:
python manage.py runserver

---

##  API Usage

Once the server is running, access the API at:
http://127.0.0.1:8000/

You can test endpoints using:
- Browser  
- Postman  
- cURL  

---

##  Project Structure (Basic)
 
project/
│── manage.py
│── app/
│── project/
│── requirements.txt
│── .gitignore

---

##  Notes

- The `.venv` folder and database files are excluded from version control.  
- Use `requirements.txt` to install dependencies.  

---

##  License

This project is for learning and educational purposes. It is licensed under the Apache 2.0 license - see the [LICENSE](LICENSE) file for details
