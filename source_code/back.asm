.high
:dicionario:
.array 
{ "chave" : "abacaxi"
"dicionario interior": {
    "mojang":"empresa"
    "aluno" : "miguel"
    "escola" : {
        "professores" : ["Juan" "Renata" "Caio" {"lula": "dilma"}]
        "alunos" : 4

        }

    }
}
:projeto_teste_extremo:
.array
{
    "metadata": {
        "versao": "1.0.4-beta"
        "autor": "Sistema de Teste"
        "tags": ["estresse", "parser", "isa", "high_session", "async_io"]
        "configuracoes_engine": {
            "render": "pixel_buffer"
            "resolucao": {
                "largura": 1920
                "altura": 1080
                "profundidade_cor": "32bit"
            }
            "flags": ["auto_save", "compress_swap", "no_bounds_check"]
        }
    }

    "big_data_set": {
        "registros_cientificos": {
            "amostra_A": {
                "sensores": ["termico", "pressao", "umidade", "vibracao"]
                "leituras": {
                    "t1": "22.5"
                    "t2": "23.1"
                    "historico_bruto": [102, 105, 110, 98, 45, 12, 0, 255]
                }
            }
            "amostra_B": {
                "status": "ativo"
                "sub_niveis": {
                    "n1": {
                        "n2": {
                            "n3": {
                                "n4": {
                                    "n5": "profundidade_maxima_atingida"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    "assets_graficos": {
        "textura_terreno": {
            "id": 5001
            "formato": "raw"
            "data_info": :textura_raw_data:
        }
        "sprites_npc": [
            { "id": "1", "nome": "guardiao", "pos": [100, 200] }
            { "id": "2", "nome": "mercador", "pos": [450, 300] }
            { "id": "3", "nome": "inimigo_boss", "propriedades": { "hp": 5000, "atq": 150 } }
        ]
    }

    "string_longa": "Esta e uma string de teste para verificar se o seu lexer aguenta buffers grandes sem quebrar o reconhecimento de tokens durante a iteracao do socket ou leitura de disco virtual vfs"
}
.code
mov r0 dicionario_len
halt