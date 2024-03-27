''' * Problem Statement                                            *
 * Have the function OffBinary(strArr) read the array of strings* 
 * stored in strArr, which will contain two elements, the first *
 * will be a positive decimal number and the second element will* 
 * be a binary number. Your goal is to determine how many digits* 
 * in the binary number need to be changed to represent the     *
 * decimal number correctly (either 0 change to 1 or vice versa)*
 *                                                              * 
 * For example: if strArr is ["56", "011000"] then your program *
 * should return 1 because only 1 digit needs to change in the  *
 * binary number (the first zero needs to become a 1) to        *
 * correctly represent 56 in binary.                            *
 *                                                              *
 * Examples                                                     *
 * Input 1: ["5624", "0010111111001"]                           *
 * Output 1: 2                                                  *
 *                                                              *
 * Input 2: ["44", "111111"]                                    *
 * Output 2: 3                                                  *
 *                                                              *'''
def OffBinary(strArr):
    return sum(a != b for a, b in zip(bin(int(strArr[0]))[2:].zfill(len(strArr[1])), strArr[1].zfill(len(bin(int(strArr[0]))[2:]))))

# Example usage:
print(OffBinary(["5624", "0010111111001"]))  # Output: 2
print(OffBinary(["44", "111111"]))           # Output: 3




-------------------or--------------------------------------------------------or-------------------------------------








def OffBinary(strArr):
    s1 = strArr[0]
    s2 = strArr[1]
    k1 = bin(int(s1))[2:]
    max_length = max(len(k1), len(s2))
    k1_padded = k1.zfill(max_length)
    s2_padded = s2.zfill(max_length)
    
    # Use the alternative method for counting differing bits
    differing_bits = sum(1 for i in range(max_length) if k1_padded[i] != s2_padded[i])
    
    return differing_bits

# Example usage
print(OffBinary(["5624", "0010111111001"]))  # Expected output: 2
print(OffBinary(["44", "111111"]))           # Expected output: 3
