# # -*- coding: utf-8 -*-
# 3.1. Loop principal e sinais
# Como a maioria dos toolkits de GUI, o GTK+ usa um modelo de programação orientada a eventos. Quando o usuário não está fazendo nada, o GTK+ fica no loop principal e aguarda a entrada. Se o usuário executar alguma ação – digamos, um clique do mouse — o loop principal “acorda” e entrega um evento para o GTK+.
# Quando widgets recebem um evento, eles frequentemente emitem um ou mais sinais. Sinais notificam seu programa que “algo interessante aconteceu” invocando funções que você conectou ao sinal. Tais funções são comumente conhecidas como callbacks ou retorno de chamada. Quando seus retornos de chamada são invocados, você normalmente toma algumas ações – por exemplo, quando um botão Abrir é clicado, você pode exibir uma caixa de diálogo de seleção de arquivos. Depois que um retorno de chamada terminar, o GTK+ retornará ao loop principal e aguardará mais entrada do usuário.
# Um exemplo genérico é:

# handler_id = widget.connect("event", callback, data)

# Em primeiro lugar, widget é uma instância de um widget que criamos anteriormente. Em seguida, o evento em que estamos interessados. Cada widget tem seus próprios eventos específicos que podem ocorrer. Por exemplo, se você tem um botão, geralmente deseja se conectar ao evento “clicked”. Isso significa que quando o botão é clicado, o sinal é emitido. Em terceiro lugar, o argumento callback é o nome da função de retorno de chamada. Ele contém o código que é executado quando os sinais do tipo especificado são emitidos. Finalmente, o argumento data inclui todos os dados que devem ser passados quando o sinal é emitido. No entanto, esse argumento é completamente opcional e pode ser deixado de fora se não for necessário.
# A função retorna um número que identifica esse par de sinal/retorno de chamada específico. É necessário desconectar de um sinal de modo que a função de retorno de chamada não seja chamada durante qualquer emissão futura ou atual do sinal ao qual está conectada.

# widget.disconnect(handler_id)

# Se você perdeu o “handler_id” por algum motivo (por exemplo, os manipuladores foram instalados usando Gtk.Builder.connect_signals()), você ainda pode desconectar um retorno de chamada específico usando a função disconnect_by_func():

# widget.disconnect_by_func(callback)

# Os aplicativos devem se conectar ao sinal “destroy” da janela de nível superior. É emitido quando um objeto é destruído, portanto, quando um usuário solicita que uma janela de nível superior é fechada, o manipulador padrão para este sinal destrói a janela, mas não finaliza o aplicativo. Conectar o sinal “destroy” da janela de nível superior à função Gtk.main_quit() resultará no comportamento desejado.
# window.connect("destroy", Gtk.main_quit)
# Chamar Gtk.main_quit() faz o loop principal dentro do retorno de Gtk.main().

# 3.2. Propriedades
# Propriedades descrevem a configuração e o estado dos widgets. Quanto aos sinais, cada widget tem seu próprio conjunto particular de propriedades. Por exemplo, um botão tem a propriedade “label”, que contém o texto do widget de etiqueta dentro do botão. Você pode especificar o nome e o valor de qualquer número de propriedades como argumentos nomeados ao criar uma instância de um widget. Para criar um rótulo alinhado à direita com o texto “Hello World” e um ângulo de 25 graus, use:
# label = Gtk.Label(label="Hello World", angle=25, halign=Gtk.Align.END)

# que é equivalente a

# label = Gtk.Label()
# label.set_label("Hello World")
# label.set_angle(25)
# label.set_halign(Gtk.Align.END)

# Em vez de usar getters e setters, você também pode obter e definir as propriedades do gobject através da propriedade “props”, como widget.props.prop_name = valor. Isto é equivalente ao mais detalhado widget.get_property(“prop-name”) e widget.set_property(“prop-name”, valor).
# Para ver quais propriedades estão disponíveis para um widget na versão em execução do GTK, você pode usar “dir” com a propriedade “props”:

# widget = Gtk.Box()
# print(dir(widget.props))

# Isto irá imprimir no console a lista de propriedades que um Gtk.Box possui.
