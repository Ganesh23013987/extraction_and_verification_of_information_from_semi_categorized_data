import cv2

def preprocess_for_ocr(image_path, output_path="preprocessed.png"):
    img = cv2.imread(image_path)

    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. VERY mild edge-preserving denoise
    denoised = cv2.bilateralFilter(
        gray,
        d=5,
        sigmaColor=25,
        sigmaSpace=25
    )

    # 3. Linear intensity scaling (no stroke thickening)
    intensified = cv2.convertScaleAbs(
        denoised,
        alpha=1.15,   # subtle contrast boost
        beta=0
    )

    cv2.imwrite(output_path, intensified)
    return output_path
