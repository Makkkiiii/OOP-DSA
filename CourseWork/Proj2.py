import os
import hashlib
import logging
import platform
import threading
import time
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import tkinter as tk
from tkinter import filedialog, messagebox, font

logging.basicConfig(filename='encryption_activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Encryption Tool")
        self.root.geometry("650x400")
        self.root.configure(bg="#2E3440")  # Dark background

        # Fonts
        self.title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        self.label_font = font.Font(family="Segoe UI", size=12)
        self.entry_font = font.Font(family="Segoe UI", size=11)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        # Track encrypted files
        self.encrypted_files = set()
        self.key = None

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title = tk.Label(self.root, text="Folder Encryption Tool", bg="#2E3440", fg="#D8DEE9", font=self.title_font)
        title.pack(pady=(15, 20))

        # Main frame container
        main_frame = tk.Frame(self.root, bg="#3B4252", bd=2, relief=tk.RIDGE)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Folder selection
        folder_frame = tk.Frame(main_frame, bg="#3B4252")
        folder_frame.pack(fill=tk.X, pady=5, padx=15)

        folder_label = tk.Label(folder_frame, text="Folder Path:", bg="#3B4252", fg="#D8DEE9", font=self.label_font)
        folder_label.pack(side=tk.LEFT, padx=(0,10))

        self.folder_entry = tk.Entry(folder_frame, font=self.entry_font, width=40, bg="#4C566A", fg="#ECEFF4", insertbackground='white')
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        browse_btn = tk.Button(folder_frame, text="Browse", font=self.button_font, bg="#5E81AC", fg="white",
                               activebackground="#81A1C1", relief=tk.FLAT, command=self.select_folder)
        browse_btn.pack(side=tk.LEFT, padx=10)
        self._add_hover_effect(browse_btn, "#81A1C1", "#5E81AC")

        # Password entry
        pw_frame = tk.Frame(main_frame, bg="#3B4252")
        pw_frame.pack(fill=tk.X, pady=10, padx=15)

        pw_label = tk.Label(pw_frame, text="Password:", bg="#3B4252", fg="#D8DEE9", font=self.label_font)
        pw_label.pack(side=tk.LEFT, padx=(0,10))

        self.password_entry = tk.Entry(pw_frame, show="*", font=self.entry_font, width=40, bg="#4C566A", fg="#ECEFF4", insertbackground='white')
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Buttons frame
        btn_frame = tk.Frame(main_frame, bg="#3B4252")
        btn_frame.pack(fill=tk.X, pady=15, padx=15)

        encrypt_btn = tk.Button(btn_frame, text="Encrypt Folder", font=self.button_font, bg="#A3BE8C", fg="#2E3440",
                                activebackground="#B5CCA6", relief=tk.FLAT, command=self.start_encryption)
        encrypt_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self._add_hover_effect(encrypt_btn, "#B5CCA6", "#A3BE8C")

        decrypt_btn = tk.Button(btn_frame, text="Decrypt Folder", font=self.button_font, bg="#BF616A", fg="#2E3440",
                                activebackground="#D08770", relief=tk.FLAT, command=self.start_decryption)
        decrypt_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self._add_hover_effect(decrypt_btn, "#D08770", "#BF616A")

        # Password Update Section
        update_frame = tk.LabelFrame(main_frame, text="Update Password", bg="#3B4252", fg="#D8DEE9", font=self.label_font, bd=2, relief=tk.GROOVE)
        update_frame.pack(fill=tk.BOTH, pady=15, padx=15)

        old_pw_frame = tk.Frame(update_frame, bg="#3B4252")
        old_pw_frame.pack(fill=tk.X, pady=5, padx=10)
        old_pw_label = tk.Label(old_pw_frame, text="Old Password:", bg="#3B4252", fg="#D8DEE9", font=self.label_font)
        old_pw_label.pack(side=tk.LEFT, padx=(0,10))
        self.old_password_entry = tk.Entry(old_pw_frame, show="*", font=self.entry_font, width=40, bg="#4C566A", fg="#ECEFF4", insertbackground='white')
        self.old_password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        new_pw_frame = tk.Frame(update_frame, bg="#3B4252")
        new_pw_frame.pack(fill=tk.X, pady=5, padx=10)
        new_pw_label = tk.Label(new_pw_frame, text="New Password:", bg="#3B4252", fg="#D8DEE9", font=self.label_font)
        new_pw_label.pack(side=tk.LEFT, padx=(0,10))
        self.new_password_entry = tk.Entry(new_pw_frame, show="*", font=self.entry_font, width=40, bg="#4C566A", fg="#ECEFF4", insertbackground='white')
        self.new_password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        update_btn = tk.Button(update_frame, text="Update Password", font=self.button_font, bg="#88C0D0", fg="#2E3440",
                               activebackground="#A3D0E8", relief=tk.FLAT, command=self.start_update_password)
        update_btn.pack(pady=10, padx=20, fill=tk.X)
        self._add_hover_effect(update_btn, "#A3D0E8", "#88C0D0")

    def _add_hover_effect(self, widget, hover_bg, default_bg):
        def on_enter(e):
            widget['background'] = hover_bg
        def on_leave(e):
            widget['background'] = default_bg
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)

    def generate_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return urlsafe_b64encode(kdf.derive(password.encode()))

    def hash_file(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def encrypt_file_double(self, file_path, key):
        try:
            original_hash = self.hash_file(file_path)
            with open(file_path, 'rb') as file:
                data = file.read()

            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(data) + padder.finalize()

            iv_aes = os.urandom(16)
            cipher_aes = Cipher(algorithms.AES(key), modes.CFB(iv_aes), backend=default_backend())
            encryptor_aes = cipher_aes.encryptor()
            encrypted_data_aes = iv_aes + encryptor_aes.update(padded_data) + encryptor_aes.finalize()

            chacha = ChaCha20Poly1305(key)
            nonce = os.urandom(12)
            encrypted_data_chacha = nonce + chacha.encrypt(nonce, encrypted_data_aes, None)

            with open(file_path + ".enc", 'wb') as file:
                file.write(encrypted_data_chacha)

            with open(file_path + ".hash", 'w') as hash_file:
                hash_file.write(original_hash)

            os.remove(file_path)
            self.encrypted_files.add(file_path + ".enc")
            logging.info(f"File encrypted: {file_path}")
        except Exception as e:
            logging.error(f"Error encrypting file {file_path}: {e}")
            messagebox.showerror("Encryption Error", f"Failed to encrypt {file_path}.\nError: {e}")

    def decrypt_file_double(self, file_path, key):
        try:
            with open(file_path, 'rb') as file:
                encrypted_data_chacha = file.read()

            nonce = encrypted_data_chacha[:12]
            chacha = ChaCha20Poly1305(key)
            encrypted_data_aes = chacha.decrypt(nonce, encrypted_data_chacha[12:], None)

            iv_aes = encrypted_data_aes[:16]
            cipher_aes = Cipher(algorithms.AES(key), modes.CFB(iv_aes), backend=default_backend())
            decryptor_aes = cipher_aes.decryptor()
            padded_data = decryptor_aes.update(encrypted_data_aes[16:]) + decryptor_aes.finalize()

            unpadder = padding.PKCS7(128).unpadder()
            data = unpadder.update(padded_data) + unpadder.finalize()

            original_file_path = file_path[:-4]
            with open(original_file_path, 'wb') as file:
                file.write(data)

            with open(original_file_path + ".hash", 'r') as hash_file:
                original_hash = hash_file.read().strip()

            os.remove(file_path)
            os.remove(original_file_path + ".hash")

            decrypted_hash = self.hash_file(original_file_path)
            if original_hash != decrypted_hash:
                logging.error(f"File integrity check failed for {original_file_path}")
                messagebox.showerror("Integrity Error", f"File integrity check failed for {original_file_path}")
                raise ValueError(f"File integrity check failed for {original_file_path}")

            self.encrypted_files.discard(file_path)
            logging.info(f"File decrypted: {original_file_path}")
        except Exception as e:
            logging.error(f"Error decrypting file {file_path}: {e}")
            messagebox.showerror("Decryption Error", f"Failed to decrypt {file_path}.\nError: {e}")

    def traverse_and_encrypt(self, folder, key):
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                if full_path.endswith('.enc') or full_path.endswith('.hash'):
                    continue
                self.encrypt_file_double(full_path, key)

    def traverse_and_decrypt(self, folder, key):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.enc'):
                    full_path = os.path.join(root, file)
                    self.decrypt_file_double(full_path, key)

    def start_encryption(self):
        folder = self.folder_entry.get()
        password = self.password_entry.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Invalid Folder", "Please select a valid folder.")
            return
        if not password:
            messagebox.showwarning("Missing Password", "Please enter a password.")
            return

        # Derive key from password with a fixed salt (or random per session, but then you must save salt)
        salt = b'static_salt_1234'  # You may want to generate and save salt per folder or session
        self.key = self.generate_key(password, salt)
        threading.Thread(target=self.traverse_and_encrypt, args=(folder, self.key), daemon=True).start()
        messagebox.showinfo("Encryption Started", "Encryption process started in background.")

    def start_decryption(self):
        folder = self.folder_entry.get()
        password = self.password_entry.get()
        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Invalid Folder", "Please select a valid folder.")
            return
        if not password:
            messagebox.showwarning("Missing Password", "Please enter a password.")
            return

        salt = b'static_salt_1234'  # Must be same salt used during encryption
        self.key = self.generate_key(password, salt)
        threading.Thread(target=self.traverse_and_decrypt, args=(folder, self.key), daemon=True).start()
        messagebox.showinfo("Decryption Started", "Decryption process started in background.")

    def start_update_password(self):
        folder = self.folder_entry.get()
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()

        if not folder or not os.path.isdir(folder):
            messagebox.showwarning("Invalid Folder", "Please select a valid folder.")
            return
        if not old_password or not new_password:
            messagebox.showwarning("Missing Password", "Please enter both old and new passwords.")
            return
        if old_password == new_password:
            messagebox.showwarning("Password Error", "New password must be different from the old password.")
            return

        threading.Thread(target=self.update_password, args=(folder, old_password, new_password), daemon=True).start()
        messagebox.showinfo("Password Update", "Password update process started in background.")

    def update_password(self, folder, old_password, new_password):
        salt = b'static_salt_1234'
        old_key = self.generate_key(old_password, salt)
        new_key = self.generate_key(new_password, salt)

        # Decrypt all encrypted files with old key
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.enc'):
                    full_path = os.path.join(root, file)
                    try:
                        self.decrypt_file_double(full_path, old_key)
                    except Exception as e:
                        logging.error(f"Failed to decrypt during password update: {full_path}, {e}")
                        messagebox.showerror("Update Error", f"Failed to decrypt {full_path} with old password.\n{e}")
                        return

        # Encrypt all files again with new key
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                if full_path.endswith('.enc') or full_path.endswith('.hash'):
                    continue
                try:
                    self.encrypt_file_double(full_path, new_key)
                except Exception as e:
                    logging.error(f"Failed to encrypt during password update: {full_path}, {e}")
                    messagebox.showerror("Update Error", f"Failed to encrypt {full_path} with new password.\n{e}")
                    return

        messagebox.showinfo("Password Update", "Password updated successfully for all files.")
        logging.info(f"Password updated for folder: {folder}")

def main():
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()