import random
import os

def clear_terminal():
    # Funzione per pulire il terminale in Ubuntu usando il comando clear
    os.system('clear')

def run_quiz(questions):
    random.shuffle(questions)  # Mescola le domande per un ordine casuale
    score = 0
    partial_score = 0  # Inizializza il punteggio per le risposte semi-corrette
    answers_given = [False] * len(questions)  # Inizializza un elenco per tracciare le risposte date
    user_answers = [None] * len(questions)  # Inizializza un elenco per memorizzare le risposte degli utenti
    current_question = 0  # Indice della domanda corrente

    while current_question < len(questions):
        clear_terminal()
        question, answers = questions[current_question]
        print(f"Domanda {current_question + 1}: {question}")
        random.shuffle(answers)  # Mescola le risposte per un ordine casuale
        
        # Stampa le risposte possibili
        for j, (answer, correct) in enumerate(answers, 1):
            print(f"{j}. {answer}")
        
        # Loop per ottenere una risposta valida dall'utente
        while True:
            user_input = input("Inserisci il numero della risposta corretta (oppure 'skip ', 'back' o 'exit'): ").strip().lower()

            if user_input.startswith('skip '):
                try:
                    skip_index = int(user_input.split()[1]) - 1
                    if 0 <= skip_index < len(questions):
                        current_question = skip_index
                        break
                    else:
                        print("Numero di domanda non valido.")
                except ValueError:
                    print("Inserisci un numero valido dopo 'skip '.")
            elif user_input == 'back':
                if current_question > 0:
                    current_question -= 1
                    break
                else:
                    print("Non puoi tornare indietro, sei alla prima domanda.")
            elif user_input == 'exit':
                print("Quiz interrotto.")
                return
            else:
                try:
                    user_answer = int(user_input)
                    if 1 <= user_answer <= len(answers):
                        answers_given[current_question] = True  # Segna che è stata data una risposta a questa domanda
                        user_answers[current_question] = (answers[user_answer - 1][0], answers[user_answer - 1][1])  # Memorizza la risposta dell'utente
                        if answers[user_answer - 1][1]:
                            score += 2
                        break  # Esci dal loop while dopo aver ottenuto una risposta valida
                    else:
                        print("Inserisci un numero valido corrispondente a una delle risposte disponibili.\n")
                except ValueError:
                    print("Inserisci un numero valido oppure usa 'skip ', 'back' o 'exit'.\n")

        current_question += 1
    
    clear_terminal()
    # Mostra lo stato delle risposte
    for i, (question, _) in enumerate(questions, 1):
        if answers_given[i - 1]:
            print(f"Domanda {i} - Risposta salvata: {user_answers[i - 1][0]}")
        else:
            print(f"Domanda {i} - Risposta non data")
    
    # Calcola il punteggio totale (corretto + parzialmente corretto)
    total_score = score + partial_score
    print(f"\nQuiz completato! Punteggio finale: {total_score}/{2 * len(questions)}")

    # Chiedi all'utente se vuole consegnare il quiz
    while True:
        answer = input("\nVuoi consegnare il quiz? (y/n): ").strip().lower()
        if answer == 'y':
            if total_score >= 18:  # Condizione per superare il quiz
                print("Complimenti! Hai superato il quiz.")
            else:
                print("Mi dispiace, non hai superato il quiz.")
            break
        elif answer == 'n':
            current_question = len([a for a in answers_given if a])  # Torna all'ultima domanda completata
            break
        else:
            print("Risposta non valida. Inserisci 'y' per sì o 'n' per no.")

questions = [
    ("Cos'è la bioinformatica e come si integra con la biologia molecolare?",
     [("Utilizza strumenti computazionali per analizzare dati biologici. Si integra con la biologia molecolare analizzando sequenze di DNA, RNA e proteine per comprendere funzioni e interazioni biologiche.", True),
      ("Si occupa della sintesi di proteine nel corpo umano.", False),
      ("Studia gli effetti dei farmaci sui virus.", False),
      ("Esamina l'evoluzione delle cellule vegetali.", False),
      ("Analizza la fotosintesi nelle piante.", False)]),

    ("Descrivi il processo di estrazione delle proteine da un campione biologico.",
     [("Include la lisi cellulare, la rimozione dei detriti cellulari mediante centrifugazione, e la raccolta del sovranatante contenente le proteine.", True),
      ("Consiste nella formazione di RNA messaggero dai dati biologici.", False),
      ("Studia le interazioni tra proteine e acidi nucleici.", False),
      ("Riproduce il ciclo cellulare nei campioni biologici.", False),
      ("Analizza la formazione dei lipidi nelle membrane cellulari.", False)]),

    ("Quali sono i passaggi chiave nella preparazione di un campione per SDS-PAGE?",
     [("Preparazione del campione con un tampone di carica contenente SDS e β-mercaptoetanolo, bollitura del campione, caricamento del campione nel gel.", True),
      ("Lavaggio del campione con acqua distillata.", False),
      ("Isolamento dei cromosomi all'interno delle cellule.", False),
      ("Studiare le sequenze di DNA nel campione biologico.", False),
      ("Misurare l'attività enzimatica nel campione di proteine.", False)]),

    ("Come funziona la tecnica di SDS-PAGE?",
     [("Denatura le proteine con SDS e le separa per peso molecolare mediante elettroforesi su gel di poliacrilammide.", True),
      ("Analizza la struttura dei lipidi nella membrana cellulare.", False),
      ("Quantifica la produzione di RNA nelle cellule vegetali.", False),
      ("Studia l'effetto dei vaccini sui batteri.", False),
      ("Misura la quantità di acqua all'interno delle cellule.", False)]),

    ("Qual è lo scopo del Western Blotting?",
     [("Identificare e quantificare specifiche proteine in un campione.", True),
      ("Analizzare le sequenze di RNA nelle cellule umane.", False),
      ("Misurare l'attività enzimatica nei campioni biologici.", False),
      ("Studiare l'evoluzione delle specie.", False),
      ("Quantificare la produzione di glucosio nelle piante.", False)]),

    ("Come si trasferiscono le proteine dal gel al filtro di nitrocellulosa durante il Western Blotting?",
     [("Mediante un campo elettrico che sposta le proteine dal gel al filtro di nitrocellulosa.", True),
      ("Utilizzando il DNA per trasportare le proteine nel filtro di nitrocellulosa.", False),
      ("Isolando le proteine in campioni biologici.", False),
      ("Quantificando la produzione di ATP nelle cellule.", False),
      ("Studiando le reazioni chimiche nelle cellule umane.", False)]),

    ("Quali sono le differenze tra anticorpi primari e secondari nel Western Blotting?",
     [("L'anticorpo primario si lega specificamente alla proteina di interesse, mentre l'anticorpo secondario, coniugato a un enzima, si lega all'anticorpo primario per rilevare il segnale.", True),
      ("Entrambi gli anticorpi si legano alle proteine di interesse nello stesso modo.", False),
      ("L'anticorpo secondario si lega direttamente alla proteina di interesse nel campione.", False),
      ("L'anticorpo primario si lega agli enzimi nelle cellule vegetali.", False),
      ("Gli anticorpi non sono utilizzati nel Western Blotting.", False)]),

    ("Spiega il principio della cromatografia di affinità.",
     [("La separazione delle proteine avviene in base alla loro affinità per un ligando immobilizzato su una resina.", True),
      ("Studia la divisione cellulare nelle colture di cellule.", False),
      ("Analizza la struttura dei lipidi nelle membrane cellulari.", False),
      ("Quantifica la produzione di RNA nei campioni biologici.", False),
      ("Misura la quantità di acqua all'interno delle cellule.", False)]),

    ("Come si purificano le proteine GFP usando la cromatografia di affinità?",
     [("Utilizzando una resina NiNTA che si lega alla Hys-tag della GFP, seguita da lavaggi per rimuovere proteine non specifiche e eluzione con imidazolo.", True),
      ("Inserendo la GFP direttamente nel gel di elettroforesi.", False),
      ("Separando le proteine in base alla loro carica molecolare.", False),
      ("Studiando le interazioni tra proteine in colture di cellule.", False),
      ("Quantificando la produzione di ATP nelle cellule.", False)]),

    ("Cos'è una Hys-tag e perché viene utilizzata?",
     [("Una sequenza di sei istidine che si lega agli ioni metallici immobilizzati, utilizzata per la purificazione delle proteine.", True),
      ("Una struttura di membrana che regola il passaggio delle proteine.", False),
      ("Un tipo di enzima che denatura le proteine durante l'elettroforesi.", False),
      ("Una proteina usata per misurare l'attività enzimatica.", False),
      ("Un composto utilizzato per trasferire le proteine su un filtro di nitrocellulosa.", False)]),

    ("Quali sono i vantaggi della cromatografia a scambio ionico rispetto ad altre tecniche di purificazione delle proteine?",
     [("Elevata capacità di carico, risoluzione e selettività.", True),
      ("Velocità di esecuzione rispetto ad altre tecniche.", False),
      ("Costo più basso rispetto ad altre tecniche di purificazione.", False),
      ("Maggiore resistenza agli agenti denaturanti.", False),
      ("Capacità di purificare DNA e RNA insieme alle proteine.", False)]),

    ("Descrivi il ruolo del tampone di carica nella cromatografia a scambio ionico.",
     [("Mantiene il pH e la forza ionica costante per favorire l'interazione tra le proteine e la resina.", True),
      ("Funge da agente chelante per eliminare metalli pesanti.", False),
      ("Agisce come stabilizzatore del gel di poliacrilammide.", False),
      ("Promuove la formazione di legami disolfuro tra le proteine.", False),
      ("Aiuta nel trasferimento delle proteine durante il Western Blotting.", False)]),

    ("Come si prepara un gel di poliacrilammide per l'elettroforesi?",
     [("Mescolando acrilammide, bisacrilammide, un tampone di elettroforesi, ammonio persolfato e TEMED, seguiti da polimerizzazione.", True),
      ("Sciogliendo le proteine nel campione biologico con una soluzione tamponata.", False),
      ("Aggiungendo coloranti per marcare le proteine nel gel.", False),
      ("Trattando il gel con SDS per denaturare le proteine.", False),
      ("Mischiando le proteine con un tampone di estrazione.", False)]),

    ("Quali sono le funzioni dell’acrilammide e del bisacrilammide nel gel di SDS-PAGE?",
     [("L'acrilammide forma il gel, mentre il bisacrilammide funge da agente reticolante.", True),
      ("Entrambi formano un tampone di carica per elettroforesi.", False),
      ("Agiscono come agenti tampone per mantenere costante il pH.", False),
      ("Denaturano le proteine nel campione biologico.", False),
      ("Stabilizzano le proteine nel gel durante l'elettroforesi.", False)]),

    ("Cos'è un Laemmli Buffer e a cosa serve?",
     [("Un tampone di carica contenente SDS e β-mercaptoetanolo per denaturare le proteine e dare loro una carica negativa uniforme.", True),
      ("Una resina utilizzata per purificare le proteine mediante cromatografia di affinità.", False),
      ("Un composto utilizzato per colorare le bande proteiche in gel di elettroforesi.", False),
      ("Un enzima utilizzato per la rilevazione del segnale nel Western Blotting.", False),
      ("Un agente stabilizzante usato durante la cristallizzazione delle proteine.", False)]),

    ("Qual è il ruolo del marker di peso molecolare nell'SDS-PAGE?",
     [("Fornisce una scala di riferimento per determinare il peso molecolare delle proteine separate.", True),
      ("Agisce come agente tampone per mantenere costante il pH nel gel.", False),
      ("Stabilizza le proteine durante l'elettroforesi.", False),
      ("Quantifica la concentrazione delle proteine nel campione biologico.", False),
      ("Aiuta nella trasformazione genetica delle cellule.", False)]),

    ("Quali sono le differenze tra il Coomassie Brilliant Blue e il Ponceau Red in termini di colorazione delle proteine?",
     [("Coomassie Brilliant Blue è più sensibile e permanente, mentre il Ponceau Red è reversibile e utilizzato per confermare il trasferimento delle proteine nel Western Blotting.", True),
      ("Entrambi sono permanenti e usati per visualizzare le proteine nel gel.", False),
      ("Ponceau Red è più sensibile del Coomassie Brilliant Blue nel rilevare proteine a bassa concentrazione.", False),
      ("Coomassie Brilliant Blue è più adatto per la colorazione di DNA e RNA.", False),
      ("Ponceau Red è più utilizzato nella cristallografia delle proteine rispetto al Coomassie Brilliant Blue.", False)]),

    ("Come funziona il meccanismo di trasferimento delle proteine in un Western Blot?",
     [("Le proteine sono spostate dal gel al filtro di nitrocellulosa applicando un campo elettrico.", True),
      ("Le proteine sono trasportate nel gel di poliacrilammide mediante centrifugazione.", False),
      ("Le proteine sono concentrate utilizzando una membrana semipermeabile.", False),
      ("Le proteine sono estratte dal campione biologico con un tampone di estrazione.", False),
      ("Le proteine sono marcate con un colorante fluorescente per la visualizzazione.", False)]),

    ("Quali sono le caratteristiche di una buona soluzione di bloccaggio nel Western Blotting?",
     [("Blocca i siti non specifici sul filtro senza interferire con il legame anticorpo-antigene, spesso contiene proteine come il latte scremato in polvere.", True),
      ("Agisce come agente tamponante per mantenere costante il pH durante il trasferimento delle proteine.", False),
      ("Stabilizza le proteine nel gel di elettroforesi durante l'elettroforesi.", False),
      ("Aiuta nella denaturazione delle proteine nel campione biologico.", False),
      ("Promuove la fluorescenza delle proteine marcate nel filtro di nitrocellulosa.", False)]),

    ("Spiega il processo di sviluppo del segnale nel Western Blotting usando BCIP/NBT.",
     [("La fosfatasi alcalina sull'anticorpo secondario converte BCIP/NBT in un prodotto blu, evidenziando le bande proteiche.", True),
      ("Le proteine sono trasferite dal gel di poliacrilammide al filtro di nitrocellulosa.", False),
      ("Il tampone di bloccaggio riduce il rumore di fondo nel Western Blotting.", False),
      ("BCIP/NBT è un colorante fluorescente utilizzato per marcare le proteine nel gel.", False),
      ("BCIP/NBT è un agente riducente che denatura le proteine nel campione biologico.", False)]),


    ("Quali sono le applicazioni principali della spettrofotometria in biologia molecolare?",
     [("Misurazione della concentrazione di proteine, acidi nucleici e attività enzimatica.", True),
      ("Separazione delle proteine in base alla loro affinità per un ligando specifico.", False),
      ("Determinazione della struttura tridimensionale delle proteine.", False),
      ("Identificazione di mutazioni genetiche nei campioni biologici.", False),
      ("Misurazione della fluorescenza delle proteine nel gel di elettroforesi.", False)]),

    ("Come si determina la concentrazione delle proteine usando uno spettrofotometro?",
     [("Misurando l'assorbanza a una lunghezza d'onda specifica e utilizzando una curva di calibrazione.", True),
      ("Analizzando la fluorescenza delle proteine nel campione biologico.", False),
      ("Misurando la conducibilità elettrica della soluzione contenente le proteine.", False),
      ("Valutando la mobilità delle proteine nel gel di poliacrilammide.", False),
      ("Calcolando la densità ottica delle bande proteiche nel Western Blotting.", False)]),

    ("Quali sono i principali tipi di colonne cromatografiche utilizzate in biologia molecolare?",
     [("Colonne di affinità, scambio ionico, esclusione dimensionale e fase inversa.", True),
      ("Colonne per la purificazione dei lipidi e degli zuccheri.", False),
      ("Colonne per l'analisi della fluorescenza delle proteine.", False),
      ("Colonne per la cristallizzazione delle proteine.", False),
      ("Colonne per la microscopia elettronica a trasmissione.", False)]),

    ("Quali sono i vantaggi dell’uso di una resina NiNTA nella purificazione delle proteine?",
     [("Elevata specificità per proteine con Hys-tag, alta capacità di legame e facilità di utilizzo.", True),
      ("Capacità di separare le proteine in base alla loro dimensione molecolare.", False),
      ("Ampia gamma di pH di lavoro senza perdita di attività.", False),
      ("Buona resistenza agli agenti denaturanti come il SDS.", False),
      ("Capacità di catturare DNA e RNA contaminanti.", False)]),

    ("Cos'è l'imidazolo e perché è usato nella cromatografia di affinità?",
     [("Un composto che compete con l'istidina per i siti di legame al nichel, usato per eluire le proteine dalla resina.", True),
      ("Un agente riducente utilizzato per denaturare le proteine nel campione biologico.", False),
      ("Un tampone di estrazione che stabilizza le proteine durante l'elettroforesi.", False),
      ("Un agente tampone che mantiene costante il pH durante l'elettroforesi su gel.", False),
      ("Un colorante utilizzato per visualizzare le proteine in gel di elettroforesi.", False)]),

    ("Quali sono le principali differenze tra la cromatografia di affinità e la cromatografia a scambio ionico?",
     [("La cromatografia di affinità separa le proteine in base alla loro affinità specifica per un ligando, mentre la cromatografia a scambio ionico separa in base alla carica.", True),
      ("La cromatografia di affinità impiega colonne più lunghe rispetto alla cromatografia a scambio ionico.", False),
      ("La cromatografia di affinità richiede l'uso di resine a scambio ionico, mentre la cromatografia a scambio ionico utilizza resine di affinità.", False),
      ("La cromatografia di affinità è più rapida della cromatografia a scambio ionico.", False),
      ("La cromatografia di affinità non richiede l'uso di buffer per mantenere costante il pH.", False)]),

    ("Descrivi il ruolo della fosfatasi alcalina nel Western Blotting.",
     [("Coniugata all'anticorpo secondario, catalizza la reazione che sviluppa il segnale colorimetrico.", True),
      ("Agisce come tampone di bloccaggio per ridurre il rumore di fondo nel Western Blotting.", False),
      ("Stabilizza le proteine durante il trasferimento dal gel al filtro di nitrocellulosa.", False),
      ("Aumenta la visibilità delle bande proteiche nel gel di elettroforesi.", False),
      ("Contribuisce alla formazione delle bande proteiche nel gel di SDS-PAGE.", False)]),

    ("Perché è importante la fase di lavaggio nella cromatografia di affinità?",
     [("Rimuove le proteine non specificamente legate alla resina, aumentando la purezza della proteina di interesse.", True),
      ("Denatura le proteine non desiderate durante la purificazione.", False),
      ("Aiuta nel trasferimento delle proteine durante il Western Blotting.", False),
      ("Mantiene costante il pH durante la separazione delle proteine.", False),
      ("Blocca i siti non specifici sul filtro di nitrocellulosa nel Western Blotting.", False)]),

    ("Come si può verificare l'efficienza del trasferimento proteico nel Western Blotting?",
     [("Colorando il filtro con Ponceau Red per visualizzare le proteine trasferite.", True),
      ("Misurando la fluorescenza delle proteine marcate nel filtro di nitrocellulosa.", False),
      ("Analizzando la conducibilità elettrica della soluzione di bloccaggio.", False),
      ("Controllando la temperatura durante il trasferimento delle proteine.", False),
      ("Quantificando la densità ottica delle bande proteiche nel gel di elettroforesi.", False)]),

    ("Quali sono le principali fonti di errore nella tecnica di Western Blotting?",
     [("Trasferimento inefficace, legame non specifico degli anticorpi, sviluppo del segnale debole o eccessivo.", True),
      ("Preparazione inefficace del tampone di carica per SDS-PAGE.", False),
      ("Utilizzo di gel di poliacrilammide non adeguatamente polimerizzato.", False),
      ("Misurazione errata della temperatura durante l'elettroforesi.", False),
      ("Impiego di anticorpi non specifici per la rilevazione delle proteine.", False)]),

    ("Cos'è una curva di calibrazione e come viene utilizzata nella spettrofotometria?",
     [("Un grafico che mostra la relazione tra assorbanza e concentrazione, utilizzato per determinare la concentrazione di un campione sconosciuto.", True),
      ("Una tecnica per separare proteine in base alla loro carica netta.", False),
      ("Un metodo per misurare la fluorescenza delle proteine in soluzione.", False),
      ("Un modello matematico per predire la struttura tridimensionale delle proteine.", False),
      ("Un approccio per analizzare la sequenza nucleotidica del DNA.", False)]),

    ("Quali sono i limiti della tecnica SDS-PAGE?",
     [("Non separa proteine con lo stesso peso molecolare, non fornisce informazioni sulla struttura nativa o sull'attività delle proteine.", True),
      ("Richiede lunghe ore di esecuzione per ottenere risultati accurati.", False),
      ("Non può essere utilizzata per analizzare campioni biologici complessi.", False),
      ("Non è in grado di distinguere tra diverse isoforme proteiche.", False),
      ("Non funziona bene con proteine altamente idrofobiche.", False)]),

    ("Come si può aumentare la sensibilità di rilevamento nel Western Blotting?",
     [("Utilizzando anticorpi di alta affinità, riducendo i tempi di lavaggio e aumentando la concentrazione del substrato di sviluppo.", True),
      ("Aumentando il pH del tampone di bloccaggio nel filtro di nitrocellulosa.", False),
      ("Aggiungendo più campione nel gel di elettroforesi per aumentare la densità delle bande proteiche.", False),
      ("Utilizzando gel di poliacrilammide con una maggiore concentrazione di SDS.", False),
      ("Riducendo la durata complessiva del processo di Western Blotting.", False)]),

    ("Qual è il principio della tecnica di immunoprecipitazione?",
     [("Utilizzare anticorpi specifici per isolare e concentrare una proteina da una miscela complessa.", True),
      ("Separare le proteine in base alla loro carica netta in una colonna cromatografica.", False),
      ("Analizzare la fluorescenza delle proteine nel gel di elettroforesi.", False),
      ("Misurare la conducibilità elettrica delle soluzioni contenenti proteine.", False),
      ("Preparare un campione di DNA per l'analisi di sequenziamento.", False)]),

    ("Quali sono le applicazioni della cromatografia a fase inversa in biologia molecolare?",
     [("Separazione e purificazione di peptidi e proteine in base alla loro idrofobicità.", True),
      ("Analisi della fluorescenza delle proteine in soluzione.", False),
      ("Determinazione della concentrazione di proteine nel campione.", False),
      ("Identificazione di mutazioni genetiche nel DNA.", False),
      ("Misurazione dell'attività enzimatica in una soluzione.", False)]),

    ("Spiega il concetto di affinità tra ligando e recettore nella cromatografia di affinità.",
     [("L'affinità è la forza con cui un ligando si lega specificamente a un recettore sulla resina cromatografica.", True),
      ("L'affinità indica la capacità di una proteina di legare un substrato specifico.", False),
      ("L'affinità descrive la capacità di un enzima di catalizzare una reazione chimica.", False),
      ("L'affinità indica la capacità di un anticorpo di riconoscere un antigene specifico.", False),
      ("L'affinità è la misura della velocità di eluizione delle proteine dalla resina cromatografica.", False)]),

    ("Quali sono le tecniche alternative alla cromatografia di affinità per la purificazione delle proteine?",
     [("Cromatografia a scambio ionico, esclusione dimensionale, precipitazione selettiva.", True),
      ("Elettroforesi su gel di poliacrilammide, Western Blotting, immunoistochimica.", False),
      ("Analisi di fluorescenza in tempo risolto, risonanza plasmonica superficiale.", False),
      ("Microscopia elettronica a trasmissione, spettrometria di massa, cristallografia a raggi X.", False),
      ("Ionizzazione elettrospray, estrazione in fase solida, reazione a catena della polimerasi.", False)]),

    ("Come si esegue un’analisi qualitativa delle proteine mediante spettrofotometria?",
     [("Misurando l'assorbanza a specifiche lunghezze d'onda e confrontando con standard noti.", True),
      ("Determinando la concentrazione di proteine attraverso una curva di calibrazione.", False),
      ("Quantificando la fluorescenza delle proteine marcate nel campione biologico.", False),
      ("Valutando l'attività enzimatica delle proteine estratte dal campione biologico.", False),
      ("Analizzando la velocità di sedimentazione delle proteine in una soluzione densità-gradiata.", False)]),

    ("Qual è il ruolo dei controlli positivi e negativi nel Western Blotting?",
     [("Assicurano la validità del risultato: il controllo positivo conferma il corretto funzionamento del sistema, il controllo negativo verifica l'assenza di risultati falsi positivi.", True),
      ("Determinano la concentrazione delle proteine nel campione biologico.", False),
      ("Quantificano la densità ottica delle bande proteiche nel gel di elettroforesi.", False),
      ("Valutano la purezza delle proteine eluite dalla resina di cromatografia.", False),
      ("Misurano l'intensità della fluorescenza delle proteine marcanti nel filtro di nitrocellulosa.", False)]),

    ("Descrivi un esempio di applicazione pratica del Western Blotting in ricerca biomedica.",
     [("Identificazione di proteine specifiche associate a malattie, come la rilevazione delle proteine prioniche nella diagnosi della malattia di Creutzfeldt-Jakob.", True),
      ("Separazione elettroforetica di proteine in un gel di poliacrilammide.", False),
      ("Purificazione di proteine attraverso cromatografia di affinità.", False),
      ("Analisi strutturale delle proteine mediante cristallografia a raggi X.", False),
      ("Stima della concentrazione di proteine nel campione biologico utilizzando uno spettrofotometro.", False)]),


    ("Quali sono i principi della centrifugazione differenziale e della centrifugazione a gradiente di densità?",
     [("La centrifugazione differenziale separa componenti cellulari in base alle loro dimensioni e densità, mentre la centrifugazione a gradiente di densità separa in base alla densità con precisione maggiore.", True),
      ("La centrifugazione differenziale separa componenti cellulari in base alla densità, mentre la centrifugazione a gradiente di densità separa in base alle dimensioni molecolari.", False),
      ("Entrambe separano le proteine in base alla loro carica netta nel campione.", False),
      ("La centrifugazione differenziale separa componenti cellulari in base alla loro velocità di sedimentazione, mentre la centrifugazione a gradiente di densità utilizza un campo elettrico per la separazione.", False),
      ("La centrifugazione differenziale separa componenti cellulari in base alla loro polarità, mentre la centrifugazione a gradiente di densità utilizza l'attrito per separare le proteine.", False)]),

    ("Quali sono i passaggi critici per evitare la degradazione delle proteine durante l'estrazione?",
     [("Utilizzare inibitori delle proteasi, lavorare a basse temperature, minimizzare il tempo di estrazione.", True),
      ("Aumentare la concentrazione di detergenti per migliorare il lisi cellulare.", False),
      ("Utilizzare tampone di carica per stabilizzare le proteine durante l'estrazione.", False),
      ("Aumentare la temperatura per accelerare il processo di estrazione.", False),
      ("Utilizzare soluzioni fortemente alcaline per favorire il rilascio delle proteine.", False)]),

    ("Cos'è una proteasi e come si può inibire la sua attività durante la preparazione dei campioni?",
     [("Enzima che degrada le proteine. Si può inibire con inibitori delle proteasi come PMSF o cocktail di inibitori.", True),
      ("Enzima che sintetizza le proteine a partire dai loro amminoacidi costitutivi.", False),
      ("Enzima che misura l'attività enzimatica delle proteine nel campione.", False),
      ("Enzima che catalizza la polimerizzazione delle proteine nel gel di elettroforesi.", False),
      ("Enzima che riduce la carica superficiale delle proteine per migliorare la separazione nel gel di SDS-PAGE.", False)]),

    ("Spiega come si può ottimizzare la risoluzione delle bande proteiche in un gel SDS-PAGE.",
     [("Ottimizzando la concentrazione di acrilammide, utilizzando un adeguato tampone di corsa, e controllando la tensione applicata.", True),
      ("Aumentando il pH del tampone di corsa per migliorare la solubilità delle proteine.", False),
      ("Utilizzando una temperatura più elevata durante l'elettroforesi per accelerare la separazione.", False),
      ("Aggiungendo più SDS al campione per aumentare la denaturazione proteica.", False),
      ("Utilizzando gel di poliacrilammide con una struttura più porosa per una migliore separazione delle proteine.", False)]),

    ("Quali sono le differenze tra un tampone di carica e un tampone di eluizione nella cromatografia?",
     [("Il tampone di carica introduce il campione nella colonna mantenendo le condizioni ottimali per il legame, mentre il tampone di eluizione rimuove le proteine legate alterando le condizioni.", True),
      ("Il tampone di carica e il tampone di eluizione sono sinonimi e possono essere usati intercambiabilmente nella cromatografia.", False),
      ("Il tampone di carica serve a bloccare siti non specifici sulla resina, mentre il tampone di eluizione controlla il flusso della soluzione attraverso la colonna.", False),
      ("Il tampone di carica viene utilizzato per concentrare le proteine legate alla resina, mentre il tampone di eluizione rimuove contaminanti non desiderati.", False),
      ("Il tampone di carica viene utilizzato prima della cromatografia, mentre il tampone di eluizione è aggiunto dopo la separazione delle proteine.", False)]),

    ("Come si può utilizzare la bioinformatica per analizzare i dati ottenuti da un esperimento di Western Blotting?",
     [("Quantificazione delle bande, analisi di pattern di espressione, correlazione con dati genomici e proteomici.", True),
      ("Determinazione della concentrazione delle proteine nel campione biologico.", False),
      ("Studio della struttura tridimensionale delle proteine utilizzando modellistica computazionale.", False),
      ("Analisi della sequenza nucleotidica del DNA per identificare mutazioni genetiche associate alle proteine studiate.", False),
      ("Misurazione dell'attività enzimatica delle proteine nel campione mediante spettrofotometria.", False)]),

    ("Quali software bioinformatici sono comunemente usati per l'analisi delle sequenze proteiche?",
     [("BLAST, Clustal Omega, PyMOL, Swiss-Prot.", True),
      ("MATLAB, R, Python, SPSS.", False),
      ("Adobe Photoshop, CorelDRAW, GIMP, Inkscape.", False),
      ("Microsoft Word, Excel, PowerPoint, Access.", False),
      ("AutoCAD, SolidWorks, CATIA, Pro/ENGINEER.", False)]),

    ("Cos'è la PAGE (Polyacrylamide Gel Electrophoresis) non denaturante e come si differenzia dalla SDS-PAGE?",
     [("Separazione delle proteine mantenendole nella loro forma nativa senza denaturazione da SDS, utilizzata per studi funzionali.", True),
      ("Metodo per analizzare l'attività enzimatica delle proteine nel campione biologico.", False),
      ("Tecnica per quantificare la fluorescenza delle proteine marcate nel campione.", False),
      ("Strumento per visualizzare la struttura tridimensionale delle proteine in soluzione.", False),
      ("Procedura per misurare la concentrazione di RNA in una miscela complessa.", False)]),

    ("Quali sono le tecniche di visualizzazione delle proteine dopo la separazione mediante elettroforesi?",
     [("Colorazione con Coomassie Brilliant Blue, argento, Western Blotting, autoradiografia.", True),
      ("Misurazione dell'assorbanza delle proteine a specifiche lunghezze d'onda.", False),
      ("Utilizzo di marcatori fluorescenti per tracciare il movimento delle proteine nel gel.", False),
      ("Analisi della fluorescenza delle proteine in soluzione mediante spettrofotometria.", False),
      ("Stima della concentrazione delle proteine attraverso una curva di calibrazione in uno spettrofotometro.", False)]),

    ("Descrivi come preparare un campione per la spettrometria di massa dopo la purificazione proteica.",
     [("Digestione delle proteine con enzimi specifici come la tripsina, desalting per rimuovere sali e detergenti, concentrazione del campione.", True),
      ("Colorazione delle bande proteiche nel gel di elettroforesi per facilitare l'identificazione.", False),
      ("Misurazione dell'attività enzimatica delle proteine nel campione mediante spettrofotometria.", False),
      ("Analisi della sequenza nucleotidica del DNA per identificare mutazioni genetiche associate alle proteine studiate.", False),
      ("Studio della struttura tridimensionale delle proteine utilizzando modellistica computazionale.", False)]),

]

run_quiz(questions)