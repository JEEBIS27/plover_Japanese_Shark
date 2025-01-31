KEYS = (
'1-','2-','3-','4-','5-',
'*-', 'T-', 'K-', 'H-', 'S-', 'Y-', 'I-', 'O-', 'i-', 'u-', 't-', 'k-',
'#',
'-6','-7','-8','-9','-0',
'-*', '-T', '-K', '-H', '-S', '-Y', '-I', '-O', '-i', '-u', '-t', '-k',
)

IMPLICIT_HYPHEN_KEYS = ('#')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*-')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Keyboard': {
        '1-' : '1',
        '2-' : '2',
        '3-' : '3',
        '4-' : '4',
        '5-' : '5',
        '*-' : 'q',
        'T-' : 'w',
        'K-' : 's',
        'H-' : 'e',
        'S-' : 'd',
        'Y-' : 'a',
        'I-' : 'c',
        'O-' : 'v',
        'i-' : 'r',
        'u-' : 'f',
        't-' : 't',
        'k-' : 'g',
        '#'  : 'b',
        '-6' : '6',
        '-7' : '7',
        '-8' : '8',
        '-9' : '9',
        '-0' : '0',
        '-*' : 'p',
        '-T' : 'o',
        '-K' : 'l',
        '-H' : 'i',
        '-S' : 'k',
        '-Y' : ';',
        '-I' : 'm',
        '-O' : 'n',
        '-i' : 'u',
        '-u' : 'j',
        '-t' : 'y',
        '-k' : 'h',
        'arpeggiate' : 'space',
        'no-op': ('\'','[',']','/')
        }
}


DICTIONARIES_ROOT = 'asset:plover_Japanese_Shark:dictionaries'
DEFAULT_DICTIONARIES = ('Plover_Japanese_Shark_.py','abbreviation_for_Shark.json','commands_for_Shark.json')
