# -*- coding: utf-8 -*-
from naoqi import ALProxy
import argparse
import json
import sqlite3
import threading
import time
from Nao_Vocabulary import nao_vocabulary
from Nao_Speech_Vocabulary import nao_speech

#### Global variables
shutdown = False
pause = False
#### /Global variables

#### Functions

def detect_command_type(palabra):
    for command_type, phrases in nao_vocabulary.items():
        if palabra in phrases:
            return command_type
    return None

def listen_stop_conditions(memory, speech_proxy):
    global shutdown, pause
    while not shutdown:
        try:
            comando = memory.getData("WordRecognized")
            if comando and len(comando) > 0:
                palabra = comando[0]
                command_type = detect_command_type(palabra)

                if(command_type == "despedida_nao"):
                    speech_proxy.say("Hasta luego.")
                    shutdown = True
                    break
                elif command_type == "pausa_lectura":
                    speech_proxy.say("Deteniendo la lectura.")
                    pause = True
                    time.sleep(0.5)
        except Exception as e:
            speech_proxy.say("Error en el hilo de escucha.")
        time.sleep(0.5)

def search_json(book):
    conn = sqlite3.connect('chapters.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Json_File FROM chapters WHERE QR_Code=?", (book,))
    fetch = cursor.fetchone()
    
    conn.close()
    
    if fetch:
        json_content = json.loads(fetch[0])
        return json_content
    else:
        return None

def read_chapter_nao(qr_code, chapter_number, speech_proxy):
    json_content = search_json(qr_code)
    
    if json_content:
        chapters = json_content["chapters"]
        if str(chapter_number) in chapters:
            chapter = chapters[str(chapter_number)]
            speech_proxy.say("Leyendo " + chapter["titulo"])
            speech_proxy.say(chapter["contenido"])
        else:
            speech_proxy.say("Capítulo no encontrado.")
    else:
        speech_proxy.say("No se encontró el libro en la base de datos.")

def conversation(ip, port):
    global shutdown, pause
    
    #### Proxies
    speech_proxy = ALProxy("ALTextToSpeech", ip, port)
    voice_recon_proxy = ALProxy("ALSpeechRecognition", ip, port)
    memory = ALProxy("ALMemory", ip, port)
    speech_proxy.setLanguage("Spanish")
    voice_recon_proxy.setLanguage("Spanish")
    
    nao_vocabulary = [
        "quiero leer", "Capítulo uno", "Capítulo 2", "Capítulo 3",
        "adios nao", "nao para", "nao detente", "me tengo que ir",
        "Lovecraft", "Arsene", "Doctor Jekyll"
    ]
    
    # Obtiene todas las frases del vocabulario para configurarlo en el proxy
    all_phrases = [phrase for phrases in nao_vocabulary.values() for phrase in phrases]
    voice_recon_proxy.setVocabulary(all_phrases, False)
    voice_recon_proxy.subscribe("NAO_listen")
    
    #### Stop flag threads
    listen_thread = threading.Thread(target=listen_stop_conditions, args=(memory, speech_proxy))
    listen_thread.start()
    
    #### Main loop
    while not shutdown:
        try:
            comando = memory.getData("WordRecognized")
            if comando and len(comando) > 0:
                palabra = comando[0]
                command_type = detect_command_type(palabra)

                if command_type == "lectura_libro":
                    speech_proxy.say("Por favor, dime el nombre del libro que quieres escuchar.")
                    
                    time.sleep(7)  # Pausa para permitir respuesta
                    book_command = memory.getData("WordRecognized")
                    
                    if book_command: 
                        bookselected = None
                        for book in nao_vocabulary["selección_libro"]:
                            if book in book_command[0]:
                                bookselected = book
                                break

                    if bookselected:
                        speech_proxy.say("Has mencionado el libro: {bookselected}")
                        speech_proxy.say("Dime qué capítulo quieres escuchar.")
                        
                        time.sleep(5)
                        chapter_command = memory.getData("WordRecognized")
                        if chapter_command: 
                            for cap in chapter_command[0]:
                                chapter_number = int(cap.split()[1])
                                pause = False
                                read_chapter_nao(bookselected,chapter_number,speech_proxy)

                                while not pause and not shutdown:
                                    time.sleep(0.1)

                                if pause:
                                    speech_proxy.say("Lectura pausada")
                                break
                    else:
                        speech_proxy.say("Libro no reconocido.")
                    
        except Exception as e:
            speech_proxy.say("Error al interpretar el comando")
            time.sleep(1)
    
    #### "MAIN"
    listen_thread.join()
    voice_recon_proxy.unsubscribe("NAO_listen")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control de NAO para lectura de libros")
    parser.add_argument("--ip", type=str, required=True, help="Dirección IP del robot NAO")
    parser.add_argument("--port", type=int, default=9559, help="Puerto del robot NAO (por defecto es 9559)")
    args = parser.parse_args()
    conversation(args.ip, args.port)