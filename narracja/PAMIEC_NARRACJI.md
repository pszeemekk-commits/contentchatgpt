# Pamięć narracji — zbieranie, łączenie i stopniowe ujawnianie

Obowiązuje od 2026-09-03. Uzupełnia SYSTEM_ECS.md. Realizuje korektę Przemka zapisaną w Ź30. Baza przechowuje więcej wiedzy niż pojedyncza publikacja ujawnia odbiorcy.

## 1. Który plik odpowiada za co

| Warstwa | Miejsce | Rola |
|---|---|---|
| Wypowiedź źródłowa | Istniejący braindump albo nowy plik w narracja/zrodla/ | Dosłowna wypowiedź, data zapisu, kontekst; bez wygładzania. Jeden plik na spójny zestaw dopowiedzeń. |
| Indeks źródeł | narracja/ZRODLA_I_USTALENIA_SYSTEMU_WIEZI.md | Stabilny identyfikator Ź i lokalizacja. Starsze źródła zachowują swoje miejsca. |
| Doświadczenie | narracja/STORY_BANK.md | Stabilne S-ID, fakty, czas, znaczenie i jego status, powiązania. Także decyzja, obserwacja lub zwykły moment bez pełnej fabuły. |
| Połączenie wielu doświadczeń | narracja/NARRATIVE_MAP.md | WATEK-ID: co je łączy, na jakiej podstawie, co każde wnosi innego. Mapa nie kopiuje pełnych historii. |
| Dzisiejszy stan | narracja/TERAZ.md | Co nadal trwa lub jest aktualnym zainteresowaniem; data potwierdzenia i źródło. |
| Niewiadoma | narracja/OPEN_LOOPS.md | O-ID, rzeczywiste pytanie, co wiadomo i czego jeszcze nie; bez obowiązku robienia serialu. |
| Co odbiorca mógł zobaczyć | narracja/CONTENT_USAGE.md | Wybrany zakres, szkic, akceptacja, publikacja, możliwy powrót i rzeczywiste reakcje. |

PERSONAL_MAP, BELIEF_SYSTEM i bank aktywów są syntezami. Aktualizuj je dopiero, gdy nowy materiał rzeczywiście zmienia dane rozpoznanie; nie dopisuj tej samej historii do wszystkich plików. Nowe wątki nie wymagają nowego banku. Gdy źródeł przybywa, wyszukuj po ID, temacie i powiązaniach, potem czytaj właściwy fragment w kontekście.

## 2. Przyjęcie nowego materiału

1. Rozpoznaj intencję: zapis/dopowiedzenie, poprawka faktu, rozwinięcie bieżącego tekstu albo zlecenie nowego tekstu. Nowa historia podana w rozmowie sama nie oznacza polecenia wstawienia jej do ostatniego posta.
2. W ramach zleconego zbierania materiału zachowaj surową wypowiedź. Jeśli już ma plik źródłowy, odwołaj się do niego. Cytowane zdania AI oddziel od słów autora; akceptacja draftu nie zmienia go w źródło biograficzne.
3. Wyszukaj istniejące zdarzenie i wątek. Dopowiedzenie do tej samej historii aktualizuje jej S-ID z nową datą i źródłem. Odrębne doświadczenie otrzymuje kolejne wolne S-ID. Nie mnoż świadectw z kopii tej samej wypowiedzi.
4. Oddziel datę zdarzenia, datę opowiedzenia, datę obecnej interpretacji i datę publikacji. Nieznana data pozostaje nieznana; można zachować ustaloną kolejność i czas trwania.
5. Rozdziel fakty, potwierdzone osobiste znaczenie, hipotezę autora i interpretację AI. Samo „chyba” jest potwierdzonym sposobem myślenia autora, a jego treść pozostaje hipotezą. Nie wygładzaj rozbieżności; zachowaj, co powiedział kiedyś i co dopowiedział teraz.
6. Dopisz potrzebne połączenia w NARRATIVE_MAP; aktywny stan w TERAZ i niewiadomą w OPEN_LOOPS tylko wtedy, gdy źródło je potwierdza. Nauka zakończona lata temu może mieć dzisiejszą otwartą interpretację.
7. Oddaj krótko: co zapisano, z czym połączono, co pozostaje niepewne, czy zlecono zmianę publikacji. Nie uruchamiaj wywiadu o szczegóły niepotrzebne do tego zapisu.

Przy kolejnej wiadomości o tym samym procesie dodaj aktualizację z datą; zachowaj wcześniejsze etapy. Przy zakończeniu oznacz stan i rzeczywisty wynik. Refleksja z dzisiaj nad dawnym zdarzeniem nie jest nowym zdarzeniem ani dowodem, że proces znów trwa. Przegląd odbywa się przy następnym wsadzie lub planowaniu treści; ten dokument nie tworzy zadania cyklicznego ani samodzielnego monitorowania życia autora.

## 3. Jak łączyć materiał

Połączenie zawiera: ID obu elementów, nazwany związek, źródło lub uzasadnienie, status i znaczenie dla przyszłego materiału. Dostępne relacje to wspólna motywacja, podobne kryterium wyboru, konsekwencja, zmiana stanowiska, sprzeczność, reinterpretacja, ta sama osoba lub miejsce. Wspólny tag nie wystarcza: „muzyka” łączy tematy, lecz „wpływ przez budowanie emocji” wskazuje znaczenie, którego status trzeba sprawdzić.

Karta wątku ma: krótkie pytanie lub motyw, powiązane S/Ź/O, różnicę między doświadczeniami, potwierdzenie/hipotezę połączenia, obecny stan oraz ścieżkę do CONTENT_USAGE. Nie musi mieć zamówionego finału. Nowa wypowiedź może potwierdzić lub podważyć dotychczasowe wyjaśnienie.

S-023 łączy się z S-005 i wątkiem pracy z ludźmi przez hipotezę Przemka o budowaniu emocji. Nie wynika z tego, że muzyka interesuje go wyłącznie zawodowo, że każda jego pasja ma ten sam powód ani że zakup tagelharpy już nastąpił.

## 4. Stopniowanie informacji w komunikacji

Przed pisaniem określ w polu CIĄGŁOŚĆ wspólnego briefu:

- **TERAZ:** co ten materiał ujawnia i jaką samodzielną myśl domyka.
- **ZNANE PUBLICZNIE:** konkretne publikacje z CONTENT_USAGE; gdy brak danych, nie zakładaj wiedzy odbiorców.
- **PÓŹNIEJ:** odrębne doświadczenie, perspektywa lub etap, który może pogłębić poznanie autora; powód oddzielenia. To pula możliwości, nie obowiązek zapowiedzi.
- **POWRÓT:** jakie nowe znaczenie wniesie callback i jaki fakt lub decyzja redakcyjna uzasadni powrót.

Wprowadź tylko tyle kontekstu, ile wymaga bieżąca myśl. Można połączyć kilka doświadczeń, jeśli razem są konieczne do jej zrozumienia. Nie dziel kompletnej historii wyłącznie dla liczby postów; nie odkładaj obiecanego wyjaśnienia. W zwykłym późniejszym poście można wrócić do zamkniętej historii z inną perspektywą, bez nowego wydarzenia i bez udawania, że zdarzyło się teraz.

Nowy czytelnik ma zrozumieć pełny materiał. Stały może połączyć go z wcześniejszymi etapami; nie musi pamiętać wszystkiego. Stan bazy, decyzja redakcyjna i wiedza odbiorcy są trzema różnymi rzeczami.

## 5. Praca od wsadu do publikacji

Ten sposób działa obok wyboru tematu z komunikatu marki. W obu przypadkach powstaje ten sam brief w glos-marki.

1. Przyjmij dosłowny wsad: myśl, pytanie odbiorcy, obserwację, case, scenę, teorię albo draft. Najpierw określ jego właściwy sens. Zachowaj to, co autor chce powiedzieć, i źródłowe napięcie lub niepewność.
2. Dopiero do tego sensu dobierz pasującą filozofię i jeden główny aktualny komunikat z sekcji 4 BRAND. Obowiązkowo zapisz w briefie numer, pełną nadrzędną myśl, konkretny rozwijany aspekt oraz uzasadnienie dopasowania; numer filaru tego nie zastępuje. Osobowość ujawnij przez rzeczywiste kryterium, reakcję, rozumowanie lub ton. Doświadczenie znajdź we wsadzie albo w pamięci. Wszystkie trzy składniki mogą już być obecne; nie dodawaj trzech obowiązkowych akapitów.
3. Dobieraj doświadczenie po znaczeniu. Krótka obserwacja z praktyki może wystarczyć; pełna dodatkowa historia wymaga uzasadnienia. Jeśli łączy się tylko tematycznie, pozostaje materiałem na później. Nie zastępuj doświadczenia frazą „z mojej praktyki” bez źródła.
4. Wybierz filar/funkcję, wartość dla odbiorcy i wkład w poznanie autora. Sprawdź TERAZ/ZNANE PUBLICZNIE/PÓŹNIEJ/POWRÓT. Następnie dobierz format i napisz, jeśli zostało to zlecone.
5. Jeśli brakujące źródło uniemożliwia zachowanie mixu lub sensu, nazwij jedną konkretną lukę po sprawdzeniu bazy. Nie zmieniaj wsadu w inną opowieść i nie wymyślaj motywacji. Gdy brak dotyczy tylko zbędnego dodatku, pomiń dodatek.

Przed tekstem wystarczy krótka informacja: sens wsadu, dopasowanie składników, co ujawniamy teraz i co zostaje do późniejszego użycia. Nie wymuszaj kolejnego zatwierdzania, jeśli autor zlecił wykonanie całości. Jeśli zapowiedział, że dopiero dostarczy wsad, zakończ zapis i przygotowanie systemu; nie wybieraj za niego materiału do następnego testu.
