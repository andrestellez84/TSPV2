import unittest
from backend.app import app


class SolverTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_solve_small_example(self):
        coords = [[0, 0], [0, 1], [1, 0]]
        response = self.client.post('/api/solve', json={'coordinates': coords})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        route = data.get('route')
        self.assertEqual(len(route), len(coords) + 1)
        self.assertEqual(route[0], 0)
        self.assertEqual(route[-1], 0)
        self.assertEqual(set(route[:-1]), set(range(len(coords))))

    def test_invalid_coordinates(self):
        response = self.client.post('/api/solve', json={'coordinates': [[1, 2, 3]]})
        self.assertEqual(response.status_code, 400)

    def test_missing_coordinates(self):
        response = self.client.post('/api/solve', json={})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
