# DS171_HexaGeeks
"E-Daftar" is Multi-platform Portal for digitizing the official process of papers in colleges/government offices.

The infrastructure is defined as follows:
- Database & REST API Server
- WebApp
- Android App

# API Documentation for Server

# Signup API
Registers user/authority to the platform and generates its user ID.

**API URL**: `<host>/auth/signup`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
	"email": "test@gmail.com",
	"password": "testtest",
	"first_name": "Test",
	"last_name": "Test",
	"dob": "01/06/2000",
        "role": "user"
}
```
**Validations done**:
- `password` cannot be less than 6 characters

**Response Header**: `JSON`
```
{
    "id": "5e79e24cd4765dd448ef1454"
}
``` 
User id will be generated and returned in the response.

# Login API
Generates a session of 6 hours for the user using Authorized token.

**API URL**: `<host>/auth/login`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
	"email": "test@gmail.com",
	"password": "testtest"
}
```

**Response Header**: `JSON`
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODUwNDYzODEsIm5iZiI6MTU4NTA0NjM4MSwianRpIjoiODFkN2ZlNmEtYzU2Yi00N2Y1LWExYjItZDAyODZkMmVlNDQwIiwiZXhwIjoxNTg1MDY3OTgxLCJpZGVudGl0eSI6eyJfaWQiOnsiJG9pZCI6IjVlNzllMjRjZDQ3NjVkZDQ0OGVmMTQ1NCJ9LCJlbWFpbCI6Im1hbnNkam90IiwiZmlyc3RfbmFtZSI6Ik1hbmpvdCIsImxhc3RfbmFtZSI6IlNpZGh1IiwicGFzc3dvcmQiOiIkMmIkMTIkYUlOVHpyT09TQkNseDdCTy5vUnZZLjIzVVk4SktUNU5qWkY5bXF5RllYMFVGSHlmaU5Tdm0iLCJkb2IiOiIwMS8wNi8yMDAwIiwicm9sZSI6InVzZXIiLCJwcml2YXRlX2tleSI6Ii0tLS0tQkVHSU4gRUMgUFJJVkFURSBLRVktLS0tLVxuTUhRQ0FRRUVJRHU3QW45MEd2QjU3SjlKUXlqNlg4TDZjYjJpOWxuc253Z04rOU9rM25TWm9BY0dCU3VCQkFBS1xub1VRRFFnQUVkdkJuNDRZemdmbkN3M0laWVVuZXY3cjJkVG95ZnFaZ0laUkRMdkpxMmJnaXdnc0t0bEZyanFralxudktzL3k4eElkVUdkWjYrVlBFRnZydTdsd0QvbHdRPT1cbi0tLS0tRU5EIEVDIFBSSVZBVEUgS0VZLS0tLS1cbiIsInB1YmxpY19rZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUZZd0VBWUhLb1pJemowQ0FRWUZLNEVFQUFvRFFnQUVkdkJuNDRZemdmbkN3M0laWVVuZXY3cjJkVG95ZnFaZ1xuSVpSREx2SnEyYmdpd2dzS3RsRnJqcWtqdktzL3k4eElkVUdkWjYrVlBFRnZydTdsd0QvbHdRPT1cbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLVxuIn0sImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.gmG1sqlkIRXdJZqgKPOvoL3jr5F5RS4RFnRwiIieP28"
}
``` 
A highly secured token will be generated which will be required for authentication when any type of action is performed by the user/authority.

# Logout API
Blacklists and revokes the access token for the current user.

**API URL**: `<host>/auth/logout`

**Request Method**: `DELETE`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{"msg": "Successfully logged out"}
```

# User API
Returns the user details along with private and public keys.

**API URL**: `<host>/user`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
    "_id": {
        "$oid": "5e79e8896ca2120a652f7139"
    },
    "email": "mansdjot",
    "first_name": "Manjot",
    "last_name": "Sidhu",
    "password": "b$ZBGfptZ1yDDPkhhtNIdmRukdAmeUjKCrqdXUyivHMkOLrAxIQ7xfK",
    "dob": "01/06/2000",
    "role": "user",
    "private_key": "-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIPkAhCDboABLILmm6q5f9GQcc+ih53pPfQfaBdkYyDGToAcGBSuBBAAK\noUQDQgAE/ncmx5RvOCRLO1CNK3Ftj50ut5XuCH1NV7a2xFEFNkgkO+USyiR8PHGN\nJ1fowbwlHj91Fkb+fTsKVbt0tyKArw==\n-----END EC PRIVATE KEY-----\n",
    "public_key": "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE/ncmx5RvOCRLO1CNK3Ftj50ut5XuCH1N\nV7a2xFEFNkgkO+USyiR8PHGNJ1fowbwlHj91Fkb+fTsKVbt0tyKArw==\n-----END PUBLIC KEY-----\n"
}
``` 

# Form API
This API will fetch all the stored forms by the authorities.

**API URL**: `<host>/form`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
[
    {
        "_id": {
            "$oid": "5f2180ebcc0048229f690d5e"
        },
        "creator": "5f217905cc0048229f690d59",
        "title": "Leave Form",
        "description": "This is a test form 1",
        "fields": [
            {
                "name": "First Name",
                "type": "text",
                "isRequired": true
            },
            {
                "name": "Last Name",
                "type": "text"
            }
        ]
    },
    {
        "_id": {
            "$oid": "5f21ad26b972291c17029241"
        },
        "creator": "5f217abfcc0048229f690d5b",
        "title": "Test 1",
        "description": "Test Description",
        "fields": [
            {
                "type": "radio",
                "question": "Yes or NO",
                "options": {
                    "1": "Yes",
                    "2": "No",
                    "3": "Maybe"
                }
            }
        ]
    },
    {
        "_id": {
            "$oid": "5f21ae2cb972291c17029242"
        },
        "creator": "5f217abfcc0048229f690d5b",
        "title": "Test 2",
        "description": "Test Description",
        "fields": [
            {
                "type": "checkbox",
                "question": "Sports you like",
                "options": {
                    "1": "Cricket",
                    "2": "Football"
                }
            },
            {
                "type": "Date",
                "question": "Date Of Birth"
            },
            {
                "type": "long_answer",
                "question": "Tell something about you."
            }
        ]
    },
    {
        "_id": {
            "$oid": "5f21b11a6932434e5fe5ffd3"
        },
        "creator": "5f217abfcc0048229f690d5b",
        "title": "Custom Form",
        "description": "Custom Form Description",
        "fields": [
            {
                "type": "radio",
                "question": "Is it hot or cold?",
                "options": {
                    "1": "Hot",
                    "2": "Cold"
                }
            },
            {
                "type": "checkbox",
                "question": "Sports you like",
                "options": {
                    "1": "Cricket",
                    "2": "Football",
                    "3": "Basketball",
                    "4": "None of the above"
                }
            },
            {
                "type": "Date",
                "question": "Date of birth"
            },
            {
                "type": "long_answer",
                "question": "Tell something about yourself."
            }
        ]
    },
    {
        "_id": {
            "$oid": "5f21bd226932434e5fe5ffd9"
        },
        "creator": "5f217abfcc0048229f690d5b",
        "title": "Test1",
        "description": "Test from heroku server",
        "fields": [
            {
                "type": "radio",
                "question": "Is it working?",
                "options": {
                    "1": "Yes",
                    "2": "No"
                }
            },
            {
                "type": "Email",
                "question": "Enter your Email."
            }
        ]
    }
]
``` 


# Form POST API
Stores the digital form in the database and returns generated id that can be used in Form GET API.

**API URL**: `<host>/form`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Request Header**: `JSON`
```
{
	"name": "Leave Form Application",
	"formId": "5f2180ebcc0048229f690d5e",
	"workflowId": "5f2180a4440db770449df8d4"
}
```

**Response Header**: `JSON`
```
{
    "id": "5e7cb42ec13149e20fbd4fa5"
}
``` 

# Form GET API
Returns the form details for a given form `id`.

**API URL**: `<host>/form/<id>`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
    "_id": {
        "$oid": "5e7cb23ecc5f7717dd5ed4ee"
    },
    "creator": "Manjot",
    "title": "Test Form 1",
    "description": "This is a test form 1",
    "fields": [
        {
            "name": "First Name",
            "type": "text",
            "isRequired": true
        },
        {
            "name": "Last Name",
            "type": "text"
        }
    ]
}
``` 
# Workflow API
A workflow defines how the form will be circulated during the signature process.
It retrieves all the workflows which are uploaded by any of the authorities.

**API URL**: `<host>/workflow`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
[
    {
        "_id": {
            "$oid": "5ed397d80c0121bee03eaf49"
        },
        "name": "Leave Form 1",
        "creatorId": "5e8e016a0b65fe342bf54f56",
        "timestamp": {
            "$date": 1590925272813
        },
        "totalStages": 3,
        "stages": [
            {
                "authId": "test-authority-id1",
                "authName": "Test Authority 1",
                "name": "Class Teacher"
            },
            {
                "authId": "test-authority-id2",
                "authName": "Test Authority 2",
                "name": "HoD"
            },
            {
                "authId": "test-authority-id3",
                "authName": "Test Authority 3",
                "name": "Dean"
            }
        ]
    },
    {
        "_id": {
            "$oid": "5ed397f80c0121bee03eaf4a"
        },
        "name": "Leave Form 2",
        "creatorId": "5e8e016a0b65fe342bf54f56",
        "timestamp": {
            "$date": 1590925304868
        },
        "totalStages": 1,
        "stages": [
            {
                "authId": "test-authority-id1",
                "authName": "Test Authority 1",
                "name": "Class Teacher"
            }
        ]
    }
]
``` 

# Workflow GET API
Retrieves the specific workflow by `id` which is uploaded by the authority.

**API URL**: `<host>/workflow/<workflow-id>`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
  "name": "Leave Form 2",
  "creatorId": "5e8e016a0b65fe342bf54f56",
  "totalStages": 1,
  "stages": [
    {
      "authId": "test-authority-id1",
      "authName": "Test Authority 1",
      "name": "Class Teacher"
    }
  ]
}
``` 

# Workflow POST API <i>`AUTHORITY ONLY`</i>
Authority can create a new workflow for the applications and form.

**API URL**: `<host>/workflow`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Request Header**: `JSON`
```
{
  "name": "Leave Form 1",
  "creatorId": "5e8e016a0b65fe342bf54f56",
  "totalStages": 3,
  "stages": [
    {
      "authId": "test-authority-id1",
      "authName": "Test Authority 1",
      "name": "Class Teacher"
    },
    {
      "authId": "test-authority-id2",
      "authName": "Test Authority 2",
      "name": "HoD"
    },
    {
      "authId": "test-authority-id3",
      "authName": "Test Authority 3",
      "name": "Dean"
    }
  ]
}
``` 

**Response Header**: `JSON`
```
{
    "id": "5ed397d80c0121bee03eaf49"
}
``` 
# Application API
For Users, it returns all the applications created by the user.
For Authorities, it returns all the applications created by him or he is assigned authority to sign at that particular stage of workflow in any application.

**API URL**: `<host>/applications`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
[
    {
        "_id": {
            "$oid": "5edb7c64680d402206533e56"
        },
        "name": "Test Application",
        "description": "",
        "creatorId": "5e8e016a0b65fe342bf54f56",
        "templateId": "5ed51e2ae1c2735dab11f827",
        "creatorName": "Admin Ji",
        "workflowId": "5ed693cfa32a2cd03995b6d5",
        "assignedId": "5e8e016a0b65fe342bf54f56",
        "formId": "5e8e01a70b65fe342bf54f57",
        "form": {
            "First Name": "Manjot",
            "Last Name": "Sidhu"
        },
        "status": -1,
        "stage": 0,
        "stages": 2,
        "timestamp": {
            "$date": 1591442532138
        },
        "hash": {
            "creatorId": "5e8e016a0b65fe342bf54f56",
            "templateId": "5ed51e2ae1c2735dab11f827",
            "workflowId": "5ed693cfa32a2cd03995b6d5",
            "formId": "5e8e01a70b65fe342bf54f57",
            "form": {
                "First Name": "Manjot",
                "Last Name": "Sidhu"
            }
        },
        "signatures": [
            "",
            ""
        ],
        "message": "Not good"
    }
]
```

**Supported Arguments**:

| Argument | Value                               | Description                               |
|:--------:|:-----------------------------------:|:-----------------------------------------:|
| filter   | `signed` or `pending` or `rejected` | Filters applications based on the status. |
| limit    | `integer`                           | Limits applications to be returned.       |   


# Application GET API
Retrieves the specific application which is created by the user or the user is assigned to the application.

**API URL**: `<host>/applications/<id>`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
    "_id": {
        "$oid": "5edb7c64680d402206533e56"
    },
    "name": "Test Application",
    "description": "",
    "message": "Not good",
    "creatorId": "5e8e016a0b65fe342bf54f56",
    "templateId": "5ed51e2ae1c2735dab11f827",
    "creatorName": "Admin Ji",
    "workflowId": "5ed693cfa32a2cd03995b6d5",
    "assignedId": "5e8e016a0b65fe342bf54f56",
    "formId": "5e8e01a70b65fe342bf54f57",
    "form": {
        "First Name": "Manjot",
        "Last Name": "Sidhu"
    },
    "status": -1,
    "stage": 0,
    "stages": 2,
    "timestamp": {
        "$date": 1591442532138
    },
    "hash": {
        "creatorId": "5e8e016a0b65fe342bf54f56",
        "templateId": "5ed51e2ae1c2735dab11f827",
        "workflowId": "5ed693cfa32a2cd03995b6d5",
        "formId": "5e8e01a70b65fe342bf54f57",
        "form": {
            "First Name": "Manjot",
            "Last Name": "Sidhu"
        }
    },
    "signatures": [
        "",
        ""
    ]
}
``` 

# Application POST API
To create an application using template id.

**API URL**: `<host>/applications`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Request Header**: `JSON`
```
{
	"name": "Test Application",
	"templateId": "5ed51e2ae1c2735dab11f827",
	"form": {
		"First Name": "Manjot",
		"Last Name": "Sidhu"
	}
}
``` 

**Response Header**: `JSON`
```
{
    "id": "5ed6942f6a1eb8977b979bf3"
}
``` 


# Application Templates API
Returns all the templates created by the authorities from which users can create Applications.

**API URL**: `<host>/applications/templates`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
[
    {
        "_id": {
            "$oid": "5ed51e2ae1c2735dab11f827"
        },
        "name": "Leave Form",
        "creatorId": "5e8e016a0b65fe342bf54f56",
        "creatorName": "Admin Ji",
        "workflowId": "5ed693cfa32a2cd03995b6d5",
        "formId": "5e8e01a70b65fe342bf54f57",
        "stages": 3,
        "timestamp": {
            "$date": 1591025194854
        }
    }
]
```

# Application Templates GET API
Retrieves the specific template which is created by the authority.

**API URL**: `<host>/applications/templates/<id>`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
    "_id": {
        "$oid": "5ed51e2ae1c2735dab11f827"
    },
    "name": "Leave Form",
    "creatorId": "5e8e016a0b65fe342bf54f56",
    "creatorName": "Admin Ji",
    "workflowId": "5ed693cfa32a2cd03995b6d5",
    "formId": "5e8e01a70b65fe342bf54f57",
    "stages": 1,
    "timestamp": {
        "$date": 1591025194854
    }
}
``` 

# Application Templates POST API <i>`AUTHORITY ONLY`</i>
To create template for an application using workflow id and form id.

**API URL**: `<host>/applications/templates`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Request Header**: `JSON`
```
{
  "name": "Leave Form",
  "workflowId": "test-workflow-id",
  "formId": "test-form-id"
}
``` 

**Response Header**: `JSON`
```
{
    "id": "5ed51e2ae1c2735dab11f827"
}
``` 

# Signing API
Authority can use this API to either sign a application or reject it with an optional message.

**API URL for Signing**: `<host>/applications/<doc-id>/sign`

**API URL for Rejecting**: `<host>/applications/<doc-id>/reject`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

To send a optional message while rejecting :

**Request Header**: `JSON`

**Request Body**: 

```
{
    "message": "Please specify correct address",
}
```

# Storage API
Retrieves all the documents which are uploaded by the user or shared to him.

**API URL**: `<host>/storage`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
[
    {
        "_id": {
            "$oid": "5ea91d61fd975a009bf1f76d"
        },
        "creator": "5e8eb5e798dbf873a992643c",
        "file": "5e8eb5e798dbf873a992643c_20200429-115329.txt",
        "fileExtension": "txt",
        "fileName": "Test name",
        "fileDescription": "test desc",
        "visibility": "private",
        "timestamp": {
            "$date": 1588141409476
        }
    }
]
``` 

**Supported Arguments**:

| Argument | Value  | Description                                  |
|:--------:|:------:|:--------------------------------------------:|
| limit    | number | Limits to number of documents to be returned |   

# Storage GET API
Retrieves the specific document which is uploaded by the user or shared to him.

**API URL**: `<host>/storage/<document-id>`

**Request Method**: `GET`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Response Header**: `JSON`
```
{
    "_id": {
        "$oid": "5ea91d61fd975a009bf1f76d"
    },
    "creator": "5e8eb5e798dbf873a992643c",
    "file": "5e8eb5e798dbf873a992643c_20200429-115329.txt",
    "fileExtension": "txt",
    "fileName": "Test name",
    "fileDescription": "test desc",
    "visibility": "private",
    "timestamp": {
        "$date": 1588141409476
    }
}
``` 

**Supported Arguments**:

| Argument | Value  | Description                      |
|:--------:|:------:|:--------------------------------:|
| download | N/A    | Downloads the specified document |   

# Storage POST API
Used to store a document by the user.

> NOTE: Allowed file extensions are: pdf, png, jpg, jpeg

**API URL**: `<host>/storage`

**Request Method**: `POST`

**Authorization Type**: `Bearer Token`

**Authorization Token**: `<user-token-obtained-on-login>`

**Request Header**: `form-data`
```
{
    'file': <selected-file-from-form>,
    'fileName': 'Test File',
    'fileDescription': 'This is my test file',
    'visibility': 'public'

}
``` 

**Response Header**: `JSON`
```
{
    "id": "5e7cb42ec13149e20fbd4fa5"
}
``` 
