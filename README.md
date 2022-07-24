# booksite
Library-book search application

Author: Kilic Arslan
Date:   20.6.2021
Description:  A standard library book searcher  that gets documents via the 
command manager and gives the output from the book-opinion tables.



After setting and activating virtual env, remember to install necessary packages.
**pip install -r requirements.txt**


NOTE1: Due to foreign key dependency,  
book instance of csv file should be uploaded before the opinion instance csv file.

**python manage.py import_csv --books books.csv**
**python manage.py import_csv --opinions opinions.csv**
**python manage.py runserver**


NOTE2: Csv files should be put in the directory :  **".../management"**
Ps: For seeing API views, check urls  '/booksapi/'   and '/opinionsapi/'

---------------------------------------------------------------------------
