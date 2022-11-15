# notes
## Tips for running the app :
- run those commands after cloning the program files and activating the virtual environment.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Authorization :
> Django-Rest-Knox third party package is used for Authorization in this API. Then you have to include a valid  Token in requests headers if you wish to ```retrive, list, add or delete``` a note.
### 1. Getting the Token:
there is two ways to get a valid Token :
1. **Login :**
- the endpoint for logging in is ```api/login/```
- Make a POST request to that endpoint, your should use this format in your JSON request body : 
```
{
  "username":"<your_username>",
  "password":"<your_password>"
}
```
- the Response should be like that :
```
{
    "expiry": "<Token_expiry_date>",
    "token": "<your_Token>"
}
```
2. **Registering :**
- the endpoint for registering a new account is ```api/register/```
- Make a POST request to that endpoint, your should use this format in your JSON request body : 
```
{
  "username":"<your_username>",
  "email":"<your_email>",
  "first_name":"<your_first_name>",
  "last_name":"<your_last_name>",
  "password":"<your_password>"
}
```
- the Response should be like that :
```
{
    "user": {
        "id": <user_id>,
        "username": "<user_name>",
        "email": "<user_email>"
    },
    "token": "<your_Token>"
}
```
## Using the API :
> All of the following endpoints requires a Token for Authorizing the user, you should add an Authorization header and use this format :
```
Token <your_Token>
```
### 1. Listing all the notes:
- the endpoint is ```api/notes/```
- Make a GET request to that endpoint, your should see a Response like that : 
```
[
    {
        "id": <note_id>,
        "title": "<note_title>",
        "content": "<note_content>",
        "date": "<note_date>",
        "author": <user_id>
    }
    
    ....
    
]
```
> in order to retrive one note by its id you could use Query params for id key, the url format should be like this : ```http://127.0.0.1:8000/api/notes/?id=<id_num>```
### 1. Adding a note:
- the endpoint is ```api/notes/```
- Make a POST request to that endpoint, your should use this format in your JSON request body : 
```
[
    {
        "title": "<note_title>",
        "content": "<note_cntent>"
    }
]
```
> date and author is detrmined by the system and added to the object.

- the Response should be like that :
```
[
    {
        "id": <note_id>,
        "title": "<note_title>",
        "content": "<note_cntent>",
        "date": "2022-11-15",
        "author": <user_id>
    }
]
```
### 1. Deleting a note:
- the endpoint is ```api/notes/?id=<note_id>```
- Make a DELETE request to that endpoint, your should see a Response like that : 
```
"Done"
```
> if you don't specify in query params the note_id that you want to delete, the system will delete all the user's notes by default.
