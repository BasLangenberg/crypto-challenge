import codecs
import base64


def hex_to_base64(hex_string):
    hex_decode = codecs.decode(hex_string, 'hex_codec')
    return base64.b64encode(hex_decode)
