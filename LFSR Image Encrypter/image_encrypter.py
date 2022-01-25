from lfsr import LFSR                                                           # Import necessary packages
from PIL import Image


# Define the Image Encrypter Class
class ImageEncrypter:                                                           # Define Class
    def __init__(self, lfsr: LFSR, file_name: str):                             # Define Initial State
        self.name = file_name
        self.lfsr = lfsr
        self.taps = lfsr.taps

    def open_image(self):                                                       # Open Target Image
        img = Image.open(self.name)
        return img

    def pixel_array(self):                                                      # Define function to have a 2d Array
        init_array = []                                                         # Initialize array
        open_img = self.open_image()
        pixel_access = open_img.load()                                          # Load data into Pixel Access
        width = open_img.width                                                  # Get image parameters
        height = open_img.height
        for z in range(0, height):
            for w in range(0,width):
                init_array.append(pixel_access[w,z])                            # Retrieve nested list of tuples
        return init_array

    def transform(self):                                                        # Define Transformation Function
        new_lfsr = self.lfsr
        og_array = self.pixel_array()
        enc_array = []                                                          # Initiate encrypted array
        for pixel in og_array:                                                  # Work tuple by Tuple
            pixel_vals = []
            for color in pixel:
                encode = int(str(new_lfsr), 2) ^ color                          # Perform XOR methodology
                pixel_vals.append(encode)
                new_lfsr = LFSR(str(new_lfsr), self.taps)                       # Perform LFSR step anew each time
            enc_array.append(tuple(pixel_vals))
        return enc_array

    def save_image(self, nomenclature: str):                                         # Define function to save image
        img_specs = self.open_image()
        data = self.transform()
        img_out = Image.new('RGB', img_specs.size)
        img_out.putdata(data)                                                   # Write data to image
        return img_out.save(nomenclature)                                       # Save Image


def main():                                                                     # Define main method for assignment
    seed = '10011010'                                                           # Initiate parameters
    tap = 5
    file_name_init = 'football.png'
    file_name_enc = 'football_encrypted.png'
    file_name_dec = 'football_decrypted.png'
    encryption = ImageEncrypter(LFSR(seed = seed, tap = tap), file_name_init)   # Perform encryption
    encryption.save_image(file_name_enc)
    decryption = ImageEncrypter(LFSR(seed = seed, tap = tap), file_name_enc)    # Perform decryption
    decryption.save_image(file_name_dec)


if __name__ == "__main__":
    main()

