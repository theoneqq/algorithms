class _const:
    class const_error(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.const_error("can't rebind const{}".format(name))
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.const_error("can't unbind const{}".format(name))
        raise NameError(name)

import sys
c = _const()
c.LUA_SIGNATURE = b'\x1bLua'
c.LUAC_VERSION = 0x53
c.LUAC_FORMAT = 0
c.LUAC_DATA = b'\x19\x93\r\n\x1a\n'
c.CINT_SIZE = 4
c.CSIZET_SIZE = 8
c.INSTRUCTION_SIZE = 4
c.LUA_INTEGER_SIZE = 8
c.LUA_NUMBER_SIZE = 8
c.LUAC_INT = 0x5678
c.LUAC_NUM = 370.5

sys.modules[__name__] = c
