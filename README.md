# Progetto: 
Costruire un simulatore che simuli una soluzione distribuita dei server di un gioco online.
> 
Instanziazione di una vm dedicata ad ogni partita che rappresenta un'istanza del server di gioco. 
Allocata all'inizio di ogni match e deallocata al termine di quest'ultimo. 
Il posizionamento di questa è legata ai giocatori, se questi in movimento, è possibile che questa migri in datacenter diversi per garantire le prestazioni di rete soddisfacenti a tutti i giocatori di quella partita. 

## TODO: 
##### OMNET++: 
Creare una rete 5g con il simulatore
* creare una policy per definire dove posizionare il server dedicato ai giocatori
* creazione di una modalità di migrazione
  * devo creare il VNF, NFVI, NFV MANO?


Creare gli attori per simulare la comunicazione di pacchetti durante un match 
* creazione utenti stub che simula le azioni in game
* creazione server stub che simula le azioni in game
* creazione main server stub per far iniziare e terminare la partita
* "progettazione" comunicazione

##### DATA: 
recuperare i dati che servono per creare la distribuzione dei dati che transitano in un match
* durata della partita
* quantità di pacchetti 
* dimensione di pacchetti
* intervallo tra un pacchetto e l'altro 
* distribuzione di questi pacchetti nell'arco della partita (laning phase, roaming, mid, end) 
* 
Recuperare quanto traffico deve gestire un server 
*boh circa sommando il traffico degli utenti e rispettive risposte?*

____
## Risorse
### Omnet
* [Omnet++ v5.5.1 windows](https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.5.1/omnetpp-5.5.1-src-windows.zip): simulatore e ide
* [Inet v3.6.6](https://github.com/inet-framework/inet/releases/download/v3.6.6/inet-3.6.6-src.tgz): librerie network
* [SimuLTE v1.1.0](https://github.com/inet-framework/simulte/archive/v1.1.0.zip): librerie simulazione LTE

*nb: non sgarrare, esattamente queste versioni altrimenti l'IDE si arrabbia*

### Env Management
* [Anaconda](https://www.anaconda.com/products/individual): toolkit usato per creare environment per eseguire il crawling sui siti web e analisi dei dati raccolti 

### Scraping
* [Scrapy](https://docs.scrapy.org/en/latest/intro/overview.html): Framework per fare crawling su siti web e gestire il traversamento del sito web  
* [RiotAPI](https://developer.riotgames.com/apis): Interfaccia fornita dagli sviluppatori di gioco per interrogare i server di gioco in maniera legittima
* [OP.GG](https://euw.op.gg/): Sito su cui si fa crawling per ottenere i dati delle partite 

### Input catching
* [Micro Mouse Macro](https://www.turnssoft.com/mini-mouse-macro.html): Software mediante il quale si raccolgono gli input di tastiera e mouse durante un intervallo di tempo predefinito
