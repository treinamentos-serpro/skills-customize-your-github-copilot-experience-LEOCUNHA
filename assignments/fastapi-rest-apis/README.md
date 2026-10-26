# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas e pratique rotas HTTP, parâmetros de caminho, validação de dados e códigos de status usando FastAPI.

## 📝 Tasks

### 🛠️ Criar uma Rota para Listar Tarefas

#### Descrição
Use o arquivo inicial fornecido para configurar e executar a aplicação. Crie uma rota `GET /tasks` que retorne todas as tarefas armazenadas como uma lista JSON.

Para preparar o ambiente e iniciar a aplicação:

```bash
python -m pip install fastapi uvicorn
python starter-code.py
```

Com o servidor em execução, consulte a documentação interativa em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Inicializar a aplicação FastAPI fornecida no arquivo inicial.
- Responder a `GET /tasks` com todas as tarefas da coleção.
- Retornar as tarefas como uma lista de objetos JSON.

### 🛠️ Consultar uma Tarefa por ID

#### Descrição
Crie uma rota `GET /tasks/{task_id}` para localizar e retornar uma tarefa específica usando seu ID. Trate IDs inexistentes com uma resposta HTTP apropriada.

#### Requisitos
O programa concluído deve:

- Receber o ID da tarefa como parâmetro de caminho do tipo inteiro.
- Retornar os dados da tarefa quando o ID existir.
- Responder com status HTTP `404` quando não houver tarefa com esse ID.

### 🛠️ Cadastrar uma Tarefa

#### Descrição
Crie uma rota `POST /tasks` que receba os dados de uma nova tarefa, valide o corpo da requisição com o modelo Pydantic fornecido e adicione a tarefa à coleção.

#### Requisitos
O programa concluído deve:

- Aceitar um título obrigatório e um campo `completed` opcional, cujo valor padrão seja `false`.
- Usar o modelo `TaskCreate` para validar os dados recebidos.
- Atribuir um ID à nova tarefa e incluí-la na coleção.
- Retornar a tarefa criada com status HTTP `201`.
