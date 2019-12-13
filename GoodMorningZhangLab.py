import numpy as np
import matplotlib.pyplot as plt

# データ生成
x = np.linspace(0, 10, 100)
y = x + np.random.randn(100)

# プロット
plt.plot(x, y, label="test")

# 凡例の表示
plt.legend()

# プロット表示(設定の反映)
plt.show()

#m-morishita
print("HELLO! MATSUO-SAN!")

#s-sakakibara
print("Nyunga dayo!")
print("dayo")