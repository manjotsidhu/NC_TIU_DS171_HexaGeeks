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
