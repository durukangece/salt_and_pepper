import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread("salt.png")

# Medyan filtresini uygulama
denoised_image = cv2.medianBlur(image, 5)

# Sonucu kaydet
cv2.imwrite("temizlenmis_resim.png", denoised_image)