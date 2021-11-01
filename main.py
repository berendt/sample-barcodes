import os
from random import randint
import treepoem

# https://stackoverflow.com/questions/2673385/how-to-generate-a-random-number-with-a-specific-amount-of-digits
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

BARCODE_TYPES = [
    "qrcode",
    "azteccode",
    "pdf417",
    "interleaved2of5",
    "code128",
    "code39"
]

NUMBER = 20
NUMBER_OF_DIGITS = 32

for barcode_type in BARCODE_TYPES:
    os.mkdir(f"samples/{barcode_type}")
    fp = open(f"samples/{barcode_type}/README.md", "w+")
    fp.write(f"# Samples for barcode type {barcode_type}\n\n")
    for i in range(NUMBER):
        data = random_with_N_digits(NUMBER_OF_DIGITS)
        image = treepoem.generate_barcode(
            barcode_type=barcode_type, 
            data=data
        )
        image.convert("1").save(f"samples/{barcode_type}/{i}.png")
        fp.write(f"## Sample {i}\n")
        fp.write(f"![]({i}.png)\n\n{data}\n\n")

    fp.close()
