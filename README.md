# customer_info_api
## Description
This is a backend API that is used to manage customer information. The data collected includes the following details:
1. Customer Name
2. Contact Information (Phone and Email)
3. Date of Birth
4. Nationality
5. Business Name
6. Business Categories (e.g., Fintech, Learning Institution, Transportation, etc.)
7. Business Registration Date
8. Age of the Business (calculated up to the current date)
9. Location Information (e.g., County, Sub-county, Ward, Building Name, and Floor)

## Tools and Technologies Used
- Django
- Django REST framework
- Django ORM
- SQLite for database​
  
## Requirements
- Python v3 and above
- pip

## Configuration
```
$ git clone https://github.com/JamesKibathi/customer_info_api/
$ pip install -r requirements.txt - Install dependencies 
$ python3 manage.py runserver - Run server

```  
Run migrations

```
$ python3 manage.py makemigrations
$ python3 migrate

```
