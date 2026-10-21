import numpy as np
import cv2


def myHarrisResponse(imgx, imgy, sigma=1.5, k=0.04):
    """Compute the Harris response from image derivatives.

    Returns
    -------
    R, Sxx, Syy, Sxy : ndarray
        Harris response and smoothed gradient-product images.
    """
    imgx = np.asarray(imgx, dtype=np.float64)
    imgy = np.asarray(imgy, dtype=np.float64)

    if imgx.shape != imgy.shape:
        raise ValueError("imgx and imgy must have the same shape")

    # form the gradient products Ix^2, Iy^2, and Ix*Iy.
    ix2 = imgx*imgx
    iy2 = imgy*imgy
    ixy = imgx*imgy


    # Gaussian smooth the three gradient products.
    # Hint: cv2.GaussianBlur(array, (0, 0), sigma)
    Sxx = cv2.GaussianBlur(ix2, (0,0), sigma )
    Syy = cv2.GaussianBlur(iy2, (0,0), sigma )
    Sxy = cv2.GaussianBlur(ixy, (0,0), sigma )

    # compute
    # R = Sxx*Syy - Sxy**2 - k*(Sxx + Syy)**2
    R = Sxx *Syy - Sxy**2 - k*(Sxx + Syy)**2

    return R, Sxx, Syy, Sxy
