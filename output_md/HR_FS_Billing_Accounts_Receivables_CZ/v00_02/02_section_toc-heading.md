# {#section .TOC-Heading}

Obsah 4

Historie dokumentu 8

1 Úvod 10

1.1 Procesy HR 10

1.1.1 Předplacení kreditu 10

1.1.2 Uložení mýtných transakcí 12

1.1.3 Vystavení pravidelné faktury za mýtné 13

1.1.4 Vystavení jednorázové faktury 14

[1.1.5]{.mark} [Vystavení pravidelné výzvy na úhradu za platby tankovací kartou]{.mark} 15

1.1.6 Re-rating 15

2 Doménový model 16

2.1 Diagram doménového modelu 16

2.2 Přehled entit 18

2.3 Atributy entit 20

2.3.1 Bill (Faktura) 20

2.3.2 Bill Item (Položka faktury) 25

2.3.3 Bill Session (Fakturační dávka) 28

2.3.4 Payment (Platba) 31

2.3.5 Payment Session (Platební transakce) 37

2.3.6 Matching (Párování plateb) 41

2.3.7 Toll Transaction Base (Mýtná transakce - základ) 42

2.3.8 Rated Toll Event (Oceněná mýtná událost) 49

2.3.9 Rated Service Event (Oceněná služba) 51

2.3.10 Bill Session Statistics (Statistika fakturační dávky) 54

2.3.11 Bill Session Steps Statistics (Statistika kroků fakturační dávky) 56

2.3.12 Bill Item Statistics (Statistika fakturační dávky podle Bill item typu a Měny) 56

[2.3.13]{.mark} [Settlement Record (Záznam vyrovnání)]{.mark} 57

2.3.14 Card Payment Request (Požadavek na platbu kartou) 57

[2.3.15]{.mark} [ERP Log (ERP Log)]{.mark} 58

[2.3.16]{.mark} [ERP Import (ERP Import)]{.mark} 58

[2.3.17]{.mark} [ERP Export (ERP Export)]{.mark} 59

2.4 Atributy konfigurovatelných číselníků 60

2.4.1 Payment Type (Typ platby) 60

2.4.2 Currency (Měna) 60

2.4.3 Rounding (Zaokrouhlování) 62

[2.4.4]{.mark} [CorvusPay Payment Method (CorvusPay platební metoda)]{.mark} 62

[2.4.5]{.mark} [Card type (Typ karty)]{.mark} 63

[2.4.6]{.mark} [CorvusPay Response Code (CorvusPay kód odpovědi)]{.mark} 63

[2.4.7]{.mark} [Process Step Scheduling (Plánování kroků zpracování)]{.mark} 64

2.5 Vysvětlení ke specifikaci entit a atributů entit 65

3 Aktéři 68

3.1 Seznam aktérů 68

[3.2]{.mark} [Seznam rolí]{.mark} 68

3.3 Pracovní týmy 68

4 Případy užití 70

4.1 Operace s platbami 71

4.1.1 Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR) 71

4.1.2 Zaplať poplatek na POS (UC.BAR.0.3.HR) 77

4.1.3 Uhraď přestupek (UC.BAR.0.20.HR) 82

5 Systémové funkce 89

5.1 Fakturace 90

5.1.1 Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.HR) 90

5.1.2 Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR) 97

5.1.3 Vytvoř fakturační dávku (SYS.BAR.0.6.HR) 104

5.1.4 Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR) 106

5.1.5 Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) 110

5.1.6 Vytvoř výzvy na úhradu za přestupky (SYS.BAR.0.13.HR) 114

5.1.7 Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR) 118

5.2 Zpracování mýtných transakcí 125

5.2.1 Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR) 125

5.2.2 Vytvoř billing details (SYS.BAR.1.9.HR) 133

5.2.3 Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR) 136

5.3 Operace s platbami 143

5.3.1 Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR) 143

5.3.2 Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR) 147

5.3.3 Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR) 149

6 Neprocesní funkcionality 154

6.1 Fakturace 154

6.1.1 Číslování faktur 154

6.1.2 Číslování plateb 155

6.1.3 Zaokrouhlování 156

6.1.4 Variabilní symbol 156

[6.1.5]{.mark} [Atributy dokumentu pro dobropis a vrubopis]{.mark} 157

6.2 BIBA - pravidla pro určení BIBA 157

6.3 Vliv plateb na BM Balance 158

7 Příloha A -- Integrační body 159

7.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) 159

7.2 Rozhraní Platební brána CorvusPay (INT.BAR.27.HR) 159

7.2.1 Online platba tokenem platební karty 159

7.2.2 Online platba platební kartou 161

7.3 Rozhraní EFT Terminal NexGo (INT.BAR.28.HR) 162

7.4 Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR) 163

7.4.1 Authorization Request (Systém → EFT) 164

7.4.2 Authorization Request Confirmation (EFT → Systém) 164

7.4.3 Authorization Response (EFT → Systém) 164

[7.5]{.mark} [Rozhraní ERP Navision (INT.BAR.30.HR)]{.mark} 166

7.6 Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR) 166

7.6.1 Registrace business premisses 167

7.6.2 Fiskalizace faktury 167

7.7 Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR) 168

[7.8]{.mark} [Rozhraní Web portal API (INT.BAR.33.HR)]{.mark} 168

[7.9]{.mark} [Rozhraní POS API (INT.BAR.34.HR)]{.mark} 168

[7.10]{.mark} [Rozhraní KIOSK API (INT.BAR.35.HR)]{.mark} 168

[7.11]{.mark} [Rozhraní IEFBO API (INT.BAR.36.HR)]{.mark} 168

7.12 Rozhraní EUCARIS (INT.TDP.06) 169

7.12.1 Rozhraní 169

8 Příloha B -- Vstupní a výstupní artefakty¨ 171

8.1 Dokumenty 171

8.1.1 Společná nastavení 171

8.1.2 Zálohová faktura za top-up (DOC.BE.01.HR) a (DOC.BE.01B.HR) 175

8.1.3 Zálohová faktura za předplacení kreditu - dobropis (DOC.BE.06) 175

8.1.4 Faktura za mýtné (DOC.BE.10.HR) a (DOC.BE.10B.HR) 175

[8.1.5]{.mark} [Detailní výpis mýtných transakcí k faktuře (DOC.BE.11)]{.mark} 177

8.1.6 Vrubopis za mýtné (DOC.BE.13.HR) 180

8.1.7 Dobropis za mýtné (DOC.BE.14.HR) 181

8.1.8 Faktura za služby (DOC.BE.16.HR) 181

8.1.9 Dobropis za služby (DOC.BE.17.HR) 181

[8.1.10]{.mark} [Faktura za smluvní pokutu (DOC.BE.19.HR)]{.mark} 181

[8.1.11]{.mark} [Dobropis za smluvní pokutu (DOC.BE.20.HR)]{.mark} 181

8.1.12 eFaktura (DOC.BE.21.HR) 181

8.1.13 Výzva k úhradě za přestupky (DOC.BE.22.HR) 181

8.1.14 Výzva k úhradě za přestupky -- Dobropis (DOC.BE.23.HR) 182

8.1.15 Proforma faktura (DOC.BE.24.HR) 182

8.2 Externí oznámení (e-mail) 182

8.2.1 Společná nastavení -- e-mail 183

8.2.2 Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR) 186

8.2.3 Unpaid toll transaction notification (NTF.BAR.13.HR) 186

8.2.4 Oznámení o vystavení faktury (NTF.BAR.21.HR) 187

8.2.5 Oznámení o vystavení účetního dokladu (NTF.DF.01.HR) 188

8.3 Externí oznámení (SMS) 188

8.3.1 Společná nastavení -- SMS 189

8.3.2 Unpaid toll transaction SMS notification (NTF.BAR.14.HR) 189

8.4 Výměnné soubory 190

8.4.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) 190

9 Příloha C -- Konfigurovatelnost modulu 194

9.1 Naplánované operace 194

[9.2]{.mark} [Konfigurační klíče]{.mark} 195

9.3 Číselníky a systémová nastavení 197

9.3.1 Payment Type (Typ platby) 197

9.3.2 Rounding (Zaokrouhlování) 198

9.3.3 CorvusPay Payment Method (CorvusPay platební metoda) 198

9.3.4 CorvusPay Response Code (CorvusPay kód odpovědi) 198