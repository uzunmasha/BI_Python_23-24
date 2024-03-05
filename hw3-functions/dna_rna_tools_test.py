from dna_rna_tools import run_dna_rna_tools


def test_transcribe():
    assert run_dna_rna_tools('ATG', 'transcribe') == 'AUG'


def test_reverse():
    assert run_dna_rna_tools('ATG', 'reverse') == 'GTA'


def test_complement():
    assert run_dna_rna_tools('AtG', 'complement') == 'TaC'


def test_reverse_complement():
    assert run_dna_rna_tools('ATg', 'reverse_complement') == 'cAT'


def test_multiple_args():
    assert run_dna_rna_tools('ATG', 'aT', 'reverse') == ['GTA', 'Ta']
