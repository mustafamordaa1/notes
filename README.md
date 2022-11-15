# notes
## Authorization :
> Django-Rest-Knox third party package is used for Authorization in this API. Then you have to include a valid  Token in requests headers if you wish to ```retrive, list or delete``` a note.
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
  "last_name":<your_last_name>",
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
### 1. Listin all the notes:
- the endpoint is ```api/notes/```
- Make a GET request to that endpoint, your should see a Response like that : 
```

