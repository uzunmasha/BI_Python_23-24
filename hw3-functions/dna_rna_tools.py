def check_nucleotides(string):
    dna_chars = set('CAGTcagt')
    rna_chars = set('CAGUcagu')

    is_dna = True
    is_rna = True

    for sequence in string:
        for char in sequence:
            if char not in dna_chars:
                is_dna = False
                break
        if not is_dna:
            break

    for sequence in string:
        for char in sequence:
            if char not in rna_chars:
                is_rna = False
                break
        if not is_rna:
            break

    dna = None
    rna = None

    if is_dna and not is_rna:
        dna = string
    elif is_rna and not is_dna:
        rna = string
    elif is_rna and is_dna:
        additional_input = input("Is this DNA or RNA?: ")
        if additional_input == 'DNA':
            dna = string
        elif additional_input == 'RNA':
            rna = string
        else:
            print("Input 'DNA' or 'RNA'")
    else:
        print("Neither DNA nor RNA")
    return dna, rna


def transcribe(dna):
    transcription_map = {"A": "A", "T": "U", "G": "G", "C": "C", "a": "a", "t": "u", "g": "g", "c": "c"}
    transcr_rna = []
    for sequence in dna:
        transcr_sequence = ""
        for nucleotide in sequence:
            if nucleotide in transcription_map:
                transcr_sequence += transcription_map[nucleotide]
            else:
                transcr_sequence += nucleotide
        transcr_rna.append(transcr_sequence)
    return transcr_rna


def reverse(dna, rna):
    if dna is not None:
        rev_dna = []
        for sequence in dna:
            reversed_sequence = sequence[::-1]
            rev_dna.append(reversed_sequence)
        return rev_dna
    elif rna is not None:
        rev_rna = []
        for sequence in rna:
            reversed_sequence = sequence[::-1]
            rev_rna.append(reversed_sequence)
        return rev_rna
    else:
        return "Empty string"


def complement(dna, rna):
    comp_map_dna = {"A": "T", "G": "C", "T": "A", "C": "G", "a": "t", "t": "a", "g": "c", "c": "g"}
    comp_map_rna = {"A": "U", "G": "C", "U": "A", "C": "G", "a": "u", "u": "a", "g": "c", "c": "g"}
    compl_seq = []

    if dna is not None:
        for sequence in dna:
            complemented_sequence = ''
            for nucl in sequence:
                if nucl in comp_map_dna:
                    complemented_sequence += comp_map_dna[nucl]
                else:
                    complemented_sequence += nucl
            compl_seq.append(complemented_sequence)
        return compl_seq
    elif rna is not None:
        for sequence in rna:
            complemented_sequence = ''
            for nucl in sequence:
                if nucl in comp_map_rna:
                    complemented_sequence += comp_map_rna[nucl]
                else:
                    complemented_sequence += nucl
            compl_seq.append(complemented_sequence)
        return compl_seq
    else:
        return "Empty string"


def reverse_complement(dna, rna):
    comp_map_dna = {"A": "T", "G": "C", "T": "A", "C": "G", "a": "t", "t": "a", "g": "c", "c": "g"}
    comp_map_rna = {"A": "U", "G": "C", "U": "A", "C": "G", "a": "u", "u": "a", "g": "c", "c": "g"}
    compl_seq_rev = []

    if dna is not None:
        for sequence in dna:
            complemented_sequence = ''
            for nucl in sequence:
                if nucl in comp_map_dna:
                    complemented_sequence += comp_map_dna[nucl]
                else:
                    complemented_sequence += nucl
            compl_seq_rev.append(complemented_sequence[::-1])
        return compl_seq_rev
    elif rna is not None:
        for sequence in rna:
            complemented_sequence = ''
            for nucl in sequence:
                if nucl in comp_map_dna:
                    complemented_sequence += comp_map_rna[nucl]
                else:
                    complemented_sequence += nucl
            compl_seq_rev.append(complemented_sequence[::-1])
        return compl_seq_rev
    else:
        return "Empty string"


def run_dna_rna_tools(*args):
    sequences = args[:-1]
    string = [value.strip().strip("'") for value in sequences]
    operation = args[-1]
    dna, rna = check_nucleotides(string)

    if operation == "transcribe":
        transcribe_result = transcribe(dna)
        if len(transcribe_result) > 1:
            return list(transcribe_result)
        else:
            return transcribe_result[0]

    if operation == "reverse":
        reverse_result = reverse(dna, rna)
        if len(reverse_result) > 1:
            return list(reverse_result)
        else:
            return reverse_result[0]

    if operation == "complement":
        complement_result = complement(dna, rna)
        if len(complement_result) > 1:
            return list(complement_result)
        else:
            return complement_result[0]

    if operation == "reverse_complement":
        reverse_complement_result = reverse_complement(dna, rna)
        if len(reverse_complement_result) > 1:
            return list(reverse_complement_result)
        else:
            return reverse_complement_result[0]
