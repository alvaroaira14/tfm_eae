import os
from create_database import create_database


if __name__ == "__main__":
    try:
        os.system(r"./myenv/Scripts/activate")
        os.system("pip install -r requirements.txt")
        print("\n--Paquetes instalados correctamente--")
    except Exception as e:
        print("An error occurred while installing packages:", e)

    create_database()   
