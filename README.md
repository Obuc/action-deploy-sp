# Action Deploy para Sharepoint Online
## 1 - Introdução
Essa action irá pegar o código dentro do repositório e inseri-lo automaticamente no Sharepoint Online desejado.

- Como funciona: Criamos um docker com a imagem `python:3`, instalamos [rclone](https://rclone.org/) e executamos um script em Python que cria um arquivo de configuração do rclone e executa o mesmo para buscar os arquivos do repositório e copia-los para uma pasta pre-definida.

## 2 - Limitações
Até o momento não é possível utilizar essa action em Sharepoint que precisa de uma autenticação interna.
Esse action foi testado com **sucesso** no seguintes casos:
- Sharepoint Online do Cliente com acesso externo liberado
- Sharepoint Online da Obuc

## 3 - Como utilizar
- Crie no seu respositório o arquivo `.github/workflows/deploy.yaml`, dentro dele insira:

```yaml
name: Testing Action
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Executa checkout no repositório 
        uses: actions/checkout@v2
      - name: Exeuctando o deploy
        uses: Obuc/action-deploy-sp@v1
        with:
          project: SuperImportante
          url_sp: https://super.sharepoint.com/sites/importante
          user: ${{ secrets.USER }}
          pass: ${{ secrets.PASS }}
          src_folder: test/
          dst_folder: deploy_test/
```

- Com o arquivo criado, iremos verificar campo a campo e para o que eles servem:
    - Campo `name: Testing Action` Nome do Workflow, no exemplo "Testing Action".
    - Campo `on: push` definimos quando esse action vai ser executar, no exemplo utilizamos `push` logo todo push que for executado no repositório irá executar esse Workflow.

_EM CONSTRUÇÃO_