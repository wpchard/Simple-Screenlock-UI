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

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

Or make it executable and run directly:
```bash
chmod +x main.py
./main.py
```

## Usage

### Normal Login
1. Application starts in full-screen mode
2. Enter username and password
3. Press Enter or click "Unlock" button
4. If credentials are correct, screen unlocks and application exits

### Admin Override
Press **Ctrl+Alt+Delete** simultaneously to bypass the login and unlock the screen immediately.

## Default Credentials

- **Username**: admin
- **Password**: admin

**Important**: Change these credentials by editing the `credentials.txt` file or implementing a management interface.

## Credential Storage

Credentials are stored in `credentials.txt` in the following format:
```
username
hashed_password
```

Passwords are hashed using SHA256 for basic security.

## Building as Executable

To create a standalone executable for distribution on Debian/Linux systems:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

This will create a standalone executable in the `dist/` directory that can be run without Python installed.

## Project Structure

```
Simple Screenlock UI/
├── main.py              # Main application
├── requirements.txt     # Python dependencies
├── credentials.txt      # Stored credentials (auto-created)
└── README.md           # This file
```

## Security Notes

- Default credentials should be changed immediately
- Passwords are hashed but stored locally; consider implementing more robust authentication
- The Ctrl+Alt+Delete override is intentionally provided for system administrators
- This is a UI-level lock; for production systems, integrate with system-level authentication

## System Requirements

- **OS**: Linux (Debian-based, tested on Raspberry Pi)
- **Python**: 3.6 or higher
- **Display**: Any resolution (scales to full screen)

## Future Enhancements

- Configuration file for customizable credentials
- Lock timeout features
- Multiple user support
- System integration (PAM, etc.)
- Logging of unlock attempts
