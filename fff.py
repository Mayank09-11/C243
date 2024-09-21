import machine
import time

# Define GPIO pins for the LEDs
red_led = machine.Pin(16, machine.Pin.OUT)
yellow_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(18, machine.Pin.OUT)

def traffic_light_simulator():
    while True:
        # Red light on for 5 seconds
        red_led.on()
        yellow_led.off()
        green_led.off()
        print("Red Light ON")
        time.sleep(5)

        # Yellow light on for 2 seconds
        red_led.off()
        yellow_led.on()
        green_led.off()
        print("Yellow Light ON")
        time.sleep(2)

        # Green light on for 5 seconds
        red_led.off()
        yellow_led.off()
        green_led.on()
        print("Green Light ON")
        time.sleep(5)

# Start the traffic light simulation
traffic_light_simulator()
