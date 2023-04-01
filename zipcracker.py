import zipfile
import threading
import os


# משתנה גלובלי שבודק אם מצאנו סיסמה
password_found = False

# פונקציה שמנסה כל פעם לפפתוח קובץ עם סיסמה בודדת
def open_zip(zip_path, password):
    try:
        # מנסה לפתוח את הקובץ עם הסיסמה ומדפיס הודעה אם הצליח
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(pwd=password.encode())
            password_found = True
            print(f"Password found: {password}")

    except Exception as e:
        # הסיסמה לא התאימה
        pass


def get_files():
    # מבקש כתובת של קובץ זיפ ובודק אם היא קיימת
    zippath = input("Enter the zip filename: ")
    while True:
        if os.path.exists(zippath):
            break
        else:
            print("The zip does not exist")
            zippath = input("Enter the zip filename: ")
    passwordpath = input("Enter the filename with the passwords: ")

    # מבקש כתובת של קובץ סיסמאות ושומר כל שורה כסיסמה
    while True:
        if os.path.exists(passwordpath):
            with open(passwordpath, "r") as f:
                lines = [line.strip() for line in f.readlines()]
            break
        else:
            print("The file does not exist")
            passwordpath = input("Enter the filename with the passwords: ")
    return zippath, lines

# פונקציה ראשית
def main():
    # מאתחל כתובת של זיפ ורשימת סיסמאות
    zip_file, password_list = get_files()
    # יוצר תהליכים
    threads = []
    for password in password_list:
        thread = threading.Thread(target=open_zip, args=(zip_file, password))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if not password_found:
        print("No password found.")

if __name__ == '__main__':
    # קורא לפונקציה ראשית
    main()