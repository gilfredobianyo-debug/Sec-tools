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

### 2. LinkSweep (linksweep.py)
A simple website link checker that finds broken links for bug bounty recon.

**What it does:**
- Takes a website URL as input
- Crawls all anchor tags `<a href>`
- Checks each external link's HTTP status
- Reports Working (200) vs Broken (404)

**Usage:**
```bash
python linksweep.py
Enter a website url: books.toscrape.com
