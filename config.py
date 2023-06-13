import numpy as np
import torch
import sympy

'''
Constants
'''
CONST_POOL = [1, 2, 10, np.pi, np.e]

'''
Numeric Operations
'''
NODE_OPS = {
    '+' : np.sum,
    '*' : np.prod,
    '=' : lambda x: x,
    'inv' : lambda x : 1/x,
    'neg' : lambda x : -x,
    'sin' : np.sin,
    'cos' : np.cos,
    'exp' : np.exp,
    'log' : np.log,
    'sqrt' : np.sqrt
}

NODE_OPS_PYTORCH = {
    '+' : torch.sum,
    '*' : torch.prod,
    '=' : lambda x: x,
    'inv' : lambda x : 1/x,
    'neg' : lambda x : -x,
    'sin' : torch.sin,
    'cos' : torch.cos,
    'exp' : torch.exp,
    'log' : torch.log,
    'sqrt' : torch.sqrt
}

NODE_ARITY = {
    '+' : 2,
    '*' : 2,
    '=' : 1,
    'inv' : 1,
    'neg' : 1,
    'sin' : 1, 
    'cos' : 1,
    'exp' : 1,
    'log' : 1,
    'sqrt' : 1
}

NODE_STR = {
    '+' : '(a)+(b)',
    '*' : '(a)*(b)',
    '=' : '(a)',
    'inv' : '1/(a)',
    'neg' : '-(a)',
    'sin' : 'np.sin(a)',
    'cos' : 'np.cos(a)',
    'exp' : 'np.exp(a)',
    'log' : 'np.log(a)',
    'sqrt' : 'np.sqrt(a)',
}

'''
Symbolic Operations
'''

NODE_OPS_SYMB = {
    '+' : lambda x, y: x + y,
    '*' : lambda x, y: x * y,
    '=' : lambda x: x,
    'inv' : lambda x : 1/x,
    'neg' : lambda x : -x,
    'sin' : lambda x: sympy.sin(x),
    'cos' : lambda x: sympy.cos(x),
    'exp' : lambda x: sympy.exp(x),
    'log' : lambda x: sympy.log(x),
    'sqrt' : lambda x: sympy.sqrt(x),
}
