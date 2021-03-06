from logpy import run, var, eq as unify, conde, Relation, fact
from logpy.goals import conso
from logpy.core import success, fail


def eq(a, b):
    """
    Simple assertion.
    I'm used to using this in my tests, and unused to unify being
    called eq, so I switched these around. Sorry.
    """
    assert a == b, "%s not equal to %s" % (a, b)


def test1():
    x = var()
    eq((5,), run(0, x,
                 unify(x, 5)))


def test2():
    x = var()
    z = var()
    eq((5,), run(0, x,
                 unify(x, z),
                 unify(z, 5)))


def test3():
    parent = Relation()
    male = Relation()

    def son(father, boy):
        return conde((parent(father, boy), male(boy)))

    fact(parent, "Abraham", "Isaac")
    fact(male, "Abraham")
    fact(male, "Isaac")

    x = var()
    assert ("Isaac",) == run(0, x, son("Abraham", x))


# Tests from the Reasoned Schemer:

def test_rs1_11():
    q = var()
    eq((True,), run(0, q, unify(True, q)))


def test_rs1_12():
    q = var()
    eq((), run(0, q, fail, unify(True, q)))


def test_rs1_13():
    q = var()
    eq((True,), run(0, q,
                    success,
                    unify(True, q)))
    

def test_rs1_16():
    q = var()
    eq(("corn",), run(0, q,
                      success,
                      unify("corn", q)))


def test_rs1_47():
    x = var()
    eq(("olive", "oil"), run(0, x,
                             conde((unify("olive", x),),
                                   (unify("oil", x),))))


def test_rs1_56():
    def teacupo(x):
        return conde((unify("tea", x),),
                     (unify("cup", x),))
    x = var()
    eq(("tea", "cup"), run(0, x, teacupo(x)))


def mvars(n):
    return tuple(var() for _ in range(n))


def cons(a, l):
    print a, type(a), l, type(l)
    return tuple((a, ) + l)


# def test_rs2_10():  # Doesn't work
#     r, x, y = mvars(3)
#     print run(0, r,
#               (heado, ("grape", "raisin", "pear"), x),
#               (heado, (("a",), ("b",), ("c",)), y),
#               (conde, [(eq, x, r[0]), (eq, y, r[1:])]))
    

def test_rs2_24():
    r, x, y, z = mvars(4)
    eq((("e", "a", "d", "c"),), run(0, r,
                                    unify(("e", "a", "d", x), r),
                                    conso(y, ("a", z, "c"), r)))
