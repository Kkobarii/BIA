from algorithm.BlindSearch import BlindSearch
from algorithm.HillClimbing import HillClimbing
from function.Ackley import Ackley
from function.Griewank import Griewank
from function.Levy import Levy
from function.Michalewicz import Michalewicz
from function.Rastrigin import Rastrigin
from function.Rosenbrock import Rosenbrock
from function.Schwefel import Schwefel
from function.Sphere import Sphere
from function.Zakharov import Zakharov
from graph.Graph import Graph

if __name__ == '__main__':
    # Create an instance of the Sphere function
    functions = [
        Sphere(),
        # Ackley(),
        # Rastrigin(),
        # Rosenbrock(),
        # Griewank(),
        # Schwefel(),
        # Levy(),
        # Michalewicz(),
        # Zakharov(),
    ]
    graph = Graph()

    # Plot the Sphere function using the Graph class
    for function in functions:
        # algorithm = BlindSearch(100, 10, function)
        algorithm = HillClimbing(100, function)
        algorithm.search()

        # Graph.plot_function(function)
        # Graph.plot_algorithm(algorithm)
        graph.animate_algorithm(algorithm)
