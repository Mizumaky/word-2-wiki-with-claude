# {#section .TOC-Heading}

Obsah 4

Historie dokumentu 9

1 Úvod 13

1.1 Procesy HR 13

1.1.1 Předplacení kreditu 13

1.1.2 Uložení mýtných transakcí 15

1.1.3 Vystavení pravidelné faktury za mýtné 16

1.1.4 Vystavení jednorázové faktury 17

[1.1.5]{.mark} [Vystavení pravidelné výzvy na úhradu za platby tankovací kartou]{.mark} 18

1.1.6 Re-rating 18

2 Doménový model 19

2.1 Diagram doménového modelu 19

2.2 Přehled entit 21

2.3 Atributy entit 23

2.3.1 Bill (Faktura) 23

2.3.2 Bill Item (Položka faktury) 29

2.3.3 Bill Session (Fakturační dávka) 33

2.3.4 Payment (Platba) 35

2.3.5 Payment Session (Platební transakce) 41

2.3.1 Payment Session Item (Položka platební transakce) 45

2.3.2 Matching (Párování plateb) 46

2.3.3 Toll Transaction Base (Mýtná transakce - základ) 47

2.3.4 Rated Toll Event (Oceněná mýtná událost) 54

2.3.5 Rated Service Event (Oceněná služba) 56

2.3.6 Bill Session Statistics (Statistika fakturační dávky) 59

2.3.7 Bill Session Steps Statistics (Statistika kroků fakturační dávky) 61

2.3.8 Bill Item Statistics (Statistika fakturační dávky podle Bill item typu a Měny) 62

[2.3.9]{.mark} [Settlement Record (Záznam vyrovnání)]{.mark} 62

2.3.10 Card Payment Request (Požadavek na platbu kartou) 63

[2.3.11]{.mark} [ERP Log (ERP Log)]{.mark} 63

[2.3.12]{.mark} [ERP Import (ERP Import)]{.mark} 63

[2.3.13]{.mark} [ERP Export (ERP Export)]{.mark} 64

2.4 Atributy konfigurovatelných číselníků 65

2.4.1 Payment Type (Typ platby) 65

2.4.2 Currency (Měna) 65

2.4.3 Rounding (Zaokrouhlování) 67

2.4.4 CorvusPay Payment Method (CorvusPay platební metoda) 67

[2.4.5]{.mark} [Card type (Typ karty)]{.mark} 68

2.4.6 CorvusPay Response Code (CorvusPay kód odpovědi) 68

2.4.7 Process Step Scheduling (Plánování kroků zpracování) 69

2.5 Vysvětlení ke specifikaci entit a atributů entit 70

3 Aktéři 73

3.1 Seznam aktérů 73

[3.2]{.mark} [Seznam rolí]{.mark} 73

3.3 Pracovní týmy 73

4 Případy užití 75

4.1 Operace s platbami 76

4.1.1 Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR) 76

4.1.2 Zaplať poplatek na POS (UC.BAR.0.3.HR) 82

4.1.3 Uhraď přestupek (UC.BAR.0.20.HR) 87

4.1.4 Zaplať Produktový balíček (UC.BAR.0.21.HR) 94

4.1.5 Zaplať OBU (UC.BAR.0.22.HR) 99

4.2 Operace s fakturami 103

4.2.1 Vytvoř proforma fakturu (UC.BAR.3.3.HR) 103

5 Systémové funkce 107

5.1 Fakturace 109

5.1.1 Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.HR) 109

5.1.2 Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR) 118

5.1.3 Vytvoř fakturační dávku (SYS.BAR.0.6.HR) 125

5.1.4 Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR) 127

5.1.5 Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) 132

5.1.6 Vytvoř výzvu na úhradu za přestupek (SYS.BAR.0.13.HR) 137

5.1.7 Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR) 140

5.2 Zpracování mýtných transakcí 147

5.2.1 Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR) 147

5.2.2 Vytvoř billing details (SYS.BAR.1.9.HR) 157

5.2.3 Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR) 160

5.3 Operace s platbami 167

5.3.1 Zúčtuj závazky a pohledávky (SYS.BAR.2.3.HR) 167

5.3.2 Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR) 172

5.3.3 Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR) 177

5.3.4 Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR) 180

5.3.5 Ověř token (SYS.BAR.2.18.HR) 184

5.3.6 Zúčtuj závazky a pohledávky Business Partnera (SYS.BAR.2.19.HR) 185

5.3.7 Tokenizuj kartu přes EFT (SYS.BAR.2.20.HR) 187

6 Systémové funkce: Web Portal API 192

6.1 Operace s platební kartou 192

6.1.1 Zprocesuj transakci platební kartou (API.BAR.0.1.HR) 192

6.2 Operace s fakturou 198

6.2.1 Vygeneruj proforma fakturu (API.BAR.1.1.HR) 198

7 Neprocesní funkcionality 200

7.1 Fakturace 200

7.1.1 Číslování faktur 200

7.1.2 Číslování plateb 201

7.1.3 Zaokrouhlování 202

7.1.4 Variabilní symbol 202

[7.1.5]{.mark} [Atributy dokumentu pro dobropis a vrubopis]{.mark} 203

7.2 BIBA - pravidla pro určení BIBA 203

7.3 Vliv plateb na BM Balance 204

8 Příloha A -- Integrační body 205

8.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) 205

8.2 Rozhraní Platební brána CorvusPay (INT.BAR.27.HR) 205

8.2.1 Tokenizace platební karty 205

8.2.2 Validace tokenu 208

8.2.3 Online platba tokenem platební karty -- synchronní 210

8.2.4 Online platba tokenem platební karty -- asynchronní 211

8.2.5 Online platba platební kartou 213

8.3 Rozhraní EFT Terminal NexGo (INT.BAR.28.HR) 215

8.4 Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR) 215

8.4.1 Authorization Request (Systém → EFT) 217

8.4.2 Authorization Request Confirmation (EFT → Systém) 217

8.4.3 Authorization Response (EFT → Systém) 217

[8.5]{.mark} [Rozhraní ERP Navision (INT.BAR.30.HR)]{.mark} 219

8.6 Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR) 219

8.6.1 Registrace business premisses 220

8.6.2 Fiskalizace faktury 220

8.7 Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR) 221

[8.8]{.mark} [Rozhraní Web portal API (INT.BAR.33.HR)]{.mark} 221

[8.9]{.mark} [Rozhraní POS API (INT.BAR.34.HR)]{.mark} 221

[8.10]{.mark} [Rozhraní KIOSK API (INT.BAR.35.HR)]{.mark} 221

[8.11]{.mark} [Rozhraní IEFBO API (INT.BAR.36.HR)]{.mark} 221

8.12 Rozhraní EUCARIS (INT.TDP.06) 222

8.12.1 Rozhraní 222

9 Příloha B -- Vstupní a výstupní artefakty¨ 224

9.1 Dokumenty 224

9.1.1 Společná nastavení 224

[9.1.2]{.mark} Zálohová faktura za top-up (DOC.BE.01.HR) [a (DOC.BE.01B.HR)]{.mark} 228

9.1.3 Zálohová faktura za předplacení kreditu - dobropis (DOC.BE.06) 228

[9.1.4]{.mark} Faktura za mýtné (DOC.BE.10.HR) [a (DOC.BE.10B.HR)]{.mark} 228

[9.1.5]{.mark} [Detailní výpis mýtných transakcí k faktuře (DOC.BE.11)]{.mark} 230

9.1.6 Vrubopis za mýtné (DOC.BE.13.HR) 233

9.1.7 Dobropis za mýtné (DOC.BE.14.HR) 233

9.1.8 Faktura za služby (DOC.BE.16.HR) 234

9.1.9 Dobropis za služby (DOC.BE.17.HR) 234

[9.1.10]{.mark} [Faktura za smluvní pokutu (DOC.BE.19.HR)]{.mark} 234

[9.1.11]{.mark} [Dobropis za smluvní pokutu (DOC.BE.20.HR)]{.mark} 234

9.1.12 eFaktura (DOC.BE.21.HR) 234

9.1.13 Výzva k úhradě za přestupky (DOC.BE.22.HR) 235

9.1.14 Výzva k úhradě za přestupky -- Dobropis (DOC.BE.23.HR) 235

9.1.15 Proforma faktura (DOC.BE.24.HR) 235

9.2 Externí oznámení (e-mail) 235

9.2.1 Společná nastavení -- e-mail 236

9.2.2 Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR) 238

9.2.3 Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction notification) (NTF.BAR.13.HR) 239

9.2.4 Oznámení o vystavení faktury (NTF.BAR.21.HR) 240

9.2.5 Oznámení o vystavení účetního dokladu (NTF.DF.01.HR) 241

[9.3]{.mark} [Externí oznámení (SMS)]{.mark} 241

[9.3.1]{.mark} [Společná nastavení -- SMS]{.mark} 241

9.3.2 Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction SMS notification) (NTF.BAR.14.HR) 242

9.4 Výměnné soubory 243

9.4.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) 243

10 Příloha C -- Konfigurovatelnost modulu 247

10.1 Naplánované operace 247

[10.2]{.mark} [Konfigurační klíče]{.mark} 249

10.3 Číselníky a systémová nastavení 250

10.3.1 Payment Type (Typ platby) 250

[10.3.2]{.mark} [Rounding (Zaokrouhlování)]{.mark} 251

10.3.3 CorvusPay Payment Method (CorvusPay platební metoda) 252

[10.3.4]{.mark} [CorvusPay Response Code (CorvusPay kód odpovědi)]{.mark} 252