# import nacl.secret
# import base64
# import binascii


# base64_key = "dGhpc2lzYWtleXdpdGgzMmxldHRlcnNpbml0ZmV0Y2g="
# base64_nonce = "/KSIvzD+EfD2ohTDS8YyXWfpzHjVrp1i"
# base64_encrypted_value = "/KSIvzD+EfD2ohTDS8YyXWfpzHjVrp1iMQBE3XbIMi0G/BowKduAtkW9uvBwoRDicvmeFfDvaez3xw=="

# key = base64.b64decode(base64_key)
# nonce = base64.b64decode(base64_nonce)
# encrypted_value = base64.b64decode(base64_encrypted_value)

# print(key)
# print(nonce)
# print(encrypted_value)

# box = nacl.secret.SecretBox(key)

# val = box.decrypt(encrypted_value)
# print(val)

import requests
import jwt

url = "https://prod-backend-ctf.us-east-1.prod-services.fetchrewards.com/token.v1.TokenService/StreamToken"

with requests.post(url, json={}, stream=True) as response:
    for line in response.iter_lines():
        if line:
            token_data = line.decode("utf-8")
            print("Raw Token Data:", token_data)

            try:
                # Extract token and decode
                token_json = eval(token_data)  # ⚠️ Be careful with eval, use json.loads() if possible
                token = token_json.get("token")
                decoded = jwt.decode(token, options={"verify_signature": False})  # Decode without verifying
                print("Decoded Token:", decoded)
            except Exception as e:
                print("Error decoding token:", e)
