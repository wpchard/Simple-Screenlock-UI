# Simple Screenlock UI

A full-screen login/lock screen application for Linux (Debian-based) systems, designed to lock the desktop and require login credentials to unlock.

## Features

- **Full-screen overlay** - Takes up entire screen and blocks all access to other programs
- **Login form** - Requests username and password
- **Cannot be closed normally** - Window cannot be closed with standard close buttons or keyboard shortcuts
- **Ctrl+Alt+Delete bypass** - System administrators can unlock with Ctrl+Alt+Delete hotkey combination
- **Persistent credentials** - Stores hashed credentials for future use
- **Default credentials** - Username: `admin`, Password: `admin`

## Requirements

- Python 3.6+
- Tkinter (usually included with Python)
- pynput (for global hotkey detection)


