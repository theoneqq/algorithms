class header():
    pass

class chunck():
    pass

class proto():
    def __init__(self, source, line_defined, last_line_defined, num_params, is_vararg, max_stack_size, code, constants, upvalues, protos, line_info, loc_vars, upvalue_names):
        self.source = source
        self.line_defined = line_defined
        self.last_line_defined = last_line_defined
        self.num_params = num_params
        self.is_vararg = is_vararg
        self.max_stack_size = max_stack_size
        self.code = code
        self.constants = constants
        self.upvalues = upvalues
        self.protos = protos
        self.line_info = line_info
        self.loc_vars = loc_vars
        self.upvalue_names = upvalue_names
