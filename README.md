QR Link Decrypter
=================

A lightweight, cross-platform graphical tool to decode QR codes from clipboard or drag-and-drop image input. Built using Python and PyQt5 with OpenCV for QR code detection.

----------------------
FEATURES  
----------------------

- Paste QR image directly from clipboard (e.g. screenshots)  
- Drag-and-drop image support (PNG, JPEG, BMP, etc.)  
- Instant QR code decoding  
- Cross-platform (Linux, Windows, macOS)

----------------------
INSTALLATION  
----------------------

Make sure Python 3.8 or newer is installed on your system.

Step 1: Clone the repository  
git clone https://github.com/YourUsername/qr-link-decrypter.git  
cd qr-link-decrypter

Step 2: Install dependencies

pip install PyQt5 Pillow opencv-python numpy

----------------------
USAGE  
----------------------

Run the script with:

python qr_link_decrypter.py

Then:
- Paste a QR code image from your clipboard (e.g. Ctrl+C a screenshot)
- Or drag and drop an image file into the app
- The decoded text (usually a URL) will appear in the result field

----------------------
LICENSE  
----------------------

This project is licensed under the MIT License. See the LICENSE file for details.

----------------------
AUTHOR  
----------------------

Ian Michael Bollinger  
Email: ian.michael.bollinger@gmail.com  
GitHub: https://github.com/iPsychonaut

----------------------
ISO DOCUMENTATION NOTES  
----------------------

This project is documented in alignment with ISO 9001 traceability:  
- Version: 1.0  
- Created: 2025-08-02  
- Reviewed: ✅ Passed initial validation  
- Dependencies: PyQt5, Pillow, OpenCV (cv2), NumPy
