
import base64

base64_str = "VEhNe0JBU0U2NF9FTkNPRElOR30=" # Replace with string to decode
decoded_bytes = base64.b64decode(base64_str)
print(decoded_bytes)

# Encode using base64
message = '"id":1, "admin":True' # Replace with your mess to encode
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)