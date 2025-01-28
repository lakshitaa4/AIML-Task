#dot product
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	m1, n1 = len(a), len(a[0])
	m2 = len(b)
	if n1 != m2:
		return -1
	c = []
	for i in a:
		hold = 0
		for j in range(len(i)):
			hold += (i[j] * b[j])
		c.append(hold)
	return c

#transpose
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = []
	m, n = len(a), len(a[0])
	for i in range(n):
		p = []
		for j in range(m):
			p.append(a[j][i])
		b.append(p)
			
	return b

#reshape
def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    flat = [elem for row in a for elem in row] 
    total_elements = len(flat)
    r, c = new_shape

    if total_elements != r * c:
        raise ValueError("Cannot reshape matrix")

    reshaped_matrix = [flat[i * c : (i + 1) * c] for i in range(r)]
    return reshaped_matrix

#mean by row or column
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for i in matrix:
			means.append(sum(i) / len(i))
	elif mode == 'column':
		for j in range(len(matrix[0])):
			s = 0
			for i in range(len(matrix)):
				s += matrix[i][j]
			means.append(s / len(matrix))
	else:
		raise ValueError("GIve correct mode")
	return means


#scalar * matrix
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] *= scalar
	return matrix
