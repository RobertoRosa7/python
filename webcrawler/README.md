# WebCrawler com Python - usando módulo scrapy

** Instalação **
```
  -> pip install scrapy
  ou
  -> conda install -c conda-force scrapy
```

Após a instalação é necessário usar shell se quiser, para isso use o comando.

```
  -> scrapy install
```

Feito isso é preciso indicar um alvo, site que será feito a extração dos dados com
o comando fetch(), returna um arquivo html que pode ser renderizado no browser
ou em formato de texto.

```
  -> fetch('https:meusite.com')
  -> view(response)
  -> print(response.text)
```

# Usando CSS Selector para extração
Exemplo:

```
  -> response.css(".product::text").extract_first()
```

extract_first() extrai somente o primeiro elemento que satisfaça a seleção do
css, se quiser todos os elementos use somente extract(). Codigo para extrar os
preços dos produtos.

```
  -> response.css(".value::text").extract()
```

# Usando Xpath para navegar pelos Nodes do HTML ou XML

Atráves do xpath podemos navegar pelas children e parent nodes, assim podemos
fazer filtros mais específicos para extrair somente informações pertinentes.

Para extrair todo código child do HTML
```
  -> response.xpath('/html').extract()
```

Para extrair todo conteúdo de div
```
  -> response.xpath('/html//div').extract()
  ou
  -> response.xpath('//div').extract()
```

Para fazer um filtro ainda mais específico
```
  -> response.xpath('//div[@class="quote"]/span[@class="text"]').extract()
  -> response.xpath('//div[@class="quote"]/span[@class="text"]/text()').extract()
```
Use text() para extrair todo texto que está no elemento



# Criando um projeto com scrapy

Para fazer um projeto com todos os dados e também exportar esses dados em formato
como cvs ou json, é preciso criar um projeto e para isso, vamos usar o scrapy

```
  -> scrapy startproject [nome_do_projeto]
  -> scrapy genspider [nome_do_spider] [endereço_da_url]
```

Após de configurar todo o arquivo devemos usar o comando para gerar os dados
```
  -> scrapy crawl aliexpress_tablets
```

Exportar Nos formato csv ou json no arquivo setting.py
```
  -> FEED_FORMAT="json"
  -> FEED_URI="aliexpress.json"
```
