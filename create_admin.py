#!/usr/bin/python3
"""Script to create an admin user."""
from models.storage import Storage
from models.admin import Admin
from sys import argv

if len(argv) != 3:
    print(f"Usage: {argv[0]} <username> <passkey>")
    exit(1)

storage = Storage()

username = argv[1]
passkey = argv[2]

admin = Admin(username=username, passkey=passkey)
storage.new(admin)
storage.save()
storage.close()

print("Admin Created Successfully")
