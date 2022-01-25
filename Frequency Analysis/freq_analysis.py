def get_freq_counts(encrypted_message):                         # Define the get_freq_counts function
    mess_list = encrypted_message.split()                       # Split the string by word (at every space)
    letters = []                                                # Initialize letters list for iteration
    mess_dict = {}                                              # Initialize dictionary for function output
    for word in mess_list:                                      # Create a list of letters present
        for char in word:
            letters.append(char)
    for letter in letters:                                      # Count the frequency of each letter
        freq = letters.count(letter)
        mess_dict[letter] = freq                                # Record the frequency of each letter in dictionary
    return mess_dict                                            # Return the dictionary


message = open('ciphertext.txt', 'r').readline()                # Open the message input file, and read the line
freq_tbl = open('freq.txt', 'r').readlines()                    # Open the frequency input file, and read line-by-line
freq_list = []                                                  # Initialize frequency list for data in input file
translator = {}                                                 # Initialize dictionary for letter-mapping


for i in range(len(freq_tbl)):                                  # Turn the given frequency list to a list of tuples
    entry = freq_tbl[i].strip().split(':')
    freq_list.append(entry)
freq_dict = dict(freq_list)                                     # Turn the given frequency list into a dictionary

for key in freq_dict:                                           # Convert dictionary values to integers
    freq_dict[key] = int(freq_dict[key])

enc_freq = get_freq_counts(message)                             # Call function to get frequency counts in message

for entry in enc_freq:                                          # Create a dictionary matching characters on freq.
    for value in freq_dict:
        if enc_freq[entry] == freq_dict[value]:
            translator[entry] = value

decryption = ''.join(translator.get(ch, ch) for ch in message)  # Replace each character in the message with new value
print(decryption)                                               # Print the decrypted message to console
