# anagrammer
This little utility embeds a dictionary into a program which spits out anagrams to its input.
It works by generating a Makefile, which in turn generates the program source and compiles it.
The dictionary is embedded as a large switch, the cases of which encode an anagram set based on prime multiplication.
This means that anagrammer should have constant time complexity.

## Usage
### Configuration
To configure, run `./configure.sh` from the directory where you wish to build.
The configuration script takes a mandatory positional dictionary argument as its final argument.
The dictionary must be a new-line separated sequence of words using only english letters.
The case is ignored.
For finding a good dictionary, I recommend [this google search](https://www.google.com/search?q=dictionary+filetype%3Atxt).
If the dictionary is especially large, you may need to use the `--max-memory memory` argument of `./configure.sh`.
This argument only works with gcc.

### Building
To build, simply run `make` in a configured build directory.
For a large dictionary, this will take some time.

### Installation
If you wish to install this program, make it available through the `PATH` environment variable.
Typically this means copying or moving it to a `PATH` directory, such as `/usr/local/bin`.
Another alternative is to append or prepend the program's directory to `PATH`.

### Invocation
To invoke `anagrammer`, assuming it's installed, run: `anagrammer arg`.
This will output all anagrams to `arg` in a comma-separated sequence.
Note that the argument does not need to be an english word, but may only contain english letters.
