import binascii

def disassemble(code):
    offset = 0
    while offset < len(code):
        opcode = code[offset]

        if opcode == 0x00:
            print(f'{offset:04X}: nop')
            offset += 1

        elif opcode == 0xC3:
            print(f'{offset:04X}: ret')
            offset += 1

        elif opcode == 0xE8:
            operand = int.from_bytes(code[offset+1:offset+5], byteorder='little', signed=True)
            target = offset + 5 + operand
            print(f'{offset:04X}: call {target:04X}')
            offset += 5

        elif opcode == 0x83 and code[offset+1] == 0xEC:
            operand = code[offset+2]
            print(f'{offset:04X}: sub esp, {operand}')
            offset += 3

        else:
            print(f'{offset:04X}: {binascii.hexlify(code[offset:offset+4]).decode()}')
            offset += 4

# example code
code = b'\x55\x8B\xEC\x83\xEC\x08\xE8\x00\x00\x00\x00\x83\xC4\x08\xC3'
disassemble(code)
