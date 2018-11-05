regex = r'''
    (?xim)
    (^.*$\s*)*

    ^
    ((?P<filename>\S+)\s+)?
    (?P<line>\d+)
    :?
    (?P<col>\d+)?
    \s*
    (?P<rule>\w+)?
    \s*
    ((?P<warning>warning)|(?P<error>error))
    \s*
    (?P<message>.+)
    $\s*
'''
