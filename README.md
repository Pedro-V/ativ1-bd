# Atividade 1 - Banco de Dados - Estudo de Tecnologia

A tecnologia escolhida foi Django, para desenvolver uma API simples que provê
funcionalidades CRUD para usuários, com nome, CPF e data de nascimento. A API
foi documentada usando swagger e `drf-yasg`.

É possível subir essa aplicação no Elastic Beanstalk da AWS, devido aos arquivos de configuração em
`.ebextensions/`. Para tal:

1. Crie um ambiente no Elastic Beanstalk (EB) cuja plataforma é Python e o domínio é
   `xyz.com`. Existem vários jeitos de interagir com a API da AWS: Console,
   SDKs, CLI.
2. Clone o repositório: `git clone https://github.com/Pedro-V/ativ1-bd.git`
3.  Altere `userAPI/setting.py` e troque o atual domínio em `ALLOWED_HOSTS` por
   `xyz.com`.
4. Gere um arquivo `.zip` do repositório **com o novo domínio**. Isso pode ser
   feito com `git archive`, `zip`, entre outros. 
5. Faça o upload e o deploy desse arquivo no seu ambiente EB. Novamente, isso
   pode ser feito de vários jeitos.
6. Acesse a aplicação em `xyz.com`
