Programa Python que pegue informações de CANAIS de Youtube:

. Iterar pela lista de palavras chave:  [tempest, youtube, estrela]

. Para cada palavra chave nesta lista realizar uma busca no site do Youtube por canais

. Extrair as informações especificadas de cada canal encontrado na página:
    * título: nome do canal
    * descrição: descrição do canal
    * url: url do canal
    * img: base64 da imagem de perfil do canal
    * query: a palavra chave utilizada na busca que encontrou o canal
    * id: um identificador único para esse canal (sugestão, existe um campo "channelId" dentro da resposta do youtube)

. Realizar a extração da próximas duas páginas, caso existirem para a busca

. Retornar uma lista (array) contendo todos as informações extraídos dos canais encontrados (elimine infos duplicadas)

Criar um fluxo secundário que vai adicionar o resultado da coleta de canais para um SQlite
