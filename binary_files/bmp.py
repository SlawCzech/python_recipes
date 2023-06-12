import math


def _int32_to_bytes(i):
    """Convert integers to bytes in little-endian format."""
    return bytes((i & 0xff, i >> 8 & 0xff, i >> 16 & 0xff, i >> 24 & 0xff))


def write_greyscale(filename, pixels):
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as f:
        f.write(b'BM')  # BMP header
        size_bookmark = f.tell()  # The next four bytes hold the filesize as a 32-bit
        f.write(b'\x00\x00\x00\x00')
        f.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        f.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = f.tell()
        f.write(b'\x00\x00\x00\x00')

        # image header
        f.write(b'\x28\x00\x00\x00')  # Image header size in bytes - 40 decimal
        f.write(_int32_to_bytes(width))  # Image width in pixels
        f.write(_int32_to_bytes(height))  # Image height in pixels
        f.write(b'\x01\x00')  # Number of image planes
        f.write(b'\x08\x00')  # Bits per pixel 8 for grayscale
        f.write(b'\x00\x00\x00\x00')  # No compression
        f.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        f.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        f.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        f.write(b'\x00\x00\x00\x00')  # Use whole color table
        f.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            f.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = f.tell()
        for row in reversed(pixels):  # BMP files are bottom to top
            row_data = bytes(row)
            f.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            f.write(padding)

        # End of file
        eof_bookmark = f.tell()

        # Fill in file size placeholder
        f.seek(size_bookmark)
        f.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        f.seek(pixel_offset_bookmark)
        f.write(_int32_to_bytes(pixel_data_bookmark))


def mandel(real, imag):
    """The logarithm of number of iterations needed to
    determine whether a complex point is in the
    Mandelbrot set.

    Args:
        real: The real coordinate
        imag: The imaginary coordinate

    Returns:
        An integer in the range 1-255.
    """
    x = 0
    y = 0
    for i in range(1, 257):
        if x * x + y * y > 4.0:
            break
        xt = real + x * x - y * y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1


def mandelbrot(size_x, size_y):
    """Make an Mandelbrot set image.

    Args:
        size_x: Image width
        size_y: Image height

    Returns:
        A list of lists of integers in the range 0-255.
    """
    return [[mandel((3.5 * x / size_x) - 2.5,
                    (2.0 * y / size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.

    Args:
        filename: The filename of a BMP file.

    Returns:
        A tuple containing two integers with the width
        and height in pixels.

    Raises:
        ValueError: If the file was not a BMP file.
        OSError: If there was a problem reading the file.
    """

    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    "Convert a bytes object containing four bytes into an integer."
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)
