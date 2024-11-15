# Robo-Tlacuaches

# Frases generadas con ayuda de ChatGPT

nao_speech = {
    "saludo_nao_respuesta": [
       "¡Hola! ¿Cómo estás?", "¡Buenos días! ¿Cómo va todo?", "¡Buenas tardes! ¿En qué te puedo ayudar?", 
       "¡Buenas noches! ¿Todo bien?", "¡Hola amigo! ¿Qué tal?", "Estoy aquí para ayudarte, ¿qué pasa?",
       "¡Hey! ¿Cómo te sientes?", "¡Hola, soy NAO! ¿Cómo estás hoy?", "¡Qué pasa! ¿Cómo va todo?",
       "¡Hola, todo bien? ¿Cómo te va?", "¡Qué tal, compañero! ¿Cómo te encuentras?", "¡Saludos! ¿Qué puedo hacer por ti?",
       "¡Hola, qué tal! Estoy listo para ayudarte", "¡Hola! ¡Me alegra verte!", "¡Hola! Siempre es un gusto verte",
       "¡Qué tal tu día hoy?", "¡Hola! Es un placer verte, ¿cómo estás?", "¡Buenas! ¿Cómo te ha ido?",
       "¡Hey! Qué bueno verte, ¿en qué te ayudo hoy?", "¡Qué tal todo por aquí?", "¡Hola! Estoy aquí para ti",
       "¡Hola de nuevo! ¿Cómo te va?", "¡Buenas! ¿En qué te ayudo hoy?", "¡Qué tal! ¿Todo bien?", 
       "¡Hola! Es un placer ver a gente como tú", "¡Buenas! ¿Qué puedo hacer por ti hoy?", 
       "¡Cómo va todo! Estoy aquí para lo que necesites", "¡Hola! ¿Te sientes bien hoy?", 
       "¡Qué gusto verte! ¿Todo va bien?", "¡Qué tal, todo en orden?", "¡Qué tal la vida! ¿Cómo estás?",
       "¡Hola! Qué bien verte, ¿cómo va todo?", "¡Qué novedades! Estoy listo para escuchar", 
       "¡Hola! ¿En qué te ayudo hoy?", "¡Saludos! Estoy aquí para ayudarte", "¡Qué gusto verte hoy!", 
       "¡Hola! ¿Cómo amaneciste?", "¡Qué tal! ¿Todo bien hoy?", "¡Saludos! ¿Qué tal tu día?",
       "¡Hola! ¿Cómo te encuentras?", "¡Hola de nuevo! Qué tal todo por aquí?"
   ],
   
   "despedida_nao_respuesta": [
       "¡Adiós! ¡Cuídate mucho!", "¡Nos vemos! Que tengas un excelente día",
       "Hasta pronto, ¡que te vaya bien!", "¡Hasta luego! Espero verte pronto",
       "Cuídate, ¡me voy por ahora!", "¡Hasta la próxima, compañero!", 
       "¡Nos vemos! ¡Cuídate mucho!", "Fue un gusto hablar contigo, ¡adiós!",
       "¡Me voy! ¡Nos vemos después!", "¡Nos vemos pronto! ¡Que descanses!",
       "¡Hasta otra! ¡Cuídate mucho!", "¡Hasta luego! ¡Que todo vaya bien!",
       "¡Adiós! ¡Que tengas una buena noche!", "¡Chao! ¡Fue un placer!",
       "¡Hasta pronto! Cuídate mucho", "¡Hasta luego! ¡Nos veremos pronto!",
       "¡Que descanses! ¡Hasta la próxima!", "¡Nos vemos pronto! ¡Hasta luego!",
       "¡Me voy! ¡Cuídate mucho! ¡Hasta luego!", "¡Hasta luego, nos vemos pronto!",
       "¡Ha sido un gusto! ¡Cuídate mucho!", "¡Nos vemos! Que todo te salga bien",
       "¡Hasta pronto! ¡Nos vemos pronto!", "¡Gracias por todo! ¡Hasta luego!",
       "¡Nos vemos mañana! ¡Que tengas un buen día!", "¡Cuídate mucho, hasta luego!",
       "¡Adiós! ¡Que tengas un día increíble!", "¡Nos vemos luego! ¡Cuídate mucho!",
       "¡Hasta luego! ¡Todo lo mejor para ti!", "¡Adiós, ha sido un placer verte!"
   ],

    "pausa_lectura_respuesta": [
        "Claro, haré una pausa.",
        "Entendido, pausando la lectura.",
        "Pausa activada, ¿quieres hacer algo más?",
        "He detenido la lectura, avísame cuando quieras continuar.",
        "Pausando ahora, dime cuando quieras seguir.",
        "Lectura detenida, estoy aquí si me necesitas.",
        "Listo, la lectura está en pausa.",
        "He parado, ¿quieres que retome más tarde?",
        "Pausa realizada, ¿qué te gustaría hacer ahora?",
        "De acuerdo, haré una pausa en la lectura.",
        "La lectura está en pausa, avísame cuando quieras continuar.",
        "He detenido la lectura por ti, ¿cómo puedo ayudarte?",
        "Pausa hecha, ¿hay algo más en lo que te pueda asistir?",
        "He detenido la lectura por ahora, ¿quieres seguir más tarde?",
        "¡He hecho una pausa! ¿Te gustaría seguir ahora o después?",
        "He detenido la lectura, por favor indícame cuando deseas continuar.",
        "Pausa realizada, dime cuándo puedo reanudar.",
        "La lectura está detenida, cuando estés listo puedo seguir.",
        "He detenido todo, cuando quieras continuar me avisas.",
        "Pausa activada, ¿qué más puedo hacer por ti?",
        "¿Listo para continuar o prefieres más tiempo de pausa?",
        "La lectura está en pausa, ¿te gustaría hablar de algo más?",
        "Pausa en marcha, ¿quieres cambiar de actividad?",
        "Lectura detenida, ¿te gustaría descansar un poco?",
        "Pausa, ¿quieres que te lea algo más tarde?"
    ],

    "reanudar_lectura_respuesta": [
        "Claro, reanudando la lectura.",
        "De acuerdo, continuaré leyendo.",
        "¡Listo! Estoy retomando la lectura.",
        "He reanudado, sigue disfrutando del libro.",
        "La lectura ha comenzado nuevamente.",
        "He vuelto al texto, continúo donde quedamos.",
        "Reanudando la lectura ahora, por favor escucha.",
        "Ahora seguimos con la lectura.",
        "He reanudado la lectura, sigue atento.",
        "¿Listo para continuar? Yo ya he retomado.",
        "Lectura reanudada, sigamos con el libro.",
        "La lectura ya continúa, avísame si necesitas algo más.",
        "Ya estoy siguiendo la lectura, continúa disfrutando.",
        "Listo, sigo desde donde dejaste.",
        "Retomando la lectura en el punto que dejamos.",
        "Ya comencé a leer de nuevo, ¿quieres seguir?",
        "Retomando la lectura, vamos a continuar.",
        "He comenzado de nuevo, sigue atento.",
        "Estoy continuando la lectura, espero que te guste.",
        "Lectura reanudada, ¿te gustaría que lea más rápido o despacio?",
        "He retomado la lectura, dime si necesitas algo.",
        "Ya estamos avanzando de nuevo, sigue conmigo.",
        "Retomando el libro, ¡seguimos adelante!",
        "Lectura retomada, sigo donde dejamos.",
        "Ya lo he reanudado, ¿te gustaría hacer una pausa después?",
        "La historia continúa, estoy leyendo desde donde paramos.",
        "Reanudando la historia, no te preocupes.",
        "Ya sigo leyendo, ¿quieres cambiar de capítulo más tarde?",
        "Comenzamos de nuevo, seguimos leyendo.",
        "Sigo con el libro, ya retomé la lectura."
    ],
        "lectura_libro_respuesta": [
        "¿Qué libro quieres que lea?",
        "¿Qué libro quieres escuchar?",
        "¿Cuál libro te gustaría que lea?",
        "¿Qué historia quieres que lea?",
        "¿Cuál libro prefieres que lea?",
        "¿Qué libro te gustaría escuchar?",
        "¿Qué quieres que lea ahora?",
        "¿De qué libro quieres que lea algo?",
        "¿Qué libro te interesa escuchar hoy?",
        "¿Quieres escuchar un libro completo?",
        "¿Te gustaría que lea una historia?",
        "¿Qué historia quieres escuchar?",
        "¿Puedo comenzar con este libro?",
    ],

    "lectura_capitulo_respuesta": [
        "¿Qué capítulo te gustaría que lea?",
        "¿Cuál capítulo prefieres escuchar ahora?",
        "¿Qué capítulo te gustaría que lea a continuación?",
        "¿Qué capítulo quieres escuchar?",
        "¿Qué capítulo te gustaría escuchar?",
        "¿Qué capítulo prefieres escuchar?",
        "¿Qué capítulo estás interesado en escuchar?",
        "¿Qué capítulo quieres que lea ahora?",

    ],

    "respuesta_leer_capitulo": [
        "Leeré el capítulo ahora.",
        "Empezaré a leer el capítulo.",
        "Voy a leer el capítulo.",
        "Comenzaré a leer ese capítulo.",
        "Leeré ahora el capítulo que elegiste.",
        "Voy a leer el capítulo ahora mismo.",
        "Comenzaré a leer el cpitulo.",
        "Empezaré a leer el capítulo que has seleccionado.",
        "Comenzaré el capítulo que me pides.",
        "Voy a comenzar con ese capítulo ahora."
    ],

        "respuesta_agradecimiento_nao": [
        "¡De nada! Es un placer ayudarte.",
        "Me alegra que te guste, ¡estoy aquí para ti!",
        "Gracias a ti por darme la oportunidad de leerte.",
        "No hay de qué, siempre estaré aquí para leerte.",
        "¡Es un placer leer para ti!",
        "Me hace feliz saber que te gusta.",
        "Estoy feliz de ayudarte, ¡gracias a ti por estar aquí!",
        "Con gusto, siempre estaré para ti.",
        "¡Qué amable de tu parte decir eso! Gracias a ti.",
        "No tienes que agradecer, siempre es un placer.",
        "Estoy aquí para lo que necesites, ¡me alegra que te guste!",
        "Gracias a ti por tu amabilidad, ¡siempre es un placer leer para ti!",
        "Es un honor ser tu compañero de lectura.",
        "¡Estoy muy feliz de que te guste mi lectura!",
        "¡Es un placer ayudarte y acompañarte durante la lectura!",
        "Aprecio mucho tus palabras, ¡estoy aquí para ti siempre!",
        "¡Gracias a ti por tu apoyo y paciencia!",
        "Me alegra mucho que disfrutes de la lectura.",
        "Gracias por tus palabras, ¡espero seguir leyéndote mucho más!",
        "Es un honor estar aquí para ti, ¡me encanta leerte!",
        "Me hace feliz saber que disfrutas la compañía.",
        "Gracias por tu confianza, siempre estaré aquí para leerte.",
        "Me alegra que te sientas bien, ¡es un placer leerte!",
        "¡Un placer ayudarte! Gracias por ser tan amable."
    ],

    "respuesta_navegacion_adelante": [
        "Adelanto al siguiente capítulo.",
        "Avanzo al siguiente capítulo.",
        "Pasando al siguiente capítulo.",
        "Siguiendo al siguiente capítulo.",
        "Voy al siguiente capítulo.",
        "Cambiando al siguiente capítulo.",
        "Pasando al próximo capítulo.",
        "Avanzando un capítulo.",
        "Voy a la siguiente página.",
        "Siguiente capítulo.",
        "Subiendo al siguiente capítulo."
    ],

    "respuesta_navegacion_atras": [
        "Retrocedo al capítulo anterior.",
        "Vuelvo al capítulo anterior.",
        "Regreso al capítulo anterior.",
        "Pasando al capítulo anterior.",
        "Retrocediendo un capítulo.",
        "Volviendo a la página anterior.",
        "Retrocediendo al capítulo anterior.",
        "Regresando al capítulo anterior.",
        "Bajando un capítulo.",
        "Volviendo al capítulo anterior.",
        "Regresando a la página anterior."
    ],
    
    "respuesta_navegacion_adelante_denegada": [
        "No hay más capítulos disponibles.",
        "Has llegado al final del libro.",
        "No puedo avanzar más, ya estás en el último capítulo.",
        "No hay capítulos siguientes en este libro.",
        "Este es el último capítulo, no puedo avanzar más.",
        "Ya llegamos al final del libro.",
        "No hay más capítulos para leer, hemos terminado.",
        "Ya has leído todos los capítulos disponibles."
    ],

    "respuesta_navegacion_atras_denegada": [
        "No puedo retroceder más, estás en el primer capítulo.",
        "Ya estás en el primer capítulo, no hay capítulos anteriores.",
        "No puedo ir más atrás, ya estás en el comienzo.",
        "Este es el primer capítulo, no hay más retrocesos.",
        "No hay capítulos anteriores, estás en el inicio del libro.",
        "Ya llegamos al principio, no hay capítulos anteriores."
    ]
}

