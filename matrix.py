"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    translation_matrix = new_matrix()
    ident(translation_matrix)
    translation_matrix[3][0] = x
    translation_matrix[3][1] = y
    translation_matrix[3][2] = z
    return translation_matrix


def make_scale( x, y, z ):
    dilation_matrix = new_matrix()
    ident(dilation_matrix)
    dilation_matrix[0][0] = x
    dilation_matrix[1][1] = y
    dilation_matrix[2][2] = z
    return dilation_matrix

def make_rotX( theta ):
    rotation_matrix = new_matrix()
    ident(rotation_matrix)
    theta = math.radians(theta)
    rotation_matrix[1][1] = math.cos(theta)
    rotation_matrix[2][2] = math.cos(theta)
    rotation_matrix[1][2] = math.sin(theta)
    rotation_matrix[2][1] = -1 * math.sin(theta)
    return(rotation_matrix)

def make_rotY( theta ):
    rotation_matrix = new_matrix()
    ident(rotation_matrix)
    theta = math.radians(theta)
    rotation_matrix[0][0] = math.cos(theta)
    rotation_matrix[0][2] = -1 * math.sin(theta)
    rotation_matrix[2][0] = math.sin(theta)
    rotation_matrix[2][2] = math.cos(theta)
    return(rotation_matrix)

def make_rotZ( theta ):
    rotation_matrix = new_matrix()
    ident(rotation_matrix)
    theta = math.radians(theta)
    rotation_matrix[0][0] = math.cos(theta)
    rotation_matrix[1][1] = math.cos(theta)
    rotation_matrix[0][1] = math.sin(theta)
    rotation_matrix[1][0] = -1 * math.sin(theta)
    return(rotation_matrix)

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
