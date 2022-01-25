Name:
Angelo Pennati

Module Info:
Module 8 - Linear Feedback Shift Registers (Due 08/01/2021 11:59 PM)

Approach: 
LFSR.py creates a class for LFSR objects. Here, we take a seed and a tap value to generate a number of different variables. 
Most importantly, we perform an XOR function using the tap key and the left-most value, in order to then successfully encrypt
the binary value. This is assigned to the step() method, which will return the value of the new right-most number. It would
perhaps have made more sense to have the step() method perform the entire operation anew, but the assignment specifications
asked for the step() method to specifically return the value of the new binary variable being added to the right of the string. 
Regardless, the LSFR class creates a string object equivalent to the LSFR encryption of the given binary string and tap combination. 

Image_Encrypter.py leverages the methods defined in LFSR.py to perform encryption and decryption of images. When an image is passed,
a 2-D array of tuples is created to represent the RGB values of each pixel. This is then encrypted using the LSFR method, updating
the encryption with every number (each color of each pixel) passed. This is done by calling the LFSR class anew on each new
string generated, ensuring complete encryption. The encrypted array is then saved to a PNG. The rest of the code is specific to the assignment,
as its main method will take the necessary inputs specified and leverage the methods described above to encrypt/decrypt an
image of a football.

PLEASE NOTE: I had initially created the 2-D arrays with a neat row structure to match the pixel rows precisely. However, this format
was not accepted by the PIL putdata function, and I therefore had to revert to handling the arrays in a less clearly formatted structure. The results
are excellent, but just something that I was wondering about as I wrote my code. Any insight is greatly appreciated :)

Known Bugs: 
N/A

