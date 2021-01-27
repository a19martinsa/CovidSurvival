import sys
import pygame
from pygame.locals import *
import musica
import random
import var
import conexion
import metodos

musica = [musica]


def evasor(self):
    anchoVen = 1920
    altoVen = 1080
    colorVen = (255, 255, 255)
    colorFondo = (0, 0, 0)
    FPS = 60
    tamanoVill = 15
    tamanoMaxVill = 60
    tamanoMinVill = 1
    velMaxVill = 8
    tasaNuevoVill = 6
    tasaMovJug = 6
    op_menu = 1
    op_musica = 1
    i = 1

    # establece un pygame, la ventana y el cursor del ratón
    pygame.init()
    relojPrincipal = pygame.time.Clock()
    superficieVentana = pygame.display.set_mode((anchoVen, altoVen), FULLSCREEN)
    pygame.display.set_caption('Evasor')
    pygame.mouse.set_visible(False)

    # establece las fuentes
    fuente = pygame.font.SysFont("Arial", 48)

    # establece los sonidos
    sonidoJuegoTerminado = pygame.mixer.Sound('juegoterminado.wav')
    sonidoJuegoTerminado.set_volume(0.1)
    pygame.mixer.music.load('gobierno.mp3')
    pygame.mixer.music.set_volume(0.1)

    # establece las imagenes
    imagenJugador = pygame.image.load('jugador2.png')
    rectanguloJugador = imagenJugador.get_rect()
    imagenVillano = pygame.image.load('covid2.png')

    # Muestra la pantalla inicial
    metodos.dibujarTexto('Esquiva el bicho', fuente, superficieVentana, (anchoVen / 3), (altoVen / 4),
                         colorVen)
    metodos.dibujarTexto('Presione una tecla para comenzar.', fuente, superficieVentana, (anchoVen / 3),
                         (altoVen / 3), colorVen)
    pygame.display.update()
    metodos.esperarTeclaJugador()

    puntmax = var.puntmax
    pygame.mixer.music.play(0, 0.0)
    while True:
        # establece el comienzo del juego
        villanos = []
        punt = 0
        rectanguloJugador.topleft = (anchoVen / 2, altoVen / 2)
        moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
        trucoReversa = trucoLento = pause = False
        contadorpausa = False
        contadorAgregarVillano = 0

        while True:  # el ciclo del juego se mantiene mientras se este jugando
            if not pause:
                punt += 1  # incrementa la puntuación

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    metodos.terminar()

                if evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        metodos.terminar()
                    # menu principal
                    if evento.key == pygame.K_q:
                        op_menu = metodos.generar_menu(op_menu, superficieVentana, colorFondo, anchoVen,
                                                       altoVen, fuente, relojPrincipal, colorVen)
                    # menu musica
                    if evento.key == pygame.K_m:
                        i = metodos.generar_menu_musica(op_musica, superficieVentana, colorFondo, anchoVen,
                                                        altoVen, fuente, relojPrincipal, colorVen, i)
                    # invertir el movimiento con la z
                    if evento.key == ord('z'):
                        trucoReversa = True
                    # ralentizar el movimiento con la z
                    if evento.key == ord('x'):
                        trucoLento = True
                    # pausar el juego con el espacio
                    if evento.key == K_SPACE:

                        conexion.Conexion.db_connect('database.db')
                        pause = True
                        if not contadorpausa:
                            contadorpausa = True
                        elif contadorpausa:
                            contadorpausa = False

                    if evento.key == K_LEFT or evento.key == ord('a'):
                        moverDerecha = False
                        moverIzquierda = True
                    if evento.key == K_RIGHT or evento.key == ord('d'):
                        moverIzquierda = False
                        moverDerecha = True
                    if evento.key == K_UP or evento.key == ord('w'):
                        moverAbajo = False
                        moverArriba = True
                    if evento.key == K_DOWN or evento.key == ord('s'):
                        moverArriba = False
                        moverAbajo = True

                if evento.type == KEYUP:
                    if evento.key == ord('z'):
                        trucoReversa = False
                        punt = 0
                    if evento.key == ord('x'):
                        trucoLento = False
                        punt = 0
                    if evento.key == K_SPACE and contadorpausa == 0:
                        pause = False
                        contadorpausa = False

                    if evento.key == K_LEFT or evento.key == ord('a'):
                        moverIzquierda = False
                    if evento.key == K_RIGHT or evento.key == ord('d'):
                        moverDerecha = False
                    if evento.key == K_UP or evento.key == ord('w'):
                        moverArriba = False
                    if evento.key == K_DOWN or evento.key == ord('s'):
                        moverAbajo = False

                if evento.type == MOUSEMOTION:
                    # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                    rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx,
                                              evento.pos[1] - rectanguloJugador.centery)
            if op_menu == 1:
                # Añade villanos en la parte superior de la pantalla, de ser necesarios.
                if not trucoReversa and not trucoLento and not pause:
                    contadorAgregarVillano += 1
                if contadorAgregarVillano == tasaNuevoVill:
                    contadorAgregarVillano = 0
                    tamanoVillano = random.randint(tamanoVill, tamanoMaxVill)
                    nuevoVillano = {
                        'rect': pygame.Rect(random.randint(0, anchoVen - tamanoVillano), 0 - tamanoVillano,
                                            tamanoVillano,
                                            tamanoVillano),
                        'velocidad': random.randint(tamanoMinVill, velMaxVill),
                        'superficie': pygame.transform.scale(imagenVillano, (tamanoVillano, tamanoVillano)),
                    }

                    villanos.append(nuevoVillano)

                # Mueve los villanos hacia abajo.
                for v in villanos:
                    if not trucoReversa and not trucoLento and not pause:
                        v['rect'].move_ip(0, v['velocidad'])
                    elif trucoReversa:
                        v['rect'].move_ip(0, -5)
                    elif trucoLento:
                        v['rect'].move_ip(0, 1)
                    elif pause:
                        v['rect'].move_ip(0, 0)

                # Elimina los villanos que han caido por debajo.
                for v in villanos:
                    if v['rect'].top > altoVen:
                        villanos.remove(v)
            if op_menu == 2:
                # Añade villanos en la parte inferior de la pantalla, de ser necesarios.
                if not trucoReversa and not trucoLento and not pause:
                    contadorAgregarVillano += 1
                if contadorAgregarVillano == tasaNuevoVill:
                    contadorAgregarVillano = 0
                    tamanoVillano = random.randint(tamanoVill, tamanoMaxVill)
                    nuevoVillano = {
                        'rect': pygame.Rect(random.randint(0, anchoVen - tamanoVillano),
                                            altoVen + tamanoVillano,
                                            tamanoVillano, tamanoVillano),
                        'velocidad': random.randint(tamanoMinVill, velMaxVill),
                        'superficie': pygame.transform.scale(imagenVillano, (tamanoVillano, tamanoVillano)),
                    }
                    villanos.append(nuevoVillano)
                # Mueve los villanos hacia arriba.
                for v in villanos:
                    if not trucoReversa and not trucoLento and not pause:
                        v['rect'].move_ip(0, -v['velocidad'])
                    elif trucoReversa:
                        v['rect'].move_ip(0, 5)
                    elif trucoLento:
                        v['rect'].move_ip(0, -1)
                    elif pause:
                        v['rect'].move_ip(0, 0)

                # Elimina los villanos que tocado techo.
                for v in villanos[:]:
                    if v['rect'].bottom < 0:
                        villanos.remove(v)

            # Mueve el jugador.
            if moverIzquierda and rectanguloJugador.left > 0:
                rectanguloJugador.move_ip(-1 * tasaMovJug, 0)
            if moverDerecha and rectanguloJugador.right < anchoVen:
                rectanguloJugador.move_ip(tasaMovJug, 0)
            if moverArriba and rectanguloJugador.top > 0:
                rectanguloJugador.move_ip(0, -1 * tasaMovJug)
            if moverAbajo and rectanguloJugador.bottom < altoVen:
                rectanguloJugador.move_ip(0, tasaMovJug)

            # Mueve el cursor del ratón hacia el jugador.
            pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)

            # Dibuja el mundo del juego en la ventana.
            superficieVentana.fill(colorFondo)

            # Dibuja el punt y el punt máximo
            metodos.dibujarTexto('Puntuación: %s' % (punt), fuente, superficieVentana, 10, 0, colorVen)
            metodos.dibujarTexto('Mejor puntuación: %s' % (puntmax), fuente, superficieVentana, 10, 40,
                                 colorVen)

            # Dibuja el rectángulo del jugador
            superficieVentana.blit(imagenJugador, rectanguloJugador)

            # Dibuja cada villano
            for v in villanos:
                superficieVentana.blit(v['superficie'], v['rect'])

            pygame.display.update()

            # Verifica si algún villano impactó en el jugador.
            if metodos.jugadorGolpeaVillano(rectanguloJugador, villanos):
                if punt > puntmax:
                    puntmax = punt  # Establece nuevo punt máximo
                    conexion.Conexion.modifJug(var.jugador,puntmax)
                break

            relojPrincipal.tick(FPS)

        # Detiene el juego y muestra "Juego Terminado"
        # pygame.mixer.music.stop()
        # sonidoJuegoTerminado.play()
        pygame.mixer.music.load('elxokas.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(0, 0.0)

        metodos.dibujarTexto('Juego Terminado', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3),
                             colorVen)
        metodos.dibujarTexto('Presione una tecla para jugar de nuevo.', fuente, superficieVentana,
                             (anchoVen / 3),
                             (altoVen / 2), colorVen)
        pygame.display.update()

        metodos.esperarTeclaJugador()

        # sonidoJuegoTerminado.stop()
        pygame.mixer.music.load('Nigths.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(0, 0.0)


def terminar():
    pygame.quit()
    conexion.Conexion.mostrarJugadores(None)


def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:  # Sale del juego al presionar ESCAPE
                    terminar()
                return


def jugadorGolpeaVillano(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False


def dibujarTexto(texto, fuente, superficie, x, y, colorVen):
    objetotexto = fuente.render(texto, 1, colorVen)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)


def generar_menu(op_menu, superficieVentana, colorFondo, anchoVen, altoVen, fuente, relojPrincipal,
                 colorVen):
    otra_pantalla = True
    op = op_menu
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('q'):
                    # Ocultar pantalla
                    otra_pantalla = False
                    # color del menu
                if evento.key == ord('1'):
                    op = 1
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    terminar()

        superficieVentana.fill(colorFondo)
        # dibujar
        dibujarTexto('Menu:', fuente, superficieVentana, (anchoVen / 3), (altoVen / 4), colorVen)
        dibujarTexto('0-Salir de juego', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 50,
                     colorVen)
        dibujarTexto('1-Primera fase', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 100,
                     colorVen)
        dibujarTexto('2-Segunda fase', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 150,
                     colorVen)
        dibujarTexto('3-Guardar partida', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 200,
                     colorVen)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op


def generar_menu_musica(op_menu, superficieVentana, colorFondo, anchoVen, altoVen, fuente, relojPrincipal,
                        colorVen, i):
    otra_pantalla = True
    op = op_menu
    lista = ['gobierno.mp3', 'InTE.mp3', 'CastleOG.mp3', 'Numb.mp3', 'Nigths.mp3', 'Counting.mp3', 'Demons.mp3',
             '7years.mp3']
    while otra_pantalla:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('m'):
                    # Ocultar pantalla
                    otra_pantalla = False
                    # color del menu
                if evento.key == ord('1'):
                    op = 1
                    pygame.mixer.music.load(lista[i])
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1, 0.0)
                    if i < 7:
                        i = i + 1
                    else:
                        i = 0
                    return i
                    otra_pantalla = False
                if evento.key == ord('2'):
                    op = 2
                    pygame.mixer.music.load('InTE.mp3')
                    pygame.mixer.music.queue('CastleOG.mp3')
                    pygame.mixer.music.queue('Numb.mp3')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('3'):
                    op = 3
                    pygame.mixer.music.load('Nigths.mp3')
                    pygame.mixer.music.queue('Counting.mp3')
                    pygame.mixer.music.queue('Demons.mp3')
                    pygame.mixer.music.queue('7years.mp3')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(0, 0.0)
                    otra_pantalla = False
                if evento.key == ord('0') or evento.key == K_ESCAPE:
                    otra_pantalla = False

        superficieVentana.fill(colorFondo)
        # dibujar
        dibujarTexto('Menu:', fuente, superficieVentana, (anchoVen / 3), (altoVen / 4), colorVen)
        dibujarTexto('0-Salir', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 50, colorVen)
        dibujarTexto('1-Siguiente canción', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 100,
                     colorVen)
        dibujarTexto('2-Lista LP', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 150, colorVen)
        dibujarTexto('3-Lista A', fuente, superficieVentana, (anchoVen / 3), (altoVen / 3) + 200, colorVen)
        pygame.display.update()
        relojPrincipal.tick(5)
    return op
