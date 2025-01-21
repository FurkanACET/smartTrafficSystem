from gpiozero import LED
from time import sleep
import cv2

# Define LEDs for traffic lights
# Trafik ışıkları için LED'leri tanımla
red_led_1 = LED(14)
yellow_led_1 = LED(15)
green_led_1 = LED(18)

red_led_2 = LED(17)
yellow_led_2 = LED(27)
green_led_2 = LED(22)

# Define DroidCam IP addresses
# DroidCam IP adreslerini tanımla
droidcam_ip_1 = "http://192.168.1.121:4747/video"
droidcam_ip_2 = "http://192.168.1.102:4747/video"

# Capture video from cameras
# Kameralardan video al
cap_1 = cv2.VideoCapture(droidcam_ip_1)
cap_2 = cv2.VideoCapture(droidcam_ip_2)

# Check if cameras are connected
# Kameraların bağlı olup olmadığını kontrol et
if not cap_1.isOpened() or not cap_2.isOpened():
    print("One or more cameras could not connect!")  # Bir veya daha fazla kamera bağlanamadı!
    exit()

# Load car detection cascade
# Araba tespiti için cascade dosyasını yükle
car_cascade = cv2.CascadeClassifier('/home/admin/Desktop/haarcascade_car.xml')

def set_traffic_lights(light_1, light_2, duration):
    """
    Control the traffic lights based on input parameters.
    Girilen parametrelere göre trafik ışıklarını kontrol et.
    """
    if light_1 == "green":
        red_led_1.off()
        yellow_led_1.off()
        green_led_1.on()
    elif light_1 == "yellow":
        red_led_1.off()
        yellow_led_1.on()
        green_led_1.off()
    else:  # light_1 == "red"
        red_led_1.on()
        yellow_led_1.off()
        green_led_1.off()

    if light_2 == "green":
        red_led_2.off()
        yellow_led_2.off()
        green_led_2.on()
    elif light_2 == "yellow":
        red_led_2.off()
        yellow_led_2.on()
        green_led_2.off()
    else:  # light_2 == "red"
        red_led_2.on()
        yellow_led_2.off()
        green_led_2.off()

    sleep(duration)

try:
    # Turn off all lights initially
    # Başlangıçta tüm ışıkları kapat
    red_led_1.off()
    yellow_led_1.off()
    green_led_1.off()
    red_led_2.off()
    yellow_led_2.off()
    green_led_2.off()

    # Read frames from cameras
    # Kameralardan kareleri oku
    ret_1, frame_1 = cap_1.read()
    ret_2, frame_2 = cap_2.read()

    if not ret_1 or not ret_2:
        print("Cannot retrieve frames from cameras!")  # Kameralardan görüntü alınamıyor!
        exit()

    # Convert frames to grayscale
    # Kareleri gri tonlamaya çevir
    gray_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)

    # Detect cars in frames
    # Karelerde araba tespiti yap
    cars_1 = car_cascade.detectMultiScale(gray_1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    cars_2 = car_cascade.detectMultiScale(gray_2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    car_count_1 = len(cars_1)
    car_count_2 = len(cars_2)

    print(f"Number of cars in the first camera: {car_count_1}")  # İlk kameradaki araba sayısı
    print(f"Number of cars in the second camera: {car_count_2}")  # İkinci kameradaki araba sayısı

    # Set traffic lights based on car counts
    # Araba sayılarına göre trafik ışıklarını ayarla
    if car_count_1 > car_count_2:
        set_traffic_lights("green", "red", 10)
        set_traffic_lights("yellow", "red", 2)
        set_traffic_lights("red", "green", 10)
        set_traffic_lights("red", "yellow", 2)
    elif car_count_2 > car_count_1:
        set_traffic_lights("red", "green", 10)
        set_traffic_lights("red", "yellow", 2)
        set_traffic_lights("green", "red", 10)
        set_traffic_lights("yellow", "red", 2)
    else:
        set_traffic_lights("yellow", "yellow", 2)

except KeyboardInterrupt:
    print("Terminating program...")  # Program sonlandırılıyor...
finally:
    # Turn off all LEDs and release resources
    # Tüm LED'leri kapat ve kaynakları serbest bırak
    red_led_1.off()
    yellow_led_1.off()
    green_led_1.off()
    red_led_2.off()
    yellow_led_2.off()
    green_led_2.off()
    cap_1.release()
    cap_2.release()
    cv2.destroyAllWindows()
