def from_S_to_T(s):
    t11 = -(s[0,0] * s[1, 1] - s[0, 1] * s[1, 0]) / s[1, 0]
    t12 = s[0, 0] / s[1, 0]
    t21 = -s[1, 1] / s[1, 0]
    t22 = 1 / s[1, 0]
    T = np.array([[t11, t12], [t21, t22]])
    return T


def from_T_to_S(t):
    s11 = t[0, 1] / t[1, 1]
    s12 = (t[0, 0] * t[1, 1] - t[0, 1] * t[1, 0]) / t[1, 1]
    s21 = 1 / t[1, 1]
    s22 = - t[1, 0] / t[1, 1]
    S = np.array([[s11, s12], [s21, s22]])
    return S