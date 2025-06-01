from tkinter import Tk
from views.login_user_view import LoginView

def main():
    root = Tk()
    LoginView(root)
    root.mainloop()

if __name__ == '__main__':
    main()