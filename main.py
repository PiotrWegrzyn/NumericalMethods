from math import *
from typing import List


def f(function_string: str, x: float) -> float:
    """ Expecting function_string to contain a function string with x variable like so: 'sin(x) + x' """
    return eval(function_string)


def print_io(func):
    def inner1(*args, **kwargs):
        returned_value = func(*args, **kwargs)

        parts = f', n = {args[3]}' if len(args) == 4 else ''
        try:
            print(f'Input:\nFunction: {args[0]}, <{args[1]}, {args[2]}> {parts}\nOutput:{returned_value}')
        except IndexError:
            pass
        return returned_value

    return inner1


@print_io
def rectangular_integration(fun: str, start: float, end: float, parts: int) -> float:
    """Rectangular integration ā«<a-b>š(š„)dxāsā<i=0 n-1>š(š„š +2š ), s = b-a/n """
    part_distance = (end - start) / parts
    tmp = 0
    for i in range(parts):
        xi = start + (i * part_distance)
        tmp += f(fun, xi + (0.5 * part_distance))

    return part_distance * tmp


@print_io
def trapezoid_integration(fun: str, start: float, end: float, parts: int) -> float:
    """Trapezoid integration ā«<a-b>š(š„)dxā (b-a/2)(š(š) + š(š)) """

    part_distance = (end - start) / parts
    tmp = 0
    for i in range(parts):
        t_start = start + (i * part_distance)
        t_end = t_start + part_distance
        tmp += part_distance / 2 * (f(fun, t_start) + f(fun, t_end))

    return tmp


def get_node_weights(nodes: int) -> List[float]:
    if nodes == 2:
        return [1,1]
    if nodes == 4:
        return [
            (1/36)*(18-sqrt(30)),
            (1/36)*(18+sqrt(30)),
            (1/36)*(18+sqrt(30)),
            (1/36)*(18-sqrt(30)),
        ]


def get_nodes(nodes: int) -> List[float]:
    if nodes == 2:
        return [-sqrt(3) / 3, sqrt(3) / 3]
    if nodes == 4:
        return [
            (-1/35) * sqrt(525-(-70*sqrt(30))),
            (-1/35) * sqrt(525+(-70*sqrt(30))),
            (1/35) * sqrt(525+(-70*sqrt(30))),
            (1/35) * sqrt(525-(-70*sqrt(30))),
        ]


@print_io
def gauss_lagendre_integration(fun: str, start: float, end: float, parts: int) -> float:
    """Trapezoid integration ā«<a-b>š(š„)dxā (b-a/2)(š(š) + š(š)) """
    weights = get_node_weights(parts)
    nodes = get_nodes(parts)
    middle = (end-start)/2

    tmp = 0
    for i in range(parts):
        ti = (start+end)/2 + (middle * nodes[i])
        tmp += weights[i] * f(fun, ti)

    return middle * tmp


@print_io
def simp_integration(fun: str, start: float, end: float) -> float:
    """Simpson integration ā«<a-b>š(š„)dxā (b-a/6) (š(š)+4š( (a+b)/2 )+š(š))"""
    return (end - start) / 6 * (f(fun, start) + (4 * f(fun, (start + end) / 2)) + f(fun, end))


if __name__ == "__main__":
    print("Rectangular integration:")
    rectangular_integration("sin(x)", 0.5, 2.5, 4)
    rectangular_integration("x**2+2*x+5", 0.5, 5, 4)
    rectangular_integration("exp(x)", 0.5, 5, 4)

    print("\nTrapezoid integration:")
    trapezoid_integration("sin(x)", 0.5, 2.5, 4)
    trapezoid_integration("x**2+2*x+5", 0.5, 5, 4)
    trapezoid_integration("exp(x)", 0.5, 5, 4)

    print("\nSimpson integration:")
    simp_integration("sin(x)", 0.5, 2.5)
    simp_integration("x**2+2*x+5", 0.5, 5)
    simp_integration("exp(x)", 0.5, 5)

    print("\nGauss Lagendre integration 2 nodes version:")
    gauss_lagendre_integration("sin(x)", 0.5, 2.5, 2)
    gauss_lagendre_integration("x**2+2*x+5", 0.5, 5, 4)
    gauss_lagendre_integration("exp(x)", 0.5, 5, 4)

    print("\nGauss Lagendre integration 4 nodes version:")
    gauss_lagendre_integration("sin(x)", 0.5, 2.5, 4)
    gauss_lagendre_integration("x**2+2*x+5", 0.5, 5, 4)
    gauss_lagendre_integration("exp(x)", 0.5, 5, 4)