# Eventex 

Sistema de Eventos encomendado pela Morena

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com a versão mais recente do python (3.10)
3. Ative o virtualenv
4. Configure a instância com o .env
5. Execute os testes

```console
git clone https://github.com/GregMasterBr/eventex-fenix.git eventex-wttd
cd eventex-wttd
python -m venv .wtdd
.wttd/Scripts/Activate.ps1
pip install -r requirements.txt ou pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma conta no pythonanywhere
2. Envie as configurações para o github e no pythoanywhere clone este repositório
3. Configure a instância com o .env. Defina uma SECRET_KEY segura para a instância
4. Defina o DEBUG=False
5. Configure o serviço de e-mail (ex: Sendgrid ou Gmail)
6. Envie o código para o github e atualize quando necessário direto no pythoanywhere (git pull)

[Passo a Passo de como fazer deploy no Pythoanywhere - Comunidade da HBNetwork](https://discord.com/channels/971167625323348068/1136718283551277096)


Projeto hospedado no Pythonanywhere  
<http://gregmasterbr.pythonanywhere.com/>
