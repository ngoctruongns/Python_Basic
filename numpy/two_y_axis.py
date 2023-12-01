import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
t = np.linspace(0, 1, 1000)
signal_full = np.sin(2 * np.pi * 3 * t) + np.sin(2 * np.pi * 5 * t)

# Tính phổ tần số và phổ tần số trung bình
fft_result = np.fft.fft(signal_full)
freq = np.fft.fftfreq(len(t))
avg_spectrum = np.abs(fft_result) / len(t)
print(f'fft result {len(fft_result)} and {len(t)}')

# Vẽ biểu đồ tín hiệu và phổ tần số trên cùng một biểu đồ
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
# ax1.set_xlabel('Thời gian (s)')
# ax1.set_ylabel('Tín hiệu dạng sine', color=color)
# ax1.plot(t, signal_full, color=color)
# ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Tạo trục Y phụ

color = 'tab:red'
ax2.set_ylabel('Phổ tần số', color=color)
ax2.plot(freq, np.abs(fft_result), color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Vẽ phổ tần số trung bình bằng đường kẻ đứt
ax2.plot(freq, avg_spectrum, linestyle='--', color='green', label='Phổ tần số trung bình')

fig.tight_layout()  # Đảm bảo không bị trôi lệnh xlabel và ylabel
plt.title('Biểu đồ tín hiệu và phổ tần số')
plt.grid()
plt.show()
