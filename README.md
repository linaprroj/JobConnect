
---

# 🌟 JobConnect

## 📖 Description

**JobConnect** is a comprehensive job connection platform designed to bridge the gap between job seekers and employers. Job seekers can create profiles, upload resumes, search for jobs, and apply to job postings. Employers can post job openings, review applications, schedule interviews, and communicate directly with job seekers. The platform aims to streamline the job search and hiring process, providing an intuitive and user-friendly interface for both parties.

## ✨ Features

- **Job Seekers:**
  - Create profiles and upload resumes.
  - Search and apply for job postings.
  - Receive notifications about application status.
  - Communicate directly with employers.

- **Job Offerers (Employers):**
  - Post job openings and manage listings.
  - Review applications and resumes.
  - Schedule interviews with job seekers.
  - Communicate directly with candidates.

## 🛠️ Technologies Used

- **Frontend:** Next.js, Tailwind CSS
- **Backend:** Python, Flask
- **Database:** MySQL
- **Dashboarding:** Power BI

## 🚀 Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- MySQL
- Node.js
- npm

### Backend Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/linaprroj/JobConnect.git
    cd JobConnect/backend
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**

    ```sql
    mysql -u root -p
    CREATE DATABASE JobConnect;
    ```

5. **Restore the database from the backup file:**

    ```bash
    mysql -u root -p JobConnect < JobConnect_backup.sql
    ```

6. **Run the Flask server:**

    ```bash
    flask run
    ```

### Frontend Setup

1. **Navigate to the frontend directory:**

    ```bash
    cd ../frontend
    ```

2. **Install the dependencies:**

    ```bash
    npm install
    ```

3. **Run the development server:**

    ```bash
    npm run dev
    ```

## 🎉 Usage

1. **Access the frontend:**
   Open your web browser and go to `http://localhost:3000`.

2. **API interactions:**
   Use `http://localhost:5000` for backend API interactions.

## 📜 License

This project is licensed under the MIT License.

---
