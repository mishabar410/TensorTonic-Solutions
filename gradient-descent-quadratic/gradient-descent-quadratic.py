def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    for step in range(steps):
        x0 = x0 - 2*a*x0 * lr - b * lr
    return x0