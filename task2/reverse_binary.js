function reverseBinary(number) {
    // Convert the number to binary representation
    let binaryString = number.toString(2);

    // Reverse the binary string
    let reversedBinaryString = binaryString.split('').reverse().join('');

    // Convert the reversed binary string back to a number
    let reversedNumber = parseInt(reversedBinaryString, 2);

    return reversedNumber;
}

// Example usage:
let originalNumber = 14;
let reversedNumber = reverseBinary(originalNumber);

console.log(`Original Number: ${originalNumber}`);
console.log(`Reversed Binary: ${reversedNumber}`);