import pyodbc
conn=pyodbc.connect('DRIVER=SQL SERVER;SERVER=LAPTOP-HLCPCTCT\SQLEXPRESS01;DATABASE=python;')
 


import uvicorn
from fastapi import FastAPI ,Response
from fastapi.responses import HTMLResponse,FileResponse

app=FastAPI()



@app.get("/insert_data")

def insert_table(empid,empname,department,salary,experience):
    result=conn.execute(f"insert into Employee values({empid} ,'{empname}','{department}',{salary},{experience})")
    result.commit()
    return FileResponse('submission.html')
    



@app.get("/delete_data")
def emp_delete(id):
    result=conn.execute(f"delete from Employee where id={id}")
    result.commit()
    return FileResponse('deletion.html')
    
 

@app.get("/employee_data")
def emp_value_insert():
    exe=conn.execute('select * from Employee')
    data=exe.fetchall()
    data=str(data)
    return {"employee":data}



if __name__=='__main__':
    uvicorn.run(app=app,host='127.0.0.1',port=8090)



 
