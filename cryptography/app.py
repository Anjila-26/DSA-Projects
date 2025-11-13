import streamlit as st
from main import SecureMessenger

# Page config
st.set_page_config(
    page_title="Secure Message Encryptor",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🔐 Secure Message Encryptor")
st.markdown("### Keep your conversations private from prying eyes!")
st.divider()

# Password input
col1, col2 = st.columns([3, 1])
with col1:
    password = st.text_input(
        "🔑 Enter Secret Password",
        type="password",
        placeholder="Share this password with your crush only!",
        help="Both you and your crush need to use the same password",
        label_visibility="visible"
    )
    
    # Apply black background to password input
    st.markdown("""
        <style>
        /* Make password input background black with white text */
        input[type="password"] {
            background-color: #000000 !important;
            color: #ffffff !important;
            border: 2px solid #333333 !important;
        }
        input[type="password"]::placeholder {
            color: #888888 !important;
        }
        </style>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    show_password = st.checkbox("Show", key="show_pwd")

if show_password and password:
    st.markdown(f"""
        <div style='background-color: #000000; color: #ffffff; padding: 1rem; 
                    border-radius: 0.5rem; border: 2px solid #333333; font-family: monospace;'>
            <strong>Password:</strong> {password}
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Tabs for encryption and decryption
tab1, tab2 = st.tabs(["🔒 Encrypt Message", "🔓 Decrypt Message"])

with tab1:
    st.markdown("#### Encrypt your message")
    
    message = st.text_area(
        "Enter your message:",
        placeholder="Type your secret message here...",
        height=150,
        key="encrypt_input"
    )
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        encrypt_btn = st.button("🔒 Encrypt", type="primary", use_container_width=True)
    
    if encrypt_btn:
        if not password:
            st.error("⚠️ Please enter a password first!")
        elif not message:
            st.error("⚠️ Please enter a message to encrypt!")
        else:
            messenger = SecureMessenger(password)
            encrypted = messenger.encrypt(message)
            
            st.success("✅ Message encrypted successfully!")
            st.text_area(
                "Encrypted Message (copy and send this):",
                value=encrypted,
                height=100,
                key="encrypted_output"
            )
            
            st.info("💡 **Tip:** Copy the encrypted message above and send it to your crush. They'll need the same password to decrypt it!")

with tab2:
    st.markdown("#### Decrypt a message")
    
    encrypted_input = st.text_area(
        "Paste encrypted message:",
        placeholder="Paste the encrypted message here...",
        height=100,
        key="decrypt_input"
    )
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        decrypt_btn = st.button("🔓 Decrypt", type="primary", use_container_width=True)
    
    if decrypt_btn:
        if not password:
            st.error("⚠️ Please enter a password first!")
        elif not encrypted_input:
            st.error("⚠️ Please paste an encrypted message!")
        else:
            messenger = SecureMessenger(password)
            decrypted = messenger.decrypt(encrypted_input)
            
            if "failed" in decrypted.lower():
                st.error(decrypted)
            else:
                st.success("✅ Message decrypted successfully!")
                st.text_area(
                    "Decrypted Message:",
                    value=decrypted,
                    height=150,
                    key="decrypted_output"
                )

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🔐 <strong>How it works:</strong> Your password is hashed using SHA-256, 
        then used to encrypt messages with XOR cipher. 
        Only someone with the correct password can decrypt your messages!</p>
        <p style='font-size: 0.9em;'>Keep your password safe and share it only with your crush! 💕</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with instructions
with st.sidebar:
    st.header("📖 Instructions")
    st.markdown("""
    **Step 1:** Create a secret password
    - Share this password privately with your crush
    - Don't let anyone else know it!
    
    **Step 2:** Encrypt your message
    - Enter your password
    - Type your message in the Encrypt tab
    - Click "Encrypt" and copy the result
    
    **Step 3:** Send the encrypted message
    - Send via any app (WhatsApp, Telegram, etc.)
    - Your sister won't understand it! 😎
    
    **Step 4:** Your crush decrypts it
    - They paste the message in the Decrypt tab
    - Enter the same password
    - Click "Decrypt" to read the message
    """)
    
    st.divider()
    
    st.header("🛡️ Security Features")
    st.markdown("""
    ✅ SHA-256 hashing
    ✅ XOR encryption
    ✅ Unique salt per message
    ✅ Base64 encoding
    ✅ Password protection
    """)