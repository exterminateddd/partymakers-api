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
Response 200
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
Response 200
```json
{
  "success": true,
  "msg": "Login Successful"
}
```
## User control `/user`
#### GET `/get_user_data/<string:username>`
Request
```json
"/<username>"
```
Response 200
```json
{
  "success": true,
  "msg": "Successfully retrieved user data.",
  "data": {
    **userOpenData
  }
}
```
Response 403
```json
{
    "success": false,
    "msg": "Not Authorized"
}
```
#### GET `/get_all_users`
Request
```json
"/"
```
Response 200
```json
{
  "success": true,
  "msg": "Successfully retrieved all users",
  "data": [{}, {}]
}
```
Response 403
```json
{
    "success": false,
    "msg": "Not Authorized"
}
```
#### GET `/get_user_bookmarked_parties/<string:username>`
Request
```json
"/<username>"
```
Response 200
```json
{
  "success": true,
  "msg": "Successfully retrieved bookmarked parties",
  "data": [{}, {}]
}
```
Response 403
```json
{
    "success": false,
    "msg": "Not Authorized"
}
```
