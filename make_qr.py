# pip install qrcode[pil]
import qrcode

USERNAME = "YOUR-GITHUB-USERNAME"   # <-- change this
url = f"https://{USERNAME}.github.io/certificates/verify/RK-B498-8037-EE4A/"
qrcode.make(url).save("certificate_qr.png")
print("Saved certificate_qr.png ->", url)
