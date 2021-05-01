# Steganography with Python and PIL

Encoding and decoding on the red channel with the LSB

## Notes on Bitwise Operations
Operator | Name |	Description	| Example
-|-|-|-|
`&` | `AND` | copies bit if exists in **BOTH** operands |	`a & b`
`\|` | `OR` | copies bit if exists in **EITHER** operand.	| `a \| b`
`^` |  `XOR` |	copies bit if in **ONE BUT NOT BOTH**. |	`a ^ b`
`~` | Unary Complement | Has the effect of **'FLIPPING'** bits. |	`~ a`
`<<` |  Binary Left Shift |	left value is moved left by num bits of right value. |	`a << 2` 
`>>` | Binary Right Shift	|  left value is moved right by num bits of right value. |	`a >> 2`
