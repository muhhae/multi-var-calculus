import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as axes3d


def draw_graph(*args, t_start=-5 * np.pi, t_end=5 * np.pi, n: int = 1000, auto_scale=False, title=None, z_lim=None, y_lim=None, x_lim=None):
    t = np.linspace(t_start, t_end, n)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for f in args:
        x, y, z = f(t)
        ax.plot(x, y, z)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    if auto_scale:
        ax.set_aspect('equal')
    if title:
        ax.set_title(title)
    if z_lim:
        ax.set_zlim(z_lim)
    if y_lim:
        ax.set_ylim(y_lim)
    if x_lim:
        ax.set_xlim(x_lim)

    plt.show()

# def main(auto_scale=True):
    # l_f = [
    #     (lambda t: (t,
    #                 1 / (1 + t**2),
    #                 t**2),
    #      '< t, 1/(1 + t^2), t^2 >'),
    #     (lambda t: (t * np.cos(t),
    #                 t * np.sin(t), t),
    #      '< t cos t, t sin t, t >'),
    #     (lambda t: (np.cos(t) * np.sin(2*t),
    #                 np.sin(t) * np.sin(2*t),
    #                 np.cos(2*t)),
    #      '< cos t sin 2t, sin t sin 2t, cos 2t >'),
    #     (lambda t: (t,
    #                 t * np.sin(t),
    #                 t * np.cos(t)),
    #      '< t, t sin t, t cos t >'),
    #     (lambda t: (t,
    #                 np.exp(t),
    #                 np.cos(t)),
    #      '< t, e^t, cos t'),
    #     (lambda t: (np.cos(2*t),
    #                 np.cos(3*t),
    #                 np.cos(4*t)),
    #      '< cos 2t, cos 3t, cos 4t >'),
    #     (lambda t: ((1 + np.cos(16 * t)) * np.cos(t),
    #                 (1 + np.cos(16 * t)) * np.sin(t),
    #                 1 + np.cos(16) * t),
    #      "Np. 37"),
    #     (lambda t: (np.sqrt(1 - 0.25 * np.cos(10 * t)**2 * 10 * t) * np.cos(t),
    #                 np.sqrt(1 - 0.25 * np.cos(10 * t)**2 * 10 * t) * np.sin(t),
    #                 0.5 * np.cos(10*t))),
    #     (lambda t: ())
    # ]

    # for f, s in l_f:
    #     draw_graph(f, t_start=0, t_end=5 * np.pi, n=1000,
    #                title=s, auto_scale=auto_scale)

    # ftmp, stmp = lambda t: (t**2, np.log(t), t), '< t^2, ln t, t >'
    # draw_graph(ftmp, t_start=np.nextafter(0, 1), t_end=5 * np.pi, n=1000,
    #            title=stmp, auto_scale=auto_scale)

    # def f(t): return t * np.cos(t), t * np.sin(t), t
    # def f_1(t): return 0*t, t, 1 + t
    # draw_graph(f, f_1, t_start=0, t_end=5 * np.pi,
    #            n=1000, auto_scale=auto_scale)


if __name__ == '__main__':
    fig  = plt.figure()
    ax = fig.add_subplot(projection='3d')
    t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    x = (2 + np.cos(1.5 * t)) * np.cos(t)
    y = (2 + np.cos(1.5 * t)) * np.sin(t)
    z = np.sin(1.5 * t)

    ax.plot(x,y,z, color='r', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_zlim(-3, 3)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.view_init(azim=160, elev=30)
    ax.set_aspect('equal')
    plt.show()
        
