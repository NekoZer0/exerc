

# Adicionando Poe como Dependência de Desenvolvimento

Poe (Poe the Poet) é uma ferramenta que permite definir e executar tarefas personalizadas em projetos Python, facilitando o gerenciamento de scripts e comandos comuns durante o desenvolvimento.

## Instalação

Para adicionar Poe como uma dependência de desenvolvimento, execute o seguinte comando no terminal:

```bash
uv add --dev poethepoet
```

Isso instalará o pacote `poethepoet` apenas para o ambiente de desenvolvimento.

## Configuração no pyproject.toml

Após a instalação, edite o arquivo `pyproject.toml` do seu projeto e adicione a seção `[tool.poe.tasks]` com as tarefas desejadas. Por exemplo:

```toml
[tool.poe.tasks]
uvrm = "uv run main.py"
st = "python saudacoes.py"
```

- `uvrm`: Executa o script principal (`main.py`) usando `uv run`.
- `st`: Executa o script de saudações (`saudacoes.py`) diretamente com Python.

## Uso

Com as tarefas configuradas, você pode executá-las facilmente via linha de comando usando o comando `poe` seguido do nome da tarefa. Por exemplo:

- Para executar a tarefa `uvrm`:
    ```bash
    poe uvrm
    ```

Isso simplifica o fluxo de trabalho, evitando a necessidade de lembrar comandos longos ou caminhos de arquivos.