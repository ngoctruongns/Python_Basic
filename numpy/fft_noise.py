import numpy as np
import matplotlib.pyplot as plt

# Tạo một tín hiệu dạng sine có tần số 5 Hz trong 1 giây với mẫu 1000 điểm
fs = 100  # Tần số lấy mẫu (samples per second)
t = np.arange(0, 1, 1/fs)  # Thời gian từ 0 đến 1 giây với 1000 mẫu
f = 5  # Tần số của tín hiệu sine (Hz)
signal_sine = np.sin(2 * np.pi * f * t)

# Tạo một tín hiệu nhiễu Gaussian
noise = np.random.normal(0, 0.2, len(t))

# Kết hợp tín hiệu sine và tín hiệu nhiễu để tạo tín hiệu hỗn hợp
signal_mixed = signal_sine + noise

# Thực hiện FFT cho tín hiệu hỗn hợp
fft_result = np.fft.fft(signal_mixed)
print(fft_result)
fft_freqs = np.fft.fftfreq(len(fft_result), 1/fs)  # Tính tần số tương ứng với các thành phần FFT

# Hiển thị phần biểu đồ phổ tần số
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal_mixed)
plt.title('Tín hiệu hỗn hợp (sin(5 Hz) + nhiễu)')
plt.xlabel('Thời gian (s)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(fft_freqs, np.abs(fft_result))
plt.title('Phổ tần số')
plt.xlabel('Tần số (Hz)')
plt.xlim(0, 10)  # Giới hạn dải tần số từ 0 đến 10 Hz
plt.grid()

plt.tight_layout()
plt.show()
