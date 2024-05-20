# Un ejemplo de reconocimiento de voz, incluso con la habilidad
# de abrir enlaces en línea si se le solicita.

# NOTE: no hay un notebook disponible de este ejemplo porque lo
# he probado sobre la marcha en mi editor de codigo.

import webbrowser
import speech_recognition as sr

r = sr.Recognizer()  # el objeto de reconocimiento

# introduce al usuario y escucha
with sr.Microphone() as source:
    # habla
    print("IA> Hola! Espero poder ayudarte hoy.")
    print("IA> Te escucho...")
    # escucha
    audio = r.listen(source, timeout=1, phrase_time_limit=5)
    # FIXME: resolver este error que interrumpe cada ejecucion por ahora...
    # > speech_recognition.exceptions.WaitTimeoutError:
    # > listening timed out while waiting for phrase to start

    # procesa el audio
    try:
        # intenta procesar
        # TODO: probar otro medio para reconocer texto, como
        #       recognize_amazon u otros :)
        texto = r.recognize_google(audio, language="es_MX")
        # devuelve el texto escuchado
        print("usted>", texto)
        # Ahora, solo por diversion, abriremos "diddileija.github.io" en el
        # dado caso de que el programa lea "diddileija" en el texto.
        if "diddileija" in str(texto).lower():
            webbrowser.open("https://diddileija.github.io")
    except:
        print("IA> No te he entendido, intenta de nuevo.")