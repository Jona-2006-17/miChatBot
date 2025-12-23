import spacy

nlp = spacy.load("es_core_news_sm")

def responder(texto: str)->str:
    info = analizar_texto(texto)

    lemas = info['lemas']
    verbos = info['verbos']
    sustantivos = info['sustantivos']

    if 'hola' in lemas:
        return '¿hola en que puedo ayudarte?'
    
    if "comprar" in verbos:
        if any(prod in texto.lower() for prod in ["celular", "telefono", "móvil"]):
            return "¿Buscas un celular? Tenemos varias opciones disponibles."
        return "¿Qué deseas comprar exactamente?"
        
    if 'precio' in lemas or 'costar' in verbos:
        return "¿De que producto te gustaria saber el precio?"
    
    if any(pal in lemas for pal in ["adiós", "chao", "hasta"]):
        return "¡Hasta luego! 😊"
        
        
    return "Aún estoy aprendiendo, ¿puedes explicarlo de otra forma?"
    
def analizar_texto(texto: str):
    #Doc = Objeto que guarda todos los datos de un texto procesado, tokenizacion, pos tagging, lematizacion, reconocimiento de entidades, analisis de dependencias
    doc = nlp(texto)

    entidades = [(ent.text, ent.label_) for ent in doc.ents]

    lemas = [token.lemma_ for token in doc]

    verbos = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    sustantivos = [token.lemma_ for token in doc if token.pos_ == "NOUN"]

    return {
        "entidades": entidades,
        "lemas": lemas,
        "verbos": verbos,
        "sustantivos": sustantivos,
    }
