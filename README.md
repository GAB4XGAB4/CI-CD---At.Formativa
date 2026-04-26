# CI-CD---At.Formativa
Projeto de CI/CD da atividade formativa da disciplina DevOps

## CI e CD com GitHub Actions

- CI: executa lint, check do Django, validacao de migrations e testes.
- CD: apos CI bem-sucedido na `main`, publica o artefato e aciona deploy real no Render.

## Como configurar deploy real no Render

1. Crie o servico Web no Render apontando para este repositorio.
2. No Render, copie a Deploy Hook URL do servico.
3. No GitHub, acesse `Settings > Secrets and variables > Actions` e crie:
	- `RENDER_DEPLOY_HOOK_URL`: URL da deploy hook do Render.
	- `RENDER_SERVICE_URL`: URL publica da aplicacao (ex.: `https://meu-app.onrender.com`).
4. Mantenha o workflow de CI aprovado na PR e faca merge para `main`.
5. O workflow de CD vai disparar automaticamente e executar o deploy no Render.
