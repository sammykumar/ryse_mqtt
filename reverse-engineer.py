import asyncio 
from bleak import BleakClient

# Right Shade Mac Addreess
# E0:75:0E:DA:FD:86

ryse_right_smartshade = "E0:75:0E:DA:FD:86"

# print(ryse_right_smartshade);

async def connect_to_device(bt_device_mac_address):
    # Replace with your Bluetooth device's MAC address
    device_address = bt_device_mac_address;

    try:
        async with BleakClient(device_address) as client:
            if client.is_connected:
                print(f"Successfully connected to the device: {device_address}")
            else:
                print(f"Failed to connect to the device: {device_address}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def write_to_shades():
    # Replace with your shades' MAC address
    device_address = "XX:XX:XX:XX:XX:XX"

    # Replace with the characteristic UUID from your logs
    characteristic_uuid = "00001300-0000-1000-8000-00805f9b34fb"  # Replace this with the actual UUID
    command = bytes.fromhex("F50301010002")  # Command from your logs

    async with BleakClient(device_address) as client:
        # Check if the device is connected
        if client.is_connected:
            print(f"Connected to {device_address}")

            # Write the command to the characteristic
            await client.write_gatt_char(characteristic_uuid, command)
            print("Command sent successfully!")
        else:
            print(f"Failed to connect to {device_address}")

# Run the asyncio event loop
asyncio.run(connect_to_device(ryse_right_smartshade))
#asyncio.run(write_to_shades())