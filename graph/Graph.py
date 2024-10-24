import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from algorithm.Algorithm import Algorithm
from algorithm.BlindSearch import BlindSearch
from algorithm.SimulatedAnnealing import SimulatedAnnealing
from function.Function import Function

INTERACTIVE = True

if INTERACTIVE:
    plt.switch_backend('tkagg')


class Graph:
    def __init__(self):
        self.points = None

    @staticmethod
    def plot_function_3d(x, y, z, color='jet_r', alpha=0.8):
        # Plot the results
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, color=color, alpha=alpha)

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
    def plot_point(ax, point, color='blue', alpha=1.0):
        x, y = point[0]
        z = point[1]

        return ax.scatter([x], [y], [z], color=color, alpha=alpha)

    @staticmethod
    def plot_algorithm(algorithm_instance: 'BlindSearch'):
        x, y, z = Graph.get_function_values(algorithm_instance.function)

        # Plot the function as grey gradient
        Graph.plot_function_3d(x, y, z, color='Grey', alpha=0.3)

        # Plot the algorithm path
        path = algorithm_instance.path
        for point in path:
            Graph.plot_point(point[1])

        # Plot the best solution
        Graph.plot_point(algorithm_instance.current_best, 'go')

        # Show the plot
        plt.title(f'{algorithm_instance.function.get_name()} - {algorithm_instance.get_name()} Plot')
        plt.show()

    def animate_algorithm(self, algorithm_instance: 'Algorithm', length=5):
        x, y, z = Graph.get_function_values(algorithm_instance.function)

        fig, ax = Graph.plot_function_3d(x, y, z, color='Grey', alpha=0.3)

        plt.get_current_fig_manager().full_screen_toggle()

        if algorithm_instance.get_path() is None:
            return

        path = algorithm_instance.get_path()
        self.points = []

        def update(frame):
            if frame == len(path):
                # if algorithm is SimmulatedAnnealing, find the lowest point in the path
                if algorithm_instance.get_name() == 'SimulatedAnnealing':
                    best = algorithm_instance.get_result()
                    for point in path:
                        if point[1][1] < best[1]:
                            best = point[1]
                    pt = Graph.plot_point(ax, best, 'blue')
                    pt.set_sizes([1000])
                    self.points.append(pt)

                # plot the result
                pt = Graph.plot_point(ax, algorithm_instance.get_result(), 'green')
                pt.set_sizes([1000])
                self.points.append(pt)

                return

            current_point = path[frame]

            if frame == 0:
                pt = Graph.plot_point(ax, current_point[1], 'red')
                self.points.append(pt)
            elif current_point[0]:
                # recolor all previous points
                for point in self.points:
                    point.set_color('black')
                    point.set_alpha(0.7)
                # plot the new point
                pt = Graph.plot_point(ax, current_point[1], 'red')
                self.points.append(pt)
            else:
                # plot the new point
                pt = Graph.plot_point(ax, current_point[1], 'black', 0.7)
                self.points.append(pt)

        interval = length * 1000 / len(path)

        ani = FuncAnimation(fig, update, frames=len(path) + 1, interval=interval, repeat=False)
        plt.title(f'{algorithm_instance.function.get_name()} - {algorithm_instance.get_name()} Plot')
        plt.show()
