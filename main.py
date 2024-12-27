import re
import argparse
import os
import tokenize
import io
import untokenize

# Remove the compiled file if it exists
if os.path.exists("compiled.py"):
    os.remove("compiled.py")

# Gen Z slang dictionary with new slang words for control structures and functions
rizz_slang = {
    "flex": "print",  # 'flex' is for 'print'
    "vibe": "def",  # 'vibe' is for 'def'
    "bet": "if",  # 'bet' is for 'if'
    "nobet": "elif",  # 'bet' is for 'if'
    "nocap": "else",  # 'no cap' is for 'else'
    "squad": "for",  # 'squad' is for 'for'
    "grind": "while",  # 'grind' is for 'while'
    "bounce": "break",  # 'bounce' is for 'break'
    "chill": "continue",  # 'chill' is for 'continue'
    "dip": "return",  # 'dip' is for 'return'
    "pause": "pass",  # 'pause' is for 'pass'
    "slide": "import",  # 'slide' is for 'import'
    "block": "try",  # 'block' is for 'try'
    "fade": "except",  # 'fade' is for 'except'
    "glow": "assert",  # 'glow' is for 'assert'
    "lit": "True",  # 'lit' is for 'True'
    "sus": "False",  # 'sus' is for 'False'
    "flexin": "len",  # 'flexin' is for 'len()'
    "loop": "range",  # 'loop' is for 'range()'
    "fam": "in",  # 'fam' is for 'in'
    "slay": "not",  # 'slay' is for 'not'
    "real": "and",  # 'real' is for 'and'
    "cap": "or",  # 'cap' is for 'or'
}

# Argument parsing to handle input files
parser = argparse.ArgumentParser()
parser.add_argument("file", type=argparse.FileType("r"))
args = parser.parse_args()

def run(runfile):
    """Execute the compiled Python code."""
    with open(runfile, "r") as rnf:
        exec(rnf.read())

def interpret(rizz_code):
    """Translate Rizz slang to valid Python code."""
    tokens = list(tokenize.generate_tokens(io.StringIO(rizz_code).readline))
    for i, token in enumerate(tokens):
        # Replace the slang with the correct Python syntax
        for slang, replacement in rizz_slang.items():
            if token.string == slang:
                tokens[i] = (token[0], replacement, token[2], token[3], token[4])
    
    # Untokenize to convert back to Python code
    python_code = untokenize.untokenize(tokens)
    
    return python_code

# Read the input file and process it
with args.file as rizz:
    rizz_code = rizz.read()
    
    # Translate Rizz code to Python code
    python_code = interpret(rizz_code)
    
    # Write the compiled Python code to a file
    with open("compiled.py", "w") as py:
        py.write(python_code)

# Run the compiled Python code
run("compiled.py")
