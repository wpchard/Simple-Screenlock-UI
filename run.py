#!/usr/bin/env python3
"""
Test script to run the screenlock application
"""

import subprocess
import sys

if __name__ == "__main__":
    try:
        subprocess.run([sys.executable, "main.py"], cwd=".", check=False)
    except KeyboardInterrupt:
        print("\nApplication closed by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error running application: {e}")
        sys.exit(1)
