#!/bin/bash
# Build script for creating a standalone executable for Debian/Linux systems

echo "Building Simple Screenlock UI..."

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip install pyinstaller
fi

#python -m PyInstaller --onefile --windowed --name screenlock main.py
# Create the executable
echo "Creating executable..."
pyinstaller --onefile \
    --windowed \
    --name screenlock \
    --icon=icon.png \
    --add-data "README.md:." \
    main.py

# Check build result
if [ -f "dist/screenlock" ]; then
    echo "✓ Build successful!"
    echo "Executable created at: dist/screenlock"
    echo ""
    echo "To run the application:"
    echo "  ./dist/screenlock"
    echo ""
    echo "To install system-wide:"
    echo "  sudo cp dist/screenlock /usr/local/bin/"
    echo "  sudo chmod +x /usr/local/bin/screenlock"
else
    echo "✗ Build failed"
    exit 1
fi
