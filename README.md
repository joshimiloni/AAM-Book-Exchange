# AAM-Book-Exchange
HTML, CSS, JS, Jquery, Bootstrap, Python, Django

AAM Book Exchange is a community for exchanging used college books and equipments. Software also includes test preparation material such as test papers and frequently asked previous year questions. This software allows the users to manage the inventory of the system with the CRUD functionality,i.e create, retrieve, update, delete.

The product will:
1. Enable users to exchange books in an organized, and transparent manner.
2. Allow exchange of equipment, such as drafters, drawing boards, etc.
3. Serve as a repository for study and test-preparation material, such as previous test papers, question lists, etc.
 
Admin Login:
Username : admin __
Password : pass@123

Test User Login:
Username : miloni-joshi __
Password : pass@123

Steps after cloning this repository:

//Create a virtual environment and install dependencies.  __
mkvirtualenv this_project __
pip install -r requirements.txt __

//Initialise database after configuring it. __
python ./manage.py syncdb __
python ./manage.py migrate __

//Run the development server. __
python ./manage.py runserver __


