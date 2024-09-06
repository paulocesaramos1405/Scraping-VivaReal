WebScraping VivaReal

O scraping 

Como eu realizei essa tarefa:
A tarefa envolve o desenvolvimento de um processo automatizado para extrair dados web scraping de um site de imóveis, que foi o VivaReal, e armazená-los em um banco de dados remoto, como o Supabase. O objetivo é coletar informações de preços, endereços e dimensões de lotes de terrenos e inseri-las em uma tabela estruturada no banco de dados.

Lógica usada:
Definir os objetivos claros da coleta de dados:

Foi necessário os coletar preços, endereços e dimensões dos lotes que estão disponíveis no site.
Esses dados devem ser consistentes, cada preço deve ter um endereço e uma dimensão associados a cada item de venda.
Após a coleta, foram armazenadas essas informações no Supabase.

Planejamento da extração de dados:

Analisar a estrutura HTML da página: Identificar quais classes e tags HTML contêm os dados necessários. Por exemplo, o preço pode estar dentro de um elemento div com uma classe específica, o endereço dentro de um span e a dimensão em outra tag.

Selecionar as ferramentas para scraping: Foi usada uma ferramenta para simular um navegador, acessar o site e baixar o HTML da página como o Cloudscraper. Para filtrar os dados relevantes dentro do HTML, foi usado uma ferramenta de parsing como o BeautifulSoup, que permite localizar as informações específicas (preço, endereço e dimensões) de forma coerente.

Definir o armazenamento dos dados:

Supabase como banco de dados: Foi usado o Supabase como o banco de dados onde os dados raspados serão armazenados. Para isso, foi armazenado em uma tabela com as colunas (price, endereco, dimensao).
Conectar ao Supabase: Para se conectar com o supabase, foram usadas as credenciais URL e chave da API do Supabase para estabelecer uma conexão com o banco de dados. Após a conexão, foi usada uma função para inserir os dados extraídos.

Lógica de consistência dos dados:

Verificação de consistência: Após extrair os dados do site, foi necessário garantir que para cada preço extraído, há um endereço e uma dimensão correspondentes. Isso é importante para evitar a inserção de dados incompletos no banco de dados.

Inserção dos dados no banco de dados:

Inserção segura: A inserção no banco de dados foi feita feita por meio de uma função que enviou as informações corretas para a tabela no Supabase. Caso a inserção apresente falha (por exemplo, devido a uma falha de conexão ou erro na tabela), o sistema deve capturar o erro e registrá-lo para futura correção.

Passo a passo da tarefa:
Preparação do ambiente:

Instalar o Python e configurar um ambiente de desenvolvimento adequado.
Instalar as bibliotecas necessárias: Cloudscraper, BeautifulSoup e a biblioteca do Supabase para interação com o banco de dados.
Coletar a estrutura HTML da página:

Acessar o site VivaReal e inspecionar o código HTML para entender onde estão localizados os dados de preços, endereços e dimensões.
Identificar as classes e tags que contêm essas informações.

Desenvolver o scraping:

Configurar o scraper para acessar o site e baixar o HTML da página.
Usar o BeautifulSoup para filtrar os elementos relevantes (preços, endereços, dimensões).
Verificar se o número de elementos extraídos para cada categoria é o mesmo.
Configurar o banco de dados no Supabase:

Criar uma tabela no Supabase com as colunas necessárias: price, endereco e dimensao.
Conectar o código ao banco de dados usando a URL do projeto e a chave da API.
Inserir os dados extraídos no Supabase:

Verificar se os dados são consistentes (nenhum dado importante está faltando).
Inserir cada conjunto de dados (preço, endereço, dimensão) no Supabase.

Monitoramento e ajustes:

Monitorar o comportamento do scraper para verificar se ele está extraindo e inserindo os dados corretamente.
Tratar possíveis erros, como bloqueios de acesso ao site ou falhas na conexão com o banco de dados.

Informações necessárias:

Estrutura HTML da página do VivaReal: Precisa identificar onde estão localizados os preços, endereços e dimensões no código HTML. Esses dados geralmente estão em classes ou tags específicas. Para isso pode-se usar o elemento inspecionar, do site, e passar o mouse em cima da informação do site. Após fazer isso, pegar o código mostrado e atrelar a função no vs code.
Credenciais do Supabase: Precisa-se da URL do projeto e da chave da API para conectar nosso código ao banco de dados.
Formato da tabela no Supabase: A tabela deve ter as colunas adequadas (price, endereco, dimensao) para armazenar as informações extraídas corretamente.

Dificuldades que podem ser encontradas:

Mudanças no HTML do site: O site pode alterar a estrutura do HTML, mudando as classes ou a organização das informações, o que pode exigir ajustes no código.
Bloqueios de anti-bot: Alguns sites podem bloquear scrapers se eles acessarem o site muitas vezes em um curto período. Para contornar isso, podem usar técnicas como Cloudscraper, que ajuda a evitar esses bloqueios.

Ferramentas necessárias:
Python: Para desenvolver o script de scraping e inserção no banco de dados.
Cloudscraper: Para simular o acesso ao site e evitar bloqueios de bot.
BeautifulSoup: Para ler e processar o HTML da página e extrair as informações necessárias.
Supabase: Para armazenar os dados coletados de forma estruturada em um banco de dados relacional.
Git: Para controle de versão do código e colaboração em equipe, caso necessário.






