# This be my homework, homie
from functools import reduce

class ShapeException(Exception):
    print("This is invalid.  Shapes are not compatible")
    exit()
    pass


def dot(vec1, vec2):
    if shape(vec1) != shape(vec2):
        raise ShapeException()
    vec_for_addition = []
    vec_len = range(len(vec1))
    for x in vec_len:
        pos_multiplication = vec1[x] * vec2[x]
        vec_for_addition.append(pos_multiplication)
    dot_total = reduce(lambda x, y: x + y, vec_for_addition)
    return dot_total
    pass


def magnitude():
    pass


def shape(num1):
    for row in num1:
        num_rows = len(num1)
        if type == list:
            num_col = len(row)
            return num_rows, num_col
        else:
            return num_rows,
    pass


def vector_add(vec1, vec2):
    if shape(vec1) != shape(vec2):
        raise ShapeException
    else:
        output_vector = []
        for i in range(len(vec1)):
            output_num = vec1[i] + vec2[i]
            output_vector.append(output_num)
        return output_vector
    pass


def vector_sub():
    if shape(vec1) != shape(vec2):
        raise ShapeException
    else:
        output_vector = []
        for i in range(len(vec1)):
            output_num = vec1[i] - vec2[i]
            output_vector.append(output_num)
        return output_vector
    pass


def vector_sum(*args):
    vecs_total = []
    vec_len = len(args[0])
    for x in range(0, vec_len):
        replacement_num = 0
        for vec in args:
            replacement_num += vec[x]
        vecs_total.append(replacement_num)
    return vecs_total
    pass


def vector_multiply(vec, scalar):
    output_vector = []
        for i in range(len(vec)):
            output_num = vec[i] * scalar
            output_vector.append(output_num)
        return output_vector
    pass


def vector_mean():
    pass


def matrix_row(matrix, idx):
    row = matrix[idx]
    return row
    pass


def matrix_col(matrix, idx):
    col = [row[idx] for row in matrix]
    return col
    pass


def matrix_scalar_multiply(matrix, scalar)
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
