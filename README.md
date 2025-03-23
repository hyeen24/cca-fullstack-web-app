# **SUSS Club Management System**  

## **Overview**  
The SUSS Club Management System is a web application designed to facilitate student club membership management at **Singapore University of Social Sciences (SUSS)**. It allows administrators to create student accounts, process applications for various clubs, and manage membership statuses efficiently.  

## **Features**  
✅ **User Authentication:** Secure login and session management with Flask-Login.  
✅ **Student Account Creation:** Admins can create student accounts with predefined roles.  
✅ **Application Processing:** Students can apply for Interest Groups or Competitive Groups, and admins can review, approve, or reject applications.  
✅ **Role-Based Access:** Admins, CCA admins, and students have different levels of access.  
✅ **MongoDB Integration:** Data is stored in a **MongoDB database** using MongoEngine.  

## **Tech Stack**  
- **Backend:** Flask, Flask-Login, Flask-MongoEngine  
- **Database:** MongoDB  
- **Frontend:** HTML, Jinja Templates, Bootstrap  
- **Authentication:** Flask-Login  
- **Deployment:** Flask development server (can be deployed on AWS, Azure, or Heroku)  

## **Installation & Setup**  
### **1. Clone the repository**  
```bash
git clone https://github.com/yourusername/suss-club-management.git
cd suss-club-management
```

### **2. Create a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
```

### **3. Install dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set up environment variables**  
Create a **.env** file in the project root and add the MongoDB connection URI:  
```
MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/suss
```

### **5. Run the application**  
```bash
flask run
```
Access the app at **http://127.0.0.1:5000/**  

## **Project Structure**  
```
suss-club-management/
│── controllers/             # Blueprint routes for authentication & manager
│   ├── auth.py
│   ├── manager.py
│── models/                  # Database models (User, Application, Groups)
│   ├── users.py
│   ├── application.py
│   ├── cca.py
│   ├── forms.py
│── templates/               # Jinja2 HTML templates
│── static/                  # CSS, JS, images
│── extensions.py            # Database & authentication setup
│── app.py                   # Main Flask app
│── requirements.txt         # Required dependencies
│── .env                     # Environment variables
│── README.md                # Project documentation
```

## **Future Enhancements**  
🚀 **Email Notifications:** Notify students about application status updates.  
🚀 **Dashboard Analytics:** Show statistics on student participation.  
🚀 **Automated Role Assignments:** Assign CCA admin roles based on eligibility.  


