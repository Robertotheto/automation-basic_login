# Automation Anywhere Basic Login
## App para realizar login usando Python

**Skills**

![Python](https://img.shields.io/badge/-Python-000?&logo=Python) ![Virtualenv](https://img.shields.io/badge/-Virtualenv-000?&logo=Virtualenv) ![Pylint](https://img.shields.io/badge/-Pylint-000?&logo=Pylint) ![Selenium](https://img.shields.io/badge/-Selenium-000?&logo=Selenium)

##
App foi desenvolvido usando os challenges da plataforma de automação **Automation Anywhere** em consiste em uma aplicação backend para realizar login em um site informando usuario e senha.

**Para inicial o projeto primeiro clone o repositorio**

    git clone https://github.com/Robertotheto/automation-basic_login.git
**Crie seu ambiente virtual**

    pip3 install virtualenv
    python3 -m venv nome_do_ambiente
**Ative seu ambiente virtual**
`source nome_do_ambiente/bin/activate` no Linux ou `nome_do_ambiente\Scripts\activate` no Windows.

**Instale as dependências do projeto**
    pip3 install -r requirements.txt
    
*OBS: Use pip3 ou python3 quando estiver em um ambiente Linux, quando no Windows utilize pip e py.*

**Para rodar o projeto digite o comando:**

    python3 main.py


**código importante para a biblioteca pylint**

    .pylintrc
          C0114, # missing-module-docstring
          C0115, # Missing-class-docstring
          C0116, # missing-function-docstring
          W0703, # Catching too general exception Exception
          R0903, # too-few-public-methods
          W0719, # broad-exception-raised

**comando para gerar nosso arquivo de requirements.txt**
   

     .venv/bin/pip3 freeze > requirements.txt
