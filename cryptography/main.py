import hashlib
import base64
from typing import Tuple

class SecureMessenger:
    def __init__(self, password: str):
        """Initialize with a password that will be used for encryption/decryption"""
        self.password = password
        
    def _generate_key(self, salt: str) -> bytes:
        """Generate encryption key from password using SHA-256"""
        key_material = (self.password + salt).encode()
        return hashlib.sha256(key_material).digest()
    
    def encrypt(self, message: str) -> str:
        """Encrypt a message using XOR cipher with hashed key"""
        # Generate a random salt
        salt = base64.b64encode(hashlib.sha256(message.encode()).digest()[:8]).decode()
        
        # Generate encryption key
        key = self._generate_key(salt)
        
        # Convert message to bytes
        msg_bytes = message.encode('utf-8')
        
        # XOR encryption
        encrypted = bytearray()
        for i, byte in enumerate(msg_bytes):
            encrypted.append(byte ^ key[i % len(key)])
        
        # Encode as base64 for easy storage/transmission
        encrypted_b64 = base64.b64encode(encrypted).decode()
        
        # Return salt + encrypted message (separated by '.')
        return f"{salt}.{encrypted_b64}"
    
    def decrypt(self, encrypted_message: str) -> str:
        """Decrypt a message"""
        try:
            # Split salt and encrypted message
            salt, encrypted_b64 = encrypted_message.split('.')
            
            # Generate same encryption key
            key = self._generate_key(salt)
            
            # Decode from base64
            encrypted = base64.b64decode(encrypted_b64)
            
            # XOR decryption (same as encryption)
            decrypted = bytearray()
            for i, byte in enumerate(encrypted):
                decrypted.append(byte ^ key[i % len(key)])
            
            return decrypted.decode('utf-8')
        except Exception as e:
            return f"Decryption failed: {str(e)}"

