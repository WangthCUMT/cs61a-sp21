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

a = Link(Link(1),Link(2,Link(3)))


def link_subsititute(lnk, old, new):
    if lnk is Link.empty:
        return Link.empty
    elif isinstance(lnk.first,Link):
        return Link(link_subsititute(lnk.first,old,new), link_subsititute(lnk.rest,old,new))
    elif lnk.first == old:
        return Link(new, link_subsititute(lnk.rest,old,new))
    else:
        return Link(lnk.first, link_subsititute(lnk.rest,old,new))

def link_count(lnk):
    if lnk is Link.empty:
        return 0
    elif isinstance(lnk.first, Link):
        return link_count(lnk.first) + link_count(lnk.rest)
    else:
        return 1 + link_count(lnk.rest)

print(link_count(a))