import ctypes
import quote_image

img = "path\\result.jpg"

ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)
