# İzometrik Dönüşümler ve Küp Çizimi

Bu proje, **Pygame** ve **OpenGL** kullanarak 3B bir küpün izometrik dönüşümlerini gerçekleştiren bir Python uygulamasıdır. Küpler belirli dönüşümlerle hareket ettirilir ve farklı renklerle çizilir.

## Kullanılan Kütüphaneler
- **Pygame**: Grafik arayüzü oluşturmak için kullanılır.
- **OpenGL (PyOpenGL)**: 3B grafiklerin çizilmesini sağlar.

## Çalıştırma Talimatları
1. Gerekli kütüphanelerin yüklü olduğundan emin olun:
   ```sh
   pip install pygame PyOpenGL PyOpenGL_accelerate
   ```
2. Python dosyasını çalıştırın:
   ```sh
   python main.py
   ```

## Uygulamanın İçeriği
Bu kod, 3B bir küpü ve eksenleri çizerek izometrik dönüşümleri uygular. Ana bileşenler şunlardır:

- **Köşe Noktaları (kosenokta)**: Küpün köşe noktaları 3B uzayda tanımlanır.
- **Küp Kenarları (kupkenar)**: Küpün çizilmesi için gereken kenar bilgileri.
- **Matris Dönüşüm Fonksiyonları**:
  - **matris_carpim**: Bir dönüşüm matrisini vektörle çarpar.
  - **noktadonustur**: Noktaları belirli bir dönüşüm matrisi ile dönüştürür.
- **Küp Çizim Fonksiyonu (kupciz)**: Küpün OpenGL kullanılarak çizilmesini sağlar.
- **Eksen Çizimi (eksenciz)**: 3B referans eksenlerini çizer.
- **İzometrik Dönüşümler**:
  - **İzometrik dönüşüm matrisi** kullanılarak nesneler izometrik perspektife dönüştürülür.
  - **Ölçekleme ve kaydırma işlemleri** ile nesneler hareket ettirilir.
