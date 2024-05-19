import httpx
from bs4 import BeautifulSoup
from typing import List, Dict

async def fetch_table_data(ano: int, opcao: str) -> List[Dict[str, str]]:
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php"
    params = {
        "ano": ano,
        "opcao": opcao
    }
    
    print(f"Fetching data for URL: {url} with params: {params}")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        print(f"HTTP Response Status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.text}")
            return []
        
        print(f"Response content (truncated): {response.text[:500]}")
        
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'tb_base tb_dados'})
        if not table:
            print("No table found with class 'tb_base tb_dados'.")
            return []
        
        headers = [th.text.strip() for th in table.find('thead').find_all('th')]
        print(f"Headers found: {headers}")
        rows = table.find('tbody').find_all('tr')  # Pegar todas as linhas
        
        data = []
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == len(headers):
                data.append({headers[i]: cells[i].text.strip() for i in range(len(cells))})
        
        print(f"Extracted data: {data}")
        return data
