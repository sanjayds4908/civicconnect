# 🏛 Smart Civic Issue Reporting System

A web-based civic complaint management platform that enables citizens to report public issues such as potholes, garbage problems, water leakage, drainage issues, and streetlight failures. The system allows citizens to submit complaints digitally and helps administrators efficiently monitor, manage, and resolve reported issues.

---

## 📌 Project Overview

The **Smart Civic Issue Reporting System** is developed to improve communication between citizens and authorities by providing a digital platform for reporting and tracking civic problems.

Citizens can register, login, submit complaints with images and location details, and track the progress of their complaints. Administrators can access a centralized dashboard to review complaints, view uploaded images, and update complaint status.

---

## 🚀 Features

### 👤 Citizen Module

- User Registration and Login
- Submit civic complaints
- Upload issue images
- Add complaint category and location
- Track complaint status
- View complaint history
- View complete complaint details

### 🛡 Admin Module

- Secure admin dashboard
- View all citizen complaints
- Access citizen details
- Preview uploaded complaint images
- Manage complaint workflow
- Update complaint status:
  - 🟡 Pending
  - 🔵 In Progress
  - 🟢 Resolved
- Monitor complaint statistics

---

## 🏗 System Workflow

```
Citizen
   |
Register / Login
   |
Submit Complaint
   |
Database Storage
   |
Admin Dashboard
   |
Review Complaint
   |
Update Status
   |
Citizen Tracks Resolution
```

---

## 🖥 System Architecture

```
              Citizen

                 |
                 |

          Web Interface
       HTML | CSS | Bootstrap

                 |
                 |

          Flask Backend

                 |
        ------------------
        |                |

     SQL Database     Image Storage

        |
        |

    Admin Dashboard
```

---

# 🛠 Technologies Used

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Backend
- Python
- Flask Framework
- Flask SQLAlchemy

## Database
- MySQL

## Development Tools
- VS Code
- Git & GitHub
- XAMPP

---

# 📂 Project Structure

```
Smart-Civic-Issue-Reporting-System/

│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── user.py
│   └── complaint.py
│
├── routes/
│   ├── auth.py
│   ├── complaints.py
│   └── admin.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── complaint_form.html
│   ├── complaint_history.html
│   └── admin.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
└── README.md
```

---

# ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/sanjayds4908/civicconnect.git
```

### 2. Open Project Folder

```bash
cd Smart-Civic-Issue-Reporting-System
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Database

Create MySQL database:

```sql
CREATE DATABASE civic_system;
```

Update database configuration inside:

```
config.py
```

---

### 6. Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

---

# 📸 Screenshots

Add screenshots of:

- User Registration/Login
- Citizen Dashboard
- Complaint Submission Page
- Complaint History
- Admin Dashboard

---

# 🔮 Future Enhancements

- Google Maps based complaint location tracking
- Email/SMS notifications
- Mobile application support
- Advanced analytics dashboard
- AI-based complaint priority classification
- Government portal integration

---

# 🎯 Project Objective

The objective of this project is to create a transparent and efficient digital platform that enables citizens to report civic issues easily and helps authorities manage complaints effectively for faster resolution.

---

# 👨‍💻 Developer

**Sanjay D S**

Electronics and Communication Engineering (ECE)

GitHub:
https://github.com/sanjayds4908

---

# ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.
