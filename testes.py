import unittest

from atividades import comer, dormir

class AtividadesTestes(unittest.TestCase):
    
    def test_comer(self):
        self.assertEqual(
            comer('quiabo', True), 
            'Estou comendo quiabo porque quero manter a forma'
        )

        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False), 
            'Estou comendo pizza pois a gente só vive uma vez'
        )

if __name__ == '__main__':
    unittest.main()


