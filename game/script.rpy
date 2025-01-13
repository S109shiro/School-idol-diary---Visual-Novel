# El juego comienza aquí.
label splashscreen:
    init python:
        from datetime import date
        from datetime import datetime
        now = datetime.now()

    if(now.month == 10 and now.day == 31):  #Halloween
            image movieH = Movie(channel="movie_dp", loop = False, play = "movie/Halloween/IntroH.avi") 
            show movieH with Dissolve(1.0)
            #$ renpy.movie_cutscene("movie/Intro1.avi", loops=0, stop_music=True)
            $ renpy.pause(90.0, hard= False)
            hide movieH with Dissolve(1.0)
            return
    elif(now.month == 12 and now.day == 24):    #Navidad
            image movieN = Movie(channel="movie_dp", loop = False, play = "movie/Christmas/IntroN.avi") 
            show movieN with Dissolve(1.0)
            #$ renpy.movie_cutscene("movie/Intro1.avi", loops=0, stop_music=True)
            $ renpy.pause(90.0, hard= False)
            hide movieN with Dissolve(1.0)
            return
    else:
        $ op = renpy.random.randint(1, 2)
        if op == 1:
            image movie1 = Movie(channel="movie_dp", loop = False, play = "movie/Op/Intro1.avi") 
            show movie1 with Dissolve(1.0)
            #$ renpy.movie_cutscene("movie/Intro1.avi", loops=0, stop_music=True)
            $ renpy.pause(90.0, hard= False)
            hide movie1 with Dissolve(1.0)
            return
        else:
            image movie2 = Movie(channel="movie_dp", loop = False, play = "movie/Op/Intro2.avi")
            show movie2 with Dissolve(1.0)
            # $ renpy.movie_cutscene("movie/Intro2.avi", loops=0, stop_music=True)
            $ renpy.pause(90.0, hard= False)
            hide movie2 with Dissolve(1.0)
            return    


label start:
    #ELECCION DE RUTAS
    $ quick_menu = False
    stop music fadeout 0.8
    play music SongMenuSelect fadein 0.5 fadeout 0.5
    scene MenuElec with Dissolve(1.5)
    menu:  
        "QUE RUTA DESEAS LEER?"
        "School Idol Diary - Honoka Kousaka":
            menu: 
                "QUE CAPITULO DESEAS"
                "CAPITULO 1 - HONOKA NO SE RENDIRÁ" : 
                    jump cap1Honoka
                "CAPITULO 2 - CONVIRTÁMONOS EN SCHOOL IDOLS" :
                    jump cap2Honoka
                "CAPITULO 3 - ¡BAILEMOS!":
                    jump cap3Honoka
                "CAPITULO 4 - QUIERO UN SALÓN PROPIO":
                    jump cap4Honoka
                "CAPITULO 5 - ¡¿TANTOS PROBLEMAS PARA UN CONCIERTO?!":
                    jump cap5Honoka
                "CAPITULO 6 - SESIÓN FOTOGRAFICA":
                    jump cap6Honoka
                "CAPITULO 7 - MI FUTURO Y EL DE YUKIHO":
                    jump cap7Honoka

        #"Ruta de Umi Sonoda":
            #jump UmiSono
    return

#NOVELA DE HONOKA
#COMIENZO DEL CAPITULO 1
label cap1Honoka:
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo1 with fade
    $ renpy.pause(3.0, hard= True)
    scene cuarto_Honoka with fade
    $ quick_menu = True
    play music Main1 fadein 1.5
    #show HonokaPan at top with dissolve 
    "Soy Honoka Kousaka, tengo 16 años. Voy en segundo año de la preparatoria Otonokizaka." with dissolve 
    "¡Y formo parte del superexitoso grupo de idols escolares μ's! Bueno, eso me gustaría decir, pero honestamente, ¿será que es cierto?" with dissolve 
    "Ah, ajajajaja, aah." with dissolve 
    scene black with dissolve
    stop music fadeout 1.5
    "Agh, no debí haber pensado eso." with dissolve 
    "¡No puedes rendirte cuando apenas estás empezando, Honoka!" with dissolve 
    "De acuerdo." with dissolve 
    "Bien, vamos otra vez, ¡con sentimiento!" with dissolve 
    voice "audio/VoiceHonoka/faitoDayo.mp3"
    $ renpy.pause(1.0, hard = True)
    scene cuarto_Honoka with fade
    play music Main1 loop fadein 1.5 fadeout 1.0
    #show KousakaHonoka at top with dissolve
    "Soy {color=#FFAE00}Honoka Kousaka{/color}, tengo 16 años." with dissolve 
    "Este abril, decidí debutar como idol escolar junto a mis amigas. Aunque a decir verdad, creo que somos muy… normales… como para llamarnos \"idols\"." with dissolve 
    "Quiero decir, nos vemos normales, no somos buenas cantando, tampoco tenemos talento en la actuación, y si ves nuestras fotos..." with dissolve 
    scene photo with Fade(.25, 0, .75, color="#fff")
    "salimos todas nerviosas, con sonrisas falsas, o posamos haciendo el símbolo de la paz, típica pose de chicas de preparatoria." with dissolve

    scene cuarto_Honoka with fade
    "Mmm, pero... un momento, ¿no acabo de decir que las idols no deben de desanimarse? ¡Así es!" with dissolve 
    "Sí, y por eso nos convertiremos en las brillantes idols con las que todos sueñan, y vamos a esforzarnos mucho, llamaremos la atención de todos y salvaremos nuestra escuela, la {b}preparatoria Otonokizaka{/b}, del cierre. ¡Lo prometo!" with dissolve 
    "En verdad, en verdad quisiera que todos nos dieran su apoyo. Porque…" with dissolve 

    scene otonoki with fade 
    play music Otonoki loop fadein 0.8 fadeout 1.5
    "La escuela a la que vamos, la escuela que amamos tanto, a la que siempre quisimos ir desde que éramos pequeñas, ha sido sentenciada a un cruel destino y cerrará dentro de 3 años." with dissolve 
    "Nuestra escuela, Otonokizaka, es una escuela pública que se encuentra en el vecindario donde nacimos." with dissolve 
    "Ah, pero aunque diga \"pública\", en realidad es una escuela \"nacional\", pero está lejos de todas las estaciones de tren, y quizás por eso todas las que asisten son chicas locales," with dissolve 
    "tampoco tiene algún club sobresaliente ni un nivel alto en educación, es completamente lo opuesto a la elegante y refinada imagen que te viene a la mente cuando escuchas \"escuela nacional\"." with dissolve 

    show UmiS at top with dissolve
    "{color=#6D56FF}Umi-chan{/color}, mi amiga de toda la vida, dice que el gobierno no tiene presupuesto para mantener la escuela, pero sería inconcebible que la cerrasen, dejando una región de la capital sin preparatoria, por eso deberían nombrar la escuela nacional en vez de cerrarla." with dissolve 
    "Sí que es la descendiente de una larga generación de artistas marciales. Sabe de todas esas cosas complicadas, ¿no?" with dissolve 
    hide UmiS with dissolve
    
    "Yo soy tonta, así que no sé nada de eso o cosas de adultos, pero sí sé que la preparatoria Otonokizaka es importante y siempre ha estado aquí." with dissolve 
    "Es el corazón de nuestro vecindario." with dissolve 
    "Barrio especial Chiyoda, Tokio. Akihabara, Kanda, Jinbocho y Ochanomizu. En medio de esos lugares, en donde gente de todo Japón se reúne, se encuentra nuestro vecindario, como si fuera un valle marrón rodeado de edificios." with dissolve 
    scene atardecer with fade
    "Ah, de hecho, quizá no haya tanta tierra como para llamarlo valle marrón, ¿o sí? Pero cuando era niña, no había tantos edificios como ahora. Era un vecindario tan tranquilo, con parques, espacios abiertos y bellos atardeceres." with dissolve 
    
    scene cielo with fade
    "Por supuesto, yo no sé si es verdad, pero mi abuela, que vive conmigo, dice que esta es una de las pocas ciudades que no desapareció con los bombardeos de la {a=https://acortar.link/zgejGa}{color=#E000FF}Guerra del Pacífico{/color}{/a} (¡¿?!)."
    "Es cierto que cuando recorres las calles puedes ver viejos edificios y muchos negocios antiguos." with dissolve 
    "Está el famoso puesto de soba. Y la tienda de dulces estilo occidental que le encanta a mi abuela, y que apareció en los libros de Shotaro Ikenami." with dissolve 
    "El restauran occidental que le gustaba al gran autor que mencionan en los libros de texto, Souseki Natsume. Y el puesto que vende delicioso sushi." with dissolve 
    "También está la venerable tienda de ramen dirigida por dos ancianitas. Y el spa, con mujeres en kimono entrando y saliendo todo el día." with dissolve 
    "En este vecindario, puedes llegar a apreciar todo tipo de escenarios antiguos, escondidos entre los viejos edificios y las casas hechas de madera y tejas." with dissolve 
    "Camina un poco y te toparás con un montón de trenes y autos, pero este vecindario está mayormente transitado por peatones." with dissolve 
    "Así se siente." with dissolve 
    "Cuando piensas en ello, es un lugar un tanto misterioso, ¿no? Pero aquí nací y aquí crecí. Este es el único lugar que conozco perfectamente." with dissolve 
    "Jardín de niños, primaria, secundaria, todas eran escuelas públicas y por supuesto, las únicas clases particulares que tuve fueron clases de piano con una señora que vive cerca de aquí" with dissolve 
    "(aunque no practicaba y luego luego lo dejé, jejeje ♡)" with dissolve
    "las clases de ábaco en el parque, oh, y las clases de caligrafía con el tío de Umi-chan." with dissolve 
    "¡Ah, y mi clase favorita era la de natación que se daba en la piscina pública! Cuando terminaban las clases, buscábamos donde jugar balón prisionero o a perseguirnos." with dissolve 
    "Subirse al tren era algo que ocurría pocas, muy pocas veces, como cuando le rogabas a tu mamá que fueran al cine durante las vacaciones de verano o primavera." with dissolve 
    "Así que, aunque estemos en el barrio especial Chiyoda, no encajamos mucho aquí, ¿o sí? Vivimos en nuestro pequeño universo de 500 metros. Jeje" with dissolve 
    "Por eso es que nunca noté que nuestro vecindario se volvía urbano." with dissolve  
    "Y, aunque estamos en medio de la ciudad, el número de niños seguía reduciéndose y también estaba el problema de la población." with dissolve 
    
    stop music fadeout 1.3
    scene black 
    "Yo nunca supe de eso..." 
    "No tenía ni idea, vivía en mi propio mundo."  
    "Ahora que lo pienso, me doy cuenta de lo tonta que fui."
    "Pero siempre pensé que este lugar, que quiero tanto y que es tan tranquilo y que siempre alumbra el sol, se quedaría así para siempre." 
    "Por eso pensaba que cuando creciera y entrara a la preparatoria, por fin sería como esas niñas mayores que veía, y que viviría una vida maravillosa."
    "..."

    scene otonoki with dissolve
    play music Otonoki loop fadein 0.8 
    "Ahora, hablando de Otonokizaka, el edificio y sus aulas son completamente normales, las estudiantes son comunes y corrientes" with dissolve 
    scene otonoki4 with fade
    "hasta los uniformes que tanto me gustan, el saco azul y la falda de tablones son ordinarios, así, mmm... si tuviera que escoger, diría que lo especial de la escuela es que…" with dissolve 
    "aunque está en medio de la ciudad ¿tiene áreas grandes y muchos árboles? Ah, y como no hay muchas estudiantes, también hay mucho espacio. Eso sería todo, creo." with dissolve 
    "Dado que he vivido todo el tiempo aquí, siempre pensé que cuando creciera, ¡usaría el uniforme de Otonoki y me volvería una estudiante de Otonoki!" with dissolve 
    "¿Por qué? No es como que recordase haber tenido algún encuentro fantástico con una de las chicas de Otonoki, o ninguna otra clase de inspiración." with dissolve 
    "Aún así, mis compañeras de clase tenían hermanas que fueron a Otonoki, las veía andar riendo y divirtiéndose juntas por el vecindario. Verlo era algo tan normal para mí, que simplemente quería ser como ellas." with dissolve 
    "¿No les pasa eso a todos?" with dissolve 
    scene otonoki2 with fade
    "Aunque no fuera una escuela especial, aunque fuera fácil entrar, aunque se tratara de una preparatoria pública común y corriente, esa escuela de la que podrías graduarte llevándotela tranquila..." with dissolve 
    "aún así, era un futuro emocionante, siempre frente a ti, pero nunca al alcance hasta que llegase el momento." with dissolve 
    "Era la escuela a la que siempre, siempre quise asistir." with dissolve 
    "Pensé que cuando creciera, sería como una de esas chicas. Ahora que lo pienso, ¿quizá también se debía a que había poca gente?" with dissolve 
    "Sin importar la época, las chicas vistiendo el uniforme de Otonokizaka siempre estaban tranquilas, no como esas chicas ricas que ves en la TV." with dissolve 
    "Se veían tan alegres y amables, parecía que recibían algún tipo de trato especial de parte de la gente del vecindario. Quizás por eso, para mí, esas chicas eran como el símbolo representativo del vecindario." with dissolve 
    "Esas chicas, con sus bellos y bien arreglados uniformes azules eran mi modelo a seguir." with dissolve 
    "Bueno, tal vez yo no me veo como una chica de esa edad. Jejeje." with dissolve 
    "Por eso aún no puedo creerlo." with dissolve 
    "La preparatoria a la que siempre quise ir, Otonokizaka, está a punto de cerrar." with dissolve 

    "Todavía lo recuerdo como si hubiera sido ayer." with dissolve 
    stop music fadeout 1.3
    play music PasilloMain loop fadein 1.0 fadeout 0.8
    scene pasillo with Fade(.25, 0, .75, color="#fff")
    "Con la ayuda de Umi-chan y {color=#A8A8A8}Kotori-chan{/color} logré sobrevivir a las clases de regularización y comencé segundo año esta primavera." with dissolve 
    "Cuando llegas a segundo, significa que ya sobreviviste el primer año en la nueva escuela y todavía no tienes que preocuparte por los exámenes de la universidad, así que es el mejor momento para divertirte, ¿no es así?" with dissolve 
    "Y el clima estaba perfecto aquella mañana, parecía que los Dioses festejaban conmigo, estaba tan emocionada de comenzar mi nueva vida en la preparatoria." with dissolve 
    "Cuando me encontré con Kotori-chan y Umi-chan, las saludé con una gran sonrisa." with dissolve 
    #show KousakaHonoka at top with dissolve
    voice "audio/VoiceHonoka/goodday.mp3"
    K_Honoka "¡Hoy es un gran día!" with dissolve 
    "Y luego…" with dissolve 
    scene beginner with dissolve
    $ renpy.pause(1.5, hard = True)
    "Con un semblante nervioso, ambas me llevaron al tablón de anuncios, en donde se encontraba la noticia del cierre de la escuela." with dissolve 
    scene beginner2 with dissolve
    $ renpy.pause(1.5, hard = True)
    "¡Ooohh, vamos!" with hpunch 
    "Me duele el pecho sólo de recordarlo. Hay gente que dice \"Lo veo y no lo creo\" pero... esa vez, eso era lo que me pasaba. Era imposible, era mentira, tenía que ser eso." with dissolve 
    "Todas las ideas y palabras se esfumaron de mi mente, en automático pellizqué mi mejilla. Quizás fue debido a la sorpresa, pero no sentía nada, apenas sentí dolor." with dissolve 
    "Y por eso pensé \"¡Ah, ya sé! ¡Es sólo un sueño!\" Y mi cabeza comenzó a dar vueltas. No estaba segura de qué pasaba, pero luego, estaba sentada en mi pupitre." with dissolve 
    scene aula with dissolve
    "Frente a mí estaban Umi-chan y Kotori-chan, preocupadas." with dissolve 
    show KotoriM at KotOtoki with dissolve
    show UmiS at UmiOtoki with dissolve
    voice "audio/VoiceKotori/001.mp3"
    M_Kotori " ¿Estás bien, Honoka-chan?" with dissolve 
    "Cuando las vi, con esa preocupación. Por fin me di cuenta. Ah, no fue un sueño." with dissolve 
    # PENDIENTE voice "audio/VoiceHonoka/.mp3"
    K_Honoka "Cierre…" with dissolve 
    "Eso quería decir que mi querida preparatoria Otonokizaka iba a desaparecer." with dissolve 
    "Luego de un tiempo, no andaría ninguna estudiante en este edificio; y esas chicas con sus uniformes, que nunca imaginé que dejaría de ver en el vecindario, también desaparecerían." with dissolve 
    "¡Ah! Y además, si cerraba, ¡¿qué pasaría con los dos años que me faltaban de preparatoria?! ¿Qué voy a hacer?" with dissolve 
    "Reprobé materias el año pasado, y en verdad no creo ser capaz de aprobar otro examen de admisión en este punto." with dissolve 
    "Kotori-chan me miró con pena y una sonrisa débil." with dissolve
    voice "audio/VoiceKotori/002.mp3" 
    M_Kotori "Parece que no tendrás que preocuparte por eso. La escuela va a cerrar hasta dentro de tres años, cuando se hayan graduado todas las estudiantes." with dissolve 
    "Ah, muy bien." with dissolve 
    "Cansada, me hundí en mi asiento." with dissolve 
    hide UmiS with dissolve
    hide KotoriM with dissolve
    "Pero, al parecer, volví a pensar en voz alta y me levanté de mi lugar." with dissolve 
    # PENDIENTE
    K_Honoka "¿TRES AÑOS?" with hpunch   
    "Recibir dos noticias así en un solo día drenó toda mi energía." with dissolve 
    scene HonokaSad with dissolve
    "A pesar de todos los esfuerzos, nuestra Otonoki iba a cerrar debido al bajo número de estudiantes, pero pasaría hasta dentro de tres años, para no afectar a las alumnas actuales." with dissolve 
    "Parecía mucho pero poco, poco pero mucho. Tres años." with dissolve 
    "El curso completo de preparatoria" with dissolve 
    "Digo, es cierto que ya no estaremos en esta escuela en tres años." with dissolve 
    "Sin importar si trato de quedarme, es normal que me gradúe en tres años." with dissolve 
    "Aunque no sé si voy a ir a la universidad o si empezaré a trabajar, ya no será mi problema para entonces, y ya no tendré derecho a oponerme al cierre." with dissolve 
    "Pero aún así…" with dissolve 
    scene aula with dissolve
    voice "audio/VoiceHonoka/004.mp3"
    K_Honoka "¿Estoy de acuerdo con esto?" with dissolve 
    "En tanto no me afecte, en tanto pueda graduarme, ¿entonces no hay problema?" with dissolve 
    "..." with dissolve 
    "..." with dissolve 
    "..." with dissolve 
    "En realidad no puedo pensar de esa forma." with dissolve 
    "¿Por qué cerrará Otonoki?" with dissolve 
    "Es imposible." with dissolve 
    "Otonoki ha sido parte de nuestra vida por tanto tiempo, y ahora, ¿va a desaparecer del mapa?" with dissolve 
    "¡N-no quiero que pase!" with hpunch
    scene HonokaCry with dissolve
    "Aquí fue cuando comenzaron a asomarse lágrimas en mis ojos." with dissolve 
    "Cuando les dije a Umi-chan y a Kotori-chan, que estaban frente a mí, se veían algo incómodas." with dissolve 
    "La mamá de Kotori-chan es la directora de la escuela, así que quizás tenga problemas por hablar así. Pero, está mal." with dissolve 
    "No pueden cerrar la escuela porque sí, sin preguntarle a las estudiantes." with dissolve 
    "Ya sé que de la escuela se encargan los adultos, ¡pero aún así! Esta escuela, Otonokizaka, le pertenece a sus estudiantes, ¿o no?" with dissolve 
    "Si cierra, bueno, ¡no podemos quedarnos aquí sin hacer nada! Si hubiéramos sabido que nuestra escuela cerraría, tal vez pudimos haber hecho algo…" with dissolve 
    "Quiero decir, sólo pusieron el letrero \"Anuncio de cierre\" en el tablón junto al anuncio en el que reclutan voluntarios para la biblioteca, como si no fuera la gran cosa." with dissolve 
    "¿No es ridículo?" with dissolve 
    "Si hay más chicas tan distraídas como yo, que nunca ven el tablón de anuncios, estarían en grandes problemas ¡ya que la escuela cerraría de repente!" with dissolve 
    "¡En serio, qué ridiculez!" with dissolve 
    scene aula with dissolve
    "¡Mm, estoy llenándome de energía otra vez!" with dissolve 
    "Debe haber algo que pueda hacer." with dissolve 
    "Por mi escuela." with dissolve 
    "Y por eso yo, Honoka, {b}nunca me voy a rendir{/b}." with dissolve 
    "Esto es lo que creo." with dissolve 
    scene otonoki with dissolve
    stop music fadeout 1.0
    play music Motivation loop fadein 1.0 fadeout 0.8
    "Si es por algo que es importante para ti, alguien importante, algo que en verdad quieres…" with dissolve 
    "Entonces nunca debes rendirte." with dissolve 
    "Sin importar qué, no te rindas, nunca, sigue intentando y sólo así tus sueños se harán realidad." with dissolve 
    "No importa si es algo pequeño." with dissolve 
    "Siempre que sigas adelante, aunque sea poco a poco, es lo único que necesitas." with dissolve 
    "Porque cuando alguien escala una gran montaña, que ocupa toda su visión y alcanza las nubes, van paso a paso." with dissolve 
    "Enfocarme en lo que está frente a mí y dirigirme al objetivo es lo único que sé hacer." with dissolve 
    "Aunque eso no significa que nunca tenga miedo, a veces, eso pienso…" with dissolve 
    scene determinacion with dissolve
    "No puedo detenerme." with dissolve 
    "Si lo hago, ya no podré seguir adelante." with dissolve 
    "En momentos como ese, en los más difíciles, en los más dolorosos, son en los que debo apretar la mandíbula y seguir adelante, aunque sea un milímetro." with dissolve 
    "No voy a perder si siempre sigo avanzando." with dissolve 
    "Así es como pienso siempre." with dissolve  
    "Pero, si me rindo, entonces ahí termina todo." with dissolve 
    "La vida es muy simple." with dissolve 
    "Cuando digo cosas como esas la gente se ríe de mí y me dice que sueno como una porrista." with dissolve 
    "Pero no me voy a unir a ningún club deportivo, ¿entendido?" with dissolve 
    "No, porque… voy a comenzar el club de idol…" with dissolve 
    "No, ¡un club de idol escolares!" with dissolve 
    "Cantaré, bailaré, seré linda y brillaré, y llamaré la atención de todos, y entonces, ¡el número de estudiantes en la preparatoria Otonokizaka aumentará!" with dissolve 
    "Un día, cuando en verdad me vuelva una idol famosa, espero que pueda expresar estos sentimientos al público" with dissolve 
    "y que sepan de estos sentimientos que no se pueden transmitir en los conciertos." with dissolve 
    scene black with Dissolve(1.3)
    image mv1 = Movie(channel="movie_dp",loop = False, play = "movie/Escenas/video1.avi", size= (1980, 1080) )
    $ quick_menu = False
    stop music
    show mv1 with Dissolve(1.0) 
    $ renpy.pause(123.0, hard= False)
    $ quick_menu = True
    hide mv1 with Dissolve(1.0)
    "¡Espero que ese día llegue pronto!" with dissolve 
    voice "audio/VoiceHonoka/sleep.mp3"
    "Y con ese deseo, me iré a dormir esta noche." with dissolve 
    "¡Mañana practicaremos duro!" with dissolve 
    $ quick_menu = False 
    scene black with fade

    #COMENTARIOS FINALES DE KOTORI
    play music coments fadein 0.8 fadeout 0.5
    scene TKotori with dissolve
    $ renpy.pause(2.0, hard = False) 
    scene comentarioKotori1 with dissolve
    $ renpy.pause(9.0, hard = False) 
    scene black with fade
    stop music fadeout 1.0
    jump cap2Honoka

#COMIENZO DEL CAPITULO 2  
label cap2Honoka: 
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo2 with fade
    $ renpy.pause(3.0, hard= True)

    scene cielo with fade
    $ quick_menu = True
    play music motivationalFree fadein 3.0 fadeout 2.5 loop
    "Todavía puedo recordar la emoción que sentí cuando leí las palabras \"idol escolar\" por primera vez." with dissolve
    "Se sentía tan emocionante como el primer amor." with dissolve 
    "Bueno, yo todavía no me he enamorado, pero supongo que así se siente. Ejejeje♡" with dissolve
    "Pues aunque aún no estoy segura, lo que sí sé, es que esa debió ser mi primera vez." with dissolve
    "Me dolía el pecho, no podía respirar, mi corazón latía muy rápido y cuando las veía, sentía que tenía la vista pegada a ellas, no podía dejar de mirar." with dissolve
    "Estaba tan emocionada que mi cuerpo parecía querer empezar a bailar por sí solo." with dissolve
    "Sí, ¿no?" with dissolve
    "Pues eso es básicamente amor, ¿no?" with dissolve
    "Debí haberme enamorado de las idols escolares." with dissolve
    "No podía quedarme así. Y en lugar de confesar mi amor…" with dissolve
    "Decidí convertirme en idol escolar también." with dissolve
    scene otonoki with Fade(.25, 0, .75, color="#fff")
    "Me volveré una idol y pelearé por el bien de la escuela Otonokizaka." with dissolve
    scene cielo with fade
    "Las idols escolares son un tipo de club muy popular entre las chicas de preparatoria de todo el país." with dissolve
    scene arise1 with dissolve
    "Hay de varios tipos. Algunos clubes son reconocidos formalmente por la escuela" with dissolve  
    scene basic with dissolve
    "mientras que otros son como la guerrilla, donde las chicas realizan las actividades de forma voluntaria, sin tener relación con los eventos escolares." with dissolve
    "Chicas que sueñan con ser idols, pero que creen que llegar a ser una de verdad es muy difícil, realizan las actividades idol y la gente viene a verlas," with dissolve
    "esas son el tipo de cosas que son popular hoy día. En resumen, es como... \"¡Mírenme, soy una idol!\" " with dissolve
    "Verán, cuando piensan en idols, vienen a la mente estas chicas súper lindas que aparecen en la TV, que son seleccionadas de entre cientos de miles de chicas o que ganan ciertas competencias" with dissolve
    "o que envían sus fotos a revistas o que tienen alguna otra razón para llamar la atención de otras personas." with dissolve
    "Ellas son chicas que considerarías especiales." with dissolve
    scene cielo with fade
    "Pero aunque no tengas el talento o la suerte o la perfecta ubicación (o sea, si no vives cerca de la gran ciudad, como Tokio, no tienes oportunidad de hacerte famosa, ¿verdad?" with dissolve
    "Ah, en realidad, nosotras vivimos en la gran ciudad, aunque no parezca. Ajaja) en estos tiempos, puedes aprovechar el internet para volverte idol." with dissolve
    "Esa es la idea detrás de este simple concepto." with dissolve
    "Mm, sí, a quien se la haya ocurrido esta idea fue un gran genio, ¡¿no?!" with dissolve
    "Yo sí lo creo." with dissolve
    "Las canciones, las coreografías, los trajes no se pueden comparar con las de las profesionales, además, es raro verlas presentarse frente a grandes audiencias." with dissolve
    scene festival with fade 
    "La mayoría de los grupos se presentan en festivales deportivos o culturales. Aunque no creo que ser una idol significa aparecer en la TV o revistas." with dissolve
    "Es el deseo de convertirse en idol." with dissolve
    "Es el deseo de convertirte en una brillante e increíble idol." with dissolve
    "Eso es lo que motiva a las chicas." with dissolve
    "Tal vez es extraño que yo lo diga, pero eso es lo que creo. Lo único que necesitas es un traje simple, una canción y un poco de conocimiento en baile." with dissolve
    "Puedes incluso copiar a una idol. Es suficiente." with dissolve
    "Incluso si nadie te va a ver al principio, con que tengas fe y no te rindas, entonces alguien vendrá algún día. ¿No es así? Tan sólo mira. ¡Ta-dá~! ♪" with dissolve
    "Todo lo que necesitas es una computadora para subir un video casero en el medio que es el mejor amigo de las minorías:" with dissolve
    "un sitio web, para compartir videos y así lograr que gente que no te conoce te vea." with dissolve
    "Existen incluso páginas para votar por las más populares, así que aunque sus actividades sólo sean locales, todas tendrán las mismas oportunidades de ser vistas por todo el mundo." with dissolve
    scene cielo with fade
    "Y por eso pensé ¡Eso es! Me convertiré en una idol escolar y haré que todo el mundo me conozca." with dissolve
    "Entonces, les hablaré sobre la preparatoria Otonokizaka y el cierre... si se interesan en ella, puede que así tengamos más alumnas en el futuro, ¿no?" with dissolve
    "Si muchas niñas de secundaria de por aquí piensan, \"¿qué hago? Otonoki es muy simple, quizás deba ir a otra escuela\", puede que eso las haga considerarlo." with dissolve
    "Y hasta chicas de más lejos pueden pensar, \"ya voy en preparatoria, no importa que tome el tren para ir a la escuela Otonokizaka. Y es escuela pública, así que no es tan costosa\"." with dissolve
    "Sólo soy una chica normal." with dissolve
    "Hasta aquí en la escuela, no destaco en absoluto." with dissolve
    "No importa que no quiera que cierren la escuela, no creo lograrlo tan rápido." with dissolve
    "Así que cuando se me ocurrió esta idea, ¡creí que era una genio!" with dissolve
    "Estaba tan feliz, comencé a emocionarme." with dissolve
    "Quería hacer una voltereta, pero no sabía cómo, así que sólo brinqué y grité" with dissolve
    voice "audio/VoiceHonoka/005.mp3"
    K_Honoka "¡Hurra!" with dissolve
    "Y entonces, les pedí a mis amigas de la infancia, Umi-chan y Kotori-chan, que se unieran." with dissolve
    scene insatisfaccion with dissolve
    "Al principio, pusieron cara de \"¡Ni de broma!\" y no les emocionaba la idea, pero terminaron aceptando y nos metimos en todo tipo de líos... pero esa es otra historia." with dissolve
    #POSIBLE LOGRO
    "Ya hablaré de eso más tarde, ¿sí?" with dissolve
    scene cielo with fade
    "Como sea, así comenzamos las actividades de idol." with dissolve
    "Hay muchos grupos así por todo Japón y, a veces, me sorprendo por lo que veo en internet." with dissolve
    "Desde Okinawa, al sur, hasta Hokkaido, al norte, ¡hay tantas idols escolares que sonríen alegremente!" with dissolve
    "Son tan lindas y todos sus trajes están bien elaborados, me hace muy feliz el sólo verlas ♡." with dissolve
    "Y justo ahora, siento que voy a tener que esforzarme mucho para que no me superen." with dissolve
    "¡Sí, nuestro grupo de idol, µ's, también va a esforzarse y así reviviremos a Otonoki!" with dissolve
    "Y mientras pensaba eso…" with dissolve
    scene black with dissolve
    "Una pregunta invadió mi mente." with dissolve
    stop music fadeout 1.3
    "A todo esto... ¿¿¿qué tipo de actividades realizan las idols escolares???" with vpunch
    "Mejor ire a casa a investigar un poco más." with dissolve
    play music home fadein 3.0 fadeout 2.5 loop
    scene cuarto_Honoka with dissolve
    play sound Mecanografia noloop
    "Al buscar en internet, hablan sobre hacer ropa, ensayar, componer canciones y todo ese tipo de cosas." with dissolve
    "Guau, oh cielos, ¡también tengo que ponerme a hacer eso!" with dissolve
    "¿Y cómo… ¿Y cómo haces todo eso?" with dissolve
    "Lo primero es la ropa... Mm, soy muy mala costurando. O más bien, no tengo idea de cómo hacer un traje así de lindo. Y uno de tienda... se vería bastante mal." with dissolve
    "Aunque quisiera hacer uno, ni siquiera puedo hacer un bordado correcto en la clase de Economía Doméstica." with dissolve
    "Agh. ¿Qué voy a hacer? Sólo pensar en ello me provoca dolor de cabeza." with dissolve
    play sound clickMouse noloop
    "Bien, a lo que sigue." with dissolve
    "Sigue... el ensayo, ¿no? ¡Bueno, eso sí lo puedo hacer! Idear una coreografía para una canción y luego ensayar. Eso es todo, ¿no?" with dissolve
    "Aunque no confío mucho en mis habilidades en el baile, me gusta mucho." with dissolve
    "En mi vida diaria, cuando algo bueno pasa, me dan ganas de bailar y pues... ¡me gusta mover el cuerpo!" with dissolve
    "Y cuando es el festival en verano siempre me gusta andar bailando, me parece muy divertido." with dissolve
    "También soy muy buena en esos juegos de ritmo y... ¿eh? ¿Qué no es lo mismo? Eh, omitamos eso entonces. ¡Ejem!" with dissolve
    play sound clickMouse noloop
    "El siguiente problema es... ¿componer canciones?" with dissolve
    "Podemos bailar todo lo que queramos, hacer toda la ropa que queramos, pero al final, si no tenemos canciones, nada importa." with dissolve
    "En lo personal, creo que una canción llena de energía, alegre y dinámica sería la mejor opción." with dissolve
    "Que con tan sólo oírla te haga feliz." with dissolve
    "Mmm..." with dissolve
    "Mmm..." with dissolve
    "¿Eh? ¿Qué cómo cuándo?" with dissolve
    "¿Y cómo compones una canción así? ¡¡Alto, nunca antes he compuesto una canción!!" with dissolve
    "Al toparme con una situación en la que nunca había pensado, entré en pánico y comencé a pensar." with dissolve
    " “Mm, esto de las idols, sigo creyendo que es una buena idea. Digo, soy una chica. Tengo fe de que mientras siga intentándolo, puedo convertirme en idol ♡”." with dissolve
    "Pero sí... no había pensado bien en todo eso de la escritura de canciones." with dissolve
    voice "audio/VoiceHonoka/004.mp3"
    K_Honoka "Haaa." with dissolve
    "Suspiré sin pensar. ¡Oh no!" with dissolve
    "Cada que suspiras se escapa una parte de tu felicidad. ¿Lo sabían?" with dissolve
    "Mi abuela siempre me dice eso, desde que era pequeña. ¡Por eso las chicas no deben suspirar así!" with dissolve
    "También tienes que alegrar a la gente a tu alrededor." with dissolve
    "Comencé a pensar otra vez…" with dissolve
    "Tal vez ser idol escolar es más difícil de lo que creí." with dissolve
    "Puede que haya subestimado todo esto." with dissolve
    "Mientras pensaba, tomé un manjuu para sacudir mi mente. El manjuu preferido de la tienda Homura, manjuu frito." with dissolve
    "Lo metí en mi boca y comencé a masticar. Y entonces…" with dissolve
    play sound idea noloop
    "¡Tiiin~♪!" with dissolve
    "¡Ya sé! ¡Tengo una idea!" with dissolve
    "En momentos como este, debes de aprender de gente con más experiencia, ¿no es verdad?" with dissolve
    scene black with dissolve
    $ renpy.pause(1.5, hard = True)

    #CAMBIO DE LUGAR
    stop music fadeout 1.3
    scene homura with dissolve
    play sound street_ambient fadein 3.0 fadeout 2.5 loop
    "En cuanto se me ocurrió la idea, me alisté y salí de casa." with dissolve
    "Luego, caminé por 20 minutos." with dissolve
    scene utx with dissolve
    "Llegué a el teatro de {b}UTX{/b} en Akihabara." with dissolve
    "Ya todos conocen el lugar, ¿no?" with dissolve
    "Ya he hablado bastante sobre las idols escolares, pero las idols que se presentan aquí, en este teatro, son las verdaderas, únicas y originales idols escolares." with dissolve
    "La escuela UTX, en Akihabara, es un nuevo y gigante rascacielos construido mero en frente de la estación Akihabara, al mismo tiempo que la remodelaban." with dissolve
    "¡Guau! Cuando vi el lugar en persona, el gran tamaño es tan imponente, hasta me dio un cosquilleo en la panza." with dissolve
    "Aunque construyeron esta preparatoria hace poco, llamó la atención de muchas estudiantes con todo su lujo y abundantes recursos y ya ganó bastante renombre como escuela aquí." with dissolve
    "Es el ejemplo del espíritu innovador de Akihabara, con esas enormes pantallas de propaganda frente a los edificios y las estudiantes yendo y viniendo se siente tan... digital." with dissolve
    "Con tan sólo verlo, uno puede notar el contraste con Otonoki. Todas las chicas en Otonoki son... pues... tranquilas y amables." with dissolve
    "¿Y cuál es la diferencia? Ah, hay muchas chicas con lentes. ¿Quizás sea eso? ¿O quizás sean esos elegantes uniformes que las hacen lucir tan bien?" with dissolve
    "Traté de olvidarme de esas cosas y seguí caminando." with dissolve
    scene utxCerca with dissolve
    play music A_RISETheme fadein 2.0 fadeout 2.5 loop
    "Ahí vi a un montón de gente reunida en la entrada del segundo piso del enorme edificio." with dissolve
    "Ahí se encuentra la entrada al teatro." with dissolve
    "Sobre la entrada, pintada de negro como en las discos, hay un letrero, igual al de los cines. Alumbrado con muchas luces." with dissolve
    voice "audio/VoiceHonoka/007.mp3"
    K_Honoka "Guau..." with dissolve
    "Un sonido salió de mi boca. Ay, abuelita, ese fue un sonido de admiración, no un suspiro, ¿okey? No voy a rendirme tan fácilmente…" with dissolve
    voice "audio/VoiceHonoka/006.mp3"
    K_Honoka "Sí que es bastante increíble... " with dissolve
    "El tamaño de aquel letrero era imponente." with dissolve
    "Justo frente a mí, vi a tres chicas." with dissolve
    scene arisePoster with dissolve
    "Se trataba del brillante grupo de idol escolares, {color=#1a94b8}A-RISE{/color}, se dice que son las #1 tanto en talento como en popularidad." with dissolve
    "Las tres integrantes: {color=#ffd966}Anju Yuuki{/color}, {color=#cc0000}Tsubasa Kira{/color} y {color=#b6d7a8}Erena Toudou{/color}." with dissolve
    "Se dice que el Departamento de Artes Escénicas es el mayor atractivo de la escuela UTX, pero sólo los que logren pasar las audiciones pueden unirse a A-RISE." with dissolve
    "Este grupo ha ganado dos veces el torneo anual de idol escolares, {color=#E4007F}Love Live!{/color}" with dissolve
    "Apenas y salen en la tele (no sé bien, pero me parece que es parte de una \"estrategia\"...)" with dissolve
    "sin embargo, las llamativas presentaciones que dan en el teatro, casi diarias, son de lo más impresionantes." with dissolve
    "Dicen que son más populares y talentosas que muchas idols profesionales." with dissolve
    "Y bueno, mientras que las integrantes de este grupo idol tienen que lidiar con horarios pesados de ensayos y prácticas todos los días, tampoco hay duda de que una vez que se gradúen podrían triunfar como verdaderas artistas de inmediato." with dissolve
    "Ya había escuchado de ellas, pero esa era la primera vez que iba a verlas en persona, lo que veía frente a mí me tenía sorprendida, estaba impactada." with dissolve
    scene utxCerca with dissolve
    "Un teatro bien equipado y carísimo, lleno de fans haciendo fila." with dissolve
    "Logré moverme hacia el frente para llegar a la taquilla." with dissolve
    "En el anuncio, vi que tenían dos presentaciones a diario." with dissolve
    "Ambas tenían un letrero que decía \"SOLD OUT\"" with dissolve
    "\"Sold out\"... significa que ya no hay boletos, ¿verdad? ¿Este bonito teatro se llena de gente todos los días...?" with dissolve
    "Ah, pero ya que todavía hay mucha gente, quizá ya no alcanzaron boleto, así que puede que esperen la devolución, o sólo desean poder ver a A-RISE cuando entren o salgan." with dissolve
    voice "audio/VoiceHonoka/004.mp3"
    K_Honoka "Haaa." with dissolve
    "Traté de contenerlo, pero… Al final, no pude evitar suspirar." with dissolve
    "Ellas son idols escolares. ¿De verdad?" with dissolve
    "Me dolía el pecho." with dissolve
    "Nunca imaginé que serían tan... tan increíbles." with dissolve
    "¿Quizas estaba soñando muy a lo grande?" with dissolve
    "Cuando lo veo de esa forma, ser idol escolar parece un sueño tan lejano como evitar que Otonoki cierre." with dissolve
    "Me siento un poco mareada." with dissolve
    "Por un segundo, me di la vuelta y comencé a alejarme. Aunque no suelo ser así." with dissolve  
    stop music fadeout 1.3
    scene mediodelCamino with dissolve
    "Y aunque siempre trato de evitar alejarme, siempre voy hacia adelante, de seguir avanzando." with dissolve
    "¡¡¡Aaaah, esta vez, mi rival es muy poderoso!!!" with vpunch
    "El enorme rascacielos de UTX imponía demasiado." with dissolve
    "Y es tan diferente del viejo, aburrido y poco colorido edificio de Otonoki." with dissolve
    scene arisePoster with dissolve
    "Las chicas de A-RISE de aquella foto eran tan diferentes a nosotras." with dissolve
    "La gente de este lado de Akihabara es muy diferente a la gente del lado de Otonoki." with dissolve
    "Me dolía el pecho, estaba triste." with dissolve
    "¿Es eso lo que todos quieren?" with dissolve
    scene mediodelCamino with dissolve
    "Aunque todavía quiero a Otonoki." with dissolve
    scene estacion with dissolve
    "Paso a paso. Sumergida en mis pensamientos, comencé a caminar a casa." with dissolve
    "Debí haber apretado los dientes en algún punto, empecé a sentir que me dolía la boca un poco." with dissolve
    voice "audio/VoiceHonoka/008.mp3"
    K_Honoka "¿Qué... estoy haciendo?" with dissolve
    voice "audio/VoiceUmi/002.mp3"
    S_Umi "¿Así que aquí andabas, Honoka?" with dissolve
    voice "audio/VoiceKotori/004.mp3"
    M_Kotori "Ah, qué bien. Fuimos a Homura porque queríamos enseñarte algo, pero no estabas ahí." with dissolve
    show KotoriM at KotOtoki with dissolve
    show UmiS at UmiOtoki with dissolve
    "De repente aparecieron Umi-chan y Kotori-chan." with dissolve
    "Mis amigas y compañeras de clase." with dissolve
    "Y también son las primeras que se unieron al grupo de μ's." with dissolve
    voice "audio/VoiceHonoka/009.mp3"
    K_Honoka "A-ah, perdón. Estaba comprando frente a la estación." with dissolve
    "Mientras respondia, Kotori me interrumpe." with dissolve
    voice "audio/VoiceKotori/005.mp3"
    M_Kotori "Mira, checa esto. Es el nuevo número de esta revista idol, y habla sobre idol escolares. Viene una historia sobre un nuevo grupo de Okayama." with dissolve
    voice "audio/VoiceHonoka/010.mp3"
    K_Honoka "¿Eh? Déjame ver." with dissolve
    "No quería que vieran mi rostro, así que hundí de prisa la cabeza en la revista." with dissolve
    "Pude sentir la mirada de Umi-chan, mis mejillas empezaron a sonrojarse." with dissolve
    "Había una foto en la revista de Kotori-chan." with dissolve
    play sound hoja noloop
    scene revistaIdols with dissolve
    play sound street_ambient fadein 3.0 fadeout 2.5 loop
    "Era una montaña, rodeada de áreas verdes." with dissolve 
    "Paradas cerca del agua de un arrozal, había 4 chicas con minifalda y debajo de ella llevaban pants y botas." with dissolve
    "¡¿E-estas son idols escolares?!" with dissolve
    "Junto a ellas, había un texto:" with dissolve
    "\"Daremos lo mejor como idols escolares, para tener el mejor recuerdo final\"." with dissolve
    voice "audio/VoiceKotori/006.mp3"
    M_Kotori "La escuela a la que van esas chicas se unirá con otra. Desaparecerá pronto, pero como la población en las montañas ha decrecido, ya todos aceptaron el hecho de que no pueden evitar el cierre." with dissolve
    voice "audio/VoiceKotori/007.mp3"
    M_Kotori "Así que hasta que eso pase, serán idols escolares como prueba de que estudiaron ahí juntas..." with dissolve
    "No podía hablar." with dissolve
    voice "audio/VoiceKotori/008.mp3"
    M_Kotori "Hay más chicas como nosotras, ¿verdad?" with dissolve
    voice "audio/VoiceHonoka/011.mp3"
    K_Honoka "S-sí." with dissolve
    voice "audio/VoiceKotori/009.mp3" 
    M_Kotori "Nos ayuda a darnos cuenta de que tenemos que esforzarnos, ¡¿verdad?!"with dissolve
    voice "audio/VoiceHonoka/011.mp3"
    K_Honoka "Sí... " with dissolve
    "Apenas puedo responder." with dissolve
    voice "audio/VoiceUmi/003.mp3"
    S_Umi "Pero no vamos a permitir que eso pase, ¿verdad, Honoka?" with dissolve
    "Era la voz de Umi-chan, tranquila y refinada." with dissolve
    play audio cerrarRevista noloop
    "Umi-chan tomó la revista de las manos de Kotori-chan y la cerró." with dissolve
    scene estacion with dissolve
    show KotoriM at KotOtoki with dissolve
    show UmiS at UmiOtoki with dissolve
    voice "audio/VoiceKotori/010.mp3"
    M_Kotori "¡Oye, todavía no marcaba la página!" with dissolve
    "Umi-chan me miró a los ojos, ignorando el grito de Kotori-chan." with dissolve
    voice "audio/VoiceUmi/004.mp3"
    S_Umi "Nosotras no vamos a probar que Otonoki existió, nosotras hacemos esto por el futuro de Otonoki." with dissolve
    "Mi cuerpo se estremeció con las palabras de Umi-chan." with dissolve
    voice "audio/VoiceHonoka/012.mp3"
    K_Honoka "S-sí, tienes razón. Es eso..." with dissolve
    "Mientras hablaba, sentí que algo se acumulaba dentro de mí." with dissolve
    voice "audio/VoiceHonoka/013.mp3"
    play music motivationalLL fadein 3.0 fadeout 2.5 loop
    K_Honoka "Es eso... sí. Me rehúso a que este sea nuestro último recuerdo de Otonoki." with dissolve
    scene utx with dissolve
    "La imagen de UTX cruzó mi mente, pero ya no tenía miedo." with dissolve
    voice "audio/VoiceHonoka/014.mp3"
    scene estacion with dissolve
    show KotoriM at KotOtoki with dissolve
    show UmiS at UmiOtoki with dissolve
    K_Honoka "No importa lo que otras escuelas hagan. ¡Nosotras vamos a lograr lo imposible!" with dissolve
    "Pude pronunciar esas palabras cuando vi a Umi-chan y Kotori-chan frente a mí." with dissolve
    "La tímida y débil Honoka había desaparecido antes de que me diera cuenta." with dissolve
    "Gracias, chicas. Tener aliadas te hace fuerte, ¿cierto?" with dissolve
    "Y en verdad tengo que devolverle el favor al vecindario y a la preparatoria Otonokizaka por haberme bendecido con tan buenas amigas." with dissolve
    voice "audio/VoiceUmi/005.mp3"
    S_Umi "Ya que estamos aquí y es fin de semana, ¿qué les parece si tenemos una pequeña asamblea? Hay muchas otras idols escolares en la revista que Kotori compró. Me sorprendió la cantidad." with dissolve
    voice "audio/VoiceKotori/011.mp3"
    M_Kotori "Oh, por favor, Umi-chan, ¿asamblea? Llamemos esto una reunión O últimamente la palabra bureast se ha puesto de moda. Como sea, sería genial si un día apareciéramos en una de esas revistas." with dissolve
    voice "audio/VoiceKotori/012.mp3"
    M_Kotori "¿También podríamos anunciarnos como chicas que desean evitar el cierre de su escuela?" with dissolve
    voice "audio/VoiceKotori/013.mp3" 
    M_Kotori "Mm, pero entonces la gente sabrá que la escuela cierra y a nadie le interesaría aplicar…" with dissolve
    "Kotori-chan seguía hablando con su dulce voz y yo comencé a pensar en esa foto de la revista." with dissolve
    scene cielo with dissolve
    "La montaña y el prado verde. El arrozal." with dissolve
    "Y, en medio de la foto, las chicas sonreían con toda la alegría del mundo." with dissolve
    "Idols escolares." with dissolve
    "¡Oigan, chicas de la preparatoria Kashiyama Minami en Okiyama!" with dissolve
    "¡En esa foto, con sus botas y minifalda, en el arrozal, creo que se veían tan lindas y llamativas como las de UTX!" with dissolve
    "Así que, vamos a esforzarnos como idols escolares." with dissolve
    "Daré lo mejor, y de verdad, de veeeeeerdad que salvaré la escuela." with dissolve
    "No podemos rendirnos." with dissolve
    "Aunque sea triste y doloroso, sin importar lo que pase, debemos seguir siendo idols sonrientes y transmitir nuestra energía a la gente." with dissolve
    "Aunque no tengamos medios, ni dinero, ni contactos, ni salón de club, tampoco canción original, somos idols escolares." with dissolve
    "Todo libro comienza con una hoja en blanco, ¿verdad?" with dissolve
    "Juro que de ahora en adelante, haré todo lo que pueda, y me esforzaré mucho como idol escolar." with dissolve
    "Supongo que debemos empezar con una canción o el salón del club, ¿no?" with dissolve
    "Hablaremos al respecto." with dissolve
    "¡Voy a dar lo mejor!" with dissolve
    stop music fadeout 1.3
    stop sound fadeout 1.3
    $ quick_menu = False 
    scene black with fade

    #COMENTARIOS FINALES DE UMI
    play music coments fadein 0.8 fadeout 0.5
    scene TUmi with dissolve
    $ renpy.pause(2.0, hard = False) 
    scene comentarioUmi1 with dissolve
    $ renpy.pause(9.0, hard = False) 
    scene black with fade
    stop music fadeout 1.0
    jump cap3Honoka

#COMIENZO DEL CAPITULO 3
label cap3Honoka:
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo3 with fade
    $ renpy.pause(3.0, hard= True)
    

    scene black with dissolve
    $ quick_menu = True
    "¡Auch, auch, auch!" with dissolve 
    "¡Ay, ya no puedo seguir!" with dissolve 
    play music home fadein 3.0 fadeout 2.5 loop
    scene HomuraCocina with dissolve
    voice "audio/VoiceHonoka/015.mp3"
    K_Honoka "¡¿Dónde están las compresas frías?!" with dissolve 
    "Saqué una compresa del refrigerador, la puse en mi pantorrilla, y…" with dissolve 
    "¡Aah! ¡Arde! ¡Qué dolor! ¡Arde mucho!" with dissolve 
    show KousakaYukiho at top with dissolve
    K_Yukiho "¡¿Podrías callarte, hermana?!" with dissolve 
    "Mi hermana Yukiho se asomó por el pasillo al oírme gritar." with dissolve  
    K_Yukiho "¡Si vas a hacer eso, hazlo en tu habitación! Y además, si te duelen los músculos por copiar esos bailes, ¿no significa que te hace falta hacer ejercicio?" with dissolve 
    K_Yukiho "Si no tienes cuidado puede que termines subiendo de peso. Tenemos una tienda de manjuu, eh, ¡así que siempre hay que comer en esta casa!" with dissolve 
    "Yukiho miró la mesa, notando el plato lleno de rebanadas de castella." with dissolve 
    "¡Agh, eran sobras que tomé del mostrador para comerlas después!" with dissolve 
    "Se burló cuando traté de esconderlas y luego regresó a su habitación." with dissolve 
    hide KousakaYukiho with dissolve
    "¡Qué grosera!" with vpunch
    "Dios, y pensar que hace poco era una niñita, siempre me andaba siguiendo, \"hermana, hermana, hermana\"." with dissolve 
    "¿A dónde se fue esa linda Yukiho?" with dissolve 
    "Sin pensarlo volví a presionar la compresa y... ¡Ay! ¡Todavía arde!" with dissolve 
    "Jaa. Esto va mal, ¿verdad? ¿Será que pueda participar mañana en la práctica? A pesar de lo que piense Yukiho, no estoy sólo copiando los bailes. La práctica de hoy fue bastante difícil." with dissolve 
    "Siguiendo la sugerencia de Umi-chan, una atlética chica que forma parte del club de kendo y arquería, ayer comenzamos con el ejercicio." with dissolve 
    "4 repeticiones de 20 sentadillas, 4 repeticiones de 10 lagartijas, 50 vueltas corriendo en las escaleras del templo, 100 levantamientos de rodilla y mucho más." with dissolve
    "¡Honestamente, pareciera que somos más bien un club deportivo que uno de idols! Estoy segura de que si no hicimos saltos fue porque a Umi-chan se le olvidó." with dissolve 
    "Cielos, tendré que ingeniármelas para que a Umi-chan no se le ocurra hacerlo mañana." with dissolve 
    "Y así, hoy me di cuenta de que los ensayos de las idols son más difíciles de lo que habíamos imaginado." with dissolve 
    scene miembros2 with dissolve
    "Primero, sólo éramos mis amigas y compañeras, Kotori-chan y Umi-chan; luego se unieron las chicas de primer año." with dissolve 
    scene miembros5 with dissolve
    "Hanayo-chan, Maki-chan y Rin-chan (con habilidades para componer música); y después" with dissolve 
    scene miembros6 with dissolve
    "Nico-chan también se unió; ¡y muchas cosas más pasaron!" with dissolve 
    "Pero ahora, siento que µ's comienza a lucir como un verdadero grupo idol." with dissolve 
    "Después de todo, es mejor que haber empezado ya con un grupo de amigas, si lo hacemos así, obtendremos nuevas y emocionantes experiencias, también aprenderemos de los talentos de Maki en la composición." with dissolve 
    "Y cuando se trata de grupos de idols, es mucho mejor tener diferentes tipos de chicas que puedan brillar de varias formas, ¿no?" with dissolve 
    scene HomuraCocina with dissolve
    "¡En lo personal, cuando se trata de pasteles, preferiría comer 10 piezas de 10 pasteles diferentes que un pastel entero de un solo sabor!" with dissolve 
    "De hecho, cuando veo por el aparador de la pastelería, me emociono tanto que no puedo escoger uno." with dissolve 
    "Pastel de fresa es la opción típica, y claro, a todos le gustan los pay de queso y pastel de chocolate, así que también debemos comer de esos, y el mousse de frambuesa, si es temporada, también hay pastel de mango." with dissolve 
    "Y aunque es simple, el dulce sabor de la tarta de almendra es difícil de resistir, me gustaría un petisú relleno de natilla, y un crujiente milhojas, cielos, babeo sólo de pensarlo." with dissolve 
    "Nom♡" with dissolve 
    "Por eso quiero que μ's sea un grupo colorido, que esté lleno de tonos y sabores, como una brillante caja de pasteles." with dissolve 
    scene presentacionUmi with dissolve
    "Ahora, el grupo está compuesto por: Umi-chan, con su gran conocimiento en arquería y poesía en la secundaria, se encarga de las letras y el ejercicio." with dissolve 
    scene presentacionKotori with dissolve
    "Y, nuestra otra chica de segundo, la amante del cosplay, Kotori-chan, a cargo del diseño de ropa y accesorios." with dissolve 
    scene presentacionHana with dissolve
    $ renpy.pause(1.0, hard=True)
    scene presentacionNico with dissolve
    "Luego, como Hanayo-chan, de primer año y Nico-chan, de tercero, siempre han amado y sabido mucho sobre idols, ellas están a cargo de las coreografías y la propaganda (aunque toda sea vía internet)." with dissolve 
    scene presentacionRin with dissolve
    "Rin-chan, de primer año, por ser parte del club de atletismo y tener buena condición, es la instructora." with dissolve 
    scene presentacionMaki with dissolve
    "Y Maki-chan, de primero, una chica rica que sabe tocar el piano desde pequeña, se encarga de componer." with dissolve  
    scene HomuraCocina with dissolve
    "Mm, ya que lo pienso, debí de haber invertido tiempo en aprender algo en lugar de andar jugando cuando salía de la primaria." with dissolve 
    "Todas estas chicas normales tienen talentos, y yo sólo dependo de ellas en todo." with dissolve 
    scene presentacionHono with dissolve
    "Siento que soy una inútil... Así que, la deprimida Honoka está a cargo de armar el horario." with dissolve 
    "Me siento mal porque técnicamente cualquier persona podría hacerlo, pero yo soy la que creó a μ's, así que de momento yo soy la líder y el centro." with dissolve 
    "De hecho, las demás son mucho mejor en esto, y esto no lo es mío." with dissolve 
    "Oh, bueno ♡" with dissolve 
    "Quizás cuando me pongo en el medio, las otras resaltan más ♪" with dissolve 
    scene HomuraCocina with dissolve
    "Después de todo, Maki una vez dijo, \"yo nunca pensé en volverme idol, pero ya que empezaron ustedes, por alguna razón, sentí que también podría hacerlo.\"" with dissolve 
    "¿No es verdad? ♪ La típica imagen de una idol no es la de una belleza extravagante, como una modelo, sino más bien una chica linda que siempre sonríe e irradia energía, ¿no?" with dissolve 
    "¡Así que hasta una chica normal como yo, podría tratar de lograrlo!" with dissolve 
    "Mm, sí, ¡muy bien! ¡En eso me convertiré, en una idol al alcance de todos! ¡O más bien, una idol que quieras apoyar, como tu compañera de clase!" with dissolve 
    "Ah, ese fue un lema que pensó Hanayo-chan." with dissolve 
    "Pero Nico-chan lo rechazó de inmediato, porque era \"¡Muy simple!\"" with dissolve  
    "A mí me había gustado." with dissolve 
    "Por supuesto, queremos convertirnos en idols famosas, pero a decir verdad, siento que \"ser la chica que se sienta junto a ti en clase\" nos queda mejor." with dissolve 
    "A veces, viene un simple pudin dentro de esas coloridas cajas de pasteles, ¿no?" with dissolve 
    "Y ese pudin puede volverse muy popular, ¿no?" with dissolve 
    "Cuando papá traía regalos, siempre compraba dos pudines. Mi hermana y yo nos regocijábamos \"¡Hurra, pudin! Y nos compraste para las dos ♪\"" with dissolve 
    "Y mi papá respondía, \"¡Claro que sí, el pudin es barato!\"" with dissolve 
    "Sin embargo, la \“compañera de clase\" Honoka, de la tienda de dulces Homura, tiene calambres ahora." with dissolve 
    "Agh, qué mal, si me sentaba, ya no podría pararme." with dissolve 
    "Mañana volveremos a ensayar, ¿podré hacerlo?" with dissolve 
    "¿Qué pasa si no puedo bailar y alguien toma mi lugar en el centro?" with dissolve 
    "No me importa ser o no el centro, pero cambiar de lugar significa más trabajo para las demás." with dissolve 
    "Todas tienen sus responsabilidades además del ensayo." with dissolve 
    "Ya soy bastante inútil, no puedo causar más problemas y faltar al ensayo por unos simples calambres." with dissolve 
    "¡Claro que no!" with dissolve 
    "¡Bien, debo esforzarme más!" with dissolve 
    "Sólo un poquito más y luego descansaré. Y mañana practicaré más. De esa forma, si alguien tiene dudas sobre la coreografía, seré una buena líder y les mostraré cómo se hace." with dissolve 
    "Sí, esa es la tarea de la que va en el centro, ¿no?" with dissolve 
    "Aunque sea temporal, soy el tipo de persona que tiene que esforzarse siempre. ¡Me gusta dar lo mejor!" with dissolve 
    "Ese era mi talento desde pequeña. Mi alegría y energía son mis más grandes virtudes, no importa qué pase, nunca me rindo, nunca me detengo." with dissolve 
    "La gente dirá que en verdad me gusta esforzarme. Practicaré." with dissolve 
    "Me aprenderé de memoria la coreografía. Tal como ahora, ¿no?" with dissolve  
    "Muy bien, ahí voy. Un, dos, tres y cuatro…" with dissolve 
    stop music fadeout 0.8
    scene black with fade
    "Después de eso, estaba flotando." with dissolve 
    "Bailaba en un sueño." with dissolve 
    "Mis adoloridos pies se sentían ligeros, como si tuviera alas y, en mi sueño, mis movimientos eran mucho mejores ♡." with dissolve 
    "¡Mis giros y saltos eran perfectos!" with dissolve 
    "Guau, ¿todas me dirán que hice un buen trabajo?" with dissolve 
    "¡Oigan, chicas! ¡Yo también me estoy esforzando!" with dissolve 
    $ quick_menu = False
    scene black with fade 
    $ renpy.pause(5.0, hard=True)
    
    # SIGUIENTE DIA
    scene cuarto_Honoka with dissolve
    $ quick_menu = True
    "Cuando desperté, mi futón olía a pura compresa fría." with dissolve 
    "Por la ventana entraba la luz de la maña..." with dissolve 
    voice "audio/VoiceHonoka/016.mp3"
    K_Honoka "¡Ay no!" with dissolve 
    "¿Me quedé dormida?" with dissolve 
    "¡No tenía tiempo de ordenar la tienda como cada mañana!" with dissolve 
    "Esperen un segundo." with dissolve 
    scene HomuraInside with dissolve
    play music home fadein 3.0 fadeout 2.5 loop
    "Bajé las escaleras y grité" with dissolve 
    voice "audio/VoiceHonoka/017.mp3"
    K_Honoka "¡Mamaaaa! ¡¿Por qué estaba durmiendo en mi habitación?! Recuerdo que llegué de la escuela ayer y me puse una compresa fría pero..." with dissolve 
    K_Yukiho "Ah, ya despertaste. ¿No te acuerdas?" with dissolve 
    "Yukiho, que ya estaba desayunando, me respondió." with dissolve 
    show KousakaYukiho at top with dissolve
    K_Yukiho "Te quedaste dormida ahí mismo en la sala, sin siquiera acabarte la castella, así que me desperté y te llevé a tu habitación. Hasta dijiste que no querías cenar." with dissolve 
    K_Yukiho "Debías estar muy cansada, creo. Tenías la expresión de un bebé somnoliento." with dissolve 
    K_Yukiho "¿Sirvió la compresa? Escuché que te dieron calambres, lo más adecuado es esperar a que pase. Dormir fue la mejor opción." with dissolve 
    "¡Oh, tenía razón! ¡Ya me sentía mucho mejor!" with dissolve 
    voice "audio/VoiceHonoka/018.mp3"
    K_Honoka "Muy bien, ya estoy lista para el ensayo de hoy ♪" with dissolve 
    "Entonces mi estómago gruñó." with dissolve 
    K_Yukiho "Pfff. Tenía mucho que no actuabas así. Cuando eras más chica, jugabas hasta cansarte y te quedabas dormida en la noche. Cuando te despertabas al día siguiente, hacías un escándalo y te comías un tazón de arroz." with dissolve 
    voice "audio/VoiceHonoka/008.mp3"
    K_Honoka "¿Eh? ¿En serio? Es un poco vergonzoso, ah... jajajaja" with dissolve 
    hide KousakaYukiho with dissolve
    "Haciendo memoria, tenía razón." with dissolve 
    "Apenas y recuerdo." with dissolve 
    "De niña, me sumergía completamente en los juegos." with dissolve 
    "Corría por ahí hasta que anochecía, sin pararme a comer algo. Me daba hambre hasta que regresaba a casa, pero entonces, estaba tan cansada, que sólo me recostaba en los cojines de los sillones de la sala y ahí me dormía." with dissolve 
    "La diferencia es que en aquel entonces, papá me llevaba a mi habitación." with dissolve 
    show KousakaYukiho at top with dissolve
    K_Yukiho "En verdad estás sumergida en esto de las idols, ¿no?" with dissolve
    voice "audio/VoiceHonoka/011.mp3" 
    K_Honoka "S-sí, supongo" with dissolve 
    "Yukiho me miró con seriedad, como si estuviera sorprendida." with dissolve 
    "Me daba pena. Ah... jajajajaja." with dissolve 
    "¡Ah, rayos, la gente va a empezar a decir otra vez que no saben quién es la hermana mayor!" with dissolve 
    "Bueno, da igual." with dissolve 
    hide KousakaYukiho with dissolve 
    "¡Aaah! ¡En verdad me voy a esforzar en la práctica de hoy!" with dissolve  
    "Soy la líder después de todo ♡" with dissolve 
    "Siento que hoy estoy llena de energía ♪" with dissolve 
    "¡Voy a bailar, bailar y bailar para demostrarles a todas como se hace!" with dissolve 
    voice "audio/VoiceHonoka/musicstart.mp3"
    "μ's, music... start!" with dissolve
    stop music fadeout 1.3
    $ quick_menu = False 
    scene black with fade

    #COMENTARIOS FINALES DE MAKI
    play music coments fadein 0.8 fadeout 0.5
    scene TMaki with dissolve
    $ renpy.pause(2.0, hard = False) 
    scene comentarioMaki1 with dissolve
    $ renpy.pause(9.0, hard = False)
    scene black with fade
    stop music fadeout 1.0 
    jump cap4Honoka

#COMIENZO DEL CAPITULO 4
label cap4Honoka:
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo4 with fade
    $ renpy.pause(3.0, hard= True)

    $ quick_menu = True

    S_Umi "¿Honoka, tu hombro no se moja?" with dissolve
    K_Honoka "No, estoy bien... Además, lo más importante es que nuestras cosas no se mojen." with dissolve
    "Caminaba bajo el paraguas color aguamarina que Umi-chan sostenía." with dissolve
    "ĺbamos hombro a hombro, sosteniendo la maleta justo frente a mí y asegurándome de que no se empapara." with dissolve
    "Gota, gota." with dissolve
    "Caían una gran cantidad de gotas." with dissolve
    "La mochila era tan grande que no podía sostenerla entre mis brazos, debido a eso se me resbalaba." with dissolve
    "Escuchaba que su contenido se agitaba." with dissolve
    K_Honoka "¿Segura que esto va a funcionar? La ropa y los pompones no deben mojarse." with dissolve
    S_Umi "¿Deberíamos correr?" with dissolve
    K_Honoka "Muy bien" with dissolve
    "Le respondí, y comenzamos a correr." with dissolve
    "Sólo un poco más y llegamos a la entrada de mi casa, la tienda de dulces Homura." with dissolve
    S_Umi "Ja... ja... fiu, parece que lo logramos." with dissolve
    K_Honoka "Sí. Gracias, Umi-chan. La próxima vez, si está nublado, ¡me aseguraré de llevar mi paraguas!" with dissolve
    S_Umi "Ninguna de nosotras espera que preveas tantas cosas. Estoy segura de que llevas el paraguas un día que no llueve, y luego se te olvida y entonces lo pierdes. Además, ni siquiera ves el estado del tiempo, ¿o sí?" with dissolve
    "Ay... Tenía razón." with dissolve
    "Antes de que pudiera contestarle, Umi-chan añadió:" with dissolve 
    S_Umi "Tu especialidad es tener la fuerza suficiente para llevar esa maleta enorme tú sola. Con esa ayuda tenemos suficiente. Y luego de eso, se fue a casa." with dissolve
    "Auch, eso no fue un cumplido, Umi-chan." with dissolve
    K_Honoka "Ya llegué." with dissolve
    "Entré a mi casa y suspiré. Una vez en mi cuarto, me eché un vistazo" with dissolve
    "Rayos, mi uniforme estaba empapado. De prisa, busqué una toalla y sequé mi uniforme y cabello." with dissolve
    "Me quité la ropa rápidamente, que sólo estaba mojada del lado derecho, y la colgué." with dissolve
    K_Honoka "Ay no, debía asegurarme de que la maleta... ¡fiu!" with dissolve
    "¡Los trajes, las cintas brillantes para el decorado del escenario, los pompones y todo lo demás estaban secos!" with dissolve
    "¡Y todo gracias a mí ♡! Ajá. ¿Ya ves, Umi-chan?" with dissolve
    "Tengo algo más que súper fuerza ♪" with dissolve
    "Pero, ¿quizá pueda secarlos con algo? No están mojados, pero sí se sienten algo húmedos, y no quiero que vayan a oler feo al secarse solos, pensé al momento de sacarlos de la maleta." with dissolve
    K_Honoka "¡Cielos, hay tantas cosas aquí!" with dissolve
    "No pude evitar gritar al ver que mi habitación desaparecía con tanta ropa y accesorios." with dissolve
    K_Honoka "En serio, ¿por qué debemos llevar y traer todas estas cosas de la escuela todo el tiempo? ¡¡Ojala tuviéramos un salón propio!!" with dissolve
    "Nuestras actividades de hoy duraron sólo como 30 minutos, así que no hay mucho que decir." with dissolve
    "Hoy, nuestro plan era preparar todo para el concierto que tenemos planeado para justo antes de las vacaciones de verano; revisar los trajes y discutir sobre el escenario y efectos, pero justo cuando teníamos todo nuestro equipo listo, comenzó a llover y todo se fastidió." with dissolve
    K_Honoka "¡Aah, de prisa! ¡Alcen todo antes de que se moje!" with dissolve
    "Cuando le pregunté a Umi-chan quién traía un paraguas, me dijo que el estado del tiempo decía que a lo mejor Ilovía en la tarde, pero yo estaba muy ocupada desayunando y ayudando en la tienda como para enterarme." with dissolve
    "Me sorprendió ver esas gototas caer del cielo tan repentinamente." with dissolve
    "Es cierto que el cielo estaba gris justo cuando terminaba el receso, y que el viento frío insinuaba que se avecinaba una tormenta, pero no pensé que en verdad Ilovería." with dissolve
    "De hecho, ni siquiera me puse a pensar en eso." with dissolve
    "Después de todo, era el tan esperado día en el que íbamos a decidir todo para nuestra presentación." with dissolve
    "Kotori-chan llevó los trajes, Rin-chan y Hanayo-chan llevaron la decoración, Umi-chan trajo las bocinas para probar el sonido, ya saben." with dissolve
    "Durante varias de las reuniones, poco a poco llevábamos nuestras cosas." with dissolve
    "Antes de darnos cuenta, ya teníamos muchas cosas listas, pero hoy, decidimos juntar todo lo necesario y terminar con nuestra práctica de baile." with dissolve
    "Toda la mañana estuve emocionada ya que hoy era el gran día que por fin íbamos a ensayar para el gran concierto, pero todo se echó a perder debido a la lluvia." with dissolve
    "Digo, nuestro espacio es el techo de la escuela, la parte más expuesta del lugar." with dissolve
    "Si llueve, no podemos realizar nuestras actividades, y sin permiso no podemos usar los salones (hace poco, Rin-chandijo que no habría problema, así que ocupamos un salón vacío, pero la maestra se enojó mucho cuando nos descubrió, jejeje)." with dissolve
    "Sip. Ahora mismo, u's es un grupo idol cualquiera, así que notenemos horarios ni establecimiento, y tampoco tenemos supervisor ni presupuesto." with dissolve
    "¡Aaaaaah, me gustaría que por lo menos tuviéramos un lugar donde poner nuestras cosas!" with dissolve
    "Ahora, les pregunto:¿Qué creen que deberíamos hacer para conseguir un salón propio?" with dissolve
    "¡Usaré este diario para pedirles su opinión!" with dissolve
    "¡Lo primero que pienso es que debemos hacer que u's sea un club oficial!" with dissolve
    "Aunque siento que eso será muy complicado." with dissolve
    "¡Lo siguiente es conseguir a una supervisora para el club! Muy buena idea, ¿no?" with dissolve
    "Si conseguimos una supervisora, será más fácilpedir permiso para usar un salón, y podríamos usar su espacio para guardar nuestras cosas." with dissolve
    "¿Verdad? ¿Verdad que sí es una buena idea?" with dissolve
    "¿Alguien conoce a alguna buena maestra?" with dissolve
    "Por cierto, los salones de música o ciencias parecen lugares perfectos para guardar nuestras cosas, así que estaría bien una profesora de ciencias o de música…" with dissolve
    "Aunque Nakajima, la maestra de música, no sería una buena idea. Ya es supervisora del club de música, así que no tendría tiempo." with dissolve
    "Honjou, la maestra de ciencias, me da un poco de miedo y no le hablo mucho. ¿Alguno de ustedes, sí?" with dissolve
    "El otro día quemé un mechero de alcohol, así que no creo que pueda ir yo... Ejeje, lamento no ser de mucha ayuda ♡" with dissolve
    "Waaaah, en ese caso, lo mejor sería que juntáramos más integrantes y nos volviéramos un club oficial, ¿no?" with dissolve
    "Eso también suena complicado, de todas formas, debemos triunfar como grupo, para que cuando la gente nos vea, piensen \"¡Yo también quiero participar!\"." with dissolve
    "¡Si no logramos eso, entonces no podemos llamarnos idols!" with dissolve
    "Y nunca podremos mostrarle al mundo lo maravilloso que es u's y atraer más estudiantes." with dissolve
    "¡Muy bien, está decidido!" with dissolve
    "¡A partir de mañana, voy a reclutar más integrantes para poder conseguir un salón!" with dissolve
    "Y para eso, tendremos que brillar y volvernos grandes idols para que la gente nos admire, ¡así que practicaré mucho más!" with dissolve
    "Dios, aún así…" with dissolve
    "Mientras escribía esto, la lluvia arreció afuera. Puede que no podamos practicar mañana." with dissolve
    "¡Aaah, de verdad quiero tener un salón propio!" with dissolve
    
    # COMENTARIOS FINALES DE UMI

#COMIENZO DEL CAPITULO 5
label cap5Honoka:
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo5 with fade
    $ renpy.pause(3.0, hard= True)

    $ quick_menu = True

    "Mañana tendremos nuestro primer concierto." with dissolve
    "Ah, siendo honesta, cuando digo \"primer\", en realidad no me refiero al verdadero, verdadero, primer concierto." with dissolve
    "Bueno, desde que hicimos µ's en abril, hemos realizado bastantes actividades escolares" with dissolve
    "Pero ahora tenemos a Eli y a Nozomi, de tercer año, con nosotras, y pronto tendremos nuestro primer evento escolar con las nueve integrantes de µ's." with dissolve
    "Y, de hecho, nos invitaron a hacerlo." with dissolve
    "Ejeje, cielos, estoy tan feliz, ¡muero de la emoción!" with dissolve
    "Cuando me acuerdo de nuestro primer concierto, incluso ahora, hace que mi corazón lata con fuerza, aunque fue un concierto trágico al que no fue nadie..." with dissolve
    "Pero ya hemos crecido desde entonces. Ahora somos nueve en total y ya tenemos algunas canciones originales." with dissolve
    "Sip, eso demuestra que mientras sigas peleando y nunca te rindas, entonces tus sueños se pueden volver realidad, ¿no es así?" with dissolve 
    "Ahora, por fin, ¡el consejo estudiantil nos pidió que diéramos un concierto! ¡Ejem!" with dissolve
    "Ah... aunque la petición viene de parte del consejo, y la presidente es una de nuestras integrantes, así que es como si nos estuviéramos invitando nosotras mismas." with dissolve
    "De todas formas, durante la Golden Week, cuando mi abuela me dijo que quería que me encargara del evento del Día del Niño frente a nuestra tienda Homura (en donde vendemos nuestros productos), eso fue... de hecho, no tienen nada que ver con esto, ¿verdad?" with dissolve
    "Cuando mi abuela me comentó eso mientras comía golosinas con Umi-chan, estábamos tan sorprendidas que casi no atragantamos. Ejeje ♪" with dissolve
    "¡Así que estoy súper emocionada por esto!" with dissolve
    "Espero que este evento sea un gran éxito y nos inviten a participar en otros." with dissolve
    "Asi subiriamos más videos y nos conocería más gente." with dissolve
    "¡Todas en u's nos llenaríamos de motivación!" with dissolve
    "Así que, aunque sólo estamos usando nuestras \"conexiones\"(como Maki lo llama), ¡estamos felices de que Eli nos esté apoyando! Aunque ya hayamos tenido nuestro debut como idols escolares, todavía nos falta mucho." with dissolve
    "¡Debemos aprovechar todas las oportunidades que tengamos!" with dissolve
    "¡Dios, sabía que reclutar a la presidente del consejo estudiantil era una grandiosa idea! ¡Tener preferencia es increíble! ♪" with dissolve
    "Sólo bromeo, ejejeje ✰" with dissolve

    #Paso de dia

    "Eh, pues... hoy nos estamos encargando de los preparativos para mañana." with dissolve
    "Y el evento es... ¡La apertura de la piscina!" with dissolve
    "Cielos, es algo \"muy de idol\", ¿no? " with dissolve
    "Normalmente, el consejo estudiantil junta a un grupo de voluntarios para abrir la piscina después de la escuela, así que no tenemos invitados de fuera y tampoco vienen muchos estudiantes... " with dissolve
    "Por supuesto, esto está lejos de ser el Festival cultural o la feria deportiva o alguno de esos eventos." with dissolve
    "Pero así podemos mostrarnos un poco más ante el público, y considero que tener la oportunidad de grabar un video en frente de la piscina nos dará buena publicidad durante el verano ✰" with dissolve
    "También voy a la piscina del parque de diversiones durante las vacaciones, pero los fines de semana, siempre hay algún espectáculo de superhéroes o idols." with dissolve
    "¡Idols bailando en trajes de baño con un escenario especial cerca de la piscina y música estruendosa!" with dissolve
    "Y siempre veo todo eso mientras disfruto un rico raspado." with dissolve
    "Sip. Era lo que algunas de nosotras quería usar para este evento. Y cuando digo \"algunas\", me refiero en realidad a Nico-chan ♪" with dissolve
    "Pero tuvimos un problema con eso, como ¿estaría bien que usáramos trajes de baño en la escuela?" with dissolve
    "¿El consejo no se enojaría con nosotras?" with dissolve
    "Además, Umi-chan se rehusó fervientemente." with dissolve
    "Al final, Kotori-chan dijo que no había mucho tiempo y que no podría hacer los trajes para todas, así que descartamos la idea." with dissolve
    "Una pena, pero así son las cosas." with dissolve
    "Los trajes de baño serán para la próxima. Digo, no es como que no me averguenza la idea de usar traje de baño... pero aún así..." with dissolve
    "Soy una idol ♪" with dissolve
    "Cuando es verano, tienes que lucir un lindo traje de baño, ¿no? Espero poder hacerlo una vez que empiecen las vacaciones ♡" with dissolve
    "Pero si, antes de darme de cuenta, ya era junio. Una hoja más en el calendario y ya son vacaciones de verano." with dissolve
    "¿A dónde se fue el tiempo? Si que vuela, ¿no? Ups, ¿estoy hablando con viejita otra vez?" with dissolve
    "¡Rayos, Umi-chan se va a enojar conmigo por no actuar como una idol! ¡No dije eso!" with dissolve
    "¡Para nada! Finjamos que no ha pasado nada, ¿de acuerdo? ♡" with dissolve
    "Como decía, eh... nuestra piscina en Otonokizaka es, por supuesto, una piscina al aire libre abierta a todo público." with dissolve
    "¡Me encaaaaaanta nadar! Tomé clases de natación cuando era niña, así que se me da muy bien ♪" with dissolve
    "Las piscinas techadas son bonitas y las puedes usar cuando sea, pero la verdadera magia de la piscina es poder jugar con tus amigos y chapotear por todos lados bajo los rayos del sol y el vasto cielo veraniego, y ¡ese momento en el que puedes zambullirte sin preocupaciones!" with dissolve
    "¿Saben de lo que hablo?" with dissolve
    "Es un poco gracioso como usamos todos esos trajes de baño infantiles." with dissolve
    "¡Así es como empieza mi época favorita del año!" with dissolve
    "Al parecer, cada año, por estas fechas, Otonoki hace una ceremonia de apertura para antes de que empiecen las clases de natación." with dissolve
    "Hasta ahora, el consejo estudiantil había reunido voluntarios, pero para ser honesta, yo nunca he sabido que hacen... esta será mi primera vez." with dissolve
    "Parece ser que rezan para que todo salga bien, dejan que la gente use la piscina un rato, juegan bingo y otras cosas parecidas." with dissolve
    "Me siento mal por enterarme de todo esto hasta ahora que la escuela está a punto de cerrar." with dissolve
    "Creo que si la gente se interesara más en nuestra escuela, no estaríamos en esta situación en primer lugar, así que nos esforzaremos mucho para este evento, y les mostraremos otra gran cosa que tiene Otonoki." with dissolve
    "Es casi un sueño que la gente venga a vernos a la ceremonia de apertura. Más bien, debemos convertirnos en ese grupo que atrae a mucha gente." with dissolve
    "¡Me voy a esforzar!" with dissolve
    "Así que, fui a la piscina." with dissolve

    #Cambio Escenario
    "Guau, ¡¿pero qué?!"  #revisar
    "La transparente agua, brillante bajo el sol veraniego, no estaba." with dissolve
    "En su lugar, había una repugnante sustancia verde. Parecía un contenedor de laboratorio." with dissolve
    "Podía imaginar sapos viviendo ahí."
    K_Honoka "¿Q-qué es esto, Eli? ¡Nuestra piscina se volvió un pantano!" with dissolve
    "Eli se encontraba cerca de la orilla, estirando las piernas." with dissolve
    A_Eli "Ah, llegaste. Justo ahora estamos drenando el agua. Ten cuidado, ¿de acuerdo?" with dissolve
    "El sonido del agua se escuchaba cerca de los pies de Eli." with dissolve
    "Por ahí se estaba drenando. ¡lug, sería horrible si me tragara!" with dissolve
    K_Honoka "Lamento llegar antes. Supongo que me emocioné mucho. No me di cuenta de que aún la estaban limpiando. Vendré después de..." with dissolve
    N_Maki "Espero no tardáramos mu- Vaya, ¡¿qué rayos?! ¡¿Es un estanque?!" with dissolve
    H_Rin "Es como pescar en el hielo ✰" with dissolve
    K_Hanayo "Ohh, quizás haya una carpa ♡" with dissolve
    "Llegaron las tres de primer año, Maki-chan, Rin-chan y Hanayo-chan, respectivamente." with dissolve
    "Por supuesto, también las sorprendió el estado de la piscina." with dissolve
    "Yo tampoco sabía de esto, pero la piscina queda llena de agua y nadie la toca durante el invierno, y pronto, hay tanto musgo y algas que ya no puedes ni ver el fondo." with dissolve
    "Admito que en verdad parecía que vivian peces ahí..." with dissolve
    "Eli miró su reloj y comentó" with dissolve
    A_Eli "no vinieron temprano. De hecho, apenas tenemos tiempo, así que sino empezamos ya no nos va a dar tiempo. ¿Dónde están las otras tre... " with dissolve
    S_Umi "Lo siento, me tocaba arreglar el salón de clases hoy..." with dissolve
    M_Kotori "Yo también tenía que limpiar." with dissolve
    "Umi-chan y Kotori-chan llegaron, jadeaban por venir corriendo. Sus rostros sonrojados mostraban un poco pena." with dissolve
    "Oh, no hay ningún problema. Se lo están tomando muy en serio. Supongo que estaban emocionadas por el gran evento..." with dissolve
    Y_Nico " Nico nii, nico nii, nico nico nii ♪ ¡La hada de la piscina, Nico-nii, ha llegado! ¡Hola, chicas! ¿Me estaban esperando?" with dissolve
    "Detras de nosotras llego Nicho-chan, su voz era más radiante que el sol. Saltó... y...oh, ¡ya llevaba puesto su traje! ¿Eh? ¿Acaso teniamos ensayo" with dissolve
    "Cuando Nico-chan iba a posar, Eli la sujetó de los brazos y la mantuvo en su lugar, llamando su atención." with dissolve
    A_Eli "Si, me preguntaba cuánto te ibas a tardar, Hadita. Ahora, primero lo primero, quítate esa ropa. ¿Pueden encargarse de esto rápido?" with dissolve
    "¿Eh? ¿Eeeehh"
    "Al darse la vuelta, Eli tenía una expresión seria y nosotras estábamos muy confundidas."
    "Al mismo tiempo, la puerta del almacén se abrió de par en par."
    all "Ah, Nozomi"
    "Era Nozomi."
    T_Nozomi "Ya todas están presentes, eh ¡Manos a la obra, chicas!"
    "Llevaba un montón de palos con pelo verde. Y varios cepillos."
    all "¡¿Queeeeé?!"
    "Gritamos al unisono. Umi-chan suspiró."
    "Un momento, ¡¿se suponía que limpiaríamos la piscina para el evento de mañana?!"


    T_Nozomi "Es más rápido cuando trabajamos todas juntas, ¿no?"
    "Comentó Nozomi mientras limpiaba su frente."
    "Las chicas y yo, tras habernos puesto nuestro uniforme deportivo, restregábamos el suelo."
    A_Eli "Lo siento. Al parecer no tuvimos dinero para contratar a quien limpiara, y cuando intentamos que las estudiantes ayudaran, nadie quiso. Y pues, ya que J's iba a dar su concierto aquí, pensé que podríamos encargarnos."
    "Añadió Eli con una sonrisa incómoda mientras juntaba todo el musgo."
    Y_Nico "iSi, claro! ¡Ya lo tenias planeado! Traté tantas veces de advertirles sobre Elichika y sus maléficas intenciones, pero..."
    "Rin-chan sostuvo la escoba de Nico-chan y trató de calmarla."
    H_Rin "Pues está bien, alguien tiene que hacerlo ♡ Yo me estoy divirtiendo. No todos los días puedes hacer esto, ¿verdad? Anda, mirame patinar en mi escoba por todo el piso de la pisci- "
    K_Hanayo "¡Rin-chan, ten cuidado!"
    "Rin-chan corrió, resbaló y cayó antes de que Hanayo-chan pudiera detenerla. Cayó al suelo de lleno, y siguió deslizandose hasta llegar al otro lado de la piscina."
    H_Rin "Tejeje... ¡Rin-chan gana el primer lugar en Deslizamiento a gran velocidad!"
    N_Maki "Agh, está bien, ¡ya no importa este desastre! ¡Puedes dejarlo todo y limpiarlo con tu cuerpo!"
    "Cuando Maki-chan está con Rin-chan y Hanayo-chan, pareciera convertirse en su madre."
    K_Honoka "Pfff"
    "El pensarlo me hizo reir."
    N_Maki "¿Qué te causa gracia, Honoka?"
    K_Honoka "Perdón, no me estoy riendo de ustedes, ¿de acuerdo?"


    "Es sólo que el que estemos limpiando así me hace sentir como si fuéramos idols de segunda, jeje."
    "Con eso en mente, miré al cielo."
    "Creo que esto no está tan mal. Si."
    "El sudor recorrió desde mi oreja hasta mi cuello."
    "Bajo este vasto cielo azul. El verano se acerca."
    "Mañana vamos a cantar junto a esta piscina."
    "No sé cuánta gente vendrá a vernos, pero quiero limpiar esta piscina como agradecimiento."
    "Ya que esta será una presentación importante para u's."
    "Daremos un paso más adelante."
    "Así es. Deberíamos estar agradecidas de poder cantar aquí. Y, para nuestra escuela, nuestra Otonoki, lo siento, no sabía que la piscina necesitaba de todo este cuidado."
    "Alguien más se dedicó a hacerlo, para que nosotraS pudiéramos disfrutarla."
    "Al ver a la presidente del consejo estudiantil, Eli, fregando con toda su fuerza, pienso ser la presidente del consejo no se trata sólo de privilegios, sino también de esforzarse al máximo, ¿verdad?"
    "¡Muy bien, yo también me esforzaré!"
    "¡Quizá no pueda lograr lo que Eli, pero daré todo de mi parte en el evento de mañana!"
    "Y para eso..."
    "¡Hoy tengo que lavar el suelo de la piscina!"
    "Le eché un vistazo, por lo menos la mitad ya estaba limpia."
    "Me sentí abrumada, ¡pero no rendirme es mi estilo de vida!"
    "De ahora en adelante, ¡me llenaré de energía y me esforzaré más!"
    "Aaaah, ¿y qué pasará mañana si no terminamos de limpiar hoy?"
    "Me rasqué la nariz, y me embarré de musgo la cara, dejandome un bigote verde."
    "Nico-chan me tomó una foto, ¿quizá podamos enseñarla en el concierto de mañana?"
    "¡Si quieren verla, deben ir al concierto de apertura de la piscina!"
    "Debería usarla como publicidad."
    "Ah, ojalá mañana sea un día soleado y despejado."
    "Para que podamos pararnos bajo ese cielo, en la piscina que nosotras mismas limpiamos, y podamos dar nuestro primer concierto como un grupo de nueve."
    "Ay no, pensar en eso hace que me emocione, ¡no voy a poder dormir!"
    K_Honoka "Uuuaaahhh..."
    "El trabajo físico te agota, ¡¿verdad?!"
    "¡Manana voy a darlo todo!"

    # COMENTARIOS FINALES DE ELI

#COMIENZO DEL CAPITULO 6
label cap6Honoka:
    stop music fadeout 0.8
    voice "audio/VoiceHonoka/IkkuyoHonoka.mp3"
    scene capitulo6 with fade
    $ renpy.pause(3.0, hard= True)

    $ quick_menu = True
    K_Honoka "Como que nadie viene, ¿no?"
    M_Kotori "Como que no..."
    "Estaba sentada junto a Kotori-chan, en un escritorio que tenía el letrero \"Inscripciones\"."
    "Pude notar el espacio vacio frente a nuestra mesa en donde se suponía que debía de haber una fila."
    "Era una tarde alegre de junio. El viento soplaba y meneaba los árboles."
    M_Kotori "¿Quizás escogimos un mal lugar?"
    K_Honoka "Quizas..."
    "Estabamos detras del gimnasio."
    "Hay un arbol enorme, una alfombra de flores y una hermosa vista de la ciudad, desde la cima de Otonokizaka."
    "Escogí este lugar porque pensé que sería perfecto para la sesión fotográfica..."
    "Ah, algo frío cayó sobre mi cabeza."
    M_Kotori "¿Oh, va a empezar a llover?"
    K_Honoka "Si, va a llover..."
    "Mientras Kotori-chan sólo repetía lo que le decía, miré al cielo, había una ligera luz tras ese montón de nubes... pic pic."
    "Cuando vi la lluvia caer desde aquellas nubes grises, me quedé boquiabierta."
    M_Kotori "¿Ow, deberíamos dejarlo por hoy?"
    "Decepcionada, miré a la libreta que estaba sobre el escritorio."
    "Sip, todavía en blanco..."
    "Era de esperarse, supongo... Llevamos esperando aquí desde que las clases terminaron, pero al final, nadie se apareció."
    "En la libreta, estaba el ejemplo que escribi, fue un desperdicio:"
    #CARTA
    M_Kotori "Aquí nos vamos a mojar. ¿Nos quitamos?"
    "La voz de Kotori-chan me hizo reaccionar, y comenzamos a mover el escritorio hacia la entrada del gimnasio."
    "Kotori-chan dijo que todavía faltaba para que oscureciera y que la lluvia podría parar, así que decidimos esperar un poco más."
    "A pesar de eso..."
    M_Kotori "Nadie viene, ¿no?"
    K_Honoka "Nop, nadie viene..."
    "Tenemos un largo camino por recorrer."
    "¿Así serán las sesiones fotográficas de las idols?"

    #RECUERDO
    Y_Nico "¡Toda idol de verdad debe tener sesiones fotográficas!"
    "Fue lo que dijo Nico-chan un día durante nuestro descanso de la práctica."
    K_Honoka "¿Sesión fotográfica? ¿Y eso qué es? ¿Que nos tomemos fotos grupales? Aunque yo sólo tengo la cámara de mi celular..."
    "Le respondí y Nico-chan ladeó la cabeza."
    Y_Nico "¡Ah, Honoka, tú nunca me decepcionas! Ni siquiera sabes que es una sesión fotografica, pequeñina"
    "En ese momento comenzó a estrujar mi cabeza con sus nudillos."
    "¡Aaaah, otra vez quedé como una tonta!"
    "Y entonces, ¿qué es una \"sesión fotográfica\"? ¿Algún término técnico de la industria?"
    "Según lo que Nico-chan explicó en las \"sesiones fotográficas de idols\" no tomamos fotos de nada, al parecer los fans se reúnen en un estudio y nos toman fotos."
    "Ya veo. En ese caso, no importa si tengo o no cámara."
    "Las idols son mucho más que sólo cantar y dar conciertos, ¿verdad?"
    "Según Nico-chan, las idols rentan estudios y realizan este tipo de eventos muy a menudo."
    "¡No por nada es la detective #1! ¡Nico-chan sabe lo suyo!"
    "Pero, somos idols escolares. O más bien, todavía nos falta mucho, mucho, muchísimo para que nos convirtamos en idols escolares, ¡¿cCómo se supone que rentemos un estudio para tener una sesión de fotos?!"
    "Ni siquiera sé donde podríamos encontrar esos estudios."
    "Tampoco puedo imaginarme cómo se hacen esas sesiones."
    "¿Cómo le hacemos?"
    "¿Y saben lo que dijo Nico-chan?"
    Y_Nico "¡Todavía tenemos mucho, mucho, mucho por aprender como idols, en cuanto a canto, baile, fama y popularidad! Básicamente, tenemos tantas, tantas, tantas cosas en las que trabajar..."
    "No creo que fuera necesario que dijera \"mucho\” y \"tantas\" varias veces..."
    Y_Nico "Ahora que Maki es parte del club, ya pudimos comenzar a trabajar en canciones originales, y hemos practicado en nuestra coreografía"
    Y_Nico "También tuvimos una lluvia de ideas, y para ser honesta, tenemos suerte de que todas seamos atléticas, ¡así que tenemos buena destreza para ser un grupo recién nacido!"
    Y_Nico "Lo único en lo que tenemos que trabajar es en ganar más fama y popularidad. ¡En especifico, debemos trabajar en la fotogenia!"
    H_Rin "¿Fotogenia? ¿Es alguna especie de comida?"
    "Nico-chan la señaló con el dedo, interrumpiéndola."
    Y_Nico "¡Oye tú! ¿Ni siquiera sabes qué significa fotogenia? ¡Por gente como tú es que el mundo está lleno de chicas que sólo saben hacer el simbolo de la paz cuando les toman fotos!"
    "¿E-está hablando de mi? Ah... jajajaja... ♡"
    Y_Nico "La palabra \"fotogenia\" se refiere a lo bien que te ves cuando te toman fotos. Ya saben de lo que hablo, ¿no?"
    Y_Nico "De esas chicas que en persona no tienen nada de especial, pero que salen súper lindas en las fotos, que se ven muy bien en selfies, o que su foto de perfil no se parece nada a ellas etc etc... "
    "Mmmm... Todas voltearon a ver a Nico-chan."
    Y_Nico "O-oigan, vamos, ¿qué están mirando? Ya sé que soy súper lista y linda, ¡pero es vergonzoso cuando me miran así!"
    "No creo que eso fuera lo que queríamos insinuar... Da igual ♡"
    K_Honoka "Tienes razón. Aún nos ponemos nerviosas cuando nos toman fotos, ¿no es así? "
    K_Honoka "Por costumbre hago el simbolo de la paz, y ya lo he pensado desde el día que lo comentaste, pero no estoy segura de si mi cara se ve mejor del lado izquierdo o del derecho."
    "Al parecer, al igual que tenemos un brazo y ojo dominante, también tenemos un lado dominante de la cara."
    Y_Nico "Oh, no sólo se trata de eso, ¿sabes? Si quieres ser una idol, debes saber sobre técnicas gravure."
    Y_Nico "En esas revistas que están llenas de fotos de idols lindas, con las mejillas sonrojadas."
    "Aah, se refiere a las fotos en trajes de baño."
    Y_Nico "No sólo se ponen los trajes de baño para lucir su pecho.Todas trabajan en detalles."
    Y_Nico "Tienen que asegurarse que su cabello baile con el viento, que las cortinas les luzcan bien, y que abran la boca de tal forma que luzcan seductoras..."
    "¡Oh, Nico-chan se acercó a mi con la boca entreabierta!"
    "¡Aay, qué traviesa!"
    Y_Nico "¿Vieron? ¡Las idols tienen que ser capaces de hacer eso todo el tiempo! Si siempre posan como si estuvieran tomando fotos de recuerdo, ju's no tendrá futuro!"
    "Entiendo. ¡Tenemos que practicar de tal forma que nos salga natural en todo momento!"
    "Y asi, recordamos y aprendimos de nuestros errores."
    "Cuando alguien nos pide una foto, en automático hacemos el signo de la paz, y nos ponemos tan tiesas que nuestras expresiones no se ven naturales."
    "Además, todo esto de posar, nunca lo habíamos considerado."
    "¡Muy bien, en ese caso!"
    K_Honoka "Oigan, ¿creen que podamos hacer, pues, nuestra versión de esa cosa de la sesión fotográfica o algo así?"
    "Los ojos de Nico-chan brillaron en cuanto me escuchó decir eso, Kotori-chan y Umi-chan suspiraron y miraron al cielo."
    "Pero si hay algo que nos intrigue, ¡tenemos que investigarlo!"
    "Ese es nuestro estilo, ¿no?"

    #FIN RECUERDO
    M_Kotori "Creo... que no debimos organizar la sesión de fotos en una tarde de entre semana... "
    K_Honoka "Si, y luego de entregar todos esos volantes..."
    "Kotori-chan y yo seguíamos a cargo del escritorio (que se había mojado un poco)."
    "Veiamos con desinterés cómo caia la lluvia."
    "Decidimos esperar a que pasaran los últimos 30 minutos antes de que cerraran la escuela."
    "¡Hello! ¿Ya terminó la sesión de fotos?"
    "Pude escuchar una voz a la distancia."
    "El rostro de Kotori-chan se iluminó y luego... se apagó."
    M_Kotori "¡Bienvenidos! Nuestro cliente de hoy es... ¡¿Rin-chan?! ¡¿Y Hanayo-chan?!"
    H_Rin "Nos preguntábamos como les iba, así que decidimos venir"
    H_Rin "Y bueno, ¿cómo va el negocio? ¿Tuvieron muchos clientes? ¿Tomaron muchas fotos? ¡No puedo esperar a que llegue mi turno!"
    "Kotori-chan sonrió de forma forzada."
    K_Honoka "Nada. ¿Tal vez nos precipitamos un poco? No hemos logrado nada."
    M_Kotori "Justo hablábamos de que quizás deberíamos dejarlo por ho-"
    H_Rin "¿En serio? Qué mal, ¡pero no hay problema!"
    H_Rin "Pensé que esto pasaría, ¡así que traje esto!"
    "En esto, sacó una cámara réflex."
    K_Honoka "¡Guau, se ve tan profesional! ¡¿De dónde la sacaste?!"
    H_Rin " Es un cachivache de mi papá ♡ Una sesión de fotos no es nada si nadie toma fotos, ¿no? No sé si es hacer trampa, pero decidí que me aparecería si no venía ningún cliente."
    K_Hanayo "Yo también. Posar y todo eso me da algo de vergúenza, pero puedo tomar fotos sin problemas. Como fan de las idols, creo que me será más fácil hacerla de fotógrafa."
    "Hanayo-chan habló con timidez."
    "Y luego, detrás de ellas... ¡Nico-chan apareció!"
    Y_Nico "Y no lo olviden, yo vine a entrenarlas. Por lo menos, hasta que lleguen clientes. De lo contrario, sólo estarán sentadas allí sin hacer nada, ¿cierto?"
    Y_Nico "¡Déjenme enseñarles lo básico sobre posar! ¡Así que, primero vayan a ponerse el traje porrista!"
    H_Rin "¿Eh? Mejor me pongo mi ropa deportiva que ese traje de porrista ♪ Me gusta la ropa casual, sabes."
    K_Hanayo "Este... creo que sólo deberíamos ponernos nuestro vestuario de conciertos. Creo que a nuestros fans les encantara vernos de cerca..."
    Y_Nico "¿En serio? Siento que ya todos están acostumbrados a ver a Honoka y Kotori disfrazadas. Por lo que las porristas serian..."
    "Las tres comenzaron una animada discusion."
    H_Rin "Cielos, hoy sólo seremos fotógrafas, ¡así que no importa cómo nos vayan a ver!"
    H_Rin "Ya sé, ¿qué te parece si nos vestimos y tomamos turnos para tomarnos fotos?"
    Y_Nico "¡Oh, esa es una buen idea!"
    Y_Nico "Me pondré el traje de porrista ♡ debo decir que me veo mucho mejor cuando me toman fotos que cuando las tomo ♡."
    K_Hanayo "Y yo sólo voy a tomar fotos, como ya lo había planeado."
    H_Rin "¡Y ustedes pueden tomarme fotos mientras tomo fotos en ropa deportiva!"
    "¿Eh, cómo que \"ustedes\"? pensé y me asomé detrás de Rin-chan."
    N_Maki "Bueno, no llego tarde, ¿verdad? Hasta traje mi cámara y todo ♪"
    T_Nozomi "Y con mi cámara instantánea, puedo autografiar las fotos en el mismo momento"
    "También llegó Nozomi-chan."
    "Maki-chan y Nozomi-chan se veían muy emocionadas al respecto, y detrás de ellas llegaron Umi-chan y Eli-chan, ¡ambas se veían de mal humor!"
    "Antes de darnos cuenta, ya había parado la lluvia."
    "Kotori-chan tenía razón. Iba a dejar de llover."
    "Después, tuvimos una gran sesión de fotos con y's, sin clientes ♡"
    "Nozomi-chan había traído varios trajes: de sacerdotisa, trajes de baño, de sirvientas y uniformes de voleibol."
    "No estoy segura de lo que tramaba, pero Kotori-chan, la amante del cosplay se emocionó y todas se divirtieron, así que no hay problema."
    "Nico-chan hasta nos enseñó como posar correctamente."
    "No tiene nada de malo que, de vez en cuando, nos tomemos el día libre y en vez de ensayar nos relajemos asi."
    "Ah, y no se preocupen, Nico-chan va a subir todas las fotos a internet, ¡así que esto cuenta como actividades de p's!"
    "Espero que mucha gente las vea."
    "¡Vamos a ver quién gana teniendo más visitas!"
    "Por favor, sigan apoyándonos ♡♡"

    # COMENTARIOS FINALES DE NICO

#COMIENZO DEL CAPITULO 7
label cap7Honoka:
    K_Honoka "¡Ya llegué!"
    "¡Fiu, la práctica de hoy fue larga! ¡Estoy agotada!"
    "Aunque los días son más largos al acercarse el verano, uno se sigue cansando cuando las prácticas terminan hasta tarde."
    "Abrí la puerta de la tienda con mucha fuerza."
    "Oh no, hice mucho ruido."
    "Mamá se va a enojar conmigo."
    K_Honoka "¡P-perdón, no medí mi fuerza! Ya vi-"
    "Asomé la cabeza y eché un vistazo al mostrador. ¿Eh?"
    "No había nadie."
    "Ni clientes tampoco. Pero normalmente, mi mamá o Yukiho, mi hermana menor, están aquí. ¿Entonces, por qué no había gente?"
    "Vi el reloj, eran las 6:23 PM."
    "Dios, eso es peligroso. Todavía faltaban 30 minutos para cerrar."
    K_Honoka "No me culpen a mi si entra un ladrón y se lleva lo que sobra de manjuu, ¿okey?"
    "Murmuré al mismo tiempo que tomaba algunos del mostrador"
    "Nom"
    "¡Mm, esa sal y azucar era lo que mi cuerpo cansado necesitaba!"
    "Tarareando, pasé por el mostrador, justo al fondo de la tienda, allí hay una escalera que dirige al segundo piso."
    "Ahí comienza la residencia de la familia Kousaka."
    "De hecho, se supone que no debo pasar por aqui."
    "En realidad debo dar la vuelta en la esquina de la tienda y usar la entrada de la casa. Pero es mucho esfuerzo ir hasta atrás de la tienda cuando simplemente puedo pasar por aquí, así que casi siempre entró por la tienda."
    "Además, el área justo a la entrada de la casa es el espacio donde se cocina, así que hay restos de azúcar, harina, sal, y casi no se puede andar."
    "En serio, aunque mamá y papá siempre nos dicen a mi y a Yukkii que debemos ordenar nuestros cuartos, su área de trabajo siempre está desordenada, a veces ese polvo llega hasta la mitad de la casa."
    "Aún así... Cuando me quejo con la abuela, sólo me responde:"
    "\"Asi es la vida de los niños cuya familia tiene negocio. Todo ese desorden es lo que nos da de comer.\""
    "Bueno, mi familia administra esta tienda desde antes de que naciera."
    "Cuando era niña (e incluso ahora ♡), siempre me decian que era la imagen de la tienda Homura, como si fuera un hecho real."
    "Cuando estaba en preescolar, sólo tenía que balbucear \"¡Bienvenido!\" al entrar a la tienda y todos me felicitarían."
    "Las viejitas del vecindario me halagarían y dirían que era muy linda."
    "Por supuesto que me gustaba."
    "Mi hermana Yukiho y yo jugábamos a que éramos las dueñas del negocio, y por mucho tiempo me sentí como la verdadera imagen de la tienda."
    "Pero"
    "Aún así..."
    "Días como estos siempre me ponen a pensar."

    "Hoy al mediodia, cuando todavia estaba en la escuela"
    "La quinta y sexta hora de clase, eran mis clases electivas: Arte y Caligrafia."
    "En arte, seguiamos trabajando en la naturaleza muerta, y en caligrafia, todavía estábamos en el grabado, como llevabamos haciendo desde hace tiempo."
    "Aún teníamos tiempo para la fecha límite de entrega, así que tuve una tarde relajada y tranquila."
    "¿Tal vez fue por eso?"
    "Al parecer la maestra también quería hacer algo, y me llamó para dar orientación."
    "Era la orientación que decidieron hacer tras haber anunciado el cierre de la preparatoria Otonokizaka."
    "Agh, sólo con decirlo me pongo triste. Fiu."
    "Recuerdan que en abril nos avisaron que la escuela iba a cerrar, ¿verdad?"
    "Aunque la escuela insistió que no cerraría hasta que todas las estudiantes se graduaran, parece que algunas familias Se preocuparon sobre el futuro de sus hijas"
    "Se puede entender, muchas de las de primer año dijeron que querían cambiarse."
    "Así que decidieron dar orientación a las chicas, para entender lo que deseaba cada una de nosotras."
    "En esas reuniones, te preguntan qué quieres hacer en el futuro. Si quieres quedarte en la escuela o no."
    "Si no quieres, ¿entonces querrás una carta de recomendación o presentarás el examen para cambiarte de escuela?"
    "Si sí quieres, entonces ¿qué planeas hacer de ahora en adelante? Preguntan ese tipo de cosas."
    "En cuanto a mi..."
    "Por supuesto que me voy a quedar en la preparatoria Otonokizaka."
    "O mas bien dicho, ¡voy a esforzarme mucho con pu's para que Otonoki no tenga que cerrar!"
    "Así que pensé que esta orientación no era importante para mi."
    "Y cuando llegó mi turno, me senté frente a la profesora y me dijo..."
    maestra "¿Kousaka, planeas quedarte en Otonoki?"
    "La maestra me hizo pasar al frente del salón."
    K_Honoka "¡Sí! ¡Me voy a quedar hasta el final! ¡De hecho, mis amigas y yo vamos a pasar los siguientes dos años tratando de evitar que la escuela cierre!"
    maestra"Ah, cierto, eres la tercera de tu familia que asiste a Otonoki, ¿Verdad? "
    "Respondió la maestra con ironía mientras leia los papeles que tenía en sus manos"
    "¡Los manjuus de Homura son muy buenos! A veces los comemos en la sala de maestros."
    K_Honoka "Oh, muchas gracias ♪ ¿Hasta a los maestros les gusta? Qué bueno escucharlo."
    maestra "¿Y también serás la tercera en heredar el negocio familiar? No, espera, la tienda parece llevar mucho más tiempo. Mm, de acuerdo a la información, tienes una hermana menor, ¿verdad? "
    maestra "Estudia el tercer año de secundaria. Un par de hermanas, ¿eh? ¿Eso significa que alguna de las dos se va a casar y su esposo ayudara con el negocio?"
    "¡¿E-esposo?! Comencé a sentirme muy incómoda"
    maestra "Mm, lamento no ser de mucha ayuda, pero no recuerdo haber escuchado que alguna alumna vaya a estudiar reposteria."
    maestra "¿Hay alguna escuela especializada en eso aqui? ¿O tu esposo se encargará de eso mientras que tú te enfocas en la administración?"
    maestra "Si es así, entonces tendrás que estudiar una carrera técnica o ir a la universidad, y no ir a una escuela especializada. ¿Ya has hablado con tus padres al respecto? ¿O tienes algún otro plan en mente? Escuché que comenzaste un nuevo club hace poco..."
    "Eh, eh, eh, eh... ¿de qué estaba hablando?"
    "Yo no he..."
    "Todas estas cosas me pusieron de cabeza."
    "Estaba boquiabierta."
    "Quizas la maestra entendió al ver mi aspecto."
    maestra "Bien, pues... la orientación como tal se llevara a cabo en otoño, ¢si? Tal vez podamos dejarlo pasar por ahora. Voy a poner que todavía estás pendiente, ¿de acuerdo?"
    K_Honoka "S-Si"
    "Apenas pude responder. La maestra me miró con seriedad."
    maestra "Aún asi, el otoño va a llegar en un abrir y cerrar de ojos, Kousaka."
    maestra "Me gusta lo alegre y animada que eres, pero ya estás en segundo año. Si no planeas ir a la universidad, creo que ya es momento de que pienses en tu futuro."
    "Pero..."
    "¿\"Ya estoy en segundo\"? ¡Más bien, a penas estoy en segundo ano!"
    "Justo ahora disfruto plenamente de mi juventud junto a y's, asi que pensé que todavía faltaba mucho para el futuro..."


    #Vuelta al presente
    K_Honoka "¡Ya llegué! ¿Hay alguien en casa? ¿Mamá? ¿Yukkii?"
    "Grité otra vez al entrar a la sala."
    "Parecía que no había nadie."
    "¿Habrán ido a hacer una entrega?"
    "Comencé a caminar a mi habitación mientras aflojaba el moño de mi uniforme, fue entonces que noté el sobre que estaba en la mesa."
    "Un gran sobre azul."
    "Al frente se podía ver que estaba dirigido a Yukiho Kousaka, del 3er año grupo A de la secundaria Otonokizaka."
    "En la parte de abajo del sobre, se veía el remitente junto a su logo impreso: Escuela Privada UTX."
    "Junto al sobre hay una hoja con letras rojas que decía: \"Información para estudiantes de nuevo ingreso\""
    "¡¡¡Aaaaaaah!!!"
    "¡¿P... p-p-p-p-por qué?!"
    "¡¿P-p-p-por qué a Yukkii?!"
    "¡¿Por qué Yukkii quiere entrar a UTX?!"
    K_Honoka "¡Mamá! ¡Mamá! ¡Mamáaaaa!"
    "Antes de darme cuenta ya andaba corriendo y gritando por toda la casa."
    K_Honoka "Oh por Dios, oh por dios, oh por dios. ¡Es Yukkii! Ella-"
    "Después de recorrer toda la casa, no encontré a nadie, así que terminé dando vueltas en la sala..."
    K_Honoka "¿Por qué? Nadie me dijo que Yukiho iba a ir a UTX... Y bueno, ¿ahora qué? Siempre hemos estado juntas. No puedo creer que lo esté considerando..."
    "Mientras seguía dando vueltas, me golpeé el pie con la mesa."
    "¡Aayy!"
    "La mesa hizo ruido y me cai... ayayayay"
    K_Honoka "Ay, mi pie... ¿Cómo pasó esto...?"
    "Me daban ganas de llorar y entonces..."
    K_Yukiho "Ah, por dios, ¿cómo puedes hacer tanto ruido cada vez que llegas a casa? Ni siquiera tengo que asomarme, ya sé que eres tú."
    K_Yukiho "Ya estás en preparatoria, ¿no? ¿Por qué no... te comportas un poco? A lo mejor así serías más popular, como Umi la del Dojo Sonoda..."
    "Era Yukiho. Pasó a la sala vistiendo ropa casual y secando su cabello con una toalla."
    K_Honoka "Yukiho..."
    "Sigue aquí. Todavía no se va a UTX. Ni yo puedo creer que haya exagerado tanto."
    "Sin tiempo que perder, traté de evitar que se me escurriera una lágrima, pero fue inútil."
    "Intenté secarla con mi dedo para que Yukiho no la viera caer por mi mejilla."
    K_Honoka "¿A-ah, estabas en el baño? Me sorprendí cuando llegué a casa y no había nadie."
    K_Yukiho "¿Y qué? ¿Pensaste que nos habías ido al País de las Maravillas o algo asi? No has cambiado nada desde preescolar, ¿o si?"
    K_Yukiho "¡Sigues siendo esa pobre niña que no soporta estar sola!" 
    "Con una mirada que decía \"¡No te pongas a llorar!\" Yukiho me dio su toalla."
    K_Honoka "G-gracias. Sudé bastante debido a la práctica de hoy, jejeje ☆ Mejor me doy un baño."
    "Me sentí un poco avergonzada, desvié la mirada."
    "Y entonces, recordé acerca del sobre de UTX."
    "Mi cuerpo se congeló. No estaba segura de que decir."
    "Así que no dije nada."
    "Y Yukiho también bajó la mirada, sin decir una palabra."
    "..."
    K_Honoka "Bueno..."
    K_Yukiho "Este..."
    "No pude evitar sonreir."
    K_Honoka "¡Hurra, te gané!"
    "Era un juego que inventamos cuando éramos niñas."
    "Sólo nosotras lo conociamos. Cuando las cosas se ponían incómodas entre nosotras, la primera en hablar ganaba."
    "Siempre hemos querido tener una fuerte conexión como hermanas. Porque hasta en los momentos más tristes y difíciles, queremos ser capaces de decir lo que sentimos."
    "Es como una promesa secreta, aunque nadie sabe cuando la hicimos exactamente."
    "Por cierto, hasta ahora, ¡voy ganando con mucha ventaja!"
    "Así de buena es una hermana mayor ♪ En la familia Kousaka, ser inteligente o ser deportista no es muy importante, ¡ser honesto y decir la verdad, sí! ¡Viva!"
    K_Yukiho "¡Ah, qué injusto! ¡TÚ siempre actúas por instinto!"
    "Yukiho parecía molesta, pero estaba sonriendo."
    "Fiu, es la Yukiho de siempre."
    K_Honoka "Bueno... Se trata de esto..."
    "Le mostré el sobre."
    K_Yukiho "Para que lo sepas, yo no fui a pedir uno de esos, ¿de acuerdo?"
    "Yukiho desvió la mirada, pero siguió hablando"
    K_Yukiho "En la mañana, nos llevaron a hacer una visita a una preparatoria. Ya sabes, esas que hacen cuando las niñas están por salir de secundaria."
    K_Yukiho "Nos llevaron a UTX y nos enseñaron cómo dan clases, vimos una presentación de A-RISE y nos dieron un montón de cosas. De verdad quieren que nos matriculemos."
    "Yukiho se sentó en la mesa y tomó una golosina, le quitó el celofán y comenzó a comerlo."
    "Cielos, y justo antes de cenar. Es raro que ella se comporte así."
    K_Yukiho "Esa escuela es tan impresionante como siempre dicen. Mira la guía. Hasta nos dieron un DVD de A-RISE y un llavero."
    "Con la golosina en la boca, Yukiho sacó el DVD para enseñármelo."
    "La miré y... Oh, era un llavero de Anju, qué lindo. Entonces recordé algo."
    K_Honoka "¿Oye, que no las visitas de la secundaria Otonokizaka siempre eran a la preparatoria Otonoki? ¿Por qué una escuela pública haría su visita a una escuela privada para niñas ricas como UTX?"
    K_Yukiho "Pues, Otonoki va a cerrar, ¿no?"
    "Agh. Se me hizo un nudo en la garganta."
    K_Yukiho "No quería decírtelo, pero para cuando yo vaya... o más bien, para cuando tenga tu edad esa preparatoria ya no va a existir."
    K_Yukiho "Los maestros en mi escuela dicen que ya es un hecho."
    "Imposible... Y si así fuera, Otonoki existe todavía."
    "Aún tenemos tres años para evitarlo."
    K_Yukiho "Si Otonoki no cerrara, todavía tendría la libertad de escoger, pero de hecho, la preparatoria ya no va a abrir inscripciones el año que entra, ¿o si?"
    K_Honoka "Eso... eso aun no lo han decidido"
    K_Yukiho "Si, pero dudo que alguien se vaya a inscribir sabiendo que no se van a poder graduar ahí. Ni yo haría algo tan tonto."
    "Yukiho no podía mirarme a la cara, desenvolvió otro bocadillo y comenzó a comerlo."
    "Era la primera vez que veia a Yukiho comportarse asi..."
    K_Honoka "¡Pues, todo va a estar bien, Yukkii! ¡u's y yo vamos a hacer todo lo posible para evitar que nuestra escuela cierre!"
    K_Honoka "No somos las únicas que deseamos salvarla. Todas son niñas bien portadas, simplemente se rinden muy rápido."
    K_Honoka "Estoy segura de que todos se pondrán contentos de saber que tú quieres matricularte ahí."
    "Asustada, fue lo único que se me ocurrió decir."
    





















# label UmiSono:
    # voice "audio/VoiceUmi/001.mp3"
   
