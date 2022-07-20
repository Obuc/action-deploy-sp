# Action Deploy para Sharepoint Online
## 1 - Introdução
Essa action irá pegar o código dentro do repositório e inseri-lo automaticamente no Sharepoint Online desejado.

- Como funciona: Criamos um docker com a imagem `python:3`, instalamos [rclone](https://rclone.org/) e executamos um script em Python que cria um arquivo de configuração do rclone e executa o mesmo para buscar os arquivos do repositório e copia-los para uma pasta pre-definida.

## 2 - Limitações
Até o momento não é possível utilizar essa action em Sharepoint que precisa de algum tipo de autenticação dupla (Ex.: Requer 2FA ou autenticação com algum controlador de domino em rede privada)

## 3 - Como utilizar
- Crie no seu respositório o arquivo `.github/workflows/deploy.yaml`, dentro dele insira:

```yaml
name: Testing Action
on: 
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Executa checkout no repositório 
        uses: actions/checkout@v2
      - name: Exeuctando o deploy
        uses: Obuc/action-deploy-sp@v1.1
        with:
          project: SuperImportante
          url_sp: https://super.sharepoint.com/sites/importante
          user: ${{ secrets.USER }}
          pass: ${{ secrets.PASS }}
          src_folder: src/
          dst_folder: deploy_test/
```

- Com o arquivo criado, iremos verificar campo a campo e para o que eles servem:
    - Campo `name: Testing Action` Nome do Workflow, no exemplo "Testing Action".
    - Campo `on: push` definimos quando esse action vai ser executar, no exemplo utilizamos `push` logo todo push que for executado no repositório irá executar esse Workflow ou você pode deixar como `on: workflow_dispatch:` que só será executado quando você entrar no painel de actions.
    - Vamos pular para o campo `project: SuperImportante` lá você deve inserir o nome do seu projeto
    - O campo `url_sp: https://super.sharepoint.com/sites/importante` deve possuir o nome do website do Sharepoint que você pretende hospedar a aplicação.
    - O campo `src_folder: src/` indica aonde está o seu código no repositório, por exemplo: src/
    - O campo `dst_folder: deploy_test/` indica aonde você estará salvando os arquivos DENTRO do Sharepoint

- Agora bastar criar os 2 Secrets de Actions no repositório contendo o **USER** com seu usuário (ex.: blabla@blabla.com.br) e **PASS** com sua senha!
**Importante**! Nunca insira sua senha manualmente sempre utilize os secrets do Github.