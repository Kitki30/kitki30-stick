import esp32
import machine
import modules.nvs as nvs

def check(tft):
    import fonts.def_8x8 as f8x8
    n_boot = esp32.NVS("boot")
    if nvs.get_int(n_boot, "firstBoot") == None:
        n_settings = esp32.NVS("settings")
        n_wifi = esp32.NVS("wifi")
        print("Devices first boot, configuring NVS.")
        tft.fill(7003)
        tft.text(f16x16, "Kitki30 Stick",0,0,65535,7003)
        tft.text(f8x8, "First boot configuration!",0,16,65535,7003)
        tft.text(f8x8, "Please wait...",0,24,65535,7003)
    
        # Boot config
        print("Configuring 'boot' NVS")
        nvs.set_int(n_boot, "firstBoot", 1)
        print("boot:firstBoot:1")
        tft.text(f8x8, "boot:firstBoot:1",0,34,65535,7003)
        nvs.set_int(n_boot, "fastBoot", 0)
        print("boot:fastBoot:0")
        tft.text(f8x8, "boot:fastBoot:0",0,42,65535,7003)
    
        # Settings config
        print("Configuring 'settings' NVS")
        nvs.set_float(n_settings, "volume", 0.5)
        print("settings:volume:0.5")
        tft.text(f8x8, "settings:volume:0.5",0,52,65535,7003)
        nvs.set_float(n_settings, "backlight", 0.5)
        print("settings:backlight:0.5")
        tft.text(f8x8, "settings:backlight:0.5",0,60,65535,7003)
    
        print("Doing soft reset")
        tft.text(f8x8, "Doing soft reset. Bye!",0,94,65535,7003)
        machine.soft_reset()