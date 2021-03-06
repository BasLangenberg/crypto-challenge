import set1


# Challenge 1
def test_hex_to_base64():
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    assert set1.hex_to_base64(input) == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


# Challenge 2
def test_xor_string():
    s1 = '1c0111001f010100061a024b53535009181c'
    s2 = '686974207468652062756c6c277320657965'
    expect = '746865206b696420646f6e277420706c6179'

    assert set1.xor_hex(s1, s2) == hex(int(expect, 16))
