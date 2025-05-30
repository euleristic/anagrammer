import sys

if len(sys.argv) != 3:
    print(f"usage: python3 {sys.argv[0]} <dictionary> <output>", file=sys.stderr)
    exit(1)

with open(sys.argv[1]) as file:
    words_raw = file.read()

character_order = "esiarntolcdugpmhbyfvkwzxjq"

words = words_raw.lower().splitlines()

primes = [2, 3]
for _ in range(len(character_order) - 2):
    candidate = primes[-1] + 2
    while not all([candidate % p for p in primes]):
        candidate += 1
    primes += [candidate]

chr_prime_map = dict(zip(character_order, primes))

def to_key(word):
    result = 1
    for c in word:
        if c not in character_order:
            return -1
        result *= chr_prime_map[c]
    return result

word_map = {}

for word in words:
    key = to_key(word)
    if key not in word_map:
        word_map[key] = []
    word_map[key] += [word]

integer_type = "__uint128_t" if max(word_map.keys()) >= 1 << 64 else "unsigned long long"

with open(sys.argv[2], "w") as output:
    output.write("#include <stdio.h>\n\n")
    output.write(f"typedef {integer_type} integer_type;\n\n")
    output.write("int main(int argc, char **argv) {\n")
    output.write("    if (argc != 2) {\n")
    output.write("        fprintf(stderr, \"usage: <word>\\n\");\n")
    output.write("        return 1;\n")
    output.write("    }\n")
    output.write("    integer_type product = 1;\n")
    output.write("    for (char *c = argv[1]; *c; ++c) {\n")
    output.write("        switch (*c) {\n")
    for c in character_order:
        output.write(" " * 12 + f"case '{c}': product *= {to_key(c)}; break;\n")
    output.write(" " * 12 + "default:\n")
    output.write(" " * 16 + "fprintf(stderr, \"Unsupported character '%c'.\", *c);\n")
    output.write(" " * 16 + "return 2;\n")
    output.write("        }\n")
    output.write("    }\n")
    output.write("    switch (product) {\n")
    for key in word_map:
        if integer_type == "uint64_t":
            output.write(f"        case {key}lu:\n")
        else:
            if key <= 1 << 64:
                output.write(f"        case ((integer_type){key}lu):\n")
            else:
                output.write(f"        case ((integer_type){key >> 64} << 64) | {key & 0xFFFFFFFFFFFFFFFF}lu:\n")
        output.write(" " * 12 + f"printf(\"{', '.join(word_map[key])}\\n\");\n")
        output.write(" " * 12 + "break;\n")
    output.write("    }\n")
    output.write("    return 0;\n")
    output.write("}\n")
