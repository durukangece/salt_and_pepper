import cv2

# Görüntüyü yükleme
image = cv2.imread("salt.png")

# Bilateral filtresini uygulama
denoised_image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# Sonucu kaydet
cv2.imwrite("temizlenmis_bilateral.png", denoised_image)