function reverseBinary(number) {
    // Convert the number to binary representation
    let binaryString = number.toString(2);

    // Reverse the binary string
    let reversedBinaryString = binaryString.split('').reverse().join('');

    // Convert the reversed binary string back to a number
    let reversedNumber = parseInt(reversedBinaryString, 2);

    return reversedNumber;
}

//Get argument from process shell
const decimalNumber = process.argv[2];

// Check if a valid number is provided as an argument
if (isNaN(decimalNumber)) {
    console.log('Please provide a valid number as a command line argument.');
} else {
    // Call the function and print the result
    const result = reverseBinary(parseInt(decimalNumber));
    console.log(`The reversed binary representation of ${decimalNumber} is: ${result}`);
}