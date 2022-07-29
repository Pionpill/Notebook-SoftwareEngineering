# Reference: https://github.com/faif/python-patterns/blob/master/patterns/behavioral/visitor.py


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = f"visit_{cls.__name__}"
            meth = getattr(self, meth_name, None)
            if meth:
                break
        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print(f"generic_visit {node.__class__.__name__}")

    def visit_B(self, node, *args, **kwargs):
        print(f"visit_B {node.__class__.__name__}")


if __name__ == "__main__":
    a, b, c = A(), B(), C()
    visitor = Visitor()
    visitor.visit(a)  # generic_visit A
    visitor.visit(b)  # visit_B B
    visitor.visit(c)  # visit_B C
