import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash,request
import mysql.connector

@app.route('/my',methods=['POST','GET'])
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

    
    
@app.route('/emp')
def emp():
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
        mycursor=mydb.cursor()
        SQL="SELECT id, name, email, phonenumber, password FROM myregister"
        mycursor.execute(SQL)
        empRows = mycursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        #cursor.close() 
        #conn.close()  
        pass
@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
    mycursor=mydb.cursor()
    sql="DELETE FROM myregister WHERE id =%s"
    
    mycursor.execute(sql,(id,))
    
    respone = jsonify('Employee deleted successfully!')
    respone.status_code = 200
    return respone


@app.route('/update/<int:id>',methods=['PUT'])
def update(id):
    my=int(id,)
    ids=request.json['id']
    name=request.json['name']
    email=request.json['email']
    phonenumber=request.json['phonenumber']
    password=request.json['password']

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ajay')
    mycursor=mydb.cursor()
    sql="UPDATE myregister SET name =%s,email=%s,phonenumber=%s,password=%s WHERE id =%s"
    val=(name,email,phonenumber,password,ids)
    mycursor.execute(sql,val)
    response=jsonify('updated')
    #response=jsonify(my)

    response.status_code=200
    return response







if __name__ =="__main__":
    
    app.run(debug=True)