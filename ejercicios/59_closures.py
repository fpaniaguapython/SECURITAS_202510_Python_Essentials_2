def get_translate_function(source_language, target_language):
    def funcion_interna(palabra_a_traducir):
        translate = (f'Traduciendo {palabra_a_traducir} de {source_language} a {target_language}')
        return translate
    return funcion_interna

source_language, target_language = 'español', 'inglés'
traductor_es_en = get_translate_function(source_language,target_language)
source_language, target_language = 'chino', 'español'
traductor_cn_es = get_translate_function(source_language,target_language)

traduccion = traductor_es_en('Casa')
print(traduccion)

traduccion = traductor_cn_es('casa-en-chino')
print(traduccion)