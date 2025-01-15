O sistema alerta o usuário quando o preço da moeda atinge um valor mínimo ou máximo pré-determinado. Aqui está uma explicação de cada parte do código:

1. Função getPrice(currency, vsCurrency)
Essa função faz uma requisição GET à API CoinGecko para buscar o preço de uma criptomoeda em relação a outra moeda. No código, estamos usando o dólar (USD) como moeda de comparação.
A URL da API é construída com os parâmetros fornecidos (currency e vsCurrency).
Caso a requisição seja bem-sucedida (status 200), a função retorna o preço da criptomoeda; caso contrário, retorna None.
2. Função showAlert(price, currency)
Exibe uma janela de alerta (usando o Tkinter) informando que o preço da criptomoeda atingiu ou ultrapassou o valor mínimo ou máximo estabelecido pelo usuário.
A janela tem um botão "OK" que, ao ser pressionado, fecha a janela. A janela também fecha automaticamente após 10 segundos.
3. Função showReturnAlert(price, currency)
Similar à função showAlert, mas é acionada quando o preço da criptomoeda volta ao intervalo definido (dentro do valor mínimo e máximo). O alerta informa que o preço voltou ao valor esperado.
4. Função startMonitoring()
Essa função é chamada quando o usuário clica no botão "Iniciar Monitoramento". Ela pega os valores inseridos pelo usuário (moeda, preço mínimo e máximo) e começa a monitorar o preço da criptomoeda.
O código tenta converter os preços inseridos para float. Caso haja um erro de conversão (valor inválido), uma mensagem de erro é exibida.
O código então entra em um loop contínuo, onde a função getPrice é chamada a cada 60 segundos para verificar o preço atual da moeda. Quando o preço atinge os limites definidos (mínimo ou máximo), um alerta é disparado. Se o preço voltar ao intervalo desejado, outro alerta é mostrado.
5. Interface Gráfica (Tkinter)
A interface permite que o usuário insira:
O nome da criptomoeda que deseja monitorar (por exemplo, "solana", "ethereum").
O preço mínimo e máximo para essa moeda.
O botão "Iniciar Monitoramento" aciona o processo de monitoramento, e a label de status exibe o andamento do processo (ex: "Monitorando Ethereum...").
6. Comportamento do Código
Quando o monitoramento é iniciado, o preço da moeda é verificado a cada 60 segundos.
Quando o preço atinge ou ultrapassa o limite definido (mínimo ou máximo), um alerta é exibido. Se o preço voltar para o intervalo entre o limite mínimo e máximo, outro alerta é mostrado.
O programa continua monitorando o preço enquanto estiver em execução, verificando a cada minuto.
Como usar:
Insira o nome da criptomoeda que deseja monitorar (como "solana", "ethereum").
Defina o preço mínimo e máximo que deseja para a criptomoeda.
Clique em "Iniciar Monitoramento" e o sistema começará a monitorar os preços.
A cada 60 segundos, a aplicação consulta a API e verifica se o preço da moeda atingiu um dos limites, exibindo alertas conforme necessário.
Esse código é útil para quem precisa monitorar preços de criptomoedas e ser notificado quando esses preços atingem valores específicos, como em operações de compra e venda ou para criar e gerenciar pools de liquidez.
