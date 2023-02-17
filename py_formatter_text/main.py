# -*- coding: utf-8 -*-

from typing import Counter


text = """
O textos em mídias digitais são, antes de tudo, partes das imagem das telas dos dispositivos, imagens que na maioria das vezes incluem elementos como menus, ícones, banners. Entre esses elementos, são os textos que os usuários mais procuram para obter as informações.
Pesquisa do Pointer Institute com a Universidade de Stanford mostra que em sites de notícias, os olhos procuram inicialmente os textos, resumos, títulos e legendas. Só depois procuram as fotos e os gráficos, às vezes depois de já terem selecionado um link e lido um artigo em página interna. (1)

Apesar da priorização do texto pelos olhos da maioria dos usuários, a leitura na tela do dispositivo digital tende a ser inquieta, pois a web e os dispositivos móveis estimulam o deslocamento e a ação do usuário, que não costuma ficar na mesma página ou tela por muito tempo. Há muitas fontes de informações e recursos, e os usuários são sempre estimulados ao deslocamento e à atividade, o que exige que os textos se adaptem a estas condições de uso.

Além disso, para fazer frente à necessidade de ação, ou deslocamento, o usuário médio não costuma ler todas as palavras dos textos online, limita-se a “varrê-los” com os olhos, o que é acentuado pelo fato da leitura no monitor ser mais lenta do que sobre papel.

Jakob Nielsen aponta que a leitura descontínua na web é feita mais comumente por usuários com maior grau de letramento. Usuários não acostumados a ler, ou com formação escolar incompleta, costumam ler os textos online palavra por palavra. De modo geral, os usuários leem 18% das palavras de um texto online.

Devido ao modo de leitura fragmentada, os editores não esperam que cada leitor se desloque entre diversas páginas de seu site para encontrar informações sobre um assunto. A leitura se faz na maioria das vezes entre páginas de diferentes sites ou plataformas, intermediada por resultados dos sites de busca, que traçam um roteiro possível de encadeamento.

A edição “mental” de diversos trechos faz com que cada usuário crie um texto novo, que, mesmo que não se explicite, é formado a partir da edição de trechos selecionados em diversas fontes.

Para atender a circunstâncias de uso tão específicas, a redação de textos para leitura online precisa se adaptar aos contextos de uso a que se destinam.
"""

def analisa_freq(text):
  count = Counter(text.lower())
  total = sum(count.values())

  proporcoes = [(char, freq / total) for char, freq in count.items()]
  proporcoes = Counter(dict(proporcoes))
  most_common = proporcoes.most_common(10)
  for carac, prop in most_common:
    print("{} => {:.2f}%".format(carac, prop * 100))

analisa_freq(text)
