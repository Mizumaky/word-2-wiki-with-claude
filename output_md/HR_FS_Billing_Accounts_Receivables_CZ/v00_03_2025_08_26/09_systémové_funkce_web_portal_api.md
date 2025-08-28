# Systémové funkce: Web Portal API

Tato kapitola popisuje případy použití pro integrační rozhraní určené pro externí GUI, které slouží jako uživatelsky orientovaná webová aplikace určená zákazníkům.

Případy použití obsahují metody Web Portal API, které jsou detailně popsány v dokumentaci na Confluence, HR_Web_Portal_API_Description_EN.

Podmínkou pro provedení případů použití popsaných v této kapitole je vytvoření User Profile v modulu AC (dle případu použití Vytvoř uživatelský účet (API.AC.01)) a úspěšné přihlášení zákazníka (VT Customer) do Web Portalu (dle případu použití Přihlaš uživatele (API.AC.08)).

| **Funkčná oblasť**        | **Prípad použitia**                                  | **API metódy**                          |
|---------------------------|------------------------------------------------------|-----------------------------------------|
| Operace s platební kartou | Zprocesuj transakci platební kartou (API.BAR.0.1.HR) | preparePaymentOrder processPaymentOrder |
|                           |                                                      | cancelPaymentOrder                      |
| Operace s fakturou        | Vytvoř proforma fakturu (API.BAR.1.1.HR)             | generateProformaBill                    |
|                           |                                                      |                                         |

: Tabulka 34: Seznam systémových funkcí pro API

## Operace s platební kartou

Operace s platební kartou prostřednictvím Web Portal API zahrňují následující procesy:

- Zprocesování transakce platební kartou

Jednotlivé podkapitoly obsahují popis metod, které jsou volány v rámci daného procesu. Popisy definují chování systému při zavolání jednotlivých metod externím systémem přes Web Portal API.

### Zprocesuj transakci platební kartou (API.BAR.0.1.HR)

#### Cíl

Cílem této systémové funkce je přijetí a zpracování požadavku na zaplacení požadované transakce platební kartou a/nebo tokenizaci platební karty, prostřednictvím externího systému přes Web Portal API.

Vzdálený systém může požadovat:

- dobití předplaceného kreditu (TopUp)

- [uhrazení]{.mark} [přestupků (Offence)]{.mark}

- uhrazení přestupků se zákonnou pokutou (CallForPayment)

- přiřazení nové platební karty k účtu [nebo vozidlu]{.mark} (SubscribePaymentCard)

- aktivaci nebo dobití kreditu Produktového balíčku (ProductPackage)

- uhrazení OBU (Obu)

#### Spuštění případu

Na požádání externího systému prostřednictvím zpráv rozhraní Web Portal API (INT.BAR.33.HR)

#### Podmínky spuštění

User Profile je autentifikovaný a autorizovaný.

#### Popis

Externí systém zavolá posloupnost metod, které zrealizují požadovanou transakci.

Metoda ***preparePaymentOrder*** (zaregistruje požadavek na transakci platební kartou pro konkrétní typ transakce)

1.  Systém přijme metodu ***preparePaymentOrder*** s požadovanými vstupnými parametry transakce.

2.  Systém vyhodnotí vstupní parametry -- pokud chybí povinný parametr nebo odkazuje na neexistující entitu nebo obsahuje nesprávný formát, Systém vrátí chybovou zprávu spolu s informací o chybě.

3.  Systém zkontroluje, zda na vstupu je správná kombinace a správná hodnota vstupních atributů pro daný payment transaction type:

| **payment transaction type** | **shopping item identifiers** | **subscribe card** | **amount**                                                                                                                                                                    |
|------------------------------|-------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Topup                        |                               | true nebo false    | \>= Currency.minimal topup amount                                                                                                                                             |
| [Offence]{.mark}             | [List of offence id]{.mark}   | [false]{.mark}     |                                                                                                                                                                               |
| CallForPayment               | List of call for payment id   | false              | = sum(Bill.total amount -- Bill.matched amount) na základě Bills ze List of call for payment id                                                                               |
| ProductPackage               | Product package id            | false              | \>= Product package.minimal topup na základě Product package id                                                                                                               |
| Obu                          | List of service id -          | false              | = sum(event.price amount VAT) Events dohledaných na základě  List of service id (Event attribute type value = Chargeable service id, Product type = Payment transaction type) |
| SubscribePaymentCard         |                               | true               |                                                                                                                                                                               |

> Pokud kontrola není úspěšná, Systém vrátí chybovou zprávu spolu s informací o chybě.

4.  Pokud Systém zjistí, že Account je ve stavu Terminated, Systém vrátí chybovou zprávu spolu s informací o chybě.

5.  Systém iniciuje transakci na platební bráně za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR) a vytvoří odpovídající Payemnt session.

6.  Systém vrátí externímu systému číslo objednávky a redirect URL platební brány pro doplnění údajů platební karty koncovým uživatelem.

Poznámka: Externí systém otevře zákazníkovi redirect URL pro zadání platebních údajů a potvrzení transakce.

Metoda **processPaymentOrder** (ověřuje výsledek platební transakce)

1.  Systém přijme metodu ***processPaymentOrder*** s požadovanými vstupnými parametry.

2.  Systém vyhodnotí vstupní parametry -- pokud chybí povinný parametr nebo odkazuje na neexistující entitu nebo obsahuje nesprávný formát, Systém vrátí chybovou zprávu spolu s informací o chybě.

3.  Systém si vyžádá stav transakce na platební bráně za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

4.  Pokud transakce byla úspěšná, Systém provede podle typu transakce potřebné návazné kroky:

    a.  Top-up (za použití případu užití Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)):

        i.  Systém updatuje Payment session a vytvoří kreditní Payment.

        ii. Pokud na vstupu bylo subscribe card = true, Systém získaný token a informace o Payment card uloží na Accountu za použití systémové funkce Pridaj platobnú kartu (SYS.VCM.4.1).

        iii. Systém o částku top-up platby navýší zůstatek předplaceného kreditu, použije se případ užití Aktualizuj zůstatek (SYS.BM.1.2) s důvod updatu balance = Top-up.

        iv. Systém zjistí údaje o top-up eventě za použití případu užití Získej produkt (SYS.PCRE.1.2.HR).

        v.  Systém vygeneruje jednorázovou fakturu za mýto za užití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

<!-- -->

i.  Systém napáruje nově vytvořený Bill na nově vytvořený Payment, tj. vytvoří Matching.

ii. Systém na základě provedého párování updatuje atributy napárovaného Bill a Payment.

    a.  CallForPayment (za použití případu užití Uhraď přestupek (UC.BAR.0.20.HR)):

        i.  Systém updatuje Payment session a vytvoří kreditní Payment.

        ii. Systém na základě každé zaplacené Unpaid Toll Transaction vytvoří odpovídající Toll Transaction ve stavu Processed, a zruší Unapid Toll Transaction.

        iii. Systém vygeneruje jednorázovou fakturu za mýto za užití systémové funkce Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR).

        iv. Systém napáruje nově vytvořenou fakturu s platbou, tj. vytvoří pro ně Matching.

        v.  Systém na základě provedého párování updatuje atributy napárovaného Bill a Payment.

        vi. Systém přenastaví na zaplacených Výzvách na úhradu Bill issue status = Replaced a Replaced by bill = reference na novou fakturu.

        vii. Systém informuje Dunning, zavoláním případu užití Aktualizuj dluh (SYS.DU.1.2.HR) s uvedením Effective date of matching provedeného párování.

        viii. Systém na základě zaplacených Přestupků updatuje záznam Alert listu.

    b.  ProductPackage (za použití případu užití Zaplať Produktový balíček (UC.BAR.0.21.HR)):

        i.  Systém updatuje Payment session a vytvoří kreditní Payment.

        ii. Systém vytvoří nový Product account (pokud Account ze vstupu byl národní Account a daný Product account na zákazníkovi neexistuje) nebo updatuje existující Product account (pokud Account na vstupu byl Product account) za použití případu užití ([Pridaj produktový]{.mark} [balíček (UC.VCM.1.6))]{.mark}.

        iii. Systém o částku platby navýší zůstatek odpovídající Product balance, použije se případ užití Aktualizuj zůstatek (SYS.BM.1.2) s Product account number.

        iv. Systém zjistí údaje o Product package eventě za použití případu užití Získej produkt (SYS.PCRE.1.2.HR).

        v.  Systém vygeneruje jednorázovou fakturu za služby za užití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

iii. Systém napáruje nově vytvořený Bill na nově vytvořený Payment, tj. vytvoří Matching.

iv. Systém na základě provedého párování updatuje atributy napárovaného Bill a Payment.

    a.  Obu (za použití případu užití Zaplať Obu (UC.BAR.0.22.HR)):

        i.  Systém updatuje Payment session a vytvoří kreditní Payment.

        ii. Systém o částku platby navýší zůstatek odpovídající Obu balance daného zákazníka a Bill issuera ve VCM.

    b.  SubscriptionPaymentCard (za použití systémové funkce Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR)):

        i.  Systém updatuje Payment session a vytvoří kreditní Payment.

        ii. Systém získaný token a informace o Payment card uloží na Accountu za použití systémové funkce Pridaj platobnú kartu (SYS.VCM.4.1).

        iii. Systém vytvoří rušící Payment session a vytvoří debetní Payment, který napáruje na kreditní Payment.

        iv. Systém zruší rezervovanou transakci na CorvusPay platební bráně.

<!-- -->

5.  Systém vrátí definované výstupní parametry externímu systému. V případě payment transaction type Topup, CallForPayment, ProductPackage na výstupu je také identifikace vygenerovaného Bill a Document. V případě payment transaction type ProductPackage na výstupu je také identifikace Product account.

6.  Postup končí.

#### Alternativní postupy

(A1) Zruš transakci platební kartou (Cancel button z redirect URL stránky)

V tomto postupu po příchodu metody preparePaymentOrder (na registraci požadavku na transakci platební kartou pro konkrétní typ transakce) nepřijde metoda processPaymentOrder, ale metoda na zrušení transakce, když zákazník použil Cancel tlačítko z redirect URL stránky.

Metoda ***cancelPaymentOrder*** (zruš požadavek na transakci platební kartou)

1.  Systém přijme metodu ***cancelPaymentOrder*** s požadovanými vstupnými parametry transakce.

2.  Systém vyhodnotí vstupní parametry -- pokud chybí povinný parametr nebo odkazuje na neexistující entitu nebo obsahuje nesprávný formát, Systém vrátí chybovou zprávu spolu s informací o chybě.

3.  Systém zruší transakci v Syst0mu, za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR) -- chybový postup Zrušení transakce zákazníkem.

4.  Systém vrátí externímu systému výsledek, číslo objednávky a další definované výstupní parametry.

Postup končí.

## Operace s fakturou

### Vygeneruj proforma fakturu (API.BAR.1.1.HR)

#### Cíl

Cílem této systémové funkce je přijetí a zpracování požadavku externího systému přes Web Portal API na vygenerování proforma faktury (Offer) na top-up nebo nákup OBU, které koncový zákazník chce zaplatit bankovním převodem.

#### Spuštění případu

Na požádání externího systému prostřednictvím zpráv rozhraní Web Portal API (INT.BAR.33.HR)

#### Podmínky spuštění

User Profile je autentifikovaný a autorizovaný.

#### Popis

Externí systém zavolá posloupnost metod, které zrealizují požadovanou transakci.

Metoda ***generateProformaBill***

1.  Systém přijme metodu ***generateProformaBill*** s požadovanými vstupnými parametry.

2.  Systém vyhodnotí vstupní parametry -- pokud chybí povinný parametr nebo odkazuje na neexistující entitu nebo obsahuje nesprávný formát, Systém vrátí chybovou zprávu spolu s informací o chybě.

3.  Systém zkontroluje, zda na vstupu je správná kombinace a správná hodnota vstupních atributů pro daný payment transaction type:

| **payment transaction type** | **shopping item identifiers** | **amount**                                                           |
|------------------------------|-------------------------------|----------------------------------------------------------------------|
| Topup                        |                               | \>= Currency.minimal topup amount                                    |
| ProductPackage               | Product package id            | \>= Product package.minimal topup na základě Product package id      |
| Obu                          | List of service id -          | = sum(event.price amount VAT) na základě Events z List of service id |

> Pokud kontrola není úspěšná, Systém vrátí chybovou zprávu spolu s informací o chybě.

4.  Pokud Systém zjistí, že Account je ve stavu Terminated, Systém vrátí chybovou zprávu spolu s informací o chybě.

5.  Systém vygeneruje Proforma fakturu za užití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

<!-- -->

7.  Systém vrátí definované výstupní parametry externímu systému - identifikace vygenerovaného Bill a Document.

8.  postup končí.