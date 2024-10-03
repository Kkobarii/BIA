import matplotlib.pyplot as plt
import numpy as np

from function.Function import Function


class Graph:
    @staticmethod
    def plot_function_3d(name, x, y, z):
        # Plot the results
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='jet_r')

        ax.set_title(f'{name} Plot')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

    @staticmethod
    def plot_function_2d(name, x, y, z):
        # Plot the results
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.contour(x, y, z, cmap='jet_r')

        ax.set_title(f'{name} Plot')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

    @staticmethod
    def plot_function(function_instance: 'Function'):
        # Get function name
        function_name = function_instance.__class__.__name__

        # Create a grid of points
        x = np.linspace(function_instance.specification.lower, function_instance.specification.upper, 100)
        y = np.linspace(function_instance.specification.lower, function_instance.specification.upper, 100)
        x, y = np.meshgrid(x, y)

        # Calculate z values using the evaluate method of the function instance
        z = np.zeros(x.shape)
        for i in range(len(x)):
            for j in range(len(y)):
                z[i][j] = function_instance.evaluate(np.array([x[i][j], y[i][j]]))

        # Plot the results
        if function_instance.specification.dimension >= 2:
            Graph.plot_function_3d(function_name, x, y, z)
        else:
            Graph.plot_function_2d(function_name, x, y, z)

        plt.show()
