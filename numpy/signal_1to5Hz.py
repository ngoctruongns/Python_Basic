import numpy as np
import matplotlib.pyplot as plt

# Thời gian mẫu (từ 0 đến 5 giây) và tần số mẫu (Hz)
sample_rate = 1000  # Số mẫu trên mỗi giây
t = np.linspace(0, 1, sample_rate, endpoint=False)

# Tạo chuỗi tín hiệu sóng sin với tần số từ 1Hz đến 5Hz
frequencies = np.linspace(1, 5, 5)  # Tần số từ 1Hz đến 5Hz
waveforms = [np.sin(2 * np.pi * f * t) for f in frequencies]

# Tập hợp tất cả các mẫu của waveform vào biến signal_full
signal_full = np.concatenate(waveforms)

# Tạo một thời gian mẫu mới cho signal_full (0 đến 5 giây)
t_full = np.linspace(0, 5, len(signal_full), endpoint=False)

# Vẽ đồ thị cho signal_full
plt.figure(figsize=(12, 4))
plt.plot(t_full, signal_full)
plt.title('Biểu đồ của signal_full')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')
plt.grid(True)
plt.show()
