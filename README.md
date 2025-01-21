# Smart Traffic System

This project is developed using Raspberry Pi 5 and two phone cameras to simulate a four-way traffic scenario. The system dynamically adjusts traffic light durations by detecting the number of vehicles and prioritizing the road with higher traffic density.

## Project Features

- **Vehicle Counting:** Real-time vehicle detection and counting using the OpenCV library.
- **Dynamic Traffic Control:** Traffic light durations are dynamically adjusted based on the road with higher density.
- **Phone Camera Integration:** Two phone cameras are used with Raspberry Pi via DroidCam.
- **Wireless Access:** Remote access to Raspberry Pi via VNC.

## Technologies Used

- **Hardware:**

  - Raspberry Pi 5 (2GB RAM)
  - 2 Android phones (used as cameras)
  - LED traffic lights
  - Breadboard and jumper wires

- **Software:**

  - Python 3
  - OpenCV
  - DroidCam
  - NumPy
  - RPi.GPIO
  - Haarcascade

## Installation

1. Prepare Raspberry Pi by following these steps:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip install opencv-python numpy RPi.GPIO
```

2. Install DroidCam on your phone and Raspberry Pi:

   - Download DroidCam app to your phone.
   - Install the DroidCam client on Raspberry Pi.

## Usage

1. Open DroidCam and connect to Raspberry Pi using the IP address.
2. Run the main Python script:

```bash
python main.py
```

3. Observe how LED traffic lights change based on traffic density.

## Contribution

Contributions are welcome via pull requests or reporting issues.

---

For any questions, feel free to contact me.



# Akıllı Trafik Sistemi (Smart Traffic System)

Bu proje, Raspberry Pi 5 ve iki adet telefon kamerası kullanarak dört yollu bir trafik simülasyonu gerçekleştirmek amacıyla geliştirilmiştir. Araç sayısını tespit ederek trafik yoğunluğuna göre trafik ışıklarının sürelerini optimize eden bir sistem oluşturulmuştur.

## Proje Özellikleri

- **Araç Sayımı:** OpenCV kütüphanesi ile gerçek zamanlı olarak arabaları algılayarak sayma işlemi yapar.
- **Dinamik Trafik Kontrolü:** Daha kalabalık olan yola öncelik verilerek LED trafik ışıklarının süreleri dinamik olarak ayarlanır.
- **Telefon Kamerası Entegrasyonu:** DroidCam aracılığıyla Raspberry Pi'ye bağlanan iki telefon kamerası kullanılmaktadır.
- **Kablosuz Erişim:** Raspberry Pi'ye VNC aracılığıyla kablosuz olarak erişim sağlanır.

## Kullanılan Teknolojiler

- **Donanım:**

  - Raspberry Pi 5 (2GB RAM)
  - 2 adet Android telefon (kamera olarak kullanılıyor)
  - LED trafik ışıkları
  - Breadboard ve jumper kablolar

- **Dil Ve Kütüphaneler:**

  - Python 3
  - OpenCV
  - DroidCam
  - NumPy
  - RPi.GPIO
  - haarcascade\_car

## Kurulum

1. Raspberry Pi'yi hazırlamak için aşağıdaki adımları takip edin:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip install opencv-python numpy RPi.GPIO
```

2. DroidCam'yi telefonunuza ve Raspberry Pi'nize kurun:
   - Telefonunuza DroidCam uygulamasını indirin.
   - Raspberry Pi'ye DroidCam istemcisini kurun.

## Kullanım

1. DroidCam'i açın ve Raspberry Pi'ye IP adresi ile bağlanın.
2. Ana Python betiğini çalıştırın:

```bash
python main.py
```

3. LED trafik ışıklarının yoğunluğa göre değiştiğini gözlemleyin.

## Katkıda Bulunma

Katkıda bulunmak isteyenler pull request gönderebilir veya sorunları issue olarak bildirebilirler.

---

Herhangi bir sorunuz için bana ulaşabilirsiniz.

