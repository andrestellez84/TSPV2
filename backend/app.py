from flask import Flask, request, jsonify
from flask_cors import CORS
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

app = Flask(__name__)
CORS(app)


def create_distance_matrix(coords):
    size = len(coords)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            matrix[i][j] = int(math.hypot(x2 - x1, y2 - y1) * 1000)
    return matrix


@app.route('/api/solve', methods=['POST'])
def solve_tsp():
    data = request.get_json()
    coords = data.get('coordinates') if data else None
    if not coords or not isinstance(coords, list):
        return jsonify({'error': 'No coordinates provided'}), 400
    if len(coords) < 2:
        return jsonify({'error': 'At least two coordinates required'}), 400
    if any(
        not isinstance(c, (list, tuple)) or len(c) != 2 or
        not all(isinstance(v, (int, float)) for v in c)
        for c in coords
    ):
        return jsonify({'error': 'Invalid coordinates format'}), 400

    distance_matrix = create_distance_matrix(coords)
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_params)
    if not solution:
        return jsonify({'error': 'No solution found'}), 500

    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))

    return jsonify({'route': route})


if __name__ == '__main__':
    app.run(debug=True)
