import unittest
from sentinel.update_fetcher import UpdateFetcher

class TestUpdateFetcher(unittest.TestCase):
    def test_fetch_updates(self):
        fetcher = UpdateFetcher()
        repos = ["facebook/react"]
        updates = fetcher.fetch_updates(repos)
        self.assertIsInstance(updates, list)

if __name__ == "__main__":
    unittest.main()