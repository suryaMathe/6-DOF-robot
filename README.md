# 6-DOF-robot
This project presents a complete 6-DOF robotic arm system It features servo-driven joints, an ultrasonic sensor for object detection, and modular components for easy customization. Ideal for learning robotics, motion planning, and embedded control systems.
# 🤖 6-DOF Robotic Arm - Full Design & Implementation

This repository documents the end-to-end development of a **6 Degrees of Freedom (6-DOF) Robotic Arm** project — covering mechanical design, electronics, Arduino control, forward kinematics, and simulation tools. The project is built with accessibility, modularity, and educational value in mind.

---

## 🧩 Components

### 🛠️ Mechanical Parts:
- Base platform (circular or square)
- Link 1 (shoulder)
- Link 2 (elbow)
- Link 3 (forearm)
- Link 4 (wrist pitch)
- Link 5 (wrist yaw)
- Link 6 (end-effector mount or gripper)
- 3D printed brackets and spacers (optional)

### ⚡ Electronics:
- 6x Servo Motors (MG996R / DS3218 / Dynamixel)
- 1x Arduino Uno or Mega
- 1x Ultrasonic Sensor (HC-SR04)
- Breadboard & jumper wires
- External power supply (5V–7.4V, 2A+)
- Voltage regulator (optional)

---

## 🖥️ CAD Design (Fusion 360)

Each link of the robotic arm is modeled as a separate component in **Autodesk Fusion 360**, allowing for:
- Individual assembly and modification
- Motion constraints using revolute joints
- Export as `.STL` for 3D printing

Dimensions used:
- Base: 10x10x2 cm  
- Link 1: 3x3x15 cm  
- Link 2: 3x3x25 cm  
- Link 3: 3x3x20 cm  
- Wrist Links: 3x3x5 cm  
- End Effector: 4 cm dia x 5 cm height

---

## 🔌 Circuit Design

An Arduino Uno controls six servo motors and an ultrasonic sensor. Power is supplied externally for stable motor operation.

### Pin Mapping:
- Servo 1 to 6 → D2 to D7  
- HC-SR04 Trigger → D8  
- HC-SR04 Echo → D9  
- External 5V → Servo VCC  
- GND shared between Arduino and servos  

---

## 🧠 Arduino Code

The Arduino sketch controls each servo using the `Servo.h` library. Basic movements and scanning logic with the ultrasonic sensor can be added.

```cpp
#include <Servo.h>
Servo s1, s2, s3, s4, s5, s6;

void setup() {
  s1.attach(2); s2.attach(3); s3.attach(4);
  s4.attach(5); s5.attach(6); s6.attach(7);
}

void loop() {
  s1.write(90); s2.write(45); s3.write(135);
  s4.write(90); s5.write(90); s6.write(90);
  delay(1000);
}
