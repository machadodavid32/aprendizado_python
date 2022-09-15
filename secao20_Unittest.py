"""
Introdução ao Unittest
Inittest - Testes unitários -> É a forma de testar unidades individuais
de um codigo fonte.
Unidades inidivuais podem ser funções, métodos, classes, módulos, etc.

Obs: Teste unitário não é específico da linguagem Python.

Parar criar nossos testes, criamos classes que herdam  de Unittest.
Testcase e a partir de então ganhamos todos os 'assertions' presentes no
módulo.

Para rodar os testes utilizamos unittes.main()

Testcase -> Casos de teste para sua unidade

# Conhecendo os assertions

Método                     Checa que

assertEqual(a, b)          a == b

assertNotEqual(a, b)       a != b

assertTrue(x)              bool(x) is True

assertFalse(x)             bool(x) is False

assertIs(a, b)             a is b

assertIsNot(a, b)          a is not b       3.1

assertIsNone(x)            x is None        3.1

assertIsNotNone(x)         x is not None    3.1

assertIn(a, b)             a in b           3.1

assertNotIn(a, b)          a not in b       3.1

assertIsInstance(a, b)     isinstance(a, b) 3.2

assertNotIsInstance(a, b)  not isinstance(a, b)  3.2

https://docs.python.org/3/library/unittest.html

Obs: Por convenção, todos os testes em um test case, devem ter seu nome iniciado com  test_

"""

# Prática - utilizando a abordagem TDD
