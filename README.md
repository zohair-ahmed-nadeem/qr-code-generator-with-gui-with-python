# 📱 QR Code Generator - Python GUI App

A simple and beginner-friendly Python GUI application that generates QR codes from any text, link, or number using the `qrcode` library and Tkinter.

---

## ✅ Features

- Convert any text, URL, or number into a QR Code
- Save the generated QR Code as a `.png` image
- User-friendly interface built with Tkinter

---

## 🖥️ GUI Preview

> A minimal and clean interface for quick QR code generation.

---

## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

### 2. Install Dependencies

Make sure Python 3 is installed. Then run:

```bash
pip install qrcode[pil]
```

### 3. Run the App

```bash
python qr_generator.py
```

---

## 🛠️ How It Works

1. **Enter** the text, URL, or number you want to convert.
2. **Enter** the name of the file you want to save it as (without extension).
3. **Click** the **Enter** button.
4. The QR code will be generated and saved in the same directory as a `.png` file.

---

## 🖼️ Example

- Input: `https://github.com/zohair-ahmed-nadeem`
- Filename: `github_qr`
- Output: `github_qr.png` in the current folder

---

## 📦 Dependencies

- `qrcode`
- `Pillow` (included with `qrcode[pil]`)
- `tkinter` (comes with Python standard library)

---

## 📌 Notes

- The QR code is saved in black and white with default settings.
- Make sure to use valid file names (no special characters).
- Images are saved in the current working directory.

---

## 👨‍💻 Author

Developed by [Zohair Ahmed](https://github.com/zohair-ahmed-nadeem)

---

## 📄 License

This project is licensed under the MIT License.
