# Define a class LFSR to act as a Linear Feedback Shift Register
class LFSR:                                                             # Declare class name
    def __init__(self, seed: str, tap: int):                            # Define Initial State
        self.register = seed
        self.taps = tap

    def length(self):                                                   # Define Function to retain Length of Seed
        length = len(self.register)
        return length

    def bit(self, i: int):                                              # Define Function to retain a given "bit"
        bit = int(self.register[-i])
        return bit

    def step(self):                                                     # Define the "step" function necessary for
        leftmost = int(self.register[0])                                # Grab the leftmost value
        tapper = int(self.register[self.length()-self.taps])            # Grab the tap value
        new_bit = leftmost ^ tapper                                     # Perform XOR operation
        return new_bit

    def __str__(self):                                                  # Print encrypted result as a string
        appended_str = (self.register + str((self.step())))
        result = appended_str[1:]
        return result


def main():                                                             # Main method to check validity
    args = [['0110100111', 2], ['0100110010', 8], ['1001011101', 5],    # Arguments given in assignment
            ['0001001100', 1], ['1010011101', 7]]

    for arg in args:                                                    # Print loop for confirmation
        confirm = (LFSR(arg[0], arg[1]))
        print(confirm, confirm.step())


if __name__ == "__main__":
    main()