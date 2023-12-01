import numpy as np
import matplotlib.pyplot as plt

# Thời gian mẫu (từ 0 đến 5 giây) và tần số mẫu (Hz)
sample_rate = 20  # Số mẫu trên mỗi giây
t = np.linspace(0, 1, sample_rate, endpoint=False)

# Tạo chuỗi tín hiệu sóng sin với tần số từ 1Hz đến 5Hz
frequencies = np.linspace(1, 5, 5)  # Tần số từ 1Hz đến 5Hz
waveforms = [np.sin(2 * np.pi * f * t)*10 for f in frequencies]

# Tập hợp tất cả các mẫu của waveform vào biến signal_full
signal_full = np.concatenate(waveforms)


# Tạo một tín hiệu nhiễu Gaussian
noise = np.random.normal(0, 0.2, len(signal_full))

# Kết hợp tín hiệu sine và tín hiệu nhiễu để tạo tín hiệu hỗn hợp
signal_mixed = signal_full + noise

# Tạo một thời gian mẫu mới cho signal_full (0 đến 5 giây)
t_full = np.linspace(0, 5, len(signal_full), endpoint=False)
print(f"Len of signal ful {len(signal_full)}")
# Thực hiện FFT
fft_result = np.fft.fft(signal_full)
# print(fft_result)

fft_abs = np.abs(fft_result)
print(f"fft_abs len {len(fft_abs)} : \n {fft_abs}")

fft_freqs = np.fft.fftfreq(len(fft_result), 1/sample_rate)  # Tính tần số tương ứng với các thành phần FFT
print(f"fft_freqs len {len(fft_freqs)} : \n {fft_freqs}")
for i in range(len(fft_freqs)):
    if 1 <= fft_freqs[i] <= 5:
        print(f'fft at {fft_freqs[i]:.1f} Hz: {fft_abs[i]:.2f}') 

# Vẽ biểu đồ tín hiệu và phổ tần số
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t_full, signal_full)
plt.title('Tín hiệu dạng sine (1-5 Hz)')
plt.xlabel('Thời gian (s)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(fft_freqs, np.abs(fft_result))
plt.title('Phổ tần số')
plt.xlabel('Tần số (Hz)')
# plt.xlim(0, 10)  # Giới hạn dải tần số từ -10 đến 10 Hz
plt.grid()

plt.tight_layout()
plt.show()
