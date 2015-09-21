# This be my homework, homie
class ShapeException(Exception):
    pass


def dot():
    pass


def magnitude():
    pass


def shape():
    pass


def vector_add():
    pass


def vector_sub():
    pass


def vector_sum():
    pass


def vector_multiply():
    pass


def vector_mean():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply(matrix, scalar):
    scalar = -1
    output_matrix = []
    for row in matrix:
        output_row = []
        for column in row:
            calculated_value = column * scalar
            output_row.append(calculated_value)
        output_matrix.append(output_row)
    return output_matrix
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
