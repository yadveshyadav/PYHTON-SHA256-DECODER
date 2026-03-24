# PYHTON-SHA256-DECODER
# 🔐 Hash Cracker Pro  
### ⚡ Offline Dictionary Attack Tool for Hash Cracking  

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🧠 Overview

**Hash Cracker Pro** is a lightweight yet powerful Python-based tool designed to perform **offline dictionary attacks** on hashed data.  

Built for **cybersecurity enthusiasts, students, and penetration testers**, it demonstrates how weak passwords can be cracked using wordlists.

---

## 🚀 Key Features

✔️ Automatic hash type detection  
✔️ Supports multiple algorithms:  
- MD5  
- SHA1  
- SHA256  
- SHA384  
- SHA512  

✔️ Crack:
- 🔹 Single hash  
- 🔹 Bulk hashes via file  

✔️ Custom wordlist support  
✔️ Fast & efficient dictionary attack  
✔️ Clean CLI interface with colored output  

---

## 🖥️ Demo

```bash
python crack.py -s 5f4dcc3b5aa765d61d8327deb882cf99
```

```
[*] Trying MD5 for 5f4dcc3b5aa765d61d8327deb882cf99
[+] (offline) 5f4dcc3b5aa765d61d8327deb882cf99 : password
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/hash-cracker-pro.git
cd hash-cracker-pro
```

---

## ▶️ Usage Guide

### 🔹 Crack Single Hash
```bash
python crack.py -s <hash>
```

### 🔹 Crack Hashes from File
```bash
python crack.py -f hashes.txt
```

### 🔹 Use Custom Wordlist
```bash
python crack.py -s <hash> -w wordlist.txt
```

---

## 🧬 How It Works

Input Hash → Detect Algorithm → Load Wordlist → Hash Each Word → Compare → Match Found ✅

---

## 📂 Project Structure

.
├── crack.py
├── wordlist.txt
└── README.md

---

## ⚠️ Disclaimer

This tool is created for **educational and ethical purposes only**.  
Do not use it for unauthorized access or illegal activities.

---

## 📈 Roadmap

- Brute-force attack mode  
- GPU acceleration  
- Rainbow table integration  
- GUI version  
- Web-based interface  

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and improve.

---

## ⭐ Support

If you like this project, give it a star ⭐

---

## 👨‍💻 Author

**Yadvesh Yadav**  
Cybersecurity Enthusiast | CSE Student  
