 WhatsApp Automation Setup Guide
 
What this does

This tool:
Connects your WhatsApp Web account
Shows your group list
Adds people to selected groups
Skips users who are already in the group

 1. What you need first
✔ A computer
Windows / Mac / Linux
✔ Google Chrome installed
✔ Python installed

Download:
 https://www.python.org/downloads/

During installation:

Tick “Add Python to PATH”
 2. Install required package

Open:

Windows → Command Prompt
Mac → Terminal

Run:

pip install WPP-Whatsapp

 3. Create project folder

Create a folder like:

whatsapp-automation/

Inside it create a file:

whatsapp-conn.py

4. Copy script into whatsapp-conn.py


5. Run the script

Open terminal inside folder and run:

python whatsapp-conn.py

6. Login to WhatsApp

When script runs:

A Chrome window opens
It shows WhatsApp Web QR code

Do this:

Open WhatsApp on your phone
Tap:
Android → ⋮ → Linked Devices
iPhone → Settings → Linked Devices
Scan QR code
7. Wait for sync

After login:

Wait ~20–30 seconds
WhatsApp loads chats and groups
8. What you will see

Script will:

Show all groups
Print group names + IDs
Process selected groups

Example:

Processing group: Test-Comms
Existing members: 4
Skipping (already exists)
Added: 6588xxxxxx@c.us

9. How phone numbers must be written

No + sign
No spaces
Country code included
Ends with @c.us

10. Important limitations (very important to explain)

This system is NOT official WhatsApp API.

So:
Sometimes it may fail if:
WhatsApp Web refreshes group is restricted (community/announcement)
number is not on WhatsApp
too many adds too fast
You may see:
“Failed”
or no confirmation even if executed
11. Safety tips
Don’t add too many numbers quickly (max ~10–20/min)
Keep WhatsApp Web tab open
Don’t log out during execution
Use one session only
12. What this script is good for

✔ Small communities
✔ Internal teams
✔ Event groups
✔ Controlled onboarding
