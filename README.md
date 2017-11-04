# AAM-Book-Exchange
HTML, CSS, JS, Jquery, Bootstrap, Python, Django, Postgres

AAM Book Exchange is a community for exchanging used college books and equipments. Software also includes test preparation material such as test papers and frequently asked previous year questions. This software allows the users to manage the inventory of the system with the CRUD functionality,i.e create, retrieve, update, delete.

The product will:
1. Enable users to exchange books in an organized, and transparent manner.
2. Allow exchange of equipment, such as drafters, drawing boards, etc.
3. Serve as a repository for study and test-preparation material, such as previous test papers, question lists, etc.
 
Admin Login:
Username : admin 
Password : pass@123

Test User Login:
Username : miloni-joshi 
Password : pass@123

Steps after cloning this repository:

//Create a virtual environment and install dependencies. 
mkvirtualenv this_project
pip install -r requirements.txt

//Initialise database after configuring it.
python ./manage.py syncdb 
python ./manage.py migrate 

//Run the development server.
python ./manage.py runserver


