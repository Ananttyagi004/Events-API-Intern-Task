Setup Instructions :
 Clone the github repo: https://github.com/Ananttyagi004/Events-API-Intern-Task
 Install requirements : pip install -r requirements.txt
 Run Server : python manage.py runserver
 Admin Panel :http://127.0.0.1:8000/   Credentials:(username=admin , password=12345)

To register http://127.0.0.1:8000/register/  (METHOD=POST)
      Also add this data to the body: 
      {
    "username":"anant004",
    "password":"123456"
}

Response:
{
    "msg": "User Created",
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjI0NTg0NSwiaWF0IjoxNzEyMTU5NDQ1LCJqdGkiOiI4MjU3ODViYzQ5MGQ0YTAxYjYzYjJhZGQ5ZWJhODgyNyIsInVzZXJfaWQiOjN9.vnIvZklZ8ul9R6wZUI-yiHOVZo-IyRdxIJYq6l8iyyg",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMTYwMzQ1LCJpYXQiOjE3MTIxNTk0NDUsImp0aSI6ImIxODUwZjVlMTNiMzQzYzNiNmE5ODI3OWRiYzI2MTU2IiwidXNlcl9pZCI6M30.JMnR5RcXIa1HTXQKLHrMUQek8JRo-cv4DQ_a3c6F6tY"
    }
}

To login http://127.0.0.1:8000/login/   (METHOD=POST)
      Also add this data to the body: 
      {
    "username":"anant004",
    "password":"123456"
}

Response:
{
    "msg": "Login Success",
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjI0NTg0NSwiaWF0IjoxNzEyMTU5NDQ1LCJqdGkiOiI4MjU3ODViYzQ5MGQ0YTAxYjYzYjJhZGQ5ZWJhODgyNyIsInVzZXJfaWQiOjN9.vnIvZklZ8ul9R6wZUI-yiHOVZo-IyRdxIJYq6l8iyyg",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMTYwMzQ1LCJpYXQiOjE3MTIxNTk0NDUsImp0aSI6ImIxODUwZjVlMTNiMzQzYzNiNmE5ODI3OWRiYzI2MTU2IiwidXNlcl9pZCI6M30.JMnR5RcXIa1HTXQKLHrMUQek8JRo-cv4DQ_a3c6F6tY"
    }
}

To View http://127.0.0.1:8000/events/   (METHOD=GET)
This route has no authentication

Response:
[
    {
        "name": "Summer Beats",
        "description": "Top DJs, live performances | EDM, pop, hip-hop | English | 18+ | 8hrs",
        "date": "2024-06-20",
        "location": "Los Angeles"
    },
    {
        "name": "Summer Beats",
        "description": "Top DJs, live performances | EDM, pop, hip-hop | English | 18+ | 8hrs",
        "date": "2024-07-28",
        "location": "Los Angeles"
    }
]
To add new Task:http://127.0.0.1:8000/post/
Authorization  Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMTU3ODAwLCJpYXQiOjE3MTIxNTY5MDAsImp0aSI6IjhkODE2MWJiMGJmODQzNTFiYWI4YmJlZjkzZDJkY2UxIiwidXNlcl9pZCI6Mn0.YajQfipoWAeKw2X9sm7X-E822vg78yNnnj4hIkyCG54
Body {
    "name": "Summer Beats ",
    "description": "Top DJs, live performances | EDM, pop, hip-hop | English | 18+ | 8hrs",
    "date": "2024-07-28",
    "location": "Los Angeles"
}
Response
{
    "msg": "Event Created"
}

For Complete update, partial update and Delete http://127.0.0.1:8000/list/1
Here one is the id of data that is to be deleted.
Authorization  Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMTU3ODAwLCJpYXQiOjE3MTIxNTY5MDAsImp0aSI6IjhkODE2MWJiMGJmODQzNTFiYWI4YmJlZjkzZDJkY2UxIiwidXNlcl9pZCI6Mn0.YajQfipoWAeKw2X9sm7X-E822vg78yNnnj4hIkyCG54

Use Put for complete update
Body {
    "name": "Summer Beats ",
    "description": "Top DJs, live performances | EDM, pop, hip-hop | English | 18+ | 8hrs",
    "date": "2024-07-28",
    "location": "Los Angeles"
}

Use Patch for partial update
Body {
    "name": "Summer Beats ",
    "description": "Top DJs, live performances | EDM, pop, hip-hop | English | 18+ | 8hrs",
    "date": "2024-07-28"
    }

Use Delete method to delete an Event