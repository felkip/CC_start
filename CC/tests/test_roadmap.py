import unittest

from app.roadmap import get_roadmap_for_profile


class RoadmapTests(unittest.TestCase):
    def test_programming_roadmap_has_expected_topics(self):
        topics = get_roadmap_for_profile("programming")
        self.assertIn("Fundamentos de lógica", topics)
        self.assertGreaterEqual(len(topics), 3)

    def test_unknown_profile_returns_beginner_topics(self):
        topics = get_roadmap_for_profile("unknown")
        self.assertEqual(topics[0], "Introdução à computação")


if __name__ == "__main__":
    unittest.main()
