import binchunk
class reader():
    data = bytearray()
    def read_byte(self):
        b = self.data[0]
        self.data = self.data[1:]
        return b

    def read_bytes(self, n):
        bs = self.data[:n]
        self.data = self.data[n:]
        return bs

    def read_uint32(self):
        i = int.from_bytes(self.data[:4], byteorder='little')
        self.data = self.data[4:]
        return i

    def read_uint64(self):
        i = int.from_bytes(self.data[:8], byteorder='little')
        self.data = self.data[8:]
        return i

    def read_lua_integer(self):
        return self.read_uint64()

    def read_lua_number(self):
        i = self.read_uint64()
        return float(i)

    def read_string(self):
        size = int(self.read_byte())
        if size == 0:
            return ""
        if size == 0xff:
            size = self.read_uint64()
        bs = self.read_bytes(size - 1)
        return bs.decode()

    def check_header(self):
        if self.read_bytes(4).decode() != binchunk.LUA_SIGNATURE:
            print("not a precompiled chunk!")
        elif self.read_byte() != binchunk.LUAC_VERSION:
            print("version mismatch!")
        elif self.read_byte() != binchunk.LUAC_FORMAT:
            print("format mismatch!")
        elif self.read_bytes(6).decode() != binchunk.LUAC_DATA:
            print("corrupted!")
        elif self.read_byte() != binchunk.CINT_SIZE:
            print("int size mismatch!")
        elif self.read_byte() != binchunk.CSIZET_SIZE:
            print("size_t size mismatch!")
        elif self.read_byte() != binchunk.INSTRUCTION_SIZE:
            print("instruction size mismatch!")
        elif self.read_byte() != binchunk.LUA_INTEGER_SIZE:
            print("lua integer size mismatch!")
        elif self.read_byte() != binchunk.LUA_NUMBER_SIZE:
            print("lua number size mismatch!")
        elif self.read_lua_integer() != binchunk.LUAC_INT:
            print("endianners mismatch!")
        elif self.read_lua_number() != binchunk.LUAC_NUM:
            print("float format mismatch!")

if __name__ == "__main__":
    r = reader()
    """
    r.data = bytearray(b'a1234123412345hello')
    print(r.read_byte())
    print(r.read_uint32())
    print(r.read_lua_number())
    print(r.read_string())
    """

    r.data = bytearray(b'\x1bLua\x53\x00\x19\x93\x0d\x0a\x1a\x0a\x04\x08\x04\x08\x04\x08\x08\x56\x78\x00\x00\x00\x00\x00\x28\x77')
    r.check_header()
