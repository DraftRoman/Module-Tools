Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 1000 + 0100 + 0010 = 1110 = 8 + 4 + 2 = 14

Convert the binary number 101101 to decimal:
Answer: 2^5 + 2^3 + 2^2 + 2^0 = 32 + 8 + 4 + 1 = 45

Which is larger: 1000 or 0111?
Answer: 1000 because 1000 is 8 and 0111 is 7

Which is larger: 00100 or 01011?
Answer: 01011 because 01011 is 11 and 00100 is 4

What is 10101 + 01010?
Answer: 11111

What is 10001 + 10001?
Answer: 100010

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 1111

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 2^8 = 256. So, we need 7 bits. b0000000 = 0, and b1111111 = 255

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer: 2 bits as 00 = 0, and 11 = 3

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer: 2^9 = 512
2^8 = 256  
 2^7 = 128  
 2^6 = 64
2^3 = 8
512 + 256 + 128 + 64 + 32 + 8 = 1000
b1111101000 = 1000
we need 10 bits

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: 1, 10, 100, 1000, 10000
1, 2, 4, 8, 16
If the binary starts with 1 or 1 followed by 0s, it will be a power of two.
We can use regexp to test the binary number.

        function testPowerOfTwo(binaryNumber) {
            return /^0*10*$/.test(String(binaryNumber))
        }

Convert the decimal number 14 to hex.
Answer: 10 = A, 11 = B, 12 = C, 13 = D, 14 = E

Convert the decimal number 386 to hex.
Answer: F = 15,
386 / 15 = 25.7333
386 - (F * 25) = 11
So, 386 = F*25+B

Convert the hex number 386 to decimal.
Answer:

Convert the hex number B to decimal.
Answer:

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer:

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer:

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer:
