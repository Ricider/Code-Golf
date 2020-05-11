q=lambda x:q([i for i in x if i<x[0]])+[x[0]]+q([i for i in x if i>x[0]]) if x else x
