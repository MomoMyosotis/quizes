import random

# Dizionario delle domande e risposte
quiz_data = {
    "Principi Filosofici": {
        "Quali sono i principi fondamentali del taekwondo?": [
            "cortesia",
            "integrità",
            "perseveranza",
            "autocontrollo",
            "spirito indomito"
        ],
},
    "Forme": {
        "Quale forma rappresenta la 'creazione del cielo e della terra'?": "Chon-ji",
        "Quale forma rappresenta il fondatore della Corea nel 2333 aC?": "Dan-gun",
        "Quale forma rappresenta il patriota?": "Do-san",
        "Quale forma rappresenta il monaco che introdusse il buddhismo?": "Won-hyo",
        "Quale forma rappresenta il sapiente?": "Yul-gok",
        "Quale forma rappresenta l'eroe che aiutò a liberare la Corea?": "Joong-gun",
        "Quale forma rappresenta lo studioso nato sul 37° parallelo?": "Toi-gye",
        "Quale forma rappresenta i giovani guerrieri che aiutarono ad unificare la Corea?": "Hwa-rang",
        "Quale forma rappresenta l'ammiraglio creatore della corazzata?": "Choong-moo",
        "Quale forma rappresenta il 19° re che riunificò la Corea?": "Kwang-gae",
        "Quale forma rappresenta il poeta con il pseudonimo 'non servo altro maestro...'?": "Po-eun",
        "Quale forma rappresenta il generale con rigida disciplina militare?": "Ge-baek",
    },
    "Numeri": {
        "Qual è il numero coreano per '1'?": "Hana",
        "Qual è il numero coreano per '2'?": "Dul",
        "Qual è il numero coreano per '3'?": "Set",
        "Qual è il numero coreano per '4'?": "Net",
        "Qual è il numero coreano per '5'?": "Daseot",
        "Qual è il numero coreano per '6'?": "Yeoseot",
        "Qual è il numero coreano per '7'?": "Ilgop",
        "Qual è il numero coreano per '8'?": "Yodul",
        "Qual è il numero coreano per '9'?": "Ahop",
        "Qual è il numero coreano per '10'?": "Yeol",
    },
    "Nomi": {
        "Come si dice 'alto' in coreano?": "Nopunde",
        "Come si dice 'medio' in coreano?": "Kaunde",
        "Come si dice 'basso' in coreano?": "Najunde",
        "Come si dice 'cintura' in coreano?": "Ti",
        "Come si dice 'forma' in coreano?": "Tul",
        "Come si dice 'gran maestro' in coreano?": "Saseong",
        "Come si dice 'istruttore' in coreano?": "Sabum",
        "Come si dice 'assistente istruttore' in coreano?": "Boosabum",
        "Come si dice 'master' in coreano?": "Sahyum",
        "Come si dice 'girare' in coreano?": "Dolgi",
    },
    "Anatomia": {
        "Qual è il termine coreano per 'avambraccio'?": "Palmok",
        "Qual è il termine coreano per 'doppio avambraccio'?": "Doo palmok",
        "Qual è il termine coreano per 'collo del piede'?": "Baldung",
        "Qual è il termine coreano per 'gomito'?": "Palkup",
    },
    "Calci": {
        "Qual è il termine coreano per 'calcio'?": "Chagi",
        "Qual è il termine coreano per 'calcio all'indietro'?": "Dwit cha jirugi",
        "Qual è il termine coreano per 'calcio circolare 360'?": "Twio dolmyo chagi",
        "Qual è il termine coreano per 'calcio laterale'?": "Yop cha jirugi",
        "Qual è il termine coreano per 'calcio circolare'?": "Dolyo chagi",
        "Qual è il termine coreano per 'calcio di laith'?": "Bituro chagi",
        "Qual è il termine coreano per 'calcio bandal ma uncino'?": "Goro chagi",
        "Qual è il termine coreano per 'calcio a martello'?": "Naeryo chagi",
        "Qual è il termine coreano per 'calcio frontale'?": "Ap chagi",
    },
    "Parate": {
        "Qual è il termine coreano per 'parata'?": "Makgi",
        "Qual è il termine coreano per 'doppia parata (tipo doppio pugno)'?": "Hechyo makgi",
        "Qual è il termine coreano per 'parata 1 wonkyo'?": "Sang palmok makgi",
        "Qual è il termine coreano per 'parata incrociata X'?": "Kyocha makgi",
    },
    "Posizioni": {
        "Qual è il termine coreano per 'posizione corta'?": "Niunja sogi",
        "Qual è il termine coreano per 'posizione lunga'?": "Gunnun sogi",
        "Qual è il termine coreano per 'posizione tipo chumbi ma un piede 90°'?": "Soojik sogi",
        "Qual è il termine coreano per 'posizione di carica laterale'?": "Goburio sogi",
        "Qual è il termine coreano per 'piedi uniti'?": "Moa sogi",
        "Qual è il termine coreano per 'posizione lunga + 1 piede'?": "Nachuo sogi",
        "Qual è il termine coreano per 'posizione corta con piede avanti punta'?": "Dwitbal sogi",
        "Qual è il termine coreano per 'posizione a cavaliere'?": "Annun sogi",
    },
    "Pugni": {
        "Qual è il termine coreano per 'pugno'?": "Joomuk",
        "Qual è il termine coreano per 'taglio di mano'?": "Sonkal",
        "Qual è il termine coreano per 'tallone'?": "Dwitchock",
    },
}

def quiz():
    total_score = 0
    total_questions = 0
    section_scores = {}
    
    categories = list(quiz_data.keys())
    random.shuffle(categories)

    for category in categories:
        print(f"\nCategoria: {category}\n")
        questions = list(quiz_data[category].items())
        random.shuffle(questions)
        section_score = 0
        section_questions = len(questions)

        for question, answer in questions:
            total_questions += 1
            user_answer = input(f"{question} ").strip().lower()
            if user_answer == answer.lower():
                print("Corretto!")
                section_score += 1
            else:
                print(f"Sbagliato! La risposta corretta è {answer}.")

        section_scores[category] = section_score

    for category, score in section_scores.items():
        print(f"\nPunteggio per la categoria '{category}': {score} su {len(quiz_data[category])}")

    total_score = sum(section_scores.values())
    total_score_percentage = (total_score / total_questions) * 100

    print(f"\nPunteggio totale: {total_score} su {total_questions}")
    print(f"Punteggio totale in centesimi: {total_score_percentage:.2f}/100")

if __name__ == "__main__":
    quiz()
