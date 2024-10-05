import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from algorithm.BlindSearch import BlindSearch
from function.Function import Function

INTERACTIVE = True

if INTERACTIVE:
    plt.switch_backend('tkagg')


class Graph:
    @staticmethod
    def plot_function_3d(x, y, z, cmap='jet_r', alpha=0.8):
        # Plot the results
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap=cmap, alpha=alpha)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        return fig, ax

    @staticmethod
    def plot_function_2d(x, y, z):
        # Plot the results
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contour(x, y, z, cmap='jet_r')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        return fig, ax

    @staticmethod
    def get_function_values(function_instance: 'Function'):
        # Create a grid of points
        x, y = function_instance.grid(100)

        # Calculate z values using the evaluate method of the function instance
        z = np.zeros(x.shape)
        for i in range(z.shape[0]):
            for j in range(z.shape[1]):
                z[i, j] = function_instance.evaluate(np.array([x[i, j], y[i, j]]))

        return x, y, z

    @staticmethod
    def plot_function(function_instance: 'Function'):
        x, y, z = Graph.get_function_values(function_instance)

        # Plot the results
        if function_instance.specification.dimension == 2:
            Graph.plot_function_3d(x, y, z)
        elif function_instance.specification.dimension == 1:
            Graph.plot_function_2d(x, y, z)
        else:
            print('Cannot plot functions with dimensions greater than 2')

        # Show the plot
        plt.title(f'{function_instance.get_name()} Plot')
        plt.show()

    @staticmethod
    def plot_point(point, color='bo', alpha=1.0):
        x, y = point[0]
        z = point[1]

        return plt.plot(x, y, z, color, alpha=alpha)

    @staticmethod
    def plot_algorithm(algorithm_instance: 'BlindSearch'):
        x, y, z = Graph.get_function_values(algorithm_instance.function)

        # Plot the function as grey gradient
        Graph.plot_function_3d(x, y, z, cmap='Greys', alpha=0.3)

        # Plot the algorithm path
        path = algorithm_instance.path
        for point in path:
            Graph.plot_point(point[1])

        # Plot the best solution
        Graph.plot_point(algorithm_instance.current_best, 'go')

        # Show the plot
        plt.title(f'{algorithm_instance.function.get_name()} - {algorithm_instance.get_name()} Plot')
        plt.show()

    @staticmethod
    def animate_algorithm(algorithm_instance: 'BlindSearch'):
        x, y, z = Graph.get_function_values(algorithm_instance.function)

        fig, ax = Graph.plot_function_3d(x, y, z, cmap='Greys', alpha=0.1)

        path = algorithm_instance.path

        def update(frame):
            current_point = path[frame]

            if frame == 0:
                Graph.plot_point(current_point[1], 'go')
            elif current_point[0]:
                last_best = next((point for point in path[:frame][::-1] if point[0]), None)

                if last_best:
                    Graph.plot_point(last_best[1], 'ko')
                Graph.plot_point(current_point[1], 'go')
            else:
                Graph.plot_point(current_point[1], 'ko', 0.3)

        # calculate interval so that the animation is 5 seconds long
        interval = 5000 / len(path)

        ani = FuncAnimation(fig, update, frames=len(path), interval=interval, repeat=False)
        plt.title(f'{algorithm_instance.function.get_name()} - {algorithm_instance.get_name()} Plot')
        plt.show()
