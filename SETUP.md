# Setup & Testing Guide

## Quick Start (Development)

### On Windows/macOS (for testing):
```bash
pip install -r requirements.txt
python main.py
```

**Note**: To exit during testing, use Ctrl+Alt+Delete (on Windows) or Alt+F4 may not work—use the hotkey or force-quit.

### On Linux/Raspberry Pi (target platform):
```bash
# Install dependencies
sudo apt-get update
sudo apt-get install python3 python3-tk python3-pip

# Install Python package dependencies
pip install -r requirements.txt

# Run the application
python3 main.py
```

## Building Standalone Executable (Linux/Debian)

```bash
# Install PyInstaller
pip install pyinstaller

# Run the build script
chmod +x build.sh
./build.sh
```

This creates `dist/screenlock` — a standalone executable that requires no Python installation.

### Installing as System Service

To make the screenlock run at system startup:

```bash
# Copy executable to system path
sudo cp dist/screenlock /usr/local/bin/screenlock
sudo chmod +x /usr/local/bin/screenlock

# Create systemd service file
sudo nano /etc/systemd/system/screenlock.service
```

Add this content:
```ini
[Unit]
Description=Simple Screenlock UI
After=graphical-session-started.target
PartOf=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/local/bin/screenlock
Restart=on-failure

[Install]
WantedBy=graphical-session.target
```

Then enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable screenlock
sudo systemctl start screenlock
```

## Default Credentials

- **Username**: `admin`
- **Password**: `admin`

### Changing Credentials

Edit `credentials.txt` directly:
```
newusername
hashed_password_here
```

Or use Python to hash a new password:
```python
import hashlib
password = input("Enter new password: ")
hashed = hashlib.sha256(password.encode()).hexdigest()
print(f"Username: {input('Username: ')}")
print(f"Password hash: {hashed}")
```

Then update `credentials.txt` with the hashed password.

## Features & Controls

| Feature | Control |
|---------|---------|
| Login | Enter username & password, press Enter or click Unlock |
| Admin Override | **Ctrl+Alt+Delete** (held simultaneously) |
| Exit | Valid login or Ctrl+Alt+Delete |
| Prevent Close | Escape, Alt+F4, and window close button are disabled |

## Troubleshooting

### Application doesn't go fullscreen
- Ensure you're running on Linux with a display manager
- Test: `DISPLAY=:0 python3 main.py`

### Hotkey detection not working
- On Linux, the application needs proper permissions
- Try: `python3 main.py` with elevated privileges if needed

### Can't exit the application
- Use **Ctrl+Alt+Delete** (the intended exit method)
- On development machine, use force-quit (Ctrl+C in terminal, or task manager)

### Credentials file not created
- Ensure write permissions in the application directory
- Manual creation: Create `credentials.txt` with:
  ```
  admin
  8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
  ```
  (This is the SHA256 hash of "admin")

## Testing Checklist

- [ ] Application starts in fullscreen
- [ ] Can enter username and password
- [ ] Invalid credentials show error message
- [ ] Valid credentials (admin/admin) unlock screen
- [ ] Escape key doesn't close application
- [ ] Alt+F4 doesn't close application
- [ ] Window close button is disabled or ineffective
- [ ] Ctrl+Alt+Delete unlocks screen immediately
- [ ] On exit, credentials.txt is created in app directory

## Next Steps

1. Test on target Raspberry Pi / Debian system
2. Configure auto-launch on system startup
3. Set custom credentials
4. Deploy as system-wide executable
5. Integrate with PAM for system authentication (advanced)
