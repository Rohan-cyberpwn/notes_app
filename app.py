import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("USER_NAME", "Guest")

note = input("Enter a note: ")

with open("notes.txt", "a") as f:
    f.write(f"{USER}: {note}\n")

print("Note saved.")
