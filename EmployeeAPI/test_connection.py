from database import get_connection


connection = get_connection()


if connection.is_connected():
    print("Connected Successfully ✅")
else:
    print("Connection Failed ❌")


connection.close()
