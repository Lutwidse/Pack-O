import codecs, dis

def rot13(code_snippets):
    return codecs.encode(code_snippets, 'rot_13')

def encrypt_py():
    with open("app\hello_world.py", "r") as a, open("app\hello_world_rot13.py", "w") as b:
        instructions = [line for line in a.readlines()]
        [b.write(rot13(i)) for i in instructions]

def execute_encrypted_py():
    with open("app\hello_world_rot13.py", "r") as f:
            [eval(compile(rot13(i), "<string>", "exec")) for i in f.readlines()]
def main():
    encrypt_py()
    execute_encrypted_py()

if __name__ == "__main__":
    main()