## Authentication `/auth`
#### **POST** `/register_user` - Registration
Request
```json
{
  "username": "",
  "password": "", // unhashed
  "firstName": "",
  "lastName": ""
}
```
Response
```json
{
  "success": true,
  "msg": "Registration Successful"
}
```
#### **POST** `/attempt_login` - Logging in
Request
```json
{
  "username": "",
  "password": "", // unhashed
  "firstName": "",
  "lastName": ""
}
```
Response
```json
{
  "success": true,
  "msg": "Login Successful"
}
```