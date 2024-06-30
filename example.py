meu_dicionario = {
    "ola": "mundo",
    "estou": "aqui"
}

outro_dicionario = {
    **meu_dicionario,
    "id": "meu_id",
    "aqui": "meu dicionario"
}

print(outro_dicionario)
