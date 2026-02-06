import pathlib

source = pathlib.Path("kernel.py").read_text()

code = compile(source, "teste.py", "exec")

print(code.co_code)