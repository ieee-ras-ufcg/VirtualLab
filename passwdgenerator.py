import bcrypt
import secrets

password = b'luizfeio'
hash_passwd = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"Stored Hash: {hash_passwd.decode()}")

passwdinput = b'pi-e=0.42'

if bcrypt.checkpw(passwdinput, hash_passwd):
    print("Welcome to IEEE RAS UFCG Virtual Lab! Redirecting...")
else:
    print("Access Denied. Try again.")

print(secrets.token_hex(32))