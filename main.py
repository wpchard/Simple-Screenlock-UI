#!/usr/bin/env python3
"""
Simple Screenlock UI - Full-screen login screen for Debian/Linux systems
Locks the screen and requires login credentials to unlock
Ctrl+Alt+Delete bypasses the login
"""

import tkinter as tk
from tkinter import messagebox
import hashlib
import os
from pathlib import Path
from pynput import keyboard

class ScreenLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Lock")
        
        # Make window fullscreen and always-on-top
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # Prevent closing window with keyboard shortcuts
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        
        # Bind Escape and Alt+F4 to do nothing
        self.root.bind('<Escape>', lambda e: 'break')
        self.root.bind('<Alt-F4>', lambda e: 'break')
        
        # Set background
        self.root.configure(bg='#1a1a1a')
        
        # Hotkey tracking for Ctrl+Alt+Delete
        self.keys_pressed = set()
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()
        
        self.create_ui()
        self.load_credentials()
        
    def create_ui(self):
        """Create the login screen UI"""
        # Center frame
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Title
        title = tk.Label(
            main_frame,
            text="System Locked",
            font=("Arial", 48, "bold"),
            bg='#1a1a1a',
            fg="#fafafa"
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            main_frame,
            text="Enter credentials to unlock",
            font=("Arial", 16),
            bg='#1a1a1a',
            fg='#cccccc'
        )
        subtitle.pack(pady=10)
        
        # Username label and entry
        username_label = tk.Label(
            main_frame,
            text="Username:",
            font=("Arial", 14),
            bg='#1a1a1a',
            fg='#ffffff'
        )
        username_label.pack(pady=(30, 5))
        
        self.username_entry = tk.Entry(
            main_frame,
            font=("Arial", 14),
            width=30,
            bg='#333333',
            fg='#ffffff',
            insertbackground='#ffffff'
        )
        self.username_entry.pack(pady=5, ipady=10)
        self.username_entry.focus()
        
        # Password label and entry
        password_label = tk.Label(
            main_frame,
            text="Password:",
            font=("Arial", 14),
            bg='#1a1a1a',
            fg='#ffffff'
        )
        password_label.pack(pady=(20, 5))
        
        self.password_entry = tk.Entry(
            main_frame,
            font=("Arial", 14),
            width=30,
            show="•",
            bg='#333333',
            fg='#ffffff',
            insertbackground='#ffffff'
        )
        self.password_entry.pack(pady=5, ipady=10)
        self.password_entry.bind('<Return>', lambda e: self.attempt_login())
        
        # Login button
        login_button = tk.Button(
            main_frame,
            text="Unlock",
            font=("Arial", 14, "bold"),
            bg='#0078d4',
            fg='#ffffff',
            width=20,
            command=self.attempt_login,
            activebackground='#106ebe',
            activeforeground='#ffffff'
        )
        login_button.pack(pady=30)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            bg='#1a1a1a',
            fg='#ff4444'
        )
        self.status_label.pack(pady=10)
        
    def load_credentials(self):
        """Load stored credentials or use defaults"""
        self.credentials_file = Path(__file__).parent / "credentials.txt"
        
        if self.credentials_file.exists():
            with open(self.credentials_file, 'r') as f:
                lines = f.readlines()
                self.stored_username = lines[0].strip() if len(lines) > 0 else "admin"
                self.stored_password = lines[1].strip() if len(lines) > 1 else self.hash_password("admin")
        else:
            self.stored_username = "admin"
            self.stored_password = self.hash_password("admin")
            self.save_credentials()
    
    def save_credentials(self):
        """Save credentials to file"""
        with open(self.credentials_file, 'w') as f:
            f.write(f"{self.stored_username}\n")
            f.write(f"{self.stored_password}\n")
    
    def hash_password(self, password):
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def attempt_login(self):
        """Validate login credentials"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == self.stored_username and self.hash_password(password) == self.stored_password:
            self.unlock_screen()
        else:
            self.status_label.config(text="Invalid username or password", fg='#ff4444')
            self.password_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.username_entry.focus()
    
    def unlock_screen(self):
        """Unlock the screen and exit"""
        self.listener.stop()
        self.root.quit()
    
    def on_key_press(self, key):
        """Track key presses for hotkey detection"""
        try:
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.keys_pressed.add('ctrl')
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                self.keys_pressed.add('alt')
            elif key == keyboard.Key.delete:
                self.keys_pressed.add('delete')
        except AttributeError:
            pass
        
        # Check for Ctrl+Alt+Delete
        if self.keys_pressed == {'ctrl', 'alt', 'delete'}:
            self.unlock_screen()
    
    def on_key_release(self, key):
        """Track key releases"""
        try:
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.keys_pressed.discard('ctrl')
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                self.keys_pressed.discard('alt')
            elif key == keyboard.Key.delete:
                self.keys_pressed.discard('delete')
        except AttributeError:
            pass
    
    def prevent_close(self):
        """Prevent window from being closed"""
        pass

def main():
    root = tk.Tk()
    app = ScreenLockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
