import random
import string

def encode(msg):
    if len(msg) > 3:
        encoded_msg = msg[1:] + msg[0]
        random_prefix = random.choices(string.ascii_lowercase, k=3)
        random_suffix = random.choices(string.ascii_lowercase, k=3)
        encoded_msg = "".join(random_prefix) + encoded_msg + "".join(random_suffix)
        return encoded_msg
    else:
        return msg[::-1]

def decode(msg):
    if len(msg) > 3:
        decoded_msg = msg[3:-3]
        decoded_msg = decoded_msg[-1] + decoded_msg[:-1]
        return decoded_msg
    else:
        return msg[::-1]

choice = int(input("Enter '1' for coding or '2' for decoding: "))
message = input("Enter your message: ")

if choice == 1:
    print("Encoded message:", encode(message))
else:
    print("Decoded message:", decode(message))