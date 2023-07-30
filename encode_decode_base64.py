
import base64
import pickle

base64_str = "VEhNe0JBU0U2NF9FTkNPRElOR30=" # Replace with string to decode
decoded_bytes = base64.b64decode(base64_str)
print(decoded_bytes)

# Encode using base64
message = "THM{BASE64_ENCODING}" # Replace with your message to encode
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)