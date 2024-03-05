# HW 3. Functions 

### Description
This readme describes the program dna_rna_tools.py designed to perform various transformations on nucleic acid sequences.

The program takes any number of arguments containing DNA or RNA sequences, along with the name of the procedure to be performed. For example, `run_dna_rna_tools('ATG', 'transcribe')`.
All arguments should be entered sequentially, separated by commas. The name of the procedure to be performed should be entered last.

**List of possible procedures**

- `transcribe` — this function takes a DNA sequence as input and converts it from nucleotides to RNA nucleotides based on complementarity.
- `reverse` — this function takes a DNA or RNA sequence as input and reverses it.
- `complement` — this function takes a DNA or RNA sequence as input and generates its complementary sequence.
- `reverse_complement` — this function takes a DNA or RNA sequence as input, generates its complementary sequence, and then reverses it.

**Usage example**

```python
run_dna_rna_tools('ATG', 'transcribe')
run_dna_rna_tools('ATG', 'aT', 'reverse')
run_dna_rna_tools('AtG', 'complement')
run_dna_rna_tools('ATg', 'reverse_complement')