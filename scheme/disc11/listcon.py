class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def link_con(a,b):
    if a is Link.empty:
        return b
    else:
        return Link(a.first, link_con(a.rest,b))

def link_remove(a,b):
    assert type(a) == type(3)
    if b is Link.empty:
        return Link.empty
    elif a != b.first:
        return Link(b.first, link_remove(a,b.rest))
    else:
        return link_remove(a,b.rest)

def link_dup(a):
    if a is Link.empty:
        return Link.empty
    else:
        return Link(a.first, Link(a.first, link_dup(a.rest)))

a = Link(1,Link(2,Link(3)))
print(link_dup(a))

