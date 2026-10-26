# 📘 Assignment: Testes Unitários com unittest

## 🎯 Objective

Aprenda a escrever e executar testes automatizados com a biblioteca `unittest` do Python, usando asserções para verificar resultados esperados e interpretar falhas.

## 📝 Tasks

### 🛠️ Executar o Teste de Exemplo

#### Descrição
Execute o teste `test_high_score_is_passing` fornecido no arquivo inicial com `python starter-code.py`. Observe como a classe `TestGradeHelpers` organiza o teste e como `self.assertTrue` verifica o resultado.

#### Requisitos
O programa concluído deve:

- Executar o arquivo pelo comando `python starter-code.py`.
- Confirmar que o teste de exemplo é executado e aprovado.
- Identificar a asserção que verifica se `is_passing(85)` retorna `True`.

### 🛠️ Testar Reprovação e Nota Limite

#### Descrição
Amplie a classe `TestGradeHelpers` com testes para uma nota abaixo do limite de aprovação e para a própria nota limite.

#### Requisitos
O programa concluído deve:

- Verificar com `self.assertFalse` que `is_passing(59)` retorna `False`.
- Verificar com `self.assertTrue` que `is_passing(60)` retorna `True`.
- Executar todos os testes e confirmar que passam.

### 🛠️ Testar a Média e Interpretar Falhas

#### Descrição
Adicione um teste para `calculate_average` usando uma lista não vazia. Em seguida, altere temporariamente o resultado esperado para um valor incorreto, execute os testes para observar a mensagem de falha e restaure o valor correto.

#### Requisitos
O programa concluído deve:

- Usar `self.assertEqual` para verificar que `calculate_average([70, 80])` retorna `75`.
- Executar a suíte completa com `python starter-code.py`.
- Identificar na saída qual teste falhou e qual era o resultado esperado e o obtido.
- Restaurar o resultado esperado correto e confirmar que todos os testes passam.
