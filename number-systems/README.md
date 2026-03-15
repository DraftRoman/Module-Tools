Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer: 2^4 = 16,
so I should start with 2^3 = 8 (1000),
14 - 8 = 6,
6 - 2^2 (0100)= 2 (0010)
14 = 1000 + 0100 + 0010 = 1110

Convert the binary number 101101 to decimal:
Answer: 2^5 + 2^3 + 2^2 + 2^0 = 32 + 8 + 4 + 1 = 45

Which is larger: 1000 or 0111?
Answer: 1000 is larger because 1000 has more places

Which is larger: 00100 or 01011?
Answer: 01011 is larger because the leading number is 01 instead of 00, and they both have 5 bits.

What is 10101 + 01010?
Answer: 11111

What is 10001 + 10001?
Answer: 100010

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer: 1111 = 15

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer: 2^8 = 256. So, we need 8 bits. b00000000 = 0, and b11111111 = 255

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
If the binary number is 1 or 1 followed by 0s, it will be a power of two.
We can use regexp to test the binary number.

function testPowerOfTwo(binaryNumber) {
return /^0*10*$/.test(String(binaryNumber))
}

Convert the decimal number 14 to hex.
Answer: 10 = A, 11 = B, 12 = C, 13 = D, 14 = E

Convert the decimal number 386 to hex.
Answer: 386 - 16^2 = 130
130 - 16 x 8 = 2
hex: 182

Convert the hex number 386 to decimal.
Answer: 3 x 16^2 + 8 x 16 + 6 x 1 = 902

Convert the hex number B to decimal.
Answer: 11

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer: 2 x 16 + 1 X 1 = 33

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: As the byte 0x21 is 33 in decimal, which is in the range of 0 full black to 255 full white. The color is close to black.

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: AA (170) means middle high red, 00 means no green, and FF (255) means full blue. The colour should be purple.

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 170, 0, 255
