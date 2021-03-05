def es_tabellina():
    #stampare la tabellina del 5
    for i in range(1, 11):
        print(5 * i)

def es_naturali():
    numeri = range(1, 51)[::-1]
    for i in numeri:
        print(i)

def es_quadrati():
    quadrati = []

    for i in range(1, 21):
        quadrati.append(i * i)

    print(quadrati)

def es_compositori():
    composers = ['Head, Michael Dewar',
    'Weill, Kurt',
    'Copland, Aaron',
    'Apostel, Hans Erich',
    'Poot, Marcel',
    'Rubbra, Edmund',
    'Finzi, Gerald',
    'Rodrigo, Joaquín',
    'Durufle, Maurice',
    'Walton, Sir William Turner',
    'Joseph, William',
    'Rodgers, Richard',
    'Berkeley, Sir Lennox',
    "Khachaturian, Aram Il'yich",
    'Giannini, Vittorio',
    'Antill, John',
    'Addinsell, Richard',
    'Kabalevsky, Dmitri Borisovich',
    'Milstein, Nathan',
    'Tippett, Sir Michael Kemp',
    'Halffter, Ernesto',
    'Bozza, Eugene',
    'Rawsthorne, Alan',
    'Seiber, Matyas',
    'Tubin, Eduard',
    'Sternefeld, Daniel',
    'Wiren, Dag Ivar',
    'Alwyn, William',
    'Frankel, Benjamin',
    'Shostakovich, Dmitri',
    'Creston, Paul',
    'Guarnieri, Mozart Camargo',
    'Maconchy, Elizabeth',
    'Rózsa, Miklós',
    'Partos, Oedoen',
    'Perkins, Frank',
    'Distler, Hugo',
    'Ferguson, Howard',
    'Messiaen, Olivier',
    'Constantinescu, Paul',
    'Holmboe, Vagn',
    'Chajes, Julius',
    'Barber, Samuel',
    'Reed, H. Owen',
    'Binge, Ronald',
    'Schuman, William Howard',
    'Glaser, Werner Wolf',
    'Elenescu, Emanuel',
    'Alain, Jehan',
    'Hovhaness, Alan',
    'Herrmann, Bernard',
    'Menotti, Gian Carlo',
    'Pettersson, Gustav Allan',
    'Guastavino, Carlos',
    'Françaix, Jean',
    'Joio, Norman Dello',
    'Lutoslavski, Witold',
    'Lloyd, George',
    'Britten, Lord Benjamin',
    'Gould, Morton',
    'Webber, William Southcombe Lloyd',
    'Truscott, Harold',
    'Surinach, Carlos',
    'Diamond, David',
    'Lilburn, Douglas',
    'Dutilleux, Henri',
    'Stevens, Bernard',
    'Ginastera, Alberto',
    'Farnon, Robert Joseph',
    'Zimmermann, Bernd Alois',
    'Rochberg, George',
    'Bernstein, Leonard',
    'Nelhybel, Vaclav',
    'Weinberg, Mieczysław',
    'Basarab, Mircea',
    'Simpson, Robert',
    'Nixon, Roger',
    'Arnold, Malcolm',
    'Petit, Pierre',
    'Raid, Kaljo',
    'Williams, James Clifton',
    'Mennin, Peter',
    'Braun, Günter',
    'Presti, Ida',
    'Tomlinson, Ernest',
    'Lamb, Peter',
    'Mechem, Kirke',
    'Orbon, Julian',
    'Jirko, Ivan',
    'Gielen, Michael',
    'Muczynski, Robert',
    'Matton, Roger',
    'Leighton, Kenneth',
    'Nelson, Ron',
    'Tormis, Veljo',
    'Shchedrin, Rodion Konstantinovich',
    'Gorecki, Henryk Mikolaj',
    'McLeod, John',
    'Mathias, William',
    'Schnittke, Alfred',
    'Part, Arvo',
    'Maw, Nicholas',
    'Kymlicka, Milan',
    'Bennett, Richard Rodney',
    'Nobre, Marlos',
    'Bruzdowicz, Joanna',
    'Holloway, Robin',
    'Tavener, John',
    'Rutter, John',
    'Tabakov, Emil',
    'Webber, Andrew Lloyd',
    'Gallant, Pierre',
    'Febel, Reinhard',
    'Saxton, Robert']

    #----------------------     PARTE 1
    num_compositori = len(composers)
    print(f"Il numero di compositori equivale a {num_compositori}")
    
    #---------------------      PARTE 2
    composers.sort()
    
    #--------------------       PARTE 3
    compositori_che_iniziano_con_s_questo_nome_e_lunghissimo = []
    for compositore in composers:
        if compositore[0].upper() == "S":
            compositori_che_iniziano_con_s_questo_nome_e_lunghissimo.append(compositore)
    print(compositori_che_iniziano_con_s_questo_nome_e_lunghissimo)

def es_lista():
    lista = [5, 10, 15, 20, 25, 50]
    for i in range(len(lista)):
        if lista[i] == 20:
            lista[i] = 200

    print(lista)

def es_media():
    values = [771, 856, 211, 702, 601, 432, 122, 484, 903, 808, 232, 336, 622, 19, 252, 235, 47, 649, 193, 479, 
          211, 950, 589, 254, 763, 350, 428, 237, 570, 662, 624, 234, 161, 407, 163, 757, 251, 296, 712, 160, 
          66, 476, 102, 172, 697, 799, 701, 596, 983, 641, 205, 569, 712, 734, 331, 238, 861, 268, 893, 396, 
          267, 772, 318, 80, 349, 228, 810, 571, 761, 338, 125, 288, 86, 705, 600, 889, 366, 40, 202, 256, 
          988, 124, 976, 714, 424, 605, 962, 1, 538, 356, 493, 725, 43, 339, 13, 18, 206, 287, 521, 548, 612]

    #media
    somma = sum(values)
    media = somma / len(values)
    print(media)

    #mediana
    values.sort()
    if len(values) % 2 == 1:
        mediana = values[ (len(values) // 2) + 1]
    else:
        num_centrale_1 = values[ (len(values) // 2)]
        num_centrale_2 = values[ (len(values) // 2) + 1]

        mediana = (num_centrale_1 + num_centrale_2) / 2

    print(mediana)

def es_jedi():
    frasi = [
    "Tutto quanto procede come avevo previsto",
    "Sia come vuoi, Jedi!",
    "Se non ti vuoi convertire, allora sarai distrutto!",
    "Giovane stolto: solo ora, alla fine, acquisti la ragione!",
    "Hai lavorato bene, Lord Vader. E ora sento che desideri continuare la ricerca del giovane Skywalker.",
    "Avete fallito, Altezza. Sono uno Jedi, come mio padre prima di me!",
    "Disattiveranno quello scudo in tempo. O questo sarà l'attacco più breve di tutti i tempi."
    ]
    lunghezze = []
    for frase in frasi:
        lunghezze.append(len(frase))

    media = sum(lunghezze) / len(lunghezze)
    print(media)
        