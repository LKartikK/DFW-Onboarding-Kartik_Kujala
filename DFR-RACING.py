import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("can_data.csv")

# CONVERTING UNIX NUMBERS INTO HUMAN REDABLE DATA (TIMESTAMPS)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# REMOVING PRESSURE TYPE AND TEMP TYPE
df = df.drop(["Pressure Type", "Temp Type"], axis=1)

# FIND THE MEAN OF ALL COLUMNS
df = df.fillna(df.mean())

# Adding a new column for the difference between Non-Avg and AVG Wheel Speed
df["Wheel Speed"] = df["Driven Avg Wheel Speed"] - df["Non-Driven Avg Wheel Speed"]

# PLOTTING RPS OVER TPS
x = df["RPM"]
y = df["TPS"]

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color="b", marker="o", s=5, alpha=0.5)

plt.xlabel("RPM")
plt.ylabel("TPS")
plt.title("RPM vs TPS")
plt.grid(True)

plt.savefig("rpm_vs_tps.png")
plt.close()

# PLOTTING COOLANT TEMP OVER TIME
x = df["timestamp"]
y = df["Coolant Temp"]

plt.figure(figsize=(6, 4))
plt.plot(x, y, color="r")

plt.xlabel("Timestamp")
plt.ylabel("Coolant Temp")
plt.title("Coolant Temp over Time")
plt.grid(True)

plt.savefig("coolant_temp_over_time.png")
plt.close()

# PLOTTING WHEEL
x = df["timestamp"]
y = df["Wheel Speed"]

plt.figure(figsize=(6, 4))
plt.plot(x, y, color="g")

plt.xlabel("Timestamp")
plt.ylabel("Wheel Speed")
plt.title("Wheel Speed over Time")
plt.grid(True)

plt.savefig("wheel_speed_over_time.png")
plt.close()

# PLOTTING LAMBDA OVER TIME
x = df["timestamp"]
y = df["Lambda"]

plt.figure(figsize=(6, 4))
plt.plot(x, y, color="g")

plt.xlabel("Timestamp")
plt.ylabel("Lambda")
plt.title("Lambda over Time")
plt.grid(True)

plt.savefig("lambda_over_time.png")
plt.close()

# PLOTTING BATTERY VOLTAGE OVER TIME
x = df["timestamp"]
y = df["Battery Volt"]

plt.figure(figsize=(6, 4))
plt.plot(x, y, color="g")

plt.xlabel("Timestamp")
plt.ylabel("Battery Volt")
plt.title("Battery Volt over Time")
plt.grid(True)

plt.savefig("battery_volt_over_time.png")
plt.close()
