# Hospital_Management_System
An Hospital Management System buit with Django and with the following fuctionalities:
1. Sign-up page for users
2. A page where users can fill in their medical information with relevant questions depending on the developer's discretion.
3. A sign-up page for medical practitioners
4. A page that displays the statistical details of the medical records gotten from the users (all users can view this page) e.g. A chart that shows the count for users with Ebola.
5. A table that displays all users and their relevant medical records (only users registered as medical practitioners can view this page).
6. A drop-down filter to show users with specified medical records of your own discretion e.g show only users with Malaria.

# How to run the application
1. Clone the repository to your local machine
2. Create a python virtual environment 
3. Change directory into the project folder where you have the requirements.txt file, and run pip install -r requirements.txt
4. Setup your database or go on and use the default django database (sqlite)
5. Next run "python manage.py migrate"
6. Then run "python manage.py runserver"

# URLS:
1. /login - Login for both user
2. /staff/signup - Staff registration
3. /user/signup - User registration
4. /logout - Logout for both user
5. /record - homepage displaying statistical details of users (All users)
6. /record/add - Add medical history for user (User Only)
7. /record/users - A table showing the users and their medical records (Staff Only)
