import cowsay

name = input("What's your name? ")
cowsay.cow(f"hello, {name}")

# Generating QR code with python
import qrcode

img = qrcode.make("https://youtu.be/EHi0RDZ31VA?si=WjU8-CPJmW3vMB1y")
img.save("qr.png", "PNG") # Now a QR should be generated in the parent folder of this file