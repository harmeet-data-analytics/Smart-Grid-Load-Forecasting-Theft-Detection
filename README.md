An Integrated Smart Grid Load Forecasting and Theft Detection System Using Python and Data Science

1. Project Overview

This project presents an integrated smart grid monitoring system that combines real-time electrical power measurement, load forecasting, and electricity theft detection using Python, Data Science, ESP32, and PZEM energy meters.

The system measures electrical power using two PZEM energy meters. The readings are transmitted through an ESP32 microcontroller and analyzed using Python. The difference between the two measured power values is used to identify abnormal conditions, while Linear Regression is used for basic load forecasting.

2. Objectives

* Monitor electrical power in real time.
* Collect voltage, current, and power measurements.
* Compare power measured at two monitoring points.
* Detect abnormal power differences that may indicate electricity theft.
* Calculate a data-driven theft detection threshold.
* Forecast the next expected power reading.
* Visualize monitoring, forecasting, and theft detection results.
* Provide a unified smart grid monitoring dashboard.

3. Hardware Components

* ESP32 Development Board
* 2 × PZEM-004T Energy Meter Modules
* 2 × CT Coils
* Relay Module
* Active Buzzer
* AC Bulbs / Loads
* Breadboard
* Jumper Wires
* AC Power Supply and required electrical wiring

4. Software and Technologies

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Arduino IDE
* ESP32
* CSV-based data storage
* Linear Regression

5. System Working

The PZEM energy meters measure electrical parameters from two monitoring points. The ESP32 receives the measurements and sends the data for analysis.

The collected readings contain parameters such as:

* Voltage
* Current
* Power
* Time

The power values from PZEM1 and PZEM2 are compared using:

Power Difference = |PZEM1 Power − PZEM2 Power|

During normal operation, the difference remains within the expected range. A threshold is calculated from the normal baseline data and is used for anomaly/theft detection.

6. Normal Baseline Analysis

A normal operating dataset was collected before performing theft detection.

Final baseline results:

* Valid readings: 655
* Mean Power Difference: 0.145 W
* Standard Deviation: 0.098 W
* Maximum Normal Difference: 0.500 W
* Calculated Theft Threshold: 0.439 W

The threshold was calculated using the mean difference plus three standard deviations.

7. Final Live Dataset

After collecting the final monitoring data, the final dataset contained:

* Total valid readings: 630
* Normal readings: 630
* Theft suspected readings: 0
* Theft percentage: 0.00%
* PZEM1 Mean Power: 6.536 W
* PZEM2 Mean Power: 6.416 W
* Mean Power Difference: 0.130 W
* Maximum Difference: 0.500 W

8. Load Forecasting

Linear Regression was used to identify the overall power trend and forecast the next power reading.

Final forecasting results:

* Total readings: 630
* Average actual power: 6.536 W
* Minimum power: 6.0 W
* Maximum power: 7.1 W
* Next predicted power: 6.293 W

The forecasting result is visualized using the Smart Grid Load Forecasting graph.

9. Theft Detection

The theft detection system compares the calculated power difference with the predefined threshold of 0.439 W.

If the difference exceeds the threshold, the system can classify the condition as:

THEFT SUSPECTED

Otherwise, the condition is classified as:

NORMAL

The final collected dataset produced 630 normal readings and no theft-suspected readings.

10. Dashboard

The final dashboard integrates four major sections:

1. Final Power Monitoring
2. Smart Grid Load Forecasting
3. Theft Detection Results
4. Power Difference Analysis

The dashboard provides a single visual interface for understanding the collected electrical data and analytical results.

11. Important Project Files

Data Files

* final_live_data.csv
* final_project_summary.csv
* load_forecasting_result.csv

Graphs

* pzem_power_comparison.png
* power_difference_threshold.png
* load_forecasting_graph.png
* final_smart_grid_dashboard.png

Python Programs

* esp32_logger.py
* final_theft_detection.py
* calculate_threshold.py
* load_forecasting.py
* final_dashboard.py

12. Final Result

The developed system successfully demonstrates:

* Electrical power monitoring using PZEM energy meters.
* ESP32-based data acquisition.
* Python-based data processing.
* Normal baseline analysis.
* Threshold-based electricity theft detection.
* Load forecasting using Linear Regression.
* Graphical visualization of electrical data.
* Integrated smart grid monitoring dashboard.

13. Future Improvements

Future versions of the system can include:

* Larger real-world datasets.
* Advanced Machine Learning models for forecasting.
* Real-time web-based monitoring.
* IoT cloud integration.
* Automated SMS or mobile notifications.
* Improved theft detection using multiple electrical parameters.
* Real-time relay and buzzer control.
* Deployment with multiple smart meter nodes.

14. Conclusion

The project demonstrates how IoT hardware and Data Science techniques can be integrated to build a smart grid monitoring and electricity theft detection system. The combination of ESP32, PZEM energy meters, Python data analysis, Linear Regression, threshold-based anomaly detection, and visualization provides a practical foundation for intelligent electrical monitoring.