import numpy as np
import matplotlib.pyplot as plt

# Tạo một tín hiệu dạng sine có tần số 5 Hz trong 1 giây với mẫu 1000 điểm
fs = 100  # Tần số lấy mẫu (samples per second)
t = np.arange(0, 1, 1/fs)  # Thời gian từ 0 đến 1 giây với 1000 mẫu
f = 5  # Tần số của tín hiệu sine (Hz)
signal = np.sin(2 * np.pi * f * t)

# Thực hiện FFT
fft_result = np.fft.fft(signal)
print(fft_result)
fft_result_abs = np.abs(fft_result)

fft_freqs = np.fft.fftfreq(len(fft_result), 1/fs)  # Tính tần số tương ứng với các thành phần FFT

# Vẽ biểu đồ tín hiệu và phổ tần số
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Tín hiệu dạng sine (5 Hz)')
plt.xlabel('Thời gian (s)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(fft_freqs, np.abs(fft_result))
plt.title('Phổ tần số')
plt.xlabel('Tần số (Hz)')
plt.xlim(0, 100)  # Giới hạn dải tần số từ -10 đến 10 Hz
plt.grid()

plt.tight_layout()
plt.show()
