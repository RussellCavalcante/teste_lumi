#Aplicativo FastAPI
**Russell Cavalcante**

Certifique-se de ter o Docker instalado para executar os testes:

## Instale a aplicação

Certifique-se de ter o Docker instalado para executar os testes:
```

cd delfos-test

docker build -t delfos_test .

docker-compose up postgresql-test -d 

docker-compose up pgadmin-test  -d

docker-compose up app -d


```

Execute os comandos de migração do projeto:

```
docker-compose run --user 1000 app sh -c 'alembic upgrade head'

docker-compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add tables assets and meansurements"'

docker-compose run --user 1000 app sh -c 'alembic upgrade head'
```

Após executar os comandos de migração, realize os testes da aplicação através do seguinte link:

```
http://localhost:8000/docs
```

Com o Swagger da aplicação, crie um usuário teste e faça login na parte superior do Swagger em Authorize:
```
Rota para registro de usuario:
    http://localhost:8000/docs#/User/user_register_user_register_post

Usuario exemplo: 
    {username:teste
     password: teste}
```
Logue na parte superior do swagger em Authorize:
![Authorize](./image.png)

Em seguida, faça a carga do arquivo assets.csv na rota para popular a tabela de assets
```
Rota para carga do arquivo:
    http://localhost:8000/docs#/Asset/create_upload_file_asset_uploadfile_post

```

e faça carga do measurements.csv para popular também a tabela do measurements
```
Rota para carga do arquivo:
    http://localhost:8000/docs#/Measurements/list_average_value_measurement_list_average_value_get
```

Em seguida, liste todos os ativos na rota abaixo:
```
Rota para listagem:
    http://localhost:8000/docs#/Asset/list_categories_asset_list_get
```

Agora a rota que lista todas as medições:
```
Rota para listagem:
    http://localhost:8000/docs#/Measurements/list_Measurements_measurement_list_get
```

Por último, a rota que calcula o valor médio:

```

Obs : lembre-se de passar os valores correspondentes aos que aparecem na listagem anterior


Rota para listagem:
    http://localhost:8000/docs#/Measurements/list_average_value_measurement_list_average_value_get
```

## Fim

EEspero que o teste tenha atendido aos requisitos do teste. Qualquer dúvida, sinta-se à vontade para entrar em contato. Fique à vontade para testar as outras rotas!
Atenciosamente, **Russell Cavalcante**# teste_lumi
