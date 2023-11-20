# El juego comienza aquí.

label start:
    stop music fadeout 0.8
    scene capitulo1 with fade
    $ renpy.pause(3.0, hard= True)
    scene cuarto_Honoka with fade
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
    voice "audio/faitoDayo.mp3"
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
    M_Kotori " ¿Estás bien, Honoka-chan?" with dissolve 
    "Cuando las vi, con esa preocupación. Por fin me di cuenta. Ah, no fue un sueño." with dissolve 
    K_Honoka "Cierre…" with dissolve 
    "Eso quería decir que mi querida preparatoria Otonokizaka iba a desaparecer." with dissolve 
    "Luego de un tiempo, no andaría ninguna estudiante en este edificio; y esas chicas con sus uniformes, que nunca imaginé que dejaría de ver en el vecindario, también desaparecerían." with dissolve 
    "¡Ah! Y además, si cerraba, ¡¿qué pasaría con los dos años que me faltaban de preparatoria?! ¿Qué voy a hacer?" with dissolve 
    "Reprobé materias el año pasado, y en verdad no creo ser capaz de aprobar otro examen de admisión en este punto." with dissolve 
    "Kotori-chan me miró con pena y una sonrisa débil." with dissolve 
    M_Kotori "Parece que no tendrás que preocuparte por eso. La escuela va a cerrar hasta dentro de tres años, cuando se hayan graduado todas las estudiantes." with dissolve 
    "Ah, muy bien." with dissolve 
    "Cansada, me hundí en mi asiento." with dissolve 
    hide UmiS with dissolve
    hide KotoriM with dissolve
    "Pero, al parecer, volví a pensar en voz alta y me levanté de mi lugar." with dissolve 
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

    "¡Espero que ese día llegue pronto!" with dissolve 
    "Y con ese deseo, me iré a dormir esta noche." with dissolve 
    "¡Mañana practicaremos duro!" with dissolve 
    
    #COMENTARIOS FINALES DE KOTORI
    scene cKotori with fade
    M_Kotori "Espero que llegue pronto el día en el que la gente después de leer esto puedan entender mejor los sentimientos de Honoka-chan." with dissolve 
    M_Kotori "¡Yo también amo a Otonoki, igual que Honoka-chan!" with dissolve 
    M_Kotori "Sigamos trabajando duro, u's, por siempre y para siempre." with dissolve 
    scene black with fade
    stop music fadeout 1.0
    scene capitulo2 with fade
    $ renpy.pause(3.0, hard= True)
    return
