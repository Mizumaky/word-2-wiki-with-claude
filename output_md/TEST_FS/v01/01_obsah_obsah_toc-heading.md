# Obsah {#obsah .TOC-Heading}

[Obsah [4](#obsah)](#obsah)

[Historie dokumentu [9](#_Toc205285640)](#_Toc205285640)

[1 Úvod [13](#úvod)](#úvod)

[1.1 Procesy HR [13](#_Toc205285642)](#_Toc205285642)

[1.1.1 Předplacení kreditu [13](#_Toc205285643)](#_Toc205285643)

[1.1.2 Uložení mýtných transakcí [15](#_Toc205285644)](#_Toc205285644)

[1.1.3 Vystavení pravidelné faktury za mýtné [16](#_Toc205285645)](#_Toc205285645)

[1.1.4 Vystavení jednorázové faktury [17](#_Toc205285646)](#_Toc205285646)

[[1.1.5]{.mark} [Vystavení pravidelné výzvy na úhradu za platby tankovací kartou]{.mark} [18](#_Toc205285647)](#_Toc205285647)

[1.1.6 Re-rating [18](#_Toc205285648)](#_Toc205285648)

[2 Doménový model [19](#doménový-model)](#doménový-model)

[2.1 Diagram doménového modelu [19](#diagram-doménového-modelu)](#diagram-doménového-modelu)

[2.2 Přehled entit [21](#_Toc205285651)](#_Toc205285651)

[2.3 Atributy entit [23](#atributy-entit)](#atributy-entit)

[2.3.1 Bill (Faktura) [23](#test-entity)](#test-entity)

[2.3.2 Bill Item (Položka faktury) [29](#bill-item-položka-faktury)](#bill-item-položka-faktury)

[2.3.3 Bill Session (Fakturační dávka) [33](#bill-session-fakturační-dávka)](#bill-session-fakturační-dávka)

[2.3.4 Payment (Platba) [35](#payment-platba)](#payment-platba)

[2.3.5 Payment Session (Platební transakce) [41](#payment-session-platební-transakce)](#payment-session-platební-transakce)

[2.3.1 Payment Session Item (Položka platební transakce) [45](#_Toc205285658)](#_Toc205285658)

[2.3.2 Matching (Párování plateb) [46](#matching-párování-plateb)](#matching-párování-plateb)

[2.3.3 Toll Transaction Base (Mýtná transakce - základ) [47](#_Toc205285660)](#_Toc205285660)

[2.3.4 Rated Toll Event (Oceněná mýtná událost) [54](#_Toc205285661)](#_Toc205285661)

[2.3.5 Rated Service Event (Oceněná služba) [56](#_Toc205285662)](#_Toc205285662)

[2.3.6 Bill Session Statistics (Statistika fakturační dávky) [59](#_Toc205285663)](#_Toc205285663)

[2.3.7 Bill Session Steps Statistics (Statistika kroků fakturační dávky) [61](#_Toc205285664)](#_Toc205285664)

[2.3.8 Bill Item Statistics (Statistika fakturační dávky podle Bill item typu a Měny) [62](#_Toc205285665)](#_Toc205285665)

[[2.3.9]{.mark} [Settlement Record (Záznam vyrovnání)]{.mark} [62](#_Toc205285666)](#_Toc205285666)

[2.3.10 Card Payment Request (Požadavek na platbu kartou) [63](#_Toc205285667)](#_Toc205285667)

[[2.3.11]{.mark} [ERP Log (ERP Log)]{.mark} [63](#_Toc205285668)](#_Toc205285668)

[[2.3.12]{.mark} [ERP Import (ERP Import)]{.mark} [63](#_Toc205285669)](#_Toc205285669)

[[2.3.13]{.mark} [ERP Export (ERP Export)]{.mark} [64](#_Toc205285670)](#_Toc205285670)

[2.4 Atributy konfigurovatelných číselníků [65](#_Toc205285671)](#_Toc205285671)

[2.4.1 Payment Type (Typ platby) [65](#_Toc205285672)](#_Toc205285672)

[2.4.2 Currency (Měna) [65](#_Toc205285673)](#_Toc205285673)

[2.4.3 Rounding (Zaokrouhlování) [67](#_Toc205285674)](#_Toc205285674)

[2.4.4 CorvusPay Payment Method (CorvusPay platební metoda) [67](#_Toc205285675)](#_Toc205285675)

[[2.4.5]{.mark} [Card type (Typ karty)]{.mark} [68](#_Toc205285676)](#_Toc205285676)

[2.4.6 CorvusPay Response Code (CorvusPay kód odpovědi) [68](#_Toc205285677)](#_Toc205285677)

[2.4.7 Process Step Scheduling (Plánování kroků zpracování) [69](#_Toc205285678)](#_Toc205285678)

[2.5 Vysvětlení ke specifikaci entit a atributů entit [70](#_Toc205285679)](#_Toc205285679)

[3 Aktéři [73](#_Toc205285680)](#_Toc205285680)

[3.1 Seznam aktérů [73](#_Toc205285681)](#_Toc205285681)

[[3.2]{.mark} [Seznam rolí]{.mark} [73](#_Toc205285682)](#_Toc205285682)

[3.3 Pracovní týmy [73](#_Toc205285683)](#_Toc205285683)

[4 Případy užití [75](#případy-užití)](#případy-užití)

[4.1 Operace s platbami [76](#_Toc205285685)](#_Toc205285685)

[4.1.1 Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR) [76](#zaplať-předplacený-kredit-pre-paid-in-single-domain-uc.bar.0.1.hr)](#zaplať-předplacený-kredit-pre-paid-in-single-domain-uc.bar.0.1.hr)

[4.1.2 Zaplať poplatek na POS (UC.BAR.0.3.HR) [82](#zaplať-poplatek-na-pos-uc.bar.0.3.hr)](#zaplať-poplatek-na-pos-uc.bar.0.3.hr)

[4.1.3 Uhraď přestupek (UC.BAR.0.20.HR) [87](#uhraď-přestupek-uc.bar.0.20.hr)](#uhraď-přestupek-uc.bar.0.20.hr)

[4.1.4 Zaplať Produktový balíček (UC.BAR.0.21.HR) [94](#zaplať-produktový-balíček-uc.bar.0.21.hr)](#zaplať-produktový-balíček-uc.bar.0.21.hr)

[4.1.5 Zaplať OBU (UC.BAR.0.22.HR) [99](#zaplať-obu-uc.bar.0.22.hr)](#zaplať-obu-uc.bar.0.22.hr)

[4.2 Operace s fakturami [103](#operace-s-fakturami)](#operace-s-fakturami)

[4.2.1 Vytvoř proforma fakturu (UC.BAR.3.3.HR) [103](#vytvoř-proforma-fakturu-uc.bar.3.3.hr)](#vytvoř-proforma-fakturu-uc.bar.3.3.hr)

[5 Systémové funkce [107](#systémové-funkce)](#systémové-funkce)

[5.1 Fakturace [109](#fakturace)](#fakturace)

[5.1.1 Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.HR) [109](#vytvoř-pravidelné-faktury-za-mýtné-sys.bar.0.1.hr)](#vytvoř-pravidelné-faktury-za-mýtné-sys.bar.0.1.hr)

[5.1.2 Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR) [118](#vytvoř-jednorázovou-fakturu-za-služby-sys.bar.0.4.hr)](#vytvoř-jednorázovou-fakturu-za-služby-sys.bar.0.4.hr)

[5.1.3 Vytvoř fakturační dávku (SYS.BAR.0.6.HR) [125](#vytvoř-fakturační-dávku-sys.bar.0.6.hr)](#vytvoř-fakturační-dávku-sys.bar.0.6.hr)

[5.1.4 Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR) [127](#naúčtuj-jednorázový-poplatek-sys.bar.0.7.hr)](#naúčtuj-jednorázový-poplatek-sys.bar.0.7.hr)

[5.1.5 Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) [132](#zagreguj-oceněné-události-do-fakturační-dávky-sys.bar.0.12.hr)](#zagreguj-oceněné-události-do-fakturační-dávky-sys.bar.0.12.hr)

[5.1.6 Vytvoř výzvu na úhradu za přestupek (SYS.BAR.0.13.HR) [137](#vytvoř-výzvu-na-úhradu-za-přestupek-sys.bar.0.13.hr)](#vytvoř-výzvu-na-úhradu-za-přestupek-sys.bar.0.13.hr)

[5.1.7 Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR) [140](#vytvoř-jednorázovou-fakturu-za-mýto-sys.bar.0.14.hr)](#vytvoř-jednorázovou-fakturu-za-mýto-sys.bar.0.14.hr)

[5.2 Zpracování mýtných transakcí [147](#_Toc205285702)](#_Toc205285702)

[5.2.1 Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR) [147](#_Toc205285703)](#_Toc205285703)

[5.2.2 Vytvoř billing details (SYS.BAR.1.9.HR) [157](#_Toc205285704)](#_Toc205285704)

[5.2.3 Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR) [160](#_Toc205285705)](#_Toc205285705)

[5.3 Operace s platbami [167](#_Toc205285706)](#_Toc205285706)

[5.3.1 Zúčtuj závazky a pohledávky (SYS.BAR.2.3.HR) [167](#_Toc205285707)](#_Toc205285707)

[5.3.2 Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR) [172](#_Toc205285709)](#_Toc205285709)

[5.3.3 Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR) [177](#_Toc205285710)](#_Toc205285710)

[5.3.4 Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR) [180](#_Toc205285711)](#_Toc205285711)

[5.3.5 Ověř token (SYS.BAR.2.18.HR) [184](#_Toc205285712)](#_Toc205285712)

[5.3.6 Zúčtuj závazky a pohledávky Business Partnera (SYS.BAR.2.19.HR) [185](#_Toc205285713)](#_Toc205285713)

[5.3.7 Tokenizuj kartu přes EFT (SYS.BAR.2.20.HR) [187](#_Toc205285714)](#_Toc205285714)

[6 Systémové funkce: Web Portal API [192](#_Toc205285715)](#_Toc205285715)

[6.1 Operace s platební kartou [192](#_Toc205285716)](#_Toc205285716)

[6.1.1 Zprocesuj transakci platební kartou (API.BAR.0.1.HR) [192](#_Toc205285717)](#_Toc205285717)

[6.2 Operace s fakturou [198](#_Toc205285718)](#_Toc205285718)

[6.2.1 Vygeneruj proforma fakturu (API.BAR.1.1.HR) [198](#_Toc205285719)](#_Toc205285719)

[7 Neprocesní funkcionality [200](#_Toc205285720)](#_Toc205285720)

[7.1 Fakturace [200](#_Toc205285721)](#_Toc205285721)

[7.1.1 Číslování faktur [200](#_Toc205285722)](#_Toc205285722)

[7.1.2 Číslování plateb [201](#_Toc205285723)](#_Toc205285723)

[7.1.3 Zaokrouhlování [202](#_Toc205285724)](#_Toc205285724)

[7.1.4 Variabilní symbol [202](#_Toc205285725)](#_Toc205285725)

[[7.1.5]{.mark} [Atributy dokumentu pro dobropis a vrubopis]{.mark} [203](#_Toc205285726)](#_Toc205285726)

[7.2 BIBA - pravidla pro určení BIBA [203](#_Toc205285727)](#_Toc205285727)

[7.3 Vliv plateb na BM Balance [204](#_Toc205285728)](#_Toc205285728)

[8 Příloha A -- Integrační body [205](#_Toc205285729)](#_Toc205285729)

[8.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) [205](#_Toc205285730)](#_Toc205285730)

[8.2 Rozhraní Platební brána CorvusPay (INT.BAR.27.HR) [205](#_Toc205285731)](#_Toc205285731)

[8.2.1 Tokenizace platební karty [205](#_Toc205285732)](#_Toc205285732)

[8.2.2 Validace tokenu [208](#_Toc205285733)](#_Toc205285733)

[8.2.3 Online platba tokenem platební karty -- synchronní [210](#_Toc205285734)](#_Toc205285734)

[8.2.4 Online platba tokenem platební karty -- asynchronní [211](#_Toc205285735)](#_Toc205285735)

[8.2.5 Online platba platební kartou [213](#_Toc205285736)](#_Toc205285736)

[8.3 Rozhraní EFT Terminal NexGo (INT.BAR.28.HR) [215](#_Toc205285737)](#_Toc205285737)

[8.4 Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR) [215](#_Toc205285738)](#_Toc205285738)

[8.4.1 Authorization Request (Systém → EFT) [217](#_Toc205285739)](#_Toc205285739)

[8.4.2 Authorization Request Confirmation (EFT → Systém) [217](#_Toc205285740)](#_Toc205285740)

[8.4.3 Authorization Response (EFT → Systém) [217](#_Toc205285741)](#_Toc205285741)

[[8.5]{.mark} [Rozhraní ERP Navision (INT.BAR.30.HR)]{.mark} [219](#_Toc205285742)](#_Toc205285742)

[8.6 Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR) [219](#_Toc205285743)](#_Toc205285743)

[8.6.1 Registrace business premisses [220](#_Toc205285744)](#_Toc205285744)

[8.6.2 Fiskalizace faktury [220](#_Toc205285745)](#_Toc205285745)

[8.7 Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR) [221](#_Toc205285746)](#_Toc205285746)

[[8.8]{.mark} [Rozhraní Web portal API (INT.BAR.33.HR)]{.mark} [221](#_Toc205285747)](#_Toc205285747)

[[8.9]{.mark} [Rozhraní POS API (INT.BAR.34.HR)]{.mark} [221](#_Toc205285748)](#_Toc205285748)

[[8.10]{.mark} [Rozhraní KIOSK API (INT.BAR.35.HR)]{.mark} [221](#_Toc205285749)](#_Toc205285749)

[[8.11]{.mark} [Rozhraní IEFBO API (INT.BAR.36.HR)]{.mark} [221](#_Toc205285750)](#_Toc205285750)

[8.12 Rozhraní EUCARIS (INT.TDP.06) [222](#_Toc205285751)](#_Toc205285751)

[8.12.1 Rozhraní [222](#_Toc205285752)](#_Toc205285752)

[9 Příloha B -- Vstupní a výstupní artefakty¨ [224](#_Toc205285753)](#_Toc205285753)

[9.1 Dokumenty [224](#_Toc205285754)](#_Toc205285754)

[9.1.1 Společná nastavení [224](#_Toc205285755)](#_Toc205285755)

[[9.1.2]{.mark} Zálohová faktura za top-up (DOC.BE.01.HR) [a (DOC.BE.01B.HR)]{.mark} [228](#_Toc205285756)](#_Toc205285756)

[9.1.3 Zálohová faktura za předplacení kreditu - dobropis (DOC.BE.06) [228](#_Toc205285757)](#_Toc205285757)

[[9.1.4]{.mark} Faktura za mýtné (DOC.BE.10.HR) [a (DOC.BE.10B.HR)]{.mark} [228](#_Toc205285758)](#_Toc205285758)

[[9.1.5]{.mark} [Detailní výpis mýtných transakcí k faktuře (DOC.BE.11)]{.mark} [230](#_Toc205285759)](#_Toc205285759)

[9.1.6 Vrubopis za mýtné (DOC.BE.13.HR) [233](#_Toc205285760)](#_Toc205285760)

[9.1.7 Dobropis za mýtné (DOC.BE.14.HR) [233](#_Toc205285761)](#_Toc205285761)

[9.1.8 Faktura za služby (DOC.BE.16.HR) [234](#_Toc205285762)](#_Toc205285762)

[9.1.9 Dobropis za služby (DOC.BE.17.HR) [234](#_Toc205285763)](#_Toc205285763)

[[9.1.10]{.mark} [Faktura za smluvní pokutu (DOC.BE.19.HR)]{.mark} [234](#_Toc205285764)](#_Toc205285764)

[[9.1.11]{.mark} [Dobropis za smluvní pokutu (DOC.BE.20.HR)]{.mark} [234](#_Toc205285765)](#_Toc205285765)

[9.1.12 eFaktura (DOC.BE.21.HR) [234](#_Toc205285766)](#_Toc205285766)

[9.1.13 Výzva k úhradě za přestupky (DOC.BE.22.HR) [235](#_Toc205285767)](#_Toc205285767)

[9.1.14 Výzva k úhradě za přestupky -- Dobropis (DOC.BE.23.HR) [235](#_Toc205285768)](#_Toc205285768)

[9.1.15 Proforma faktura (DOC.BE.24.HR) [235](#_Toc205285769)](#_Toc205285769)

[9.2 Externí oznámení (e-mail) [235](#_Toc205285770)](#_Toc205285770)

[9.2.1 Společná nastavení -- e-mail [236](#_Toc205285771)](#_Toc205285771)

[9.2.2 Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR) [238](#_Toc205285772)](#_Toc205285772)

[9.2.3 Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction notification) (NTF.BAR.13.HR) [239](#_Toc205285773)](#_Toc205285773)

[9.2.4 Oznámení o vystavení faktury (NTF.BAR.21.HR) [240](#_Toc205285774)](#_Toc205285774)

[9.2.5 Oznámení o vystavení účetního dokladu (NTF.DF.01.HR) [241](#_Toc205285775)](#_Toc205285775)

[[9.3]{.mark} [Externí oznámení (SMS)]{.mark} [241](#_Toc205285776)](#_Toc205285776)

[[9.3.1]{.mark} [Společná nastavení -- SMS]{.mark} [241](#_Toc205285777)](#_Toc205285777)

[9.3.2 Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction SMS notification) (NTF.BAR.14.HR) [242](#_Toc205285778)](#_Toc205285778)

[9.4 Výměnné soubory [243](#_Toc205285779)](#_Toc205285779)

[9.4.1 Rozhraní TC HR -- HAC (INT.BAR.26.HR) [243](#_Toc205285780)](#_Toc205285780)

[10 Příloha C -- Konfigurovatelnost modulu [247](#_Toc205285781)](#_Toc205285781)

[10.1 Naplánované operace [247](#_Toc205285782)](#_Toc205285782)

[[10.2]{.mark} [Konfigurační klíče]{.mark} [249](#_Toc205285783)](#_Toc205285783)

[10.3 Číselníky a systémová nastavení [250](#_Toc205285784)](#_Toc205285784)

[10.3.1 Payment Type (Typ platby) [250](#_Toc205285785)](#_Toc205285785)

[[10.3.2]{.mark} [Rounding (Zaokrouhlování)]{.mark} [251](#_Toc205285786)](#_Toc205285786)

[10.3.3 CorvusPay Payment Method (CorvusPay platební metoda) [252](#_Toc205285787)](#_Toc205285787)

[[10.3.4]{.mark} [CorvusPay Response Code (CorvusPay kód odpovědi)]{.mark} [252](#_Toc205285788)](#_Toc205285788)