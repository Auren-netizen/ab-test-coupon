import numpy as np
import pandas as pd

np.random.seed(42)

n_users = 10000

data = pd.DataFrame({
    "user_id": np.arange(1, n_users + 1),
    "group": np.random.choice(["treatment", "control"], size=n_users),
    "date": pd.date_range("2026-01-01", periods=n_users, freq="min")
})

data["coupon"] = (data["group"] == "treatment").astype(int)

conversion_probability = np.where(
    data["coupon"] == 1,
    0.15,
    0.10
)

data["converted"] = np.random.binomial(
    1,
    conversion_probability
)

data["order_amount"] = np.where(
    data["converted"] == 1,
    np.random.gamma(shape=5, scale=20, size=n_users),
    0
).round(2)

data["refund"] = np.where(
    data["converted"] == 1,
    np.random.binomial(1, 0.08, size=n_users),
    0
)

data.to_csv("data/coupon_data.csv", index=False)

print("模拟数据生成完成！")
print(data.head())
print(data.shape)