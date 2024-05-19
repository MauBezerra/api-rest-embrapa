from fastapi import FastAPI, HTTPException
from typing import List, Dict
from scraping import fetch_table_data
from mapping import option_mapping

app = FastAPI()

@app.get("/dados/{ano}/{tipo}", response_model=List[Dict[str, str]])
async def get_dados(ano: int, tipo: str):
    opcao = option_mapping.get(tipo)
    if not opcao:
        raise HTTPException(status_code=400, detail=f"Opção inválida: {tipo}")
    
    try:
        dados = await fetch_table_data(ano, opcao)
        return dados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
