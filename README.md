The dataset contains data regarding the engine performance. The code performs several analysis steps. It loads the CSV file using pandas to clean the data, and I have converted the UNIX timestamps into readable time (real date/time) values so time-series graphs work properly. I have removed the unnecessary columns like the Pressure Type and Temp Type because they are repeated information. I filled the missing values using column means by replaceing it with each column's average. This prevents errors during plotting and calculations. I created a new feature (Wheel Speed Difference). This column estimates how the driven wheels behave compared to non-driven. These values indicate things like: wheel slip, traction loss, sensor mismatch, and changes during acceleration/braking.

I have generated 4 graphs:
1) RPM vs TPS - This is a scatter plot showing the releationship between engine RPM and throttle position. 
![RPM vs TPS](Graphs%20Pictures/rpm_vs_tps.png)
2) Coolant Temperature over Time - This plot shows how coolant temperature changes throughout the drive.
![Coolant Temp](Graphs%20Pictures/coolant_temp_over_time.png)
3) Wheel Speed Difference over Time - This plot shows my derived wheel speed difference over time.
![Wheel Speed Difference](Graphs%20Pictures/wheel_speed_over_time.png)
4) Battery Voltage over Time - This plot shows how battery voltage changes over the session. 
![Battery Voltage](Graphs%20Pictures/battery_volt_over_time.png)


Conclusions: 
1. RPM vs TPS helps confirm how throttle input relates to engine response. Such as, if the points increase togetherm, throttle to RPM behavior is consistent. 
2. Cooland Temp over Time shows whether the engine reaches and maintains a stable temperature. 
3. Wheel speed difference is useful for detecting traction related events. Such as, the graph near to zero most of the time suggests stable traction, and larger deviations suggest slip, braking events, or uneven wheel behavior. 
4. Battery Voltage over Time indicates whether the voltage regulation seems stable. A stable line is good, but any drops or spikes can point to load changes or electrical issues. 