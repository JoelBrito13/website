# Smart Room

A dynamic Django template for personal Portfolios. Its is build to contain the The **Skills**, **Experiences**, **Projects**, **Education**, **Certificates** along with other pertinent informations. 

<img src="presentation/website.png">

This webpage was build in django, the deployment were prepared for been in a heroku server, the media is storaged in Google Storage and the static files are in the project used WhiteNoise. 

For local use, you can change the media roots to local and the DataBase to sqllite in  __/website/settings.py/__. Also uncomment the media line in  __/website/urls.py/__


## Templates and Images Used:

* [Website Base Template](https://github.com/user-cube/aboutMePT)
* [404 page](https://codepen.io/andrew-lawendy/pen/deOpMZ)
* [500 page](https://codepen.io/dariocorsi/pen/YOeYrJ)
* [No Content Page](https://codepen.io/ricardpriet/pen/qVZxNo)
* [css bar animation](https://www.youtube.com/watch?v=JkhhzfkXFSA)

* [Google storage](https://django-storages.readthedocs.io/en/latest/backends/gcloud.html)
* [Heroku Deployment](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)

* [project default image](https://unsplash.com/photos/SYTO3xs06fU)
* [education default image](https://unsplash.com/photos/2JIvboGLeho)
* [Experience defaul image](https://unsplash.com/photos/uf2nnANWa8Q)


## Static items

The used items for this project are located in __/website/static/__, however the specific for the portifolio owner are located __/website/static/icon/__ and __/website/static/image/__.


## ENV variables

* SECRET_KEY 
* DEBUG 
* ALLOWED_HOSTS 
* DB_HOST 
* DB_PORT 
* DB_NAME 
* DB_PASS 
* DB_USER  
* DEBUG_COLLECTSTATIC
* DJANGO_STATIC_HOST
* GOOGLE_CREDENTIALS

Tal como foi definido na arquitetura do projeto, dissemos que íamos criar uma pwa baseada na aplicação web, para a criação de uma pwa, a Google exige:
* Seja acessível nos seus servidores de criação
* Esteja em HTTPS
* Quando feita em react usar a versão `production build`

Para que isto seja feito, um container na VM que nos foi fornecida não permite que a mesma seja criada. De modo a alcançar estes requisitos colocamos todo o nosso código no Heroku, assim, podemos fazer deploy do mesmo lá fornecendo os serviços que precisamos.
Dado as especificidade do Heroku, o deploy é mais rápido e simples quando o código se encontra em repositórios separados, dái termos tantos repositórios.

### CI/CD
Existem mecanismos de CI/CD implementados.
No que diz respeito a CI, foi feito integração com o Github Actions que trata de todo o processo de CI.
O CD ficou a cargo do Heroku que, após o Github Actions dar um parecer positivo, inicia o seu processo de deployment.

### Cloud AMQP
Uma vez que colocamos todos os serviços fora da UA, tivemos de recorrer ao alojamento do rabbit também fora da UA, para isso usamos a Cloud AMQP serviço fornecido pelos criadores do RabbitMQ.

### Mongo Atlas
Da mesma forma que tivemos de colocar o Rabbit fora da UA, fizemos o mesmo com o MongoDB, passando assim o Mongo para o Mongo Atlas serviço fornecido pelos criadores do mesmo..

### Deploy
Como foi mencionado anteriormente, colocamos tudo fora da UA, deste modo os serviços podem acedidos em:
* **Frontend** - [Heroku](https://iesfrontend.herokuapp.com/)
* **SpringBoot** - [Heroku](https://iesapi.herokuapp.com/)
* **Flask API** - [Heroku](https://ies-controller.herokuapp.com/)

**Nota**: A API não pode ser acedida no / uma vez que não tem um caminho definido para o mesmo, de qualquer modo, pode ser consultada a parte da [documentação](https://iesapi.herokuapp.com/swagger-ui.html#/)

## Links

### Backlog
Para o backlog optamos pelo Pivotal Tracker o mesmo pode ser acedido <a href="https://www.pivotaltracker.com/n/projects/2410465">aqui</a>.

### Documentos
Os documentos do projeto podem ser encontrados na pasta da Google Drive, contém sempre a versão mais atualizada dos mesmos uma vez que a ferramenta definida para a escrita de relatórios foi o Google Docs, a pasta encontra-se <a href="https://drive.google.com/drive/folders/1Q3gWHAxaBDn8KbCLEB_KCepWUc4GiT_G?usp=sharing">aqui</a>.

## Sensores
Este repositório contém todo o código dos sensores tanto dos criados virtualmente usados numa primeira fase, assim como os que foram posteriormente implementados via hardware.
<img src="presentation/files.png">

### Pasta gen_info
Nesta pasta encontram-se os primeiros sensores implementados de forma virtual, daqui, apenas foi usado posteriormente o de CO2 uma vez que não conseguimos arranjar sensores digitais para o efeito.

### Pasta nfc_reader
Nesta pasta encontra-se a implementação do código do leitor RFID-RC522.
Este sensor encontra-se ligado a dois leds, um verde e um vermelho que indicam os acessos da pessoa, isto é, caso a pessoa tenha acesso, o led vermelho apaga-se e o verde acede, caso não tenha é feito um switch entre o led vermelho e o led verde.
A isto foi ainda anexado um buzzer que toca consoante o acesso ser válido ou inválido.

### Pasta sensor_temp_humidity
Nesta pasta encontra-se a implementação do código do sensor DHT11 que mede humidade e temperatura.
<img src="presentation/vista_cima.jpg">
<img src="presentation/vista_lateral.jpg">

#### Video de demonstração
Pode ser encontrado na pasta `presentation`.