import serial
import serial.tools.list_ports
import time

def find_responsive_port(baudrate=115200, timeout=1):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        try:
            ser = serial.Serial(port.device, baudrate=baudrate, timeout=timeout)
            ser.write(b'TEST\n')  # Replace with your device's test command
            time.sleep(1) # Give the device time to respond
            response = ser.readline().strip()
            if response:  # Or check for a specific response
                ser.close()
                return port.device
            ser.close()
        except (OSError, serial.SerialException):
            pass
    return None

device_port = find_responsive_port()
if device_port:
    print(f"Device found on port: {device_port}")
else:
    print("Device not found")