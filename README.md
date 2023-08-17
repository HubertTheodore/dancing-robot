# Dancing Robot

As a group of 4, we built a dancing robot able to perform various dance moves while also having additional features. These features included playing music and lighting up LEDs while the robot is dancing, robot performs dance moves according to input from a keypad, the keypad can be played as a piano, and the current state of the robot is displayed on an LCD screen. 

My responsibility was to help design and implement the dance moves using CircuitPython as well as setting up the LEDs so that they can light up while the robot is dancing.

## Table of Contents

- [Design and Implementation](#designAndImplementation)
- [Final Result](#finalResult)

## Design and Implementation <a name="designAndImplementation"></a>

A keypad was used to receive user input, and the songs and dances that would play varied based on the button pressed by the user. In terms of hardware components, we used a Raspberry Pi Pico W, 4 servo motors, 3 RGB LEDs, a keypad, an LCD screen, and a buzzer.

The following diagrams show the types of input that the keypad receives and how it interacts with the hardware.

![block1](https://github.com/HubertTheodore/dancing-robot/assets/55958230/071e86bf-9d91-4f3d-b2b6-6932afe679ac)
![block2](https://github.com/HubertTheodore/dancing-robot/assets/55958230/d831ebcb-9f26-4aad-a0ad-59fdeac58bd5)

Hardware fritzing: 

![fritzing](https://github.com/HubertTheodore/dancing-robot/assets/55958230/1ebbd22b-95cc-4885-a773-90d851430249)

Pictures of the physical components:

![robot1](https://github.com/HubertTheodore/dancing-robot/assets/55958230/d86583c4-9ff6-45b5-90ed-e933d0d95c0a)
![robot2](https://github.com/HubertTheodore/dancing-robot/assets/55958230/ab15ec31-bf46-4b4b-aed1-e854188c4aa3)

## Final Result <a name="finalResult"></a>

[Dancing Robot Demo](https://www.youtube.com/watch?v=FwHS9Bj4zys)

![final](https://github.com/HubertTheodore/dancing-robot/assets/55958230/8fe539a8-4654-42cd-87d0-3b7f80b52d24)
