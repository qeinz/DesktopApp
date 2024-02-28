import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x600")

        # Use Windows-like styling
        self.style = ttk.Style()
        self.style.theme_use('winnative')  # Change theme to 'winnative' for Windows-like appearance
        self.style.configure('TButton', padding=6, relief="flat", background="#4d4dff", foreground="white")
        self.style.map('TButton', background=[('active', '#668cff')])

        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(root)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check credentials (dummy check)
        if username == "user" and password == "password":
            self.root.destroy()
            self.open_main_window()
        else:
            # Display error message for invalid credentials
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_main_window(self):
        main_window = tk.Tk()
        main_window.title("Main Window")
        main_window.geometry("800x600")

        # Create a frame for navigation bar
        navigation_frame = tk.Frame(main_window, width=200, bg="#f0f0f0", borderwidth=0, relief="flat")
        navigation_frame.pack(side="left", fill="y")

        # Add navigation buttons with icons
        home_icon_url = "https://cdn-icons-png.flaticon.com/512/992/992684.png"
        response = requests.get(home_icon_url)
        home_icon_data = response.content
        home_icon = Image.open(io.BytesIO(home_icon_data))
        home_icon = home_icon.resize((32, 32), Image.LANCZOS)  # Resize icon to fit button
        home_icon_tk = ImageTk.PhotoImage(home_icon)

        home_button = ttk.Button(navigation_frame, text="Home", image=home_icon_tk, compound="left", style='TButton')
        home_button.image = home_icon_tk
        home_button.pack(pady=10, padx=10, anchor="w")

        profile_icon_url = "https://cdn-icons-png.flaticon.com/512/149/149071.png"
        response = requests.get(profile_icon_url)
        profile_icon_data = response.content
        profile_icon = Image.open(io.BytesIO(profile_icon_data))
        profile_icon = profile_icon.resize((32, 32), Image.LANCZOS)  # Resize icon to fit button
        profile_icon_tk = ImageTk.PhotoImage(profile_icon)

        profile_button = ttk.Button(navigation_frame, text="Profile", image=profile_icon_tk, compound="left", style='TButton')
        profile_button.image = profile_icon_tk
        profile_button.pack(pady=10, padx=10, anchor="w")

        settings_icon_url = "https://cdn-icons-png.flaticon.com/512/2942/2942139.png"
        response = requests.get(settings_icon_url)
        settings_icon_data = response.content
        settings_icon = Image.open(io.BytesIO(settings_icon_data))
        settings_icon = settings_icon.resize((32, 32), Image.LANCZOS)  # Resize icon to fit button
        settings_icon_tk = ImageTk.PhotoImage(settings_icon)

        settings_button = ttk.Button(navigation_frame, text="Settings", image=settings_icon_tk, compound="left", style='TButton')
        settings_button.image = settings_icon_tk
        settings_button.pack(pady=10, padx=10, anchor="w")

        # Create a frame for main content with a separator line
        main_content_frame = tk.Frame(main_window, bg="#ffffff", borderwidth=1, relief="sunken")
        main_content_frame.pack(side="left", fill="both", expand=True)

        # Switch between profile and settings pages
        self.profile_page = ProfilePage(main_content_frame)
        self.settings_page = SettingsPage(main_content_frame)

        main_window.mainloop()


class ProfilePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Add profile information widgets
        profile_label = ttk.Label(self, text="User Profile", font=("Helvetica", 16))
        profile_label.pack(pady=10)

        # Example profile information
        profile_info_label = ttk.Label(self, text="Username: user\nEmail: user@example.com\nProfile Picture: ", justify="left")
        profile_info_label.pack(pady=5)

        # Example profile picture (you can replace this with actual user profile picture)
        profile_pic_url = "https://via.placeholder.com/150"
        response = requests.get(profile_pic_url)
        profile_pic_data = response.content
        profile_pic = Image.open(io.BytesIO(profile_pic_data))
        profile_pic = profile_pic.resize((150, 150), Image.LANCZOS)
        profile_pic_tk = ImageTk.PhotoImage(profile_pic)

        profile_pic_label = ttk.Label(self, image=profile_pic_tk)
        profile_pic_label.image = profile_pic_tk
        profile_pic_label.pack(pady=5)

class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Add settings widgets
        settings_label = ttk.Label(self, text="Settings", font=("Helvetica", 16))
        settings_label.pack(pady=10)

        # Example settings options
        language_label = ttk.Label(self, text="Language:")
        language_label.pack(pady=5)
        language_combobox = ttk.Combobox(self, values=["English", "German", "French"])
        language_combobox.pack(pady=5)

        notification_label = ttk.Label(self, text="Notifications:")
        notification_label.pack(pady=5)
        notification_checkbox = ttk.Checkbutton(self, text="Receive notifications")
        notification_checkbox.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
