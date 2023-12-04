# El juego comienza aquí.
label splashscreen:
    $ op = renpy.random.randint(1, 2)
    if op == 1:
        image movie1 = Movie(channel="movie_dp", loop = False, play = "movie/Intro1.avi")
        show movie1 with dissolve
        #$ renpy.movie_cutscene("movie/Intro1.avi", loops=0, stop_music=True)
        $ renpy.pause(90.0, hard= False)
        hide movie1 with dissolve
        return
    else:
        image movie2 = Movie(channel="movie_dp", loop = False, play = "movie/Intro2.avi")
        show movie2 with dissolve
        # $ renpy.movie_cutscene("movie/Intro2.avi", loops=0, stop_music=True)
        $ renpy.pause(90.0, hard= False)
        hide movie2 with dissolve
        return


label start:
    #ELECCION DE RUTAS
    $ quick_menu = False
    stop music fadeout 0.8
    play music SongMenuSelect fadein 0.5 fadeout 0.5
    scene MenuElec with Dissolve(1.5)
    menu:  
        "QUE RUTA DESEAS LEER?"
        "Ruta de Honoka Kousaka":
            menu: 
                "QUE CAPITULO DESEAS"
                "CAPITULO 1 - HONOKA NO SE RENDIRÁ" : 
                    jump cap1Honoka
                "CAPITULO 2 - CONVIRTÁMONOS EN SCHOOL IDOLS" :
                    jump cap2Honoka
                "CAPITULO 3 - ¡BAILEMOS!":
                    jump cap3Honoka
                #"CAPITULO 4 - ":
                
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
    show HonokaPan at top with dissolve 
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
    show KousakaHonoka at top with dissolve
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

    show UmiS at UmiOtoki with dissolve
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
    show KousakaHonoka at top with dissolve
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
    $ renpy.movie_cutscene("movie/video1.avi", loops=0, stop_music=True)
    stop music
    "¡Espero que ese día llegue pronto!" with dissolve 
    voice "audio/VoiceHonoka/sleep.mp3"
    "Y con ese deseo, me iré a dormir esta noche." with dissolve 
    "¡Mañana practicaremos duro!" with dissolve 
    $ quick_menu = False 
    scene black with fade

    #COMENTARIOS FINALES DE KOTORI
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
    scene revistaIdols with dissolve
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
    K_Honoka "Es eso... sí. Me rehúso a que este sea nuestro último recuerdo de Otonoki." with dissolve
    play music motivationalLL fadein 3.0 fadeout 2.5 loop
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
    scene TUmi with dissolve
    $ renpy.pause(2.0, hard = False) 
    scene comentarioUmi1 with dissolve
    $ renpy.pause(9.0, hard = False) 
    scene black with fade
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
    #scene exercise with dissolve
    "Siguiendo la sugerencia de Umi-chan, una atlética chica que forma parte del club de kendo y arquería, ayer comenzamos con el ejercicio." with dissolve 
    "4 repeticiones de 20 sentadillas, 4 repeticiones de 10 lagartijas, 50 vueltas corriendo en las escaleras del templo, 100 levantamientos de rodilla y mucho más." with dissolve
    "¡Honestamente, pareciera que somos más bien un club deportivo que uno de idols! Estoy segura de que si no hicimos saltos fue porque a Umi-chan se le olvidó." with dissolve 
    "Cielos, tendré que ingeniármelas para que a Umi-chan no se le ocurra hacerlo mañana." with dissolve 
    scene HomuraCocina with dissolve
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
    $ quick_menu = False 
    scene black with fade

    #COMENTARIOS FINALES DE MAKI
    scene TMaki with dissolve
    $ renpy.pause(2.0, hard = False) 
    scene comentarioMaki1 with dissolve
    $ renpy.pause(9.0, hard = False)
    scene black with fade 
    jump cap4Honoka


label cap4Honoka:
    
        




# label UmiSono:
    # voice "audio/VoiceUmi/001.mp3"
   
