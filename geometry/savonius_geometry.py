import numpy as np
import matplotlib.pyplot as plt

d = 0.55
beta = 0.182
theta_deg = 180

r = d / 2
e = beta * d
a = r * (1 - beta)

D = 2 * (a + r)
print(D)
theta = np.radians(theta_deg)
phi = np.linspace(-theta / 2, theta / 2, 100)

x1 = a + r * np.cos(phi + np.pi / 2)
y1 = r * np.sin(phi + np.pi / 2)

x2 = -x1
y2 = -y1
plt.figure(figsize=(5, 5))
plt.plot(x1, y1, label="Blade 1")
plt.plot(x2, y2, label="Blade 2")
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.gca().set_aspect("equal")
plt.legend()
plt.savefig("geometry_check.png", dpi=150)
np.savetxt("blade1_points.csv", np.column_stack([x1, y1]), delimiter=",", header="x,y", comments="")
np.savetxt("blade2_points.csv", np.column_stack([x2, y2]), delimiter=",", header="x,y", comments="")
t = 0.01

r_out = r + t / 2
r_in = r - t / 2

xo = a + r_out * np.cos(phi + np.pi / 2)
yo = r_out * np.sin(phi + np.pi / 2)

xi = a + r_in * np.cos(phi + np.pi / 2)
yi = r_in * np.sin(phi + np.pi / 2)

bx1 = np.concatenate([xo, xi[::-1], xo[:1]])
by1 = np.concatenate([yo, yi[::-1], yo[:1]])

bx2 = -bx1
by2 = -by1

plt.figure(figsize=(5, 5))
plt.plot(bx1, by1, label="Blade 1")
plt.plot(bx2, by2, label="Blade 2")
plt.axhline(0, color="gray", lw=0.5)
plt.axvline(0, color="gray", lw=0.5)
plt.gca().set_aspect("equal")
plt.legend()
plt.savefig("geometry_outline.png", dpi=150)
np.savetxt("blade1_outline.csv", np.column_stack([bx1, by1]), delimiter=",", header="x,y", comments="")
np.savetxt("blade2_outline.csv", np.column_stack([bx2, by2]), delimiter=",", header="x,y", comments="")
