import cloudscraper
from bs4 import BeautifulSoup
from supabase import create_client, Client

url = "https://zjwuhcvgfxreiekzslsg.supabase.co" 
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpqd3VoY3ZnZnhyZWlla3pzbHNnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzOTMwNjIsImV4cCI6MjA0MDk2OTA2Mn0.9tCT9YSi9NALtERQORcYS2YfbjkF7DP3mH-rBYwcNXY"  # Substitua pela chave de API do Supabase

supabase: Client = create_client(url, key)

def inserir_dados_supabase(preco, endereco, dimensao):
    
    try:
        response = (
    supabase.table("imoveis")
    .insert({"price": preco,   "endereco": endereco,"dimensao": dimensao})
    .execute()
)
        print("dados salvos com sucesso: " + preco + " " + endereco + " " + dimensao)
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

scraper = cloudscraper.create_scraper()
url = 'https://www.vivareal.com.br/venda/ceara/eusebio/lote-terreno_residencial/#onde=,Cear%C3%A1,Eus%C3%A9bio,,,,,city,BR%3ECeara%3ENULL%3EEusebio,-14.791623,-39.283324,&itl_id=1000183&itl_name=vivareal_-_botao-cta_buscar_to_vivareal_resultado-pesquisa'
response = scraper.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

prices = soup.find_all('div', class_='property-card__price')
enderecos = soup.find_all('span', class_='property-card__address')
dimensoes = soup.find_all('span', class_='property-card__title js-cardLink js-card-title')

if len(prices) == len(enderecos) == len(dimensoes):
    for i in range(len(prices)):
        preco = prices[i].get_text(strip=True)
        endereco = enderecos[i].get_text(strip=True)
        dimensao = dimensoes[i].get_text(strip=True)
        
        if not preco or not endereco or not dimensao:
            print(f"Dados incompletos: Preço: {preco}, Endereço: {endereco}, Dimensão: {dimensao}")
        else:
            inserir_dados_supabase(preco, endereco, dimensao)
else:
    print(f"O número de preços ({len(prices)}), endereços ({len(enderecos)}) e dimensões ({len(dimensoes)}) não é consistente.")

