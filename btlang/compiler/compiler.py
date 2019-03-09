from ast import literal_eval
from bytecode import Instr, Bytecode
from lark import Transformer


class Compiler(Transformer):
    def literal(self, tokens):
        token = tokens.pop()
        return Instr("LOAD_CONST", literal_eval(token))

    def name(self, tokens):
        token = tokens.pop()
        return Instr("LOAD_NAME", token.value.strip("`"))

    def spec(self, tokens):
        return list(tokens)

    def call(self, tokens):
        func = tokens.pop(0)
        if len(tokens) > 0:
            spec = tokens.pop()
        else:
            spec = []

        return Bytecode(
            [func, *spec, Instr("CALL_FUNCTION", len(spec)), Instr("RETURN_VALUE")]
        )

    def compile(self, *args, **kwargs):
        return super().transform(*args, **kwargs).to_code()
