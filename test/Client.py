import socket
import time
import pickle
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
host = '10.110.5.24'
port = 9001
client.connect((host, port))

# sample = {"cfg_cfwserver_1_ip": "0.0.0.155", "cfg_cfwserver_2_ip": "0.0.0.156", "cfg_gamepad_1": "Gamepad 1",
#           "cfg_gamepad_2": "Gamepad 2", "cfg_rov1": "None", "cfg_rov2": "None", "cfg_underwater_visibility": 0,
#           "cfg_rov_1_camera_bw_mode": false, "cfg_rov_2_camera_bw_mode": false, "cfg_balkong_bolt_detach": false,
#           "cfg_balkong_square_pin_detach": false, "cfg_wlr_main": true, "cfg_wlr_seconday": false,
#           "cfg_wlr_spooling": false, "cfg_wlr_speed": 0, "cfg_wlr_selection": "None", "cfg_crane_turret": false,
#           "cfg_crane_elbow": false, "cfg_crane_arm": false, "cfg_crane_teather": false, "cfg_crane_speed": 0}


from_server = client.recv(1024)
while True:
    if from_server:
        data = pickle.loads(from_server)
        # print(data)
        print(data)
    else:
        print("None")
    time.sleep(0.5)
client.close()


