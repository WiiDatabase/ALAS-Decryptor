ALAS Decryptor
==============
This Python 3 script decrypts ALAS files from the Wii's Region Select channel (rgnsel).
Thanks to Larsenv from [RiiConnect24](https://rc24.xyz/) for figuring out the keys, the format and creating the initial script!

## Usage
1. Install PyCryptodome
2. Put your encrypted ALAS files in the subdirectory "address" of this script
3. Run decryptor.py
4. Your decrypted ALAS files are in the "address/decrypted" directory!

### And after that?
1. Decompress the LZ77 U8 archive with [DSDecmp](https://www.romhacking.net/utilities/789/) (`dsdecmp ALAS_FILE`)
2. Extract the U8 archive with ShowMiiWads, U8Tool or Wiimms SZS Tools (`wszst x ALAS_FILE`)

## Technical stuff
1. Remove the first 320 bytes (the RSA signature) from the ALAS file
2. Decrypt it with AES-256-CBC mode and the key `FF4C1AE3D4FFD236712E258A1F0B91E72C9125B0DF94C1691BCEF13011F16C0F` with `862D7D8676A630A82972AB9735E1A5CE` as initialization vector
3. Remove the first 32 bytes from the decrypted data and you get an LZ77-compressed U8 archive

## More?
* Check out the [WiiDatabase Wiki](https://wiki.wiidatabase.de/wiki/Regionsauswahl_(Kanal)) (German)!
* Use WiiConnect24 again with [RiiConnect24](https://rc24.xyz/)!
