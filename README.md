# Sec-tools
Python security tools for learning cloud security - scans HTTP security headers, checks URL status and information leaks, and analyzes logs. Built with Python, requests, and socket.  Learning path: Python - Linux - Networking - AWS

### 1. file_reader.py
Smart file handler that safely reads files. If file doesn't exist, it auto-creates it. Supports JSON, CSV, and TXT formats.

**Features:**
- Auto-detects file type
- Creates missing files to prevent crashes
- Handles JSON, CSV, TXT
- Error handling for safe operation

**Usage:**
python smart_file_handler.py
