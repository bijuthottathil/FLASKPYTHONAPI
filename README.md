# FLASK API to insert Employeer records in Posgres DB

![image](https://github.com/user-attachments/assets/6dd4842a-f5b0-4e62-9aca-e40bd2028ecf)

Make sure that you setup postgres db locally and setup Pgadmin to access schema like below
![image](https://github.com/user-attachments/assets/6b29488e-87a2-4659-a14b-7141d2a08174)

Schema used- Adventure
User- postgres
password-postgres
server-localhost
port-5432

Created new table in DB. We will be inserting records to this table
![image](https://github.com/user-attachments/assets/bcb91697-b31f-4c28-a988-9cbfa2b7bdc3)

Next Open VS Code  and create below file in a foder. Make sure that  python is available in envrironment. Source code is attached in git

![image](https://github.com/user-attachments/assets/986156a5-534d-4300-b157-4e03c72deb2c)


Please put proper DB configurations, based on your setup

Open Powershell

![image](https://github.com/user-attachments/assets/6425f343-6c9b-45ff-8d1c-0b2150ed4889)

Run the command -->  pip install Flask==1.1.4    ( to install flask packages)

To compile python file --> python emp_add_api.py. 

![image](https://github.com/user-attachments/assets/0e554046-a09e-4f0b-8bcd-8177846f86f1)

If API is running , you will see http://127.0.0.1:5000 and you can click this url, you will see  404 not found error in new blank page. No need to worry. API is ready to consume now


Next open a bash window
![image](https://github.com/user-attachments/assets/aa5b1fae-da0d-45b9-93a8-a0cb7e55ea24)

Run the command to execute API by passing records in JSON format.(If you are familiar with postman, you can use that too)

 curl -X POST http://127.0.0.1:5000/employees -H "Content-Type: application/json" -d '{"name": "Biju", "department": "IT", "role": "Data Engineer"}'


 ![image](https://github.com/user-attachments/assets/15feaf2e-a923-4034-850f-97cde1bc0779)


 This call will invoke API and store details in table


 ![image](https://github.com/user-attachments/assets/7ae4791f-ccfa-42d6-962d-5ef3bef7f91c)

 Check the result in Postgres DB now


 ![image](https://github.com/user-attachments/assets/f127250d-0d98-4147-b3f5-abc79d83459f)


 We are successfully called API and added entries in DB








