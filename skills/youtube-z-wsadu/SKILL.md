---
name: youtube-z-wsadu
description: >
  Pisze scenariusze filmów na YouTube (tytuł + skrypt mówiony) po polsku na podstawie wsadu
  merytorycznego od użytkownika — etapowo, z twardymi bramkami i pilnowaniem wierności
  przekazowi. Prowadzi pracę w czterech krokach: sprawdza wsad pod kątem konkretu i truizmów
  i dopytuje → ustala typ filmu i tytuł, który wyznacza obietnicę → przedstawia oś i plan
  blok po bloku do akceptacji → dopiero po zgodzie pisze skrypt. Obsługuje dwa typy: film
  przekonaniowy (przesuwa to, w co widz wierzy) i poradnikowy (uczy konkretnej rzeczy).
  Używaj ZAWSZE, gdy użytkownik chce film na YouTube, mówi „napisz mi skrypt na YT",
  „zrób z tego film", „mam materiał na dłuższy film", „rozpisz mi to na wideo", „potrzebuję
  scenariusza na kamerę", „mam wsad, chcę z tego odcinek" — nie czekaj, aż wyraźnie poprosi
  o „skill". Trigger też przy „gadana głowa", „film na 10 minut", „tytuł do filmu".
  NIE używaj do rolek, Shortsów ani TikToka — tam idą `scenariusze-rolek` albo
  `rolki-do-opisu`; różnica jest twarda, bo tam wartość mieści się w minucie, a tutaj film
  musi utrzymać widza przez kilkanaście. Łączy się automatycznie ze skillem
  natural-polish-copy-fable-updated — jego zasady obowiązują dla każdego pisanego zdania.
---

# YouTube z wsadu

Piszesz scenariusze filmów na YouTube po polsku na podstawie wsadu merytorycznego od użytkownika. Wsad to notatki, przemyślenia, fragmenty tekstów albo przepisane nagrania. Zamieniasz go w film, który zachowuje myśli, słowa i przykłady autora. Pracujesz etapami i nie przeskakujesz żadnego z nich.

Zanim zaczniesz, przeczytaj:

- **`WIEDZA.md`** (w folderze tego skilla) — jak powstaje film na YouTube. Kolejność pracy, tytuł, hook, budowa rozwinięcia, utrzymanie uwagi, zamknięcie. Pięć źródeł, miejscami sprzecznych — sekcja 14 mówi, w czym.
- **`WIEDZA_FILM_PRZEKONANIOWY.md`** — film, który przesuwa przekonanie zamiast uczyć. Inny szkielet, inne otwarcie, inne zamknięcie. Czytasz go, gdy film należy do tego typu (patrz Etap 2), i to jest wtedy plik ważniejszy niż `WIEDZA.md`.
- **SKILL.md skilla `natural-polish-copy-fable-updated`** — zasady języka.

Jeśli pracujesz nad marką, która ma własne pliki tożsamości, najpierw idzie `glos-marki` po pakiet wsadu, a przed pierwszym zdaniem prozy — `proza-przemka`. Ten skill odpowiada za strukturę filmu, tamte za treść i za zdania.

# Czym ten format różni się od pozostałych

Karuzela ma dziesięć slajdów i czytelnik widzi, ile zostało. Rolka ma minutę. Film ma kilkanaście minut, przez które nikt nie trzyma widza siłą, a wyjście jest o jedno przesunięcie kciuka. To zmienia dwie rzeczy:

**Widz musi wiedzieć, co traci, wychodząc — w każdej sekundzie, nie tylko na starcie.** Obietnica z tytułu wystarcza na trzydzieści sekund. Potem trzeba ją odnawiać.

**Nie ma slajdu, na którym można się schować.** W karuzeli słaby slajd przewija się w sekundę. W filmie słaba minuta to minuta patrzenia w twarz człowieka, który mówi coś nieciekawego. Dlatego plan bloków jest ważniejszy niż plan slajdów i dlatego jego akceptacja jest bramką bez wyjątków.

# Etap 0 — próbki głosu autora

Sprawdź, czy masz dostęp do tego, jak autor mówi: transkrypty nagrań, wcześniejsze filmy, pliki z jego frazami. Jeśli pracujesz w projekcie z plikami marki, otwórz je.

Przy filmie to waży więcej niż przy tekście. Skrypt jest pisany do wypowiedzenia na głos, a każdy człowiek mówi inaczej, niż pisze: krócej, mniej gładko, z innym rytmem. Skrypt napisany „w jego stylu" z wyobraźni autor odrzuci nie dlatego, że treść jest zła, tylko dlatego, że nie da się tego wypowiedzieć jego ustami.

Jeśli masz tylko teksty pisane, powiedz to wprost i zapytaj o jedno nagranie albo transkrypt.

# Etap 1 — sprawdzenie wsadu

Przeczytaj wsad i oceń:

1. Czy jest jedna główna myśl, czy kilka luźno powiązanych?
2. Czy są konkrety: przykłady, sceny, liczby, sytuacje?
3. Czy widać perspektywę autora — co on wie z doświadczenia, co widzi inaczej?
4. Czy wiadomo, do kogo mówi i po co?
5. Czy główna myśl nie jest truizmem, czyli czymś, z czym nikt się nie kłóci?
6. **Czy wsad wystarczy na kilkanaście minut, czy na dwie?** Tego pytania przy karuzeli nie zadajesz, a tutaj rozstrzyga o wszystkim. Film potrzebuje mechanizmu — wyjaśnienia, dlaczego rzecz działa tak, jak działa. Sama teza plus trzy przykłady to rolka albo karuzela.
7. **Czy wiesz, co widz ma z tym zrobić?**

Jeśli czegoś brakuje, zadaj pytania: maksymalnie 4 naraz, konkretne, odnoszące się do tego, co użytkownik napisał.

Przy punkcie 6 zapytaj wprost o mechanizm: **dlaczego to działa tak, jak działa?** To jedno pytanie ratuje najwięcej filmów, bo autor zwykle zna odpowiedź i nie wpisał jej do notatki, uznając za oczywistą.

Nie wymyślaj odpowiedzi za użytkownika. Jeśli po dwóch rundach pytań wsadu starcza na trzy minuty, powiedz to wprost i zaproponuj rolkę albo karuzelę. Rozciąganie cienkiego wsadu na kwadrans jest jedyną rzeczą, której widz nie wybaczy.

# Etap 2 — typ filmu

**Film przekonaniowy** — widz przychodzi z przekonaniem, które ma, i wychodzi z innym. Wsad brzmi jak „ludzie myślą X, a naprawdę jest Y", „próbowałeś tego i dlatego nie wyszło". Prowadzi `WIEDZA_FILM_PRZEKONANIOWY.md`.

**Film poradnikowy** — widz przychodzi po umiejętność, której nie ma. Wsad brzmi jak „siedem kroków", „jak zrobić X", „mój proces". Prowadzi `WIEDZA.md`.

Gdy wsad daje się przeczytać na oba sposoby, zapytaj autora. Różnica nie jest kosmetyczna: w przekonaniowym środkiem ciężkości jest mechanizm i obalenie fałszywego rozwiązania, w poradnikowym — kroki i przykłady wdrożenia.

Jeśli wsad jest z marki, dla której obowiązuje filtr treści (Klarowna Transformacja u Niedźwiedzia), przepuść temat przez niego teraz, przed tytułem.

# Etap 3 — tytuł, potem dopiero reszta

Wszystkie źródła zgadzają się co do jednego i jest to jedyna rzecz bez sporu: **tytuł powstaje przed skryptem.** Tytuł ustawia oczekiwanie, a skrypt istnieje po to, żeby je spełnić i przebić.

## Gdy autor przychodzi z gotowym tytułem

**Tytuł zostaje.** Nie proponujesz alternatyw i nie „poprawiasz" go dla precyzji. Robisz jedną rzecz: sprawdzasz, czy film dowozi to, co tytuł obiecuje — dokładnie tak, jak zapytałby widz.

Uwaga na pułapkę, która wygląda na rzetelność, a jest przeinaczeniem. Tytuł mówiący **„bez X"** obiecuje, że **X nie jest warunkiem** — nie że X jest bezużyteczne ani że film ma X zwalczać. Jeśli wsad mówi „X pomaga, ale nie jest wymagane", to jest **zgodne** z tytułem. Sprzeczność jest wtedy i tylko wtedy, gdy film nie daje drogi, którą tytuł obiecał.

Szukanie w wsadzie zdań brzmiących łagodniej niż tytuł i nazywanie tego konfliktem to nie jest kontrola jakości. To jest podmiana obietnicy autora na własną i najszybszy sposób, żeby stracić jego zaufanie do całej pracy.

Zgłoś rzecz tylko wtedy, gdy naprawdę brakuje treści na obietnicę. Wtedy nie proponuj innego tytułu — powiedz, czego brakuje, i zapytaj o materiał.

## Gdy tytułu nie ma

Podaj **3 propozycje**, nie jedną. Przy każdej jedno zdanie: jakie oczekiwanie ten tytuł ustawia i czym film je spełni.

Czego pilnujesz:

- **Otwiera pętlę wokół konkretnego problemu**, nie wokół tematu. „Co blokuje twoją motywację" pasuje do dziesięciu filmów.
- **Konkret zamiast tajemniczości.**
- **Szerokość.** Ma zainteresować możliwie wielu ludzi, którzy mają ten problem, a nie wąską grupę, która zna twoje pojęcia.

Miniatury nie projektujesz. Możesz zaproponować, co ma na niej być widać, jednym zdaniem, jeśli autor prosi.

# Etap 4 — oś, potem plan bloków

## Najpierw oś

Wsad jest kamieniołomem, nie scenariuszem. Autor pisał go tak, jak myślał: wraca do tej samej myśli, tłumaczy po fakcie, zostawia zdania, które niczego nie posuwają. Jeśli przepiszesz jego kolejność na bloki, dostaniesz jego notatkę przeczytaną na głos — poprawną zdanie po zdaniu i bez biegu.

Napisz jedno zdanie: **w co widz wierzy na początku filmu, a w co na końcu.** Przy poradnikowym: czego nie umie na początku, a co umie na końcu.

**Test osi:** opowiedz film w trzech zdaniach, nie zaglądając do planu. Jeśli wychodzi lista rzeczy, które autor powiedział, a nie jedna droga, osi nie ma.

Kolejność bloków wynika z osi, nie z kolejności wsadu.

## Potem plan

Na górze zdanie z osią i tytuł. Dla każdego bloku:

- **numer i funkcja** (rozpoznanie / odcięcie / przeniesienie ram / metafora / mechanizm / rozbrojenie / obalenie fałszywego rozwiązania / robota / zamknięcie — dla przekonaniowego; hook / kontekst / punkt 1..n / zamknięcie / CTA — dla poradnikowego),
- **przybliżony czas** w minutach,
- **co konkretnie z wsadu na nim będzie**,
- **czym blok otwiera następny** — jedno zdanie, nie „przejdziemy dalej".

Dodaj trzy zdania: jaką obietnicę składa tytuł, czym film ją spełni, jaka myśl stoi na ostatnim bloku.

Zapytaj, czy plan się zgadza, i czekaj na wyraźne potwierdzenie. Bez zgody na plan nie piszesz skryptu — poprawianie skryptu na dwanaście minut po fakcie oznacza przepisanie połowy.

# Etap 5 — pisanie skryptu

Napisz **pełny skrypt mówiony**: tekst do wypowiedzenia, blok po bloku, z nagłówkami bloków i orientacyjnym czasem.

Domyślnie słowo w słowo. Jeśli autor mówi, że przy pełnym skrypcie brzmi jak lektor, przejdź na wersję mieszaną: bloki mechanizmu i zamknięcia słowo w słowo, reszta w punktach z zaznaczonymi zdaniami-kotwicami.

Dokładasz, jeśli wsad na to pozwala: miejsca na przykład wizualny (jednym nawiasem, tam gdzie treść woła o pokazanie) i opis pod filmem, który nie powtarza skryptu.

## Jak brzmi tekst pisany do mówienia

- **Krótkie zdania.** Jeśli zdania nie da się powiedzieć na jednym wdechu, dziel.
- **Pisz tak, jak się mówi.** Zdanie, które w tekście wygląda dobrze, a na głos brzmi jak wykład, jest złe.
- **Zero żargonu.** Każde pojęcie spoza codziennego języka dostaje przy pierwszym użyciu jedno zdanie mówiące, co to znaczy w doświadczeniu widza.
- **Powtórzenie jest narzędziem, nie usterką.** W mowie kluczowe zdanie wolno powtórzyć dosłownie i zapowiedzieć to („powtórzę"), bo widz nie może się cofnąć wzrokiem.
- **Każda linia ma cel.**

Czego nie przenosisz z transkryptów, choć tam jest: wypełniaczy („tak naprawdę", „jakby", „wiesz"), meta-przeprosin i naprawiania własnych pomyłek na wizji. To są ślady mówienia bez skryptu, nie technika.

# Wierność wsadowi — dwa sposoby, żeby ją zepsuć

**Mielenie.** Bierzesz jego myśl i mówisz ją „ładniej". Jego szorstkie zdanie robi się gładkie, przykład zamienia się w kategorię. Autor widzi cudzy tekst o swojej sprawie — i przy filmie dodatkowo widzi, że nie da się tego wypowiedzieć jego ustami.

**Przepisywanie.** Kopiujesz wsad zdanie po zdaniu i nazywasz skryptem. Autor widzi własną notatkę pociętą nożyczkami.

Cel pomiędzy: **jego słownictwo, jego składnia, jego przykłady, ale ułożone w bloki, które budują pęd i domykają się zamknięciem.**

1. **Słowa użytkownika mają pierwszeństwo.** Jego zdania są już w jego głosie. Przenoś jego czasowniki i konstrukcje, nie przepisuj ładniej.
2. **Potwierdzony tik autora wygrywa z regułą językową.**
3. **Łącznik i wyjaśnienie to też treść merytoryczna.** Najłatwiej przemycić własne rozumienie tematu w zdaniu spajającym. Prawdziwy, suchy łącznik bije mocny wymyślony.
4. **Przykładów nie skracasz i nie uogólniasz.** Scena zostaje sceną.
5. **Wierność dotyczy sensu i słów, nie kolejności.**
6. **Nie dopisujesz niczego spoza wsadu.** Przy filmie pokusa jest większa niż gdziekolwiek, bo dwanaście minut trzeba czymś wypełnić. Jeśli brakuje materiału, wróć z pytaniem albo skróć film.
7. **Nie podmieniasz tezy autora na własną, ostrożniejszą wersję.** Jeśli on mówi „bez X", film mówi „bez X". Zmiękczanie jego stanowiska, żeby brzmiało bezpieczniej, jest tym samym naruszeniem co dopisanie treści.
8. **Myśl ze wsadu ma zwykle drugie dno.** Sprawdź, co dane zdanie znaczy dla bohatera, zanim zrobisz z niego oś.

# Otwarcie

Pierwsze trzydzieści sekund. Dwa zadania: potwierdzić, że widz dobrze kliknął, i dać powód, żeby został.

**W filmie poradnikowym** pierwsze zdania nawiązują do tego, co obiecał tytuł, i od razu je przebijają. Najbardziej wyrazista rzecz idzie jak najbliżej startu, nie na koniec.

**W filmie przekonaniowym** otwarciem jest rozpoznanie, nie dowód wartości. Widz ma powiedzieć „to jest o mnie", zanim padnie teza. Trzy sposoby w `WIEDZA_FILM_PRZEKONANIOWY.md` sekcja 2.

Czego nie robisz:

- **Nie wyliczasz osiągnięć autora**, dopóki nie są potrzebne. Autorytet stoi po pierwszym konkrecie.
- **Nie sprzedajesz filmu** — „to będzie naprawdę wartościowy materiał" kasuje samo siebie.
- **Nie mówisz „myślisz, że X"** przy obalaniu przekonania. Wypowiedz je jako gołe twierdzenie i dopiero obal.

Przywitanie na starcie nie jest błędem, jeśli jest krótkie i jest stałym znakiem kanału. Zakaz dotyczy rozgrzewki, nie sekundy przywitania.

# Mechanizm

W filmie przekonaniowym to jest środek ciężkości.

**Wykładaj mechanizm na łatwiejszym przypadku, jeśli temat właściwy jest wstydliwy.** Widz uczy się, jak coś działa, zanim wie, że to o nim, więc nie ma czego bronić. Dopiero potem przenosisz zdaniem „i dokładnie tak samo jest z…".

**Buduj pojęcia w kolejności, każde przez scenę.** Nie definicja, tylko obraz, z którego definicja wychodzi sama.

**Mechanizm bez obrazu zostaje abstrakcją.** Zdanie opisujące, jak coś działa, potrzebuje sceny z życia widza.

**Jedna metafora nośna na cały film.** Obraz z życia widza, nie autorski i nie poetycki. Trzy dobre metafory rozbijają film, jedna go trzyma.

**Wiedza wchodzi tylko wtedy, gdy rozbraja przekonanie tego widza w tym filmie.** Jeśli blok zaczyna tłumaczyć, jak coś działa w ogóle, wypadł do wykładu.

# Gdy film nazywa u widza coś wstydliwego

**Kolejność, która działa: konkretny objaw → rozpoznanie → dopiero potem skąd to jest.** Wyjaśnienie pochodzenia jest nagrodą za rozpoznanie, nie wstępem do niego.

**Mechanizm zawsze opisany jako nieświadomy.** Postaw granicę odpowiedzialności wprost: dopóki nie widziałeś, nie mogłeś wybierać; od momentu, w którym widzisz, wybór jest twój.

**Rozbrajaj po drodze, nie w osobnym bloku.** Cztery formy, wszystkie krótkie, wszystkie w tym samym miejscu co diagnoza: zaprzeczenie skrajności, odebranie sobie wyższości, przyznanie się do tego samego, przyznanie, że model jest uproszczeniem.

**Test oskarżenia.** Przeczytaj trzy kolejne bloki tak, jakby ktoś mówił ci to w twarz. Jeśli brzmią jak lista zarzutów, brakuje zdania o tym, skąd to się wzięło.

# Fałszywe rozwiązanie

Blok, którego nie ma w żadnym poradniku, a bez którego film przekonaniowy nie działa: **to, co widz już próbował, i dlaczego nie wyszło.**

Konstrukcja mocna: fałszywe rozwiązanie nie jest po prostu nieskuteczne — ono **pogłębia dokładnie ten problem, który miało rozwiązać.**

**Przyznaj mu wartość, zanim postawisz granicę.** „To jest zajebista praca, ale nie dotyka jednego" jest mocniejsze niż „to nie działa", bo widz, który tej rzeczy próbował, nie musi bronić własnej decyzji. Przyznanie wartości nie osłabia tezy — to jest część tego, co czyni ją wiarygodną.

Bez tego bloku widz słucha rozwiązania z myślą „próbowałem, nie działa" i nic więcej do niego nie dojdzie.

# Blok, który wskazuje robotę

Tu najłatwiej wyprodukować zdanie brzmiące mądrze i nieznaczące nic. „Sięgnij do źródła", „popracuj nad tym w środku", „to się dzieje na głębszym poziomie". Każde da się wkleić do dowolnego innego filmu — i to jest test.

Robota działa, gdy ma **liczbę, próg albo dokładne zdanie do wypowiedzenia**. Nigdy sama postawa.

Trzy rzeczy, które idą źle:

- **Ucieczka w abstrakcję** — im mniej wiesz, gdzie leży robota, tym bardziej poetycko brzmi to, co napiszesz.
- **Wykład zamiast treści** — badanie albo liczba wsypane, żeby blok wyglądał merytorycznie.
- **Zgadywanie metody autora** — jeśli robota leży w tym, co on robi zawodowo, nie zrekonstruujesz tego z wsadu. Zapytaj.

# Przejścia

Blok kończy się czymś, co otwiera następny. Nie „przejdźmy dalej" i nie „i tu robi się ciekawie" — to udaje napięcie. Przejście mówi coś prawdziwego i zostawia otwarte, dlaczego tak jest.

Najlepsze wyrasta z ostatniego zdania poprzedniego bloku. Numerowanie jest w porządku, jeśli razem z numerem pada treść.

# Zamknięcie

**Zamykaj rozróżnieniem, nie podsumowaniem.** Dwa takty, obie połowy zbudowane wcześniej w tym filmie.

Trzy rzeczy, którymi zamknięcie się psuje:

- **Podsumowanie.** Streszczenie tego, co już padło, nie jest zamknięciem.
- **Import z zewnątrz.** Zamknięcie nie może wprowadzać mechanizmu ani pojęcia, którego widz nie widział.
- **Metafora bez rozpakowania.** Zamknięcie ląduje na konkrecie: zachowaniu, przyczynie, fakcie.

**Test bohatera:** podstaw pod ostatnie zdanie widza tego filmu i zapytaj, czy on już tego nie robi.

# CTA

**Nic nie stoi po zamknięciu.**

**Jedno CTA, nie trzy.**

**Prośba w środku jest w porządku**, jeśli wyrasta z bloku, w którym stoi.

**Generyczne CTA jest gorsze niż żadne.** Jeśli nie masz prośby, która wynika z tej treści, przenieś ją do opisu.

Jeśli film ma sprzedawać, sprawdź w plikach oferty, co konkretnie sprzedaje — nie zgaduj ceny ani struktury.

# Długość

Nie ma reguły i żadne źródło jej nie podaje. Film kończy się tam, gdzie kończy się materiał, a nie tam, gdzie wypada.

Praktycznie: jeden mechanizm plus rozbrojenie plus robota plus zamknięcie to zwykle 8–15 minut. Jeśli plan ma więcej niż sześć bloków merytorycznych, sprawdź, czy pod numeracją jest oś — lista dziesięciu punktów rozpada się po ósmym, gdy trzyma ją tylko numeracja.

# Poprawki

Poprawiaj tylko wskazane miejsca. Nie przepisuj całego skryptu i nie ruszaj bloków zaakceptowanych.

Jeden wyjątek: **jeśli odrzucane są zamknięcie, blok z robotą albo mechanizm, problem zwykle leży w osi całego filmu.** Bloki końcowe pękają pierwsze, bo to one muszą coś domknąć. Objaw: poprawiasz to samo miejsce po raz trzeci i za każdym razem brzmi pusto.

Wtedy zatrzymaj się i powiedz to autorowi wprost, zamiast serwować czwartą wersję.

# Autotest przed oddaniem

1. **Same nagłówki bloków po kolei.** Czy niosą przekaz? Czy któryś zaprzecza poprzedniemu? Czy teza nie wraca w trzech blokach w różnych słowach?
2. **Test obietnicy.** Przeczytaj tytuł, potem ostatni blok. Czy film dowiózł to, co obiecał?
3. **Test na głos.** Trzy przypadkowe akapity wypowiedziane. Każde zdanie, którego nie da się powiedzieć na jednym wdechu, przepisz.
4. **Test oskarżenia i wprowadzonych pojęć.**
5. **Test fałszywego rozwiązania.** Czy film mówi, czego widz już próbował i dlaczego to pogłębiło problem?
6. **Test przenośności.** Trzy najbardziej „mądre" zdania — czy pasują do filmu o czymkolwiek innym? Wytnij.
7. **Test bohatera na zamknięciu.**
8. **Nic po zamknięciu.**
9. **Checklista z `natural-polish-copy-fable-updated`.** Cała, nie z pamięci.
