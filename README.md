# Projeto
Marombas é uma aplicação web criada para pessoas que gostam de exibir seus músculos na academia, mas tem vergonha de se expor em suas redes sociais convencionais, com isso Marombas foi pensado justamente para elas.

### Desenvolvimento
Marombas foi desenvolvido em [Python 3.7.0](https://www.python.org/) e [Django 2.1](https://www.djangoproject.com/), a aplicação foi desenvolvida como material final de meses de estudo focado inteiramente em web.

## Acesse o site
Os arquivos estáticos são hospedados na Amazon S3 para funcionar corretamente em conjunto com o Heroku.

[Acesse o site da aplicação](https://marombas.herokuapp.com/) e veja funcionando

## Veja todo o código
Caso queira visualizar melhor todo o código e os programas usados disponibilizei a pasta venv que eu usei em todo o trabalho, basta ir no terminal mac ou linux e digitar
```
$source venv/bin/activate. 
```

## Rodar testes
Para rodar os testes do projeto basta estar na mesma pasta que se encontra o arquivo manage.py e rodar o código no console
```
python3 manage.py test
```
Se quiser rodar em uma app específica, basta inserir o nome de uma das pasta que possuem testes na frente de test
```
python3 manage.py test core
```
Ao todo foram feitos 47 testes, averiguando views, forms, urls e models.
