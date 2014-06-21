class Double(object):
    def __init__(self, *args):
        if len(args) >= 1:
            self._name = args[0]

    def __repr__(self):
        address = hex(id(self))

        if hasattr(self, '_name'):
            return '<Double of {!r} object at {}>'.format(self._name, address)
        else:
            return '<Double object at {}>'.format(address)
