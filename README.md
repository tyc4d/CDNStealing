# CDNStealing

## Installation

```python
Python
pip install -r requirement.txt

Python3
pip3 install -r requirement.txt
```

## Run the application
- All-in-one startup script
   - Windows > win_runboth.bat
   - Linux > linux_runboth.sh
Which can start both Web Lookup System and User Info Fetching

## Visit Web Page
http://<IP>:8010

You may change port at web.py on line 155

## Content
- web.py -> Using Flask as main framework
  - Routes
    - / (GET)
    - /operations (GET,POST)
    - /s/<randomID> (GET)
    - /visitLogs (GET)
    - /entryLogs (GET)
    - /appendLogs (GET,POST)
- fetch.py -> Fetch Forum Data after the link being visit
  - Lookup mysql [visited] column
  - Send requests to forum to get cached user info
