import numpy as np                                                                      # Import necessary packages


class MatrixNotInvertible(Exception):                                                   # Create Exception Class
    pass


class DetIsZero(MatrixNotInvertible):                                                   # Create Exception Subclass 1
    pass


class MatrixNotSq(MatrixNotInvertible):                                                 # Create Exception Subclass 2
    pass


class HillCypher:                                                                       # Create HillCypher class
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',     # Create letter array
                'R','S','T','U','V','W','X','Y','Z']
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]     # Create number array
    dict_1 = dict(zip(letters, numbers))                                                # Create dictionaries
    dict_2 = dict(zip(numbers, letters))

    def determinant(matrix):                                                            # Define determinant formula
        return np.linalg.det(matrix)

    def invertible(matrix):                                                             # Define invertibile function
        try:
            if matrix.shape[0] == matrix.shape[1]:                                      # Check whether matrix is sq.
                if HillCypher.determinant(matrix) != 0:                                 # Check whether det = 0
                    print("The matrix is invertible.")
                    return True
                else:
                    raise DetIsZero                                                     # Raise appropriate exceptions
            else:
                raise MatrixNotSq
        except MatrixNotSq:
            print("The matrix is not square.")
        except DetIsZero:
            print("The determinant is 0.")

    def mod_inverse(n, m):                                                              # Define mod_inverse calculation
        result = pow(n,-1,m)
        return result

    def encrypt(P, K, modulus):                                                         # Define encryption function
        if HillCypher.invertible(K):
            out_arr = np.empty([int(len(P)/K.shape[0]), K.shape[0]])                    # Initialize outwards array
            string_list = np.asarray([HillCypher.dict_1[char] for char in P])           # Convert plaintext to array
            input_mat = np.reshape(string_list, [int(len(P)/K.shape[0]), K.shape[0]])   # Shape array appropriately
            for i in range(input_mat.shape[0]):
                out_arr[i] = np.matmul(K.transpose(), input_mat[i]) % modulus           # Perform calculation
            out_arr_letters = np.vectorize(HillCypher.dict_2.get)(out_arr)              # Conform to desired shape
            out_linear = np.ndarray.flatten(out_arr_letters)                            # Prepare array for string print
            out_str = ''
            for letter in out_linear:                                                   # Print string
                out_str += letter
            print(f'Plaintext: {P}')
            print(f'Plaintext Column Vectors: {input_mat}')
            print(f'Ciphertext: {out_str}')
            print(f'Ciphertext column vectors: {out_arr}')
            return out_arr
        else:
            return 'redflag'                                                            # Return False if not invertible

    def decrypt(C, K, modulus):                                                         # Define decryption function
        mmi_det = HillCypher.mod_inverse(round(HillCypher.determinant(K)), modulus)     # Calculate determinant and mod
        k_step = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])                       # Initialize new key values
        k_step_2 = k_step * mmi_det
        new_keys = k_step_2 % modulus                                                   # Multiply by inverse det.
        P_2 = np.empty([C.shape[0], C.shape[1]])                                        # Initialize array for output
        for i in range(C.shape[0]):                                                     # Perform calculation
            P_2[i] = np.matmul(new_keys.transpose(), C[i]) % modulus
        decrypt_letters = np.vectorize(HillCypher.dict_2.get)(P_2)                      # Prepare array for decryption
        decrypt_linear = np.ndarray.flatten(decrypt_letters)
        decrypt_str = ''
        for letter in decrypt_linear:                                                   # Print string
            decrypt_str += letter
        print(f'Plaintext: {decrypt_str}')
        print(f'Plaintext column vectors: {P_2}')
        return P_2


# Define inputs for main method
P = 'ATTACKATDAWN'                                                                      # PlainText Input
modulus = 26                                                                            # Modulus Input
K_1 = np.array([[19,3],[8,12],[4,7]])                                                   # Key Inputs
K_2 = np.array([[7,11], [8,11]])
K_3 = np.array([[5,4],[15,12]])

# Execute the code, using the inputs above
Input_1_Enc = HillCypher.encrypt(P, K_1, modulus)
if isinstance(Input_1_Enc, np.ndarray):
    HillCypher.decrypt(Input_1_Enc, K_1, modulus)
else:
    pass

Input_2_Enc = HillCypher.encrypt(P, K_2, modulus)
if isinstance(Input_2_Enc, np.ndarray):
    HillCypher.decrypt(Input_2_Enc, K_2, modulus)
else:
    pass

Input_3_Enc = HillCypher.encrypt(P, K_3, modulus)
if isinstance(Input_3_Enc, np.ndarray):
    HillCypher.decrpyt(Input_3_Enc, K_3, modulus)
else:
    pass
















