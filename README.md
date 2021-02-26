# Django

To get started
* Install python (I'm using version 3.7.9, didn't try yet for other version)
    >https://www.python.org/downloads/windows/ (Windows)
    
    >sudo apt-get install python3.7  (Linux)
* Create Virtual Environment (venv):
    >python venv venv
* Activate virtual environment:
    >venv\scripts\activate.bat (Windows) 
    
    >venv/bin/activate (Linux)
* Install package:
    >pip install -r requirements.txt
* Environment Varible (EMAIL_USER, EMAIL_PASS, GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE_CONTENTS)
    * For windows
      >https://www.youtube.com/watch?v=IolxqkL7cD8
    * For Linux 
      >https://www.youtube.com/watch?v=5iWhQWVXosU&t
    * Edit in Setting.py (not recommended)
      >edit os.environ.get() to the respective value
* Start the server locally:
    >python manage.py runserver

Link on Heroku
https://a17kedjango.herokuapp.com/

Credit to

Assoc. Prof. Muhammad Munim Bin Ahmad Zabidi
>munim@utm.my

Reference
Corey Schafer 
>https://www.youtube.com/c/Coreyms

Django Google Drive Storage
>https://django-googledrive-storage.readthedocs.io/en/latest/

![alt text](https://github.com/tanwailiang97/server_py/blob/master/WhatsApp%20Image%202021-02-24%20at%2022.32.09.jpeg)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Screenshot%202021-02-26%20160537.png)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Use%20case.jpeg)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Sequence%20diagram%201.jpeg)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Sequence%20diagram%202.jpeg)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Sequence%20diagram%203.jpeg)
![alt text](https://github.com/tanwailiang97/server_py/blob/master/Sequence%20diagram%204.jpeg)
