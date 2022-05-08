import matplotlib.pyplot as plt


def plot3d(x1, x2, y, colorbar=True):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    c = range(1, len(y)+1)

    img = ax.scatter(x1, x2, y, c=c, cmap=plt.hot())
    ax.text(x1[0], x2[0], y[0], '%s' % (str(1)), size=10, zorder=1, color='k')
    ax.text(x1[len(y)-1], x2[len(y)-1], y[len(y)-1], '%s' % (str(len(y))), size=10, zorder=1, color='k')

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('y')
    if colorbar:
        cbar = plt.colorbar(img)
        cbar.set_label('Epoch')
    plt.show()
