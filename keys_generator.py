def gcd(a, b):
    while a > 0 and b > 0:
        a %= b
        a, b = b, a
    return a + b

def get_keys(p, q):
    """Returns private and public keys as follows: private_key, public_key"""
    n = p * q
    lambda_n = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
    d = int(pow(65537, -1, lambda_n))
    return hex(d), hex(n)