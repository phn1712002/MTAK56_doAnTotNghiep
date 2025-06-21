def rk4_1step(dy_dt, t, y, h):
  k1 = h * dy_dt(t, y)
  k2 = h * dy_dt(t + h/2, y + k1/2)
  k3 = h * dy_dt(t + h/2, y + k2/2)
  k4 = h * dy_dt(t + h, y + k3)
  y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
  return y