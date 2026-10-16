import unittest
import lesson7 as m

class LessonTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual((m.Matrix([[1,2]])+m.Matrix([[3,4]])).rows,[[4,6]])
        self.assertAlmostEqual(m.total_fabric([m.Coat(6.5),m.Suit(2)]),5.8)
        self.assertEqual((m.Cell(12)+m.Cell(3)).quantity,15)
        self.assertEqual(m.Cell(12).make_order(5),"*****\\n*****\\n**".replace("\\n","\n"))

if __name__ == "__main__":
    unittest.main()
