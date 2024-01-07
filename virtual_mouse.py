import cv2
import math
import mediapipe as mp
# Aual 109: Importar as classes (Button e Controller) do módulo pynput.mouse
from pynput.mouse import Button, Controller
import pyautogui

# Aula 109: Iniciando o objeto Controller usando a variável mouse
mouse = Controller()

# Capturando os quadros do vídeo da webcan 
cap = cv2.VideoCapture(0)

# Aula 109 - Obtendo a largura e a altura da janela do vídeo para verificar a contagem dos dedos
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

# Aula 109 - Obtendo o tamanho da tela usando size do módulo pyautogui nas var screen_width e screen_height
(screen_width, screen_height) = pyautogui.size()

# Módulos da biblioteca MediaPipe 
mp_hands = mp.solutions.hands # Detecta 1º a palma da mão e, depois, os 21 pontos de referência na palma da mão.
mp_drawing = mp.solutions.drawing_utils # Desenha as linhas de conexão entre os 21 pontos de referência.

# Método Hands - usa 2 parâmetros: min_detection_confidence(confiança mínima de detecção) e min_tracking_confidence (confiança mínima de rastreamento)
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

# Variavel global "pinch" (pinça) - Detectar o gesto de uma pinça
pinch = False

# Defina uma função para contar os dedos
def countFingers(image, hand_landmarks, handNo=0):

    # Aula 109: Definindo a variável 'pinch' dentro do função, precisamos garantir que ela seja global
	global pinch

	if hand_landmarks:
        # Obtenha todos os pontos de referência da PRIMEIRA mão VISÍVEL
		landmarks = hand_landmarks[handNo].landmark

        # Conte os dedos - Inicialmente vazia
		fingers = []

		for lm_index in tipIds:
            # Obtenha os valores y da ponta e da parte inferior do dedo
			finger_tip_y = landmarks[lm_index].y 
			finger_bottom_y = landmarks[lm_index - 2].y

            # Verifique se ALGUM DEDO está ABERTO ou FECHADO
			if lm_index !=4:
				if finger_tip_y < finger_bottom_y:
					fingers.append(1)


				if finger_tip_y > finger_bottom_y:
					fingers.append(0)

		totalFingers = fingers.count(1)

		# FAZENDO A PINÇA
		# Desafio 01: Desenhe uma LINHA entre a PONTA DO DEDO e a PONTA DO POLEGAR


		#  Desafio 02: Desenhar o centro da linha - CÍRCULO no CENTRO da LINHA entre a PONTA DO DEDO e a PONTA DO POLEGAR

		
		# Desafio 03: Calcule a DISTÂNCIA entre a PONTA DO DEDO e a PONTA DO POLEGAR
		

		# Desafio 04: Defina a posição do mouse na tela em relação ao tamanho da janela de resultado	
		

		# Desafio 05: Verifique as condições de formação da PINÇA
		


# Defina uma função para 
def drawHandLanmarks(image, hand_landmarks):

    # Desenhar as conexões entre os pontos de referência
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)



while True:
	success, image = cap.read()
	
	image = cv2.flip(image, 1)

    # Detecte os pontos de referência das mãos 
	results = hands.process(image)

    # Obtenha a posição do ponto de referência do resultado processado
	hand_landmarks = results.multi_hand_landmarks

    # Desenhe os pontos de referência
	drawHandLanmarks(image, hand_landmarks)

    # Obtenha a posição dos dedos da mão        
	countFingers(image, hand_landmarks)

	cv2.imshow("Controlador de Midia", image)

    # Saia da tela ao pressionar a barra de espaço
	key = cv2.waitKey(1)
	if key == 27:
		break

cv2.destroyAllWindows()