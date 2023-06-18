from app import app
from flask import jsonify
import json
from flask import request
import mysql.connector
@app.route('/create',methods=['POST','GET'])
def create_emp():
    name=request.json['name']
    email=request.json['email']
    phonenumber=request.json['phonenumber']
    password=request.json['password']
    if name and email and phonenumber and password and request.method == 'POST':
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
        mycursor=mydb.cursor()
        sqlQuery="INSERT INTO myregister(name,email,phonenumber,password) VALUES(%s,%s,%s,%s)"
        val=(name,email,phonenumber,password)
        mycursor.execute(sqlQuery,val)
        mydb.commit()
        response=jsonify('Employee added successfully')
        response.status_code=200
        return response
    else:
        return jsonify('error')
    
    
@app.route('/read')
def emp():
    try:
        # command checking
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
        mycursor=mydb.cursor(dictionary=True)
        SQL="SELECT id, age, technology, experience FROM myemploys"
        mycursor.execute(SQL)
        empRows = mycursor.fetchall()
        #res=json.dump(empRows)
        respone=jsonify(empRows)
        #respone = jsonify( res)
        
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        #cursor.close() 
        #conn.close()  
        pass
@app.route('/read/<int:id>')
def reax_one(id):
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
        mycursor=mydb.cursor(dictionary=True)
        SQL="SELECT id, name, email, phonenumber, password FROM myregister WHERE id=%s"
        mycursor.execute(SQL,(id,))
        empRows = mycursor.fetchone()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
    mycursor=mydb.cursor()
    sql="DELETE FROM myregister WHERE id =%s"
    
    mycursor.execute(sql,(id,))
    mydb.commit()
 
    
    respone = jsonify('Employee deleted successfully!')
    respone.status_code = 200
    return respone
@app.route('/update/<int:id>',methods=['POST','GET'])
def update(id):
    
    
    name=request.json['name']
    email=request.json['email']
    phonenumber=request.json['phonenumber']
    password=request.json['password']
    if name and email and phonenumber and password and request.method == 'POST':
      mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
      mycursor=mydb.cursor()
      sql="UPDATE myregister SET name =%s,email=%s,phonenumber=%s,password=%s WHERE id =%s"
      val=(name,email,phonenumber,password,id)
      mycursor.execute(sql,val)
      mydb.commit()
      response=jsonify('updated')
    
     
      response.status_code=200
      return response
    else:
        return jsonify('error')
if __name__ =="__main__":
    
    app.run(port=4445,debug=True)