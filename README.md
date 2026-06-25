# QPSK-Digital-Communication-System-Simulation
Bu proje, Python ve NumPy kullanılarak geliştirilmiş uçtan uca (end-to-end) bir dijital haberleşme zinciri simülasyonudur. Projede QPSK (Quadrature Phase Shift Keying) modülasyonu, AWGN (Eklemeli Beyaz Gaussian Gürültü) kanalı ve karar teorisine dayalı bir demodülasyon mimarisi modellenmiştir.Sistem performansı, farklı SNR (Sinyal-Gürültü Oranı) değerlerine karşılık gelen BER (Bit Hata Oranı) hesaplanarak analiz edilmektedir.

Özellikler (Features)
Rastgele Veri Üretimi: Simülasyon için N uzunluğunda rastgele bit dizisi oluşturulması.
QPSK Sembol Eşleme (Mapping): Bit çiftlerinin (bit-pairs) faz düzleminde kompleks sembollere (I + jQ) normalize edilmiş enerji (E_s = 1) ile aktarılması.
AWGN Kanal Modeli: Belirlenen SNR (dB) değerine göre kanaldaki gürültü gücünün hesaplanması ve sinyale kompleks Gaussian gürültüsü eklenmesi.
Karar Teorisi Tabanlı Demodülasyon: Alınan gürültülü sinyalin reel (I) ve sanal (Q) bileşenlerinin işaretlerine göre (Quadrant tespiti) yeniden bitlere dönüştürülmesi.
Performans Analizi: Toplam sembol hatası, bit hatası ve BER (Bit Error Rate) metriklerinin anlık hesabı.

Gereksinimler (Requirements)
Projeyi çalıştırmak için bilgisayarınızda Python 3.x ve NumPy kütüphanesinin kurulu olması gerekir.

Bash
pip install numpy
Kullanım (Usage)
Kodu çalıştırmak için terminal veya komut satırından ilgili Python dosyasını tetiklemeniz yeterlidir:

Bash
python Signal_Equlization_PY.py
Parametreleri Özelleştirme
Kodun en üstündeki şu parametreleri değiştirerek farklı senaryoları test edebilirsiniz:

Python
N = 1000      # Toplam bit sayısı (Örn: İstatistiki başarı için 100000 yapabilirsiniz)
SNR_dB = 10   # Sinyal-Gürültü Oranı (Değeri artırarak BER'in düştüğünü gözlemleyin)
Örnek Çıktı (Sample Output)
SNR_dB = 10 ve N = 1000 için örnek bir simülasyon çıktısı:

Plaintext
--- QPSK Simulation @ SNR = 10 dB ---
Total transmitted bits (N): 1000
Total received symbol errors: 1
Total bit errors: 1
Bit Error Rate (BER): 0.0010
