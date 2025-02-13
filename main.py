import cv2
import numpy as np
import os
import easyocr

# Path ke folder Material dan Result
material_folder = 'Material'
result_folder = 'Result'

# Pastikan folder Result ada
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# Inisialisasi EasyOCR
reader = easyocr.Reader(['en'])  # Ganti 'en' dengan bahasa yang Anda gunakan

# Fungsi untuk menghapus teks dari gambar dengan inpainting
def remove_text_with_inpainting(image_path):
    # Baca gambar
    img = cv2.imread(image_path)
    h_img, w_img, _ = img.shape

    # Deteksi teks menggunakan EasyOCR
    results = reader.readtext(img)

    # Buat mask untuk area teks
    mask = np.zeros_like(img)

    for (bbox, text, prob) in results:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        cv2.rectangle(mask, tl, br, (255, 255, 255), -1)

    # Gunakan inpainting untuk mengisi area teks
    result_image = cv2.inpaint(img, mask[:, :, 0], 3, cv2.INPAINT_TELEA)

    return result_image

# Loop melalui semua file dalam folder Material
for filename in os.listdir(material_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(material_folder, filename)
        result_image = remove_text_with_inpainting(image_path)
        result_image_path = os.path.join(result_folder, filename)
        cv2.imwrite(result_image_path, result_image)
        print(f"Processed {filename} and saved to {result_image_path}")
