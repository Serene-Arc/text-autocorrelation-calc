# Text Autocorrelation Calculator

This is a simple tool to calculate the autocorrelation of a string of text. This is useful in the cryptanalysis of certain ciphers such as the Vigenere cipher.

The tool can be run with the following command, and outputs to a corresponding output file.

```bash
python3 -m autocorrelationcalc <cipher-file-1> ... <cipher-file-n>
```

## Options

The following options are available.

- `-s, --include-spaces` is a flag to include spaces in the analysis of the text; they are otherwise stripped out
- `-c, --case-sensitive` is a flag to keep case intact for the analysis of characters