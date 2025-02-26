from app import create_app

#import mysql.connector
#con =  mysql.connector.connect(host= 'localhost', database= 'task_manager', user='root', password='rootpassword')

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
