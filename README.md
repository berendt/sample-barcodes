# sample-barcodes

For the preparations of an asset management in combination with Netbox we needed
a larger amount of barcodes for preliminary tests. Anyhow we didn't find anything
usable and so this repository was created.

In the directory ``samples`` is for each barcode type a ``README.md`` file with 20
generated barcode image of this type.

* [azteccode](samples/azteccode/README.md)
* [code128](samples/code128/README.md)
* [code39](samples/code39/README.md)
* [interleaved2of5](samples/interleaved2of5/README.md)
* [pdf417](samples/pdf417/README.md)
* [qrcode](samples/qrcode/README.md)

In principle, barcodes can be generated for all barcode types supported by
[bwipp/postscriptbarcode](https://github.com/bwipp/postscriptbarcode).
Feel free to create a PR to add new types. [treepoem](https://github.com/adamchainz/treepoem)
is used for the creation of the barcodes.

## Installation

Prepare the Python environment:

```
pipenv install
```

You’ll also need Ghostscript installed. On Ubuntu/Debian this can be installed with:

```
apt-get install ghostscript
```

On Mac OS X use:

```
brew install ghostscript
```

## Usage

```
python3 main.py
```

## Conversion to PDFs

```
cd samples/azteccode; pandoc README.md -o ../../azteccode.pdf; cd ../../
cd samples/code128; pandoc README.md -o ../../code128.pdf; cd ../../
cd samples/code39; pandoc README.md -o ../../code39.pdf; cd ../../
cd samples/interleaved2of5; pando README.md -o ../../interleaved2of5.pdf; cd ../../
cd samples/pdf417; pandoc README.md -o ../../pdf417.pdf; cd ../../
cd samples/qrcode; pandoc README.md -o ../../qrcode.pdf; cd ../../
```
